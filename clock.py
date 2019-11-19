import tkinter
import time
import threading

import tkinter.font as tkFont

#创建应用程序窗口，设置标题和大小
root = tkinter.Tk()
root.title('作答时间')
root['width'] = 800
root['height'] = 120

TimerOver = 0

#创建Text组件，放置一些文字


#创建倒计时按钮组件

ft = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD)
btnTime = tkinter.Label(root,fg = 'white',bg = 'red', text='', font=ft)
btnTime.place(x=120, y=35, width=500, height=60)



def stop():
    for i in range(300,-1,-1):
        minute = int(i/60)
        sec = i%60
        btnTime['text'] = '剩余作答时间 : ' + str(minute)+ '分' + str(sec) + '秒'
        time.sleep(1)
    btnTime['text'] = "作答超时"
    time.sleep(5)
    print("计时结束")
    root.destroy()



# 创建并启动线程
def startTimer():
    t = threading.Thread(target=stop)
    t.start()
    root.mainloop()



