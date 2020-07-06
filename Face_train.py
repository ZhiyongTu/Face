import random
from keras import backend as K
from keras.layers import Conv2D, MaxPooling2D, Dropout, ZeroPadding2D
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from load_data import load_dataset, resize_image, IMAGE_SIZE
# 结合CUDA加速技术训练模型


# 数据预处理
class Dataset:
    def __init__(self, path_name):
        # 训练集
        self.train_images = None
        self.train_labels = None

        # 测试集
        self.test_images = None
        self.test_labels = None

        # 数据集加载路径
        self.path_name = path_name

        # 当前库采用的维度顺序
        self.input_shape = None

        # 人脸分类数量
        self.nb_classes = None

    # 装载数据集并按照交叉验证的原则分割数据集
    def load(self, img_rows=IMAGE_SIZE, img_cols=IMAGE_SIZE, img_channels=3):
        # 装载数据集
        images, labels, face_num = load_dataset(self.path_name)
        self.nb_classes = face_num

        # 按交叉验证的原则分割训练集和测试集
        train_images, _, train_labels, _ = train_test_split(
            images, labels, test_size=0.1, random_state=random.randint(0, 100))
        _, test_images, _, test_labels = train_test_split(
            images, labels, test_size=0.1, random_state=random.randint(0, 100))

        # 判断后端系统：TensorFlow/Theano，重组训练数据集
        if K.image_data_format() == 'channels_first':
            train_images = train_images.reshape(
                train_images.shape[0], img_channels, img_rows, img_cols)
            test_images = test_images.reshape(
                test_images.shape[0], img_channels, img_rows, img_cols)
            self.input_shape = (img_channels, img_rows, img_cols)
        else:
            train_images = train_images.reshape(
                train_images.shape[0], img_rows, img_cols, img_channels)
            test_images = test_images.reshape(
                test_images.shape[0], img_rows, img_cols, img_channels)
            self.input_shape = (img_rows, img_cols, img_channels)

        # 输出训练集和测试集的数量
        print(train_images.shape[0], 'train samples')
        print(test_images.shape[0], 'test samples')

        # 根据类别数量nb_classes将类别标签进行one-hot编码使其向量化
        train_labels = np_utils.to_categorical(train_labels, self.nb_classes)
        test_labels = np_utils.to_categorical(test_labels, self.nb_classes)

        # 像素数据浮点化以便归一化
        train_images = train_images.astype('float32')
        test_images = test_images.astype('float32')

        # 归一化,图像的各像素值归一化到0~1区间
        train_images /= 255
        test_images /= 255

        self.train_images = train_images
        self.test_images = test_images
        self.train_labels = train_labels
        self.test_labels = test_labels


# 搭建CNN网络模型
class Model:
    def __init__(self):
        self.model = None
        self.history = None

    # 搭建模型
    def build_model(self, dataset, nb_classes):
        # 定义一个序贯模型
        self.model = Sequential()

        # 顺序添加CNN模型的各个网络层
        # 输入/卷积层
        # 对图片的边界填充0，以控制卷积以后特征图的大小
        self.model.add(ZeroPadding2D((1, 1), input_shape=dataset.input_shape))
        self.model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))

        # 卷积层，选取32个特征卷积核，大小为3∗3
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))

        # 池化层，过滤器大小为2*2，长和宽的步长均为2
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # 卷积层，选取64个特征卷积核，大小为3∗3
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))

        # 卷积层，选取64个特征卷积核，大小为3∗3
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))

        # 池化层，过滤器大小为2*2，长和宽的步长均为2
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # 卷积层，选取128个特征卷积核，大小为3∗3
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))

        # 卷积层，选取128个特征卷积核，大小为3∗3
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))

        # 卷积层，选取128个特征卷积核，大小为3∗3
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))

        # 池化层，过滤器大小为2*2，长和宽的步长均为2
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        self.model.add(Flatten())  # Flatten层

        # 全连接层, 输出节点个数为512
        self.model.add(Dense(512, activation='relu'))
        self.model.add(Dropout(0.5))

        # 全连接层, 输出节点个数为512
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.5))

        # 分类层
        self.model.add(Dense(nb_classes, activation='softmax'))

        # 打印模型
        self.model.summary()

    # 训练模型
    def train(self, dataset, batch_size=20, nb_epoch=100, data_augmentation=False):
        # 编译模型
        # sgd = SGD(lr=0.0007, decay=1e-6, momentum=0.9, nesterov=True)  # 生成一个优化器对象
        self.model.compile(loss='categorical_crossentropy',  # 损失函数：categorical_crossentropy
                           optimizer=Adam(),  # 优化器：Adam
                           metrics=['acc'])  # 打印准确率

        # 不使用数据增强（从训练数据中利用旋转、翻转、加噪声等方法创造新的训练数据，有意识的提升训练数据规模，增加模型训练量）
        if not data_augmentation:
            self.history = self.model.fit(dataset.train_images,
                                          dataset.train_labels,
                                          batch_size=batch_size,
                                          epochs=nb_epoch,
                                          validation_data=(
                                              dataset.test_images, dataset.test_labels),
                                          shuffle=True)
        # 使用数据增强
        else:
            # 定义数据生成器对象data_create用于数据增强，data_create每被调用一次则生成一组数据
            data_create = ImageDataGenerator(
                featurewise_center=False,  # 是否使输入数据去中心化（均值为0）
                samplewise_center=False,  # 是否使输入数据的每个样本均值为0
                featurewise_std_normalization=False,  # 是否数据标准化（输入数据除以数据集的标准差）
                samplewise_std_normalization=False,  # 是否将每个样本数据除以自身的标准差
                zca_whitening=False,  # 是否对输入数据施以ZCA白化
                rotation_range=10,  # 数据提升时图片随机转动的角度(范围为0～180)
                width_shift_range=0.0,  # 数据提升时图片水平偏移的幅度（单位为图片宽度的占比，0~1之间的浮点数）
                height_shift_range=0.0,  # 数据提升时图片垂直偏移的幅度
                horizontal_flip=True,  # 是否进行随机水平翻转
                vertical_flip=False)  # 是否进行随机垂直翻转

            # 计算整个训练样本集的数量，用于特征值归一化、ZCA白化等处理
            data_create.fit(dataset.train_images)

            # 利用生成器训练模型
            self.history = self.model.fit_generator(
                data_create.flow(dataset.train_images,
                                 dataset.train_labels, batch_size=batch_size),
                steps_per_epoch=dataset.train_images.shape[0],
                epochs=nb_epoch,
                validation_data=(dataset.test_images, dataset.test_labels))

    def save_model(self, file_path):
        self.model.save(file_path)

    def load_model(self, file_path):
        self.model = load_model(file_path)

    def evaluate(self, dataset):
        score1 = self.model.evaluate(
            dataset.test_images, dataset.test_labels, verbose=1)
        print("test %s: %.6f%%" %
              (self.model.metrics_names[1], score1[1] * 100))
        print("test %s: %.6f" % (self.model.metrics_names[0], score1[0]))
        score2 = self.model.evaluate(
            dataset.train_images, dataset.train_labels, verbose=1)
        print("train %s: %.6f%%" %
              (self.model.metrics_names[1], score2[1] * 100))
        print("train %s: %.6f" % (self.model.metrics_names[0], score2[0]))

    # 识别人脸
    def face_predict(self, image):
        # 判断后端系统：TensorFlow/Theano，确定维度顺序
        if K.image_data_format() == 'channels_first' and image.shape != (1, 3, IMAGE_SIZE, IMAGE_SIZE):
            image = resize_image(image)  # 尺寸与训练集一致：IMAGE_SIZE x IMAGE_SIZE
            image = image.reshape((1, 3, IMAGE_SIZE, IMAGE_SIZE))  # 针对1张图片进行预测
        elif K.image_data_format() == 'channels_last' and image.shape != (1, IMAGE_SIZE, IMAGE_SIZE, 3):
            image = resize_image(image)
            image = image.reshape((1, IMAGE_SIZE, IMAGE_SIZE, 3))

        # 改为浮点数并归一化
        image = image.astype('float32')
        image /= 255

        # 计算输入属于各个类别的概率，输出概率最大的类别
        result_probability = self.model.predict_proba(image)
        print('result:', result_probability, max(result_probability[0]))

        # 给出类别预测
        result = self.model.predict_classes(image)

        # 返回类别预测结果
        return max(result_probability[0]), result[0]


def main():
    dataset = Dataset('./data/')
    dataset.load()  # 1 导入数据集
    model = Model()
    model.build_model(dataset, dataset.nb_classes)  # 2 搭建模型
    model.train(dataset)  # 3 训练模型
    model.save_model(file_path='./model/model')  # 4 储存模型
    model.evaluate(dataset)  # 5 模型评估


if __name__ == '__main__':
    main()
