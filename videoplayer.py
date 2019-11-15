import cv2
import time

class VideoPlayer:
    def __init__(self,video_path):
        self.cap = cv2.VideoCapture(video_path)
        self.waitkey = cv2.waitKey(0)
        self.isStop = False

    def get_cap(self):
        return self.cap.read()
    
    def get_cap_frame(self):
        return self.cap.get(cv2.CAP_PROP_POS_FRAMES)

    def restart(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    
    def saveImg(self,frame):
        cv2.imwrite("image.jpg",frame)

player = VideoPlayer("video.mp4")

# i=0
# while(1):
#     if player.isStop == False:
#         ret,frame = player.get_cap()
        
#     # print(i,player.get_cap_frame())

#     # if i==200:
#     #     player.restart()

#     # if i==300:
#     #     player.isStop = True
    
#     # if i==400:
#     #     player.isStop = False

#     # if i==500:
#     #     player.saveImg(frame)

#     # cv2.imshow('frame', frame)
#     if cv2.waitKey(24) & 0xFF == ord('q'):
#         break
    
#     i += 1

# player.cap.release()
# cv2.destroyAllWindows()
    
    