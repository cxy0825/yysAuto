from pyautogui import click 
# import pyautogui
import time
import random
from datetime import datetime
import win32gui
import win32api
import threading
from keyboard import wait


#司机号的窗口句柄
SJ_HWND ="0"
#打手号的窗口句柄
DS_HWND ="0"
def randomTime(min:int,max:int):
    return round(random.uniform(min,max),2) 
def nowTime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#切换窗口
def switchWindow(HWND):
    if HWND !="0":
        print(f"{nowTime()} 开始切换窗口",flush=True)
        win32gui.SetForegroundWindow(HWND)
        print(f"{nowTime()} 开始切换结束",flush=True)
        return True
    else:
        print("窗口获取错误重新获取")
        return False

def yuhun(step:datetime):
    # x = round(random.uniform(-60,60)) 
    # y = round(random.uniform(-60,60)) 
    #移动鼠标
    print(f"{nowTime()} 司机号点击挑战",flush=True)
    click()
    # pyautogui.moveRel(x,y,round(random.uniform(0.5,1.2),1) )
    #开始进入游戏
    time1 = step+randomTime(1,2);
    print(f"{nowTime()} 下一次点击间隔:{time1}",flush=True)
    time.sleep(time1)
    #移回鼠标
    # pyautogui.moveRel(-x,-y,round(random.uniform(0.5,1.2),1) )
    #等待多少秒后执行点击  点击领取奖励
    #第一个账号领取
    click()
    time2 = 1+randomTime(1,2);
    print(f"{nowTime()} 下一次点击间隔:{time2}",flush=True)
    #等待多少秒后点击 领取奖励
    time.sleep(time2)
    #领取奖励完成
    click()
    print(f"{nowTime()} 司机号领取完毕:{time2}",flush=True)
    print(f"{nowTime()} 切换打手号",flush=True)
    #切换打手号窗口
    flag = switchWindow(DS_HWND)

    time.sleep(0.6)
    #第二个账号开始领取
    click()
    time2 = 1+randomTime(1,2);
    print(f"{nowTime()} 下一次点击间隔:{time2}",flush=True)
    # 等待多少秒后点击 领取奖励
    time.sleep(time2)
    #领取奖励完成
    click()
    print(f"{nowTime()} 打手号领取完毕:{time2}",flush=True)
    print(f"{nowTime()} 切换回司机号",flush=True)
    #切换司机窗口
    flag2 = switchWindow(SJ_HWND)

    #睡眠
    time3 = 3+randomTime(1,2.2)
    print(f"{nowTime()} 等待{time3}后继续下一次",flush=True)
    time.sleep(time3)

#获取当前鼠标所在位置的窗口句柄
def getHWND():
    point = win32api.GetCursorPos()
    hwnd = win32gui.WindowFromPoint(point)
    return hwnd

#监听键盘事件
#司机号的设置
def keyZ():
    print("鼠标放入司机号窗口按 z 设置司机号")
    while True:
        wait('z')
        global SJ_HWND
        SJ_HWND = str(getHWND())
        print("司机号"+str(SJ_HWND))
#打手号的设置
def keyX():
    print("鼠标放入司机号窗口按 x 设置打手号")
    while True:
        wait('x')
        global DS_HWND
        DS_HWND = str(getHWND())
        print("打手号"+str(DS_HWND))

if __name__=="__main__":
    # time.sleep(3)
    # point = win32api.GetCursorPos()
    # hwnd = win32gui.WindowFromPoint(point)
    # print(hwnd)
    # 
    t1 = threading.Thread(target =keyZ)
    t2 = threading.Thread(target =keyX)
    t1.start()
    t2.start()

    # print("选择功能")
    # print("1. 挖土")
    # # print("2. 连点器")
    # key = input("选择功能\n")
    
    input("任意键开始")
    print(SJ_HWND)
    print(DS_HWND)
    #校验窗口句柄
    while (SJ_HWND=="0" or DS_HWND=="0"):
        print("账号设置未完成",flush=True)
        time.sleep(0.5)

    stepTime2 = 22
    stepTime2 = input("输入战斗时间 默认是22s,建议根据自己的战斗时间填写\n")
    print("10秒后开始任务,把鼠标移动到按钮上")
    count = 1;
    time.sleep(10)
    while True:
        yuhun(float(stepTime2))
        print(f"执行完成,完成了{count}次",flush=True)
        count =count+1
    
    # if key=="1":
       
    # elif key=="2":
    #     print("先把鼠标移动到按钮上")
    #     key2 = input("输入战斗时间 默认是18s,建议根据自己的战斗时间填写\n")
    #     print("10秒后开始任务,调整好窗口顺序")
    #     time.sleep(15)
    #     # pyautogui.click()
    #     while True:
    #         yuhun(float(key2))
    # else: 
    #     print("没有!!!!!!!!!!!!!!!!!!")
    