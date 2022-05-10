# Parent_Child_control
# ĐỒ ÁN CUỐI KÌ HỆ ĐIỀU HÀNH 19_3

**GIÁO VIÊN HỖ TRỢ: Thái Hùng Văn** 

---

# Table conttent

---

# Thông tin thành viên và bài phân công công việc

**CÔNG VIỆC CHUNG**

- Tìm hiểu tài liệu
- Bàn luận hướng giải quyết từng câu hỏi
- Họp bàn đồ án hằng ngày
- Cùng hoàn thành báo cáo.

**HỌ TÊN**

Trần Bảo Tín

Phạm Thành Đạt

Trần Vũ Việt Cường


**CÔNG VIỆC RIÊNG**

- Hoàn thành các ý chính câu 1
- Các hàm chức năng câu 2 (các chức năng trong C2.1.1, C2.1.2.2)
- Xử lí vùng găng
- Edit video demo

- Kiểm tra, chỉnh sửa câu 1
- Đảm nhận xây dựng GUI, các chức năng còn lại trong Câu 2.
- Demo video

# Các chức năng và mức độ hoàn thành.

| Nhiệm vụ | Độ hoàn thành  |
| --- | --- |
| Câu 1 | 100% |
| Câu 2 C0 | 100% |
| Câu 2 C1 | 100% |
| Câu 2 C2.1.1 | 100% |
| Câu 2 C2.1.2.1 | 100% |
| Câu 2 C2.1.2.2 | 100% |
| Câu 2 P | 100% |

# 1. Câu 1

## 1.1 **Bộ nhớ ảo (Vitural memory)**

Bộ nhớ ảo là sự trừu tuợng hóa của HĐH, nó cung cấp cho người lập trình một không gian địa chỉ lớn hơn không gian địa chỉ vật lý thực sự. Bộ nhớ ảo được thiết kế để kết hợp giữa RAM và dung lượng trên đĩa cứng.

Điều này có nghĩa là khi RAM sắp hết, bộ nhớ ảo có thể di chuyển dữ liệu từ nó sang một không gian được gọi là paging file hoặc swap file (linux). Quá trình này cho phép giải phóng RAM để máy tính có thể hoàn thành tác vụ.

Bộ nhớ ảo có thể được triển khai bằng cách phân trang hoặc phân đoạn. 

Lợi ích của bộ nhớ ảo:

- Lập trình viên không lo lắng với việc các máy tính khác nhau có kích thước bộ nhớ vật lý khác nhau.
- Phân mảnh trong môi trường đa trương,

## 1.2 **Phân trang**

### 1.2.1 Cơ chế phân trang

Cơ chế phân trang như sau. Một địa chỉ logic bao gồm hai phần, phần biểu diễn **vị trí page** và biểu diễn **vị trí phần tử** trong một page. Mọi thôi tin được lưu trong bảng mô tả ánh xạ **page table.** Từ đó có thể suy ra được địa chỉ vật lý. **NOTE**: khác với phân đoạn, mỗi trang trong phân trang có kích thước bằng nhau.

![Figure 1.1 Cơ chế phân trang](image/Untitled.png)

Figure 1.1 Cơ chế phân trang

### 1.2.2 Ánh xạ

Trong việc ánh xạ từ **Logical memory** đến **Physical memory**, cần làm rõ các điều sau:

- Ở bộ nhớ vật lý được chia thành các **frame,** có kích thước đúng bằng một page trong bộ nhớ ảo.
- Việc ánh xạ từ bộ nhớ ảo bằng cách so khớp với thông tin trong bảng mô tả **page table. Ví dụ** trong hình biên dưới, page số 0 sẽ nằm ở frame thứ 1, page 1 tương ứng frame 4.

![Figure 1.2 Phương thức ánh xạ.](image/Untitled%201.png)

Figure 1.2 Phương thức ánh xạ.

### 1.2.3 Địa chỉ ảo.

Địa chỉ luận lý gồm có:

- Số hiệu trang (**Page number**) p
- Địa chỉ tương đối trong trang (**Page offset**) d

Nếu kích thước của không gian địa chỉ luận lý là $2^m$, và kích thước của trang là $2^n$  (đơn vị là byte hay word tùy theo kiến trúc máy) thì bảng phân trang sẽ có tổng cộng $2^m / 2^n = 2^{m-n}$  mục (entry)

![Figure 1.3 Địa chỉ ảo.](image/Untitled%202.png)

Figure 1.3 Địa chỉ ảo.

## 1.3 Khảo sát thực tế trên hệ thống máy tính x86_64

Ở phần này em khảo sát trên máy tính cá nhân của em. Máy sử dụng kiến trúc x86_64 trên nhân linux.

![Figure 1.4 Thông tin máy tính cá nhân,](image/Untitled%203.png)

Figure 1.4 Thông tin máy tính cá nhân,

Dựa trên các thông tin từ hệ điều hành cung cấp cùng các thông tin mặc định của kiến trúc x86_64. Em nhận được các thông số như sau.

**Page size:** Em sử dụng lệnh `pagesize` ****để kiểm tra kích thước mỗi page. Theo như kết quả trả về đó là 4096 Byte, đồng nghĩa **frame size** cũng là 4096 Byte

![Figure 1.5 Page size.](image/Untitled%204.png)

Figure 1.5 Page size.

**Kích thước bộ nhớ ảo:** RAM + swap space = 8106180608 + 4828688384 =  12934868992 (bytes)

**Số khung trang vật lý:** Số bytes trên RAM / page size = 8106180608 / 4096 = 1979048 (bytes)

---

Các thông số trên là những thứ em có thể lấy từ máy tính. Đến phần tiếp theo em dựa vào thông tin trên [kernel linux](https://github.com/torvalds/linux/find/master). Intel `x86_64` có số địa chỉ thực chất chỉ 48 bits (16 bit trên không đuợc sử dụng và định nghĩa giá trị), 48 bit địa chỉ ảo được biễu diễn như sau:

| 9 bit PML4I
 (page map level 4 index) | 9 bit PDPTI
 (page directory pointer table index) | 9 bit PDI
 (page directory index) | 9 bit PTI
 (page table index) | 12 bit offset |
| --- | --- | --- | --- | --- |

---

**Số bit tối thiểu để quản lí các offset trong trang:** Là số bit cần thiết để đánh só các địa chỉ trong page. Ta đã có pagesize là 4096 bytes. Vậy ta cần ít nhất 12 bit để đánh các offset. Hợp lý với bảng biễu diễn trên.

**Số bit quản lí ô nhớ:** 48 bits

**Số frame logic tối đa trên không gian tiến  trình:**

- Theo lý thuyết số frame tối đa sẽ bằng  $2^{\text{bit biễu diễn địa chỉ logic}} / \text{pagesize} = 2^{48} /  2^{12} = 2^{36} \text{ frame}$
- Nhưng theo Document của linux `user-space virtual memory` chỉ có 128 TB. Vậy số frame tối đa trên `x86_64` là $2^{47} / 2^{12} = 2^{35} \text{ frame}$.

```
====================================================
Complete virtual memory map with 4-level page tables
====================================================

Notes:

 - Negative addresses such as "-23 TB" are absolute addresses in bytes, counted down
   from the top of the 64-bit address space. It's easier to understand the layout
   when seen both in absolute addresses and in distance-from-top notation.

   For example 0xffffe90000000000 == -23 TB, it's 23 TB lower than the top of the
   64-bit address space (ffffffffffffffff).

   Note that as we get closer to the top of the address space, the notation changes
   from TB to GB and then MB/KB.

 - "16M TB" might look weird at first sight, but it's an easier to visualize size
   notation than "16 EB", which few will recognize at first sight as 16 exabytes.
   It also shows it nicely how incredibly large 64-bit address space is.

========================================================================================================================
    Start addr    |   Offset   |     End addr     |  Size   | VM area description
========================================================================================================================
                  |            |                  |         |
 0000000000000000 |    0       | 00007fffffffffff |  128 TB | user-space virtual memory, different per mm
```

---

**Tài liệu tham khảo**

[linux/mm.rst at master · torvalds/linux](https://github.com/torvalds/linux/blob/master/Documentation/x86/x86_64/mm.rst)

[Paging on Intel x86-64](https://www.iaik.tugraz.at/teaching/materials/os/tutorials/paging-on-intel-x86-64/)

---

# 2. Câu 2

## 2.1 Ý tưởng thiết kế

**Theo yêu cầu của đề bài, chúng em lên ý tưởng thiết kế sàn phẩm như sau:**

- **Ứng dụng đồ hoạ, thân thiện với người dùng:** Vì là một sản phẩm có tính ứng dụng và thực tiễn, cho nên chúng em quyết định xây dựng một phần mềm ứng dụng đồ hoạ. Bên cạnh đó, mục tiêu sản phẩm là dành cho quản lí trẻ em, nên sản phẩm phải thân thiện, dễ sử dụng.
- **Áp dụng các kiến thức về quản lí tiến trình, đồng bộ hoá**: Vì là đồ án môn HDH, do đó chúng em áp dụng các kiến thức về quản lí tiến trình và đồng bộ hoá vào sản phẩm.
- **Áp dụng ổ đĩa ảo**: Áp dụng ổ đỉa ảo để lưu trữ và đồng bộ dữ liệu trong quá trình sử dụng.

**Các công nghệ, thư viện mà bọn em sử dụng:**

- **Ổ đĩa ảo:** One Drive.
- **Ngôn ngữ lập trình:** `python`
- **Các thư viện**:
    - `tkinter` : dùng để tạo đồ hoạ
    - `PIL, Pillow` : dùng thao tác với file dạng ảnh
    - `glob` : đọc thư mục
    - `threading` : dùng để tạo các tiểu trình song song.
    - `time, datetime` : dùng để thao tác với dữ liệu thời gian
    - `gTTS,  playsound` : dùng để tạo các thông báo âm thanh
    - `pyautogui, pynput` : dùng để theo dõi hình ảnh và key của trẻ.
    

**Cấu trúc file code và file, thư mục dữ liệu**:

```markdown
root
		|
		data
				|
				history # Dùng để chứa các file chứa thời gian sum còn lại của chương trình
				|     |
				|     interrupt.txt # Dùng để chứa thời điểm được phép sử dụng 
				|			              # (đề phòng trường hợp trong khoảng interrupt, 
				|										# trẻ tắt máy rồi bật lại)
				|
				user.dat # Dùng để chứa mật khẩu
				|
				status.txt # Dùng để chứa thời gian cho phép đăng nhập (nếu như mật khẩu sai lần thứ 3) 
		history_time # Dùng để lưu lịch sử sử dụng của trẻ
		|
		image # Dùng để chứa các file hình ảnh được chụp khi trẻ sử dụng máy
		|
		key # Dùng để chứa các file theo dõi key mà trẻ nhập
		|
    background.jpg # Chứa hình ảnh nền cho chương trình lấy mật khẩu
		|
		C.py # Chứa hàm thực thi chứa năng của chương trình C (khi đăng nhập thành công)
		|
		P.py # Chương trình P
		|
		thong_bao_thoi_gian.py # Dùng để xây dựng các hàm xử lí thời gian
		|
		Main.py # Chương trình C 
		|
		text.txt # Chứa các thông tin khung giờ sử dụng
		|
		flag.txt # Chứa giá trị cờ hiệu để xứ lí đồng bộ
		
```

## 2.2 Sơ bộ về chương trình Child và Parent

### 2.2.1 Chương trình Child

Các thông tin cơ bản về chương trình:
• Ngôn ngữ lập trình: Python
• Môi trường viết code:
• Môi trường thực thi: hệ điều hành Windows, chạy dưới dạng console 
applicaition.
Giải thích ý nghĩa của output:
• Nếu gặp định dạng khung giờ có dạng (ví dụ mẫu): F06:00 T06:45, có 
nghĩa đây là thể hiện cho khung giờ từ 06:00 đến 06:45.
• Nếu gặp định dạng (ví dụ mẫu: F07:30 T11:30 D60 I20, có nghĩa là trong 
khoảng thời gian từ 07:30 đến 11:30 có thể sử dụng máy, nhưng mỗi lần bật 
TRANG 13
máy thì chỉ được dùng tối đa 60 phút – sau đó máy sẽ không hoạt động cho 
đến khi đã ngắt đủ 20 phút.
Để thuận tiện cho việc báo cáo, nhóm đã thay đổi tất cả các thời gian chờ và chạy 
thành 1 phút.
II.2.2. Chương trình C
Theo yêu cầu, chương trình sẽ được chạy ở chế độ autorun. Để thực hiện việc này, 
ta cần đặt file .py chứa source code của chương trình vào folder Startup bằng cách 
nhấn tổ hợp phím Windows + R (mở hộp thoại Run) sau đó nhập vào shell:startup)
Mô tả cách chương trình hoạt động:
Bước 1:
Khi khởi động máy tính, chương trình C sẽ được tự động chạy, việc đầu tiên là 
yêu cầu người sử dụng nhập mật khẩu:
Source code:
Khi nhận được mật khẩu do người dùng nhập vào, chương trình sẽ truy cập vào 
thư mục sharing với máy của phụ huynh. Tại đó, chương trình sẽ kiểm tra mật 
khẩu mà người dùng nhập vào. Nếu mật khẩu đó là parent thì sẽ trả về P, children 
thì trả về C còn nếu không thuộc 2 mật khẩu trên thì in ra “Incorrect Password” và 
TRANG 14
bắt người dùng nhập lại nếu nhập không đúng 3 lần thì sẽ tắt máy và khóa máy 
trong 10 phút tiếp theo không được sử dụng máy nhờ vào hàm Time_can_use.
Điều này sẽ lưu khung giờ sử dụng máy vào một file riêng và chương trình sẽ
kiểm tra file này mỗi khi bật máy để xem người sử dụng đã có thể ở trong khung 
giờ được sử dụng máy hay chưa.
Bước 2:
Trường hợp mật khẩu đã nhập là của phụ huynh, chương trình sẽ in ra thông tin 
cho biết mật khẩu vừa rồi là của phụ huynh và bạn có 60 phút đếm ngược để sử
dụng máy, tính từ thời điểm này.
Hết 60 phút, chương trình sẽ quay trở lại bước 1 và người sử dụng phải nhập lại 
mật khẩu một lần nữa.
TRANG 15
Bước 3:
Trường hợp mật khẩu đã nhập là của trẻ, chương trình sẽ kiểm tra rằng trẻ đã ở
trong khung thời gian được sử dụng máy hay chưa.
Nếu hiện tại không nằm trong khung thời gian được sử dụng máy, chương trình sẽ
thông báo ra khoảng thời gian tiếp theo sử dụng máy và mở 1 tiến trình tự tắt máy 
sau 15 giây và yêu cầu nhập mật khẩu, nếu người dùng nhập đúng mật khẩu của 
parent thì sẽ được sử dụng máy tiếp.
Nếu đang trong khung thời gian có thể sử dụng máy, chương trình sẽ in ra người 
dùng đã nhập mật khẩu trẻ và các khung thời gian sử dụng và in ra thời gian còn 
lại trẻ được dùng máy tính và sau bao lâu mới được mở lại lần nữa.
Lúc này, chương trình sẽ thực hiện giám sát:
• Chạy chương trình chụp màn hình, lưu lại file chụp màn hình dựa theo 
ngày tháng năm giờ phút giây chụp vào thẳng thư mục sharing.
TRANG 16
Lệnh trong hàm main này dùng để tạo 1 tiến trình riêng sẽ chụp màn 
hình mỗi 60 giây vừa qua:
• Chạy chương trình kiểm tra thay đổi trong file của phụ huynh. Hàm 
checkDiff kiểm tra dữ liệu trong file đã bị thay đổi hay chưa, nếu đã bị
thay đổi thì chương trình sẽ cập nhật lại các khung thời gian mới.
Lệnh dưới đây được sử dụng để tạo 1 tiến trình kiểm tra file đã bị thay 
đổi hay chưa cứ 60 giây 1 lần
• Chương trình thông báo khi chỉ còn 1 phút sử dụng
Hàm checkTime có nhiệm vụ thông báo:
Hàm speakOut dùng để thông báo qua loa:
Sử dụng 2 dòng lệnh sau để tạo 1 tiến trình thông báo khi chỉ còn 1 phút
II.2.3. Chương trình P
Chương trình P được tạo ra với các chức năng sau:
II.2.3.1. Xem thông tin thời khóa biểu
Hàm xem và in ra thời khóa biểu được sử dụng máy của trẻ:
TRANG 17
Cần có một hàm để đọc ra các thông tin có trong file và trả về danh sách các giá trị
thời gian bắt đầu học, thời gian kết thúc, thời lượng mỗi lần truy cập, thời gian 
ngắt:
Output của chức năng này:
TRANG 18
II.2.3.2. Chỉnh sửa, điều chỉnh file
Vì chương trình P có thể được truy cập từ cả 2 máy (máy cha và máy mẹ) nên ở
chức năng này cần phải xử lý bài toán tránh 2 tiến trình từ 2 máy cùng đi vào 
critical section. Ở đây, nhóm sử dụng semaphore để giải quyết bài toán này:
Bước 1:
Đọc giá trị semaphore từ file flag.txt (1: cho phép tiến trình vào xử lý, 0: tiến trình 
phải đợi do có tiến trình khác đang xử lý)
Bước 2:
Kiểm tra giá trị semaphore, nếu khác 1 thì có nghĩa tiến trình cần phải đợi và quay 
lại để tiếp tục việc kiểm tra:
Nếu bằng 1 thì sẽ tạo 1 đối tượng semaphore với giá trị đầu vào là giá trị
semaphore đọc được:
Bước 3:
Đặt lại giá trị semaphore trong file flag.txt để ngăn các tiến trình khác đi vào
Bước 4:
TRANG 19
Thực hiện việc điều chỉnh và cập nhật lại file thời khoá biểu của trẻ
Bước 5:
Đặt lại giá trị semaphore lên 1 và cập nhật lại file flag.txt để đánh dấu đã xong và 
tiến trình khác có thể truy cập vào, sau đó thoát chương trình
Output của chức năng này sẽ được nhóm thể hiện trong video demo.
II.2.3.3. Xem lịch sử sử dụng máy tính của trẻ
Output chức năng này sẽ in ra lịch sử đăng nhập trên máy trẻ để ba mẹ có thể quản 
lý với mỗi dòng tương ứng là ngày tháng năm, thời gian đăng nhập trên máy
TRANG 20
III. Tham khảo
Chung:
- Slide bài giảng của thầy Thái Hùng Văn, trường Đại học Khoa Học Tự
Nhiên.
Câu 1:
- Sách Operating System Concepts của các tác giả: Abraham Silberschats; 
Peter Baer Galvin, Grey Gagne
- Tham khảo một ít từ các nguồn tài liệu ngẫu nhiên trên Internet.
Câu 2:
- https://www.geeksforgeeks.org/synchronization-by-using-semaphore-inpython/
- https://stackoverflow.com/questions/12435211/python-threading-timerrepeat-function-every-n-seconds?fbclid=IwAR1RNnOz24ajsvc7gqqA1LnJI6_1JHkD7imd2ucIcRB4CGtQIWQ4ziHZ9
