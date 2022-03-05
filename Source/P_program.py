import os
import sys
import time
import threading

# Tạo class Time để lưu trữ giá trị thời gian dưới dạng giờ và phút
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

# Đọc và lấy các giá trị từ file
def getDataFromFile(filename):
    with open(filename, 'r') as file:
        time_from_list = []
        time_to_list = []
        duration_list = []
        interupt_list = []

        for i, line in enumerate(file.readlines()):
            line = line.strip().split()
            signal = line[0].find(':')
            time_from_list.append(
                Time(int(line[0][1:signal]), int(line[0][signal+1:])))
            signal = line[1].find(':')
            time_to_list.append(
                Time(int(line[1][1:signal]), int(line[1][signal+1:])))

            if len(line) > 2:
                for index, temp in enumerate(line):
                    if index > 1:
                        if temp[0] == 'D':
                            duration_list.append((i, int(temp[1:])))
                        elif temp[0] == 'I':
                            interupt_list.append((i, int(temp[1:])))

        return time_from_list, time_to_list, duration_list, interupt_list

# Điều chỉnh các giá trị thời gian trong file theo nhu cầu người dùng
def configTimeSchedule(time_from_list, time_to_list, duration_list, interupt_list):
    menu = '''BANG DANH SACH CAC GIA TRI THOI GIAN MUON THAY DOI
    F: Thoi gian bat dau
    T: Thoi gian ket thuc
    D: Thoi luong su dung
    I: Thoi gian ngat
    E: Thoat va luu thay doi'''

    be_changed = True
    while be_changed:
        line_number = int(input('Nhap dong du lieu can thay doi gia tri (danh so tu 0): '))
        while True:
            print(menu)

            label = input(
                '\nNhap nhan gia tri can thay doi theo bang danh sach: ')
            if label == 'F':
                F_label = input(
                    'Thay doi: A. Gio -- B.Phut -- C. Gio va phut ?  ')
                if F_label == 'A':
                    hour = int(input('Nhap gio muon thay doi (0 -24): '))
                    time_from_list[line_number].hour = hour
                elif F_label == 'B':
                    minute = int(input('Nhap phut muon thay doi (0- 60): '))
                    time_from_list[line_number].minute = minute
                else:
                    hour = int(input('Nhap gio muon thay doi (0 -24): '))
                    minute = int(input('Nhap phut muon thay doi (0- 60): '))
                    time_from_list[line_number].hour = hour
                    time_from_list[line_number].minute = minute

            elif label == 'T':
                T_label = input(
                    'Thay doi: A. Gio -- B.Phut -- C. Gio va phut ?  ')
                if T_label == 'A':
                    hour = int(input('Nhap gio muon thay doi (0 -23): '))
                    time_to_list[line_number].hour = hour
                elif T_label == 'B':
                    minute = int(input('Nhap phut muon thay doi (0- 59): '))
                    time_to_list[line_number].minute = minute
                else:
                    hour = int(input('Nhap gio muon thay doi (0 -23): '))
                    minute = int(input('Nhap phut muon thay doi (0- 59): '))
                    time_to_list[line_number].hour = hour
                    time_to_list[line_number].minute = minute

            elif label == 'D':
                index_list = [i[0] for i in duration_list]
                if line_number not in index_list:
                    print('Hien chua co thoi luong su dung cho dong nay!')
                    decision = input(
                        'Ban co muon thiet lap thoi luong khong (Y/N)?  ')
                    if decision == 'Y':
                        duration = int(
                            input('Nhap thoi luong muon thiet lap: '))
                        duration_list.append((line_number, duration))

                else:
                    duration = int(input('Nhap thoi luong muon thay doi: '))
                    for i in range(len(duration_list)):
                        if duration_list[i][0] == line_number:
                            duration_list[i] = (line_number, duration)
                            break

            elif label == 'I':
                index_list = [i[0] for i in interupt_list]
                if line_number not in index_list:
                    print('Hien chua co thoi gian ngat su dung cho dong nay!')
                    decision = input(
                        'Ban co muon thiet lap thoi gian ngat khong (Y/N)?  ')
                    if decision == 'Y':
                        interupt = int(
                            input('Nhap thoi gian ngat muon thiet lap: '))
                        interupt_list.append((line_number, interupt))

                else:
                    interupt = int(
                        input('Nhap thoi gian ngat muon thay doi: '))
                    for i in range(len(interupt_list)):
                        if interupt_list[i][0] == line_number:
                            interupt_list[i] = (line_number, interupt)
                            break
            else:
                break

        question = input('Ban co muon tiep tuc thay doi khong (Y/N)?  ')
        if question == 'Y' or question == 'y':
            be_changed = True
        elif question == 'N' or question == 'n':
            print('\nFile da duoc thay doi thanh cong!')
            be_changed = False

# Viết và lưu lại file
def writeToFile(filename, time_from_list, time_to_list, duration_list, interupt_list):
    with open(filename, 'w') as fileout:
        for i in range(len(time_from_list)):
            if time_from_list[i].hour == 0:
                fileout.write('F00')
            else:
                if time_from_list[i].hour >= 1 and time_from_list[i].hour <= 9:
                    fileout.write(f'F0{time_from_list[i].hour}')
                else:
                    fileout.write(f'F{time_from_list[i].hour}')

            if time_from_list[i].minute == 0:
                fileout.write(':00')
            else:
                if time_from_list[i].minute >= 1 and time_from_list[i].minute <= 9:
                    fileout.write(f':0{time_from_list[i].minute}')
                else:
                    fileout.write(f':{time_from_list[i].minute}')

            if time_to_list[i].hour == 0:
                fileout.write(' T00')
            else:
                if time_to_list[i].hour >= 1 and time_to_list[i].hour <= 9:
                    fileout.write(f' T0{time_to_list[i].hour}')
                else:
                    fileout.write(f' T{time_to_list[i].hour}')

            if time_to_list[i].minute == 0:
                fileout.write(':00')
            else:
                if time_to_list[i].minute >= 1 and time_to_list[i].minute <= 9:
                    fileout.write(f':0{time_to_list[i].minute}')
                else:
                    fileout.write(f':{time_to_list[i].minute}')

            for j in range(len(duration_list)):
                if duration_list[j][0] == i:
                    fileout.write(f' D{duration_list[j][1]}')
                    break

            for j in range(len(interupt_list)):
                if interupt_list[j][0] == i:
                    fileout.write(f' I{interupt_list[j][1]}')
                    break

            fileout.write('\n')

# Xem thời khóa biểu của trẻ 
def viewSchedule(filename):
    print('\n==============THOI KHOA BIEU=================\n')
    with open(filename, 'r') as file:
        for i, line in enumerate(file.readlines()):
            print('Day {} - {}\n'.format(i + 1, line))

# Xem lịch sử đăng nhập vào máy của trẻ
def viewHistoryAction(filename):
    print('\n===============LICH SU DANG NHAP TREN MAY CUA TRE===============\n')
    with open(filename, 'r') as file:
        for line in file.readlines():
            print(line)
    
# Xử lý trường hợp các tiến trình cùng đi vào critical section sử dụng semaphore
def checkFile(flagfile, filename):
    semaphore = None
    while True:
        with open(flagfile, 'r') as file:
            semaphore = int(file.readline())

        #Gía trị đầu tiên của semaphore = 1
        print(semaphore) 
        
        # Nếu semaphore = 0 có nghĩa là đang có một tiến trình khác xử lý 
        if semaphore != 1:
            time.sleep(2)
            continue
        
        #Nếu semaphore = 1, cho phép tiến trình thực hiện
        #Tạo 1 đối tượng semaphore với giá trị là 1 số nguyên để biểu diễn số lần gọi phương thức acquire() và release()
        # để tăng giá trị ban đầu khởi tạo
        
        semaphore = threading.Semaphore(semaphore)
        
        # Giảm counter xuống 1
        semaphore.acquire()

        #Viết vào file flag.txt giá trị semaphore mới để biết được đang có tiến trình xử lý
        with open(flagfile, 'w') as file:
            file.write(str(semaphore._value))
        
        print(semaphore)
                
        #Thực hiện việc điều chỉnh file thời khóa biểu của trẻ
        time_from_list, time_to_list, duration_list, interupt_list = getDataFromFile(
            filename)
        configTimeSchedule(time_from_list, time_to_list,
                           duration_list, interupt_list)
        writeToFile(filename, time_from_list, time_to_list,
                    duration_list, interupt_list)
        
        
        #Tăng counter lên 1
        semaphore.release()
        
        #Set lại giá trị semaphore để biết đã hoàn thành và trả lại cho các tiến trình khác đi vào xử lý
        with open(flagfile, 'w') as file:
            file.write(str(semaphore._value))
        print(semaphore)
        break

#In ra chức năng chương trình P thực hiện
def drawMenu():
    print('=================CAC CHUC NANG CUA CHUONG TRINH P=====================')
    print('\n1. Doc file va xem file')
    print('\n2. Chinh sua file')
    print('\n3. Xem lich su dang nhap cua tre')
    print('\n0. Thoat')

if __name__ == '__main__':
    link_parentfile = r'C:\Users\ASUS\OneDrive\Sharing\data'
    link_childfile = r'C:\Users\ASUS\OneDrive\Sharing\data_child'
    
    while True:
        drawMenu()
        
        choice = int(input('\n\nNhap lua chon: '))
        if choice < 0 or choice > 3:
            print('\nLua chon khong hop le. Xin vui long nhap lai!')
            os.system('pause')
        
        elif choice == 0:
            print('\nThoat thanh cong')
            os.system('pause')
            break
        
        elif choice == 1:
            time_from_list, time_to_list, duration_list, interupt_list = getDataFromFile(link_parentfile + r'\\time.txt')
            viewSchedule(link_parentfile + r'\\time.txt')
            os.system('pause')
            
        elif choice == 2:
            checkFile(link_parentfile + r'\\flag.txt', link_parentfile + r'\\time.txt')
        
        elif choice == 3:
            viewHistoryAction(link_childfile + r'\\history.txt')
            os.system('pause')