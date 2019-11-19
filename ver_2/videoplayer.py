import cv2

class CVideoPlayer:
    def __init__(self):
        self.isPause = False
        self.isStop = True
        self.tracker = cv2.TrackerBoosting_create()
        self.roi_list = []
        self.ok = False

    def draw_(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN :
            self.ix,self.iy = x,y

        elif event == cv2.EVENT_LBUTTONUP:
            cv2.rectangle(self.frame,(self.ix,self.iy),(x,y),(255,0,0),1)
            self.roi_list.append([self.ix,self.iy,x-self.ix,y-self.iy])
            self.ok = self.tracker.init(self.frame,(self.ix,self.iy,x-self.ix,y-self.iy))

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
        i= 0
        while(1):
            if self.isPause == False:
                ret, self.frame = self.cap.read()

            if self.ok:
            # Tracking success
                bbox = self.tracker.update(self.frame)
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(self.frame, p1, p2, (255,0,0), 2, 1)
                i+=1
                print(i)

            cv2.imshow("frame",self.frame)
            cv2.setMouseCallback('frame',self.draw_)
        
            if cv2.waitKey(24) & 0xFF == ord('q'):
                break
         
        self.cap.release()
        cv2.destroyAllWindows()