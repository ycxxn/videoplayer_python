import cv2

class CVideoPlayer:
    def __init__(self):
        self.isPause = False
        self.isStop = True
        self.tracker = cv2.TrackerBoosting_create()
        self.roi_list = []
        self.ok = False
        self.tracker_type = 'BOOSTING'
        self.index = 0
        self.drawing = False

    def tracker_select(self,index):
        tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
        tracker_type = tracker_types[index]

        if tracker_type == 'BOOSTING':
            self.tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            self.tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            self.tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            self.tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            self.tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            self.tracker = cv2.TrackerGOTURN_create()

        self.tracker_type = tracker_type
        self.index = index

    def draw_(self,event,x,y,flags,param):
        drawing = False 

        if event == cv2.EVENT_LBUTTONDOWN :
            self.drawing = True 
            self.isPause = True
            self.ix,self.iy = x,y

        # elif event == cv2.EVENT_LBUTTONUP:
        elif event == cv2.EVENT_MOUSEMOVE:
            print(self.drawing)
            if self.drawing == True:
                cv2.rectangle(self.frame,(self.ix,self.iy),(x,y),(255,0,0),1)
                self.roi_list.append([self.ix,self.iy,x-self.ix,y-self.iy])
                self.ok = self.tracker.init(self.frame,(self.ix,self.iy,x-self.ix,y-self.iy))
                self.isPause = False
                print("fuck")

        if event == cv2.EVENT_MBUTTONDOWN:
            self.roi_list = []
            self.tracker_select(self.index)

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
            print(self.tracker)
            if self.isPause == False:
                ret, self.frame = self.cap.read()
            if not ret:
                break

            timer = cv2.getTickCount()
            ok, bbox = self.tracker.update(self.frame)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            if ok:
            # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(self.frame, p1, p2, (255,0,0), 2, 1)
                i+=1
                print(i)

            cv2.putText(self.frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
            cv2.putText(self.frame, self.tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)

            cv2.imshow("frame",self.frame)
            cv2.setMouseCallback('frame',self.draw_)
        
            if cv2.waitKey(24) & 0xFF == ord('q'):
                break
         
        self.cap.release()
        cv2.destroyAllWindows()