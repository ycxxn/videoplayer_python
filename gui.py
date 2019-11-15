import tkinter as tk
from videoplayer import VideoPlayer
import cv2

window = tk.Tk()
# top_frame = tk.Frame(window,width=320, height=240)
top_frame = tk.Frame(window)

# 將元件分為 top/bottom 兩群並加入主視窗
top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

# 建立事件處理函式（event handler），透過元件 command 參數存取
def button_restart():
    player.restart()

def button_start():
    player.isStop = False

def button_stop():
    player.isStop = True

def button_save():
    player.saveImg(frame)
    

# 以下為 bottom 群組
# bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)
# bottom_button = tk.Button(bottom_frame, text='quit', fg='black', command=echo_hello)
# # 讓系統自動擺放元件（靠下方）
# bottom_button.pack(side=tk.BOTTOM)

bottom_button1 = tk.Button(bottom_frame, text='restart', fg='black',command=button_restart)
bottom_button1.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
bottom_button2 = tk.Button(bottom_frame, text='start', fg='black',command=button_start)
bottom_button2.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
bottom_button3 = tk.Button(bottom_frame, text='stop', fg='black',command=button_stop)
bottom_button3.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
bottom_button4 = tk.Button(bottom_frame, text='save', fg='black',command=button_save)
bottom_button4.pack(side=tk.TOP, fill=tk.X, expand=tk.YES)


player = VideoPlayer("video.mp4")

while(1):
    if player.isStop == False:
        ret,frame = player.get_cap()

    cv2.imshow('frame', frame)
    if cv2.waitKey(24) & 0xFF == ord('q'):
        break
    
    window.update()

# window.mainloop()


player.cap.release()
cv2.destroyAllWindows()

