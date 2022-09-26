import cv2 as cv
from LogUtils.Log import Log


class VideoUtils:

    @classmethod
    def check_rtsp(cls, rtsp: str = None):
        """

        :param rtsp:
        :return:
        """
        if rtsp:
            video = cv.VideoCapture(rtsp)
            if video.isOpened():
                return True
            else:
                return False
        else:
            print('input rtsp is null')

if __name__ == '__main__':

    log = Log()
    demo = VideoUtils()
    res = demo.check_rtsp('rtsp://admin:Tt@123456@112.5.102.152:554/cam/realmonitor?channel=1&subtype=1')
    log.loginfo(text=str(res))