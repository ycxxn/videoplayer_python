import cv2

class CVideoPlayer:
    def __init__(self):
        self.isPause = False
        self.isStop = True

        # Mouse Event
        self.drawing = False
        self.mode = True 
        self.ix,self.iy = -1,-1
        self.roi_list = []
        #

    def draw_(self,event,x,y,flags,param):

        if event == cv2.EVENT_LBUTTONDOWN :
            # self.drawing = True
            # if self.drawing == True:
            self.ix,self.iy = x,y

        elif event == cv2.EVENT_LBUTTONUP:
            # self.drawing = False
            # if self.drawing == True:
            cv2.rectangle(self.frame,(self.ix,self.iy),(x,y),(255,0,0),1)
            # print(self.ix,self.iy,x,y)
            # print("xmin:{xmin} ymin:{ymin} xmax:{xmax} ymax:{ymax}".format(xmin=self.ix,ymin=self.iy,xmax=x,ymax=y))
            self.roi_list.append([self.ix,self.iy,x,y])
                # print(self.roi_list)
                # self.ix,self.iy=-1,-1
            # self.drawing = False
        if event == cv2.EVENT_MBUTTONDOWN:
            self.roi_list = []

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
            if ret == False:
                break
            print(self.roi_list)
            cv2.imshow("frame",self.frame)
            cv2.setMouseCallback('frame',self.draw_)
            if cv2.waitKey(24) & 0xFF == ord('q'):
                break
         
        self.cap.release()
        cv2.destroyAllWindows()