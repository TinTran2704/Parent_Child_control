import os
import time
from datetime import datetime
import pyttsx3
import pyautogui
import sys
from threading import Timer

link_parent = r'C:\Users\ADMIN\OneDrive\TinTran\data'
link_child = r'C:\Users\ADMIN\OneDrive\TinTran\data_child'
class RepeatTimer(Timer): #Hàm tạo tiến trình lặp sau 1 khoảng thời gian
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def Shut_down(): #Hàm shutdown
    os.system('shutdown -s')

def Time_can_use(n = 10): #Hàm cấm máy tính mở được trong n phút tới
    time_can_use = link_child + r'\\time_use.txt.txt'
    with open(time_can_use, 'w') as f:
        t = getTimeNow()
        hour = int(t[:2])
        minute = int(t[3:]) + n
        if minute >= 60:
            hour += 1
            minute -= 60
        f.write('{}:{}'.format(hour, minute))

def inputPass(): #Hàm nhập mật khẩu
    count = 0
    password = link_parent + r'\\password.txt'
    file = open(password, 'r')
    pass_ = file.readlines()
    while True:
        password = input('password: ')

        if password == pass_[1].strip():
            print('You input Child password')
            return "C"
        elif password == pass_[0].strip():
            print('You input Parent password')
            return "P"
        else:
            print('Incorrect password!')
            count += 1
        if count == 3:
            Time_can_use()
            Shut_down()
            return None

def getTimeNow(): #Lấy thời gian hiện tại
    return datetime.now().strftime("%H:%M")

def hour_to_num(string): #Đổi giờ phút thành phút
    if string == '' or string == None:
        return 0
    return int(string[0:2])*60 + int(string[3:])

def checkinTime(time_from, time_to): #Kiểm tra có trong thời gian mở máy hay không
    now = datetime.now().strftime("%H:%M")
    if hour_to_num(time_from) < hour_to_num(now) and hour_to_num(time_to) > hour_to_num(now):
        return True
    return False

def Time_plus_minute(time, minu):  #Cộng thời gian cho 1 số phút
    hour = int(time[:2])
    minute = int(time[3:]) + minu
    if minute >= 60:
        hour += 1
        minute -= 60
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    return '{}:{}'.format(hour, minute)

def readfile_time(filename): #Đọc file time.txt bên folder cha
    file = open(filename, 'r')
    list_el = list()
    for line in file.readlines():
        list_el.append(line.strip().split(' '))
    return list_el

def min_time_to_use(list_time): #Kiếm thời gian gần nhất mở được máy
    temp = list()
    temp_from = list()
    for time in list_time:
        t_from, t_to, t_duration ,t_rest = readLine(time) 
        temp_from.append(t_from)
        if hour_to_num(getTimeNow()) < hour_to_num(t_from):
            temp.append(hour_to_num(t_from) - hour_to_num(getTimeNow()))
        temp.append(1440 + hour_to_num(t_from) - hour_to_num(getTimeNow())) #Trong trường hợp hết khung giờ hôm nay
    return min(temp)

def readLine(line): #Lưu các thông số trong 1 dòng từng biến
    time_from = None
    time_to = None
    time_duration = 0
    time_rest = 0
    for item in line:
        if item[0] == 'F':
            time_from = item[1:]
            continue
        if item[0] == 'T':
            time_to = item[1:]
            continue
        if item[0] == 'D':
            time_duration = item[1:]
            continue
        if item[0] == 'I':
            time_rest = item[1:]
            continue
    return time_from, time_to, int(time_duration) ,int(time_rest)

def speakOut(string): #Đọc ra loa
    speech = pyttsx3.init()
    speech.say(string)
    speech.runAndWait()

def inform_next_use(list_time): #thông báo giờ gần nhất có thể sử dung
    t = min_time_to_use(list_time)
    h = int(t/60)
    m = t - h*60
    inform = '{} hours and {} minutes left until using computer time.'.format(h,m)
    speakOut(inform)
 
def next_use(list_time):  #thông báo lần tiếp theo sử dụng
    t = min_time_to_use(list_time)
    h = int(t/60)
    m = t - h*60
    inform = '{} hours and {} minutes fo the next using computer time.'.format(h,m)
    print(inform)

def takeScreenshot(): #Chụp màn hình theo format year_month_day_hour_minute_second
    filename = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.png'
    take_screen = pyautogui.screenshot()
    take_screen.save(r'C:\Users\ADMIN\OneDrive\TinTran\data_child\ScreenShot\\{}'.format(filename))

def Print_now_use(from_, to, dur, rest): #In ra khung thời gian được sử dụng bây giờ
    print('From: {}'.format(getTimeNow()))
    if dur == None:
        dur = 0
    minu = 0
    after = ''
    if hour_to_num(to) <= hour_to_num(getTimeNow()) + int(dur) or int(dur) == 0:
        after = 'To: {}'.format(to)
        print(after)
        minu = hour_to_num(to) - hour_to_num(getTimeNow())
    else:
        time = Time_plus_minute(getTimeNow(), dur)
        after = 'To: {}'.format(time)
        print(after)
        minu = dur
    print('Inform time use of Children')
    print('Shut down after {} minutes'.format(minu))
    history = link_child + r'\\history.txt'
    with open (history, 'a') as file:
        now = datetime.now().strftime("%d:%m:%Y, %H:%M")
        file.write('{} - {}\n'.format(now, after[4:]))
        file.close()

def run(n): #Máy chạy n phút
    print('\nInform time use of computer')
    print('Use the computer for {} minutes'.format(n))
    time.sleep(n*60)

def rest(n): #Máy nghỉ n phút
    Time_can_use(1)
    os.system('shutdown -l')
    
time_list = link_parent + r'\time.txt'
list_time = readfile_time(time_list)
def checkDiff(filename = r'C:\Users\ADMIN\OneDrive\TinTran\data\time.txt', list_time = list_time): #Kiểm tra file bị thay đổi
    list_new = readfile_time(filename)
    if list_new != list_time:
        print('File have been changed')
        for i in range(len(list_time)):
            list_time[i] = list_new[i]

def checkTime(): #Thông báo khi còn 1 phút sử dụng máy
	speakOut("You have 1 minutes left using the computer")

def Children_do():
    time_list = link_parent + r'\time.txt'
    list_time = readfile_time(time_list)
    #Print_time_use(list_time)
    check_in_time = False
    for item in list_time:
        t_from, t_to, t_duration ,t_rest = readLine(item) 
        if checkinTime(t_from, t_to): #Kiểm tra có trong khung thời gian sử dụng hay không
            Print_now_use(t_from, t_to, t_duration ,t_rest)
            next_use(list_time)
            check_in_time = True
            #take screenshot
            take_scr = RepeatTimer(60, takeScreenshot) #Khởi tạo tiến trình screenshot
            checkfile_change = RepeatTimer(60, checkDiff) #Khởi tạo tiến trình xem file có bị đổi hay không
            take_scr.start()
            checkfile_change.start()
            if t_duration > 0 and hour_to_num(getTimeNow()) + t_duration < hour_to_num(t_to):
                count_time = Timer((t_duration - 1)*60,checkTime) #Sau n - 1 phút thì thông báo gần hết giờ sử dụng
                count_time.start()
                run(t_duration)
                take_scr.cancel()
                checkfile_change.cancel()
                rest(t_rest)

            else: 
            	count_time = Timer(hour_to_num(t_to) - 1 - hour_to_num(getTimeNow())*60,checkTime) #Sau n - 1 phút thì thông báo gần hết giờ sử dụng
                run(hour_to_num(t_to) - hour_to_num(getTimeNow()))
                Shut_down()
                return None

    if check_in_time == False: #Cờ kiểm tra xem có nằm trung khung thời gian được sử dụng hay không
        inform_next_use(list_time)
        flag = False
        shut_down = Timer(15, Shut_down) #Create thread
        shut_down.start()
        while True:
            c = inputPass()
            if c == "P":
                flag = True
                shut_down.cancel() #Nếu nhập đúng mật khẩu của parent thì hủy lệnh Shutdown
                break

def main():
    time_use = link_child + '\\time_use.txt'
    with open(time_use, 'r') as f:
        time_wait = f.readline().strip()
        n = hour_to_num(getTimeNow()) - hour_to_num(time_wait)
        if n > 0:
            f.close()
        else: 
            speech = pyttsx3.init()
            inform = '{} minutes left until using computer time.'.format(n)
            speech.say(inform)
            speech.runAndWait()
            f.close()
            Shut_down()
            
    c = inputPass()
    while True:
        if c == "P":
            run(60)
            c = inputPass()
            continue
        if c == "C":
            Children_do()

if __name__ == "__main__":
	main()