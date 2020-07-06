import json
import cv2
from Face_train import Model


class Face_recognition:
    def __init__(self):
        with open('need/contrast_table', 'r') as f:
            self.contrast_table = json.loads(f.read())
        self.model = Model()
        self.model.load_model(file_path='./model/model')
        # 框住人脸的矩形边框颜色
        self.color = (255, 255, 255)

        # 捕获指定摄像头的实时视频流
        self.cap = cv2.VideoCapture(0)

        # 读取视频路径
        # PATH_VIDEO = u'E:/user/python_project/DCNN/video1.mp4'
        # self.cap = cv2.VideoCapture(PATH_VIDEO)

        # 人脸识别分类器本地存储路径
        self.cascade_path = "need/haarcascade_frontalface_default.xml"

    def recongition(self):
        # 识别时间10秒；如果置信度大于60%，则识别成功并登录界面；否则至10秒后识别失败并退出
        time = 0
        while True:
            result = "unknown"  # 初始化识别失败
            time += 1

            ret, frame = self.cap.read()  # 读取一帧视频

            if ret is True:
                # 图像灰化，降低计算复杂度
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            else:
                continue

            # 使用人脸识别分类器，读入分类器
            cascade = cv2.CascadeClassifier(self.cascade_path)

            # 利用分类器识别出人脸
            faceRects = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
            if len(faceRects) > 0:
                for faceRect in faceRects:
                    x, y, w, h = faceRect

                    # 截取脸部图像提交给模型识别身份
                    image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                    probability, name_number = self.model.face_predict(image)
                    print(name_number)
                    name = self.contrast_table[str(name_number)]

                    # print('name_number:', name_number)
                    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), self.color, thickness=2)

                    # 文字提示身份
                    cv2.putText(frame, name, (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    if probability > 0.6:
                        result = name
                        cv2.putText(frame, name, (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
                        # confidence = "{0}%".format(round(100 - probability))
                        # 释放摄像头并销毁所有窗口
                        self.cap.release()
                        cv2.destroyAllWindows()  # 退出摄像头
                        return result
                    else:
                        cv2.putText(frame, 'unknown', (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        confidence = "{0}%".format(round(100 - probability))
                        cv2.putText(frame, str(confidence), (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),
                                    1)
            cv2.imshow("face_recognition", frame)

            k = cv2.waitKey(1)
            if k == 27:
                break
            elif time > 100:  # 大约10秒识别时间
                break

        self.cap.release()
        cv2.destroyAllWindows()
        return result  # 返回识别结果：人名或“unknown”


def main():
    fr = Face_recognition()
    return fr.recongition()


if __name__ == '__main__':
    main()
