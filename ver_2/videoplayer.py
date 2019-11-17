import cv2

class CVideoPlayer:
    def __init__(self):
        self.isPause = False
        self.isStop = True

    def draw_(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("Button down")
        if event == cv2.EVENT_LBUTTONUP:
            print("Button up")

    def SaveImg(self):
        cv2.imwrite("image.jpg",self.frame)

    def Restart(self):
        # if self.isStop == True:
        #     self.isStop = False
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    def CreateVideoPlayback(self,video_path = "video.mp4"):
        self.cap = cv2.VideoCapture(video_path)

        while(1):
            if self.isPause == False:
                ret, self.frame = self.cap.read()
            cv2.imshow("frame",self.frame)
            cv2.setMouseCallback('frame',self.draw_)
            if cv2.waitKey(24) & 0xFF == ord('q'):
                break
         
        self.cap.release()
        cv2.destroyAllWindows()