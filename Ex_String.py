# Bài 1 Viết hoa toàn bộ chữ cái đầu từ trong câu cho trước nhập vào từ bàn phím. Các chữ cái còn lại viết thường.

n = int(input("Nhap vao n: "))
lst = []
for i in range(n):
    lst.append(input(f"Nhap vao chuoi {i + 1}: "))

for i in range(n):
    print(f"Test {i + 1}: {lst[i].title()}")


# Bài 2. Đếm số lượng nguyên âm, phụ âm trong câu cho trước.
# "a" "i", "e", "o", "u"

nguyen_am = 0
phu_am = 0
str = "Hello"
for i in range(0, len(str), 1):
    if(str[i].lower() == "a"):
        nguyen_am += 1
    elif(str[i].lower() == "e"):
        nguyen_am += 1
    elif (str[i].lower() == "i"):
        nguyen_am += 1
    elif (str[i].lower() == "u"):
        nguyen_am += 1
    elif (str[i].lower() == "o"):
        nguyen_am += 1
    else:
        phu_am += 1
print(nguyen_am)
print(phu_am)

# Bài 3. Đếm số từ có trong một chuỗi kí tự cho trước nhập vào từ bàn phím.

def count_word():
    str = input(f"Nhap vao chuoi: ")
    word = str.split()
    return len(word)

n = int(input("Nhap vao n: "))
for i in range(0, n, 1):
    kt = count_word()
    print(f"Text {i + 1}: {kt}")

# Bài 4. Liệt kê các từ theo thứ tự xuất hiện trong câu. Các từ phân tách nhau bằng 1 dấu cách.

#############################################################################################
# NGUON: https://www.geeksforgeeks.org/python-remove-unwanted-spaces-from-string/
# KEYWORD: "python string remove extra whitespace"

# initializing string
test_str = "GfG is good         website"

# printing original string
print("The original string is : " + test_str)

# using split() + join()
# remove additional space from string
res = " ".join(test_str.strip().split())

# printing result
print("The strings after extra space removal : " + str(res))

# #############################################################################################
# Cac phat hien moi: "str.isspace()" neu chuoi la khoan trong "   " thi tra ve gia tri "True" nguoc lai "False"
#                    "str.strip()" bo khoan trang co trong chuoi
# VD: str = " abca "; dung "str.strip(' a')" => str = "bc"
# VD: str = " abcba "; dung "str.strip(' ac')" => str = "bcb"

n = int(input(f"Nhap vao n: "))
for i in range(0, n, 1):
    str = input(f"Nhap vao chuoi {i + 1}: ")
    newStr = " ".join(str.strip().split())
    print(f"Text {i + 1}: {newStr}")

# Bài 5. Tìm số lần xuất hiện của chuỗi s2 trong chuỗi s1.

def kiem_tra_chuoi_con(s1, s2):
   if s2 in s1:
       print(s1.count(s2))
   else:
       print('Chuoi "{}" khong xuat hien trong chuoi "{}"'.format(s2, s1))

n = int(input(f"Nhap vao n: "))
for i in range(n):
    s1 = input(f"Nhap vao chuoi 1: ")
    s2 = input(f"Nhap vao chuoi 2: ")
    print(f"Text {i + 1}: ")
    kiem_tra_chuoi_con(s1, s2)

# Bài 6. Thay thế toàn bộ chuỗi old bởi chuỗi new trong chuỗi string

n = int(input(f"Nhap vao n: "))
for i in range(n):
    str1 = input(f"Nhap vao chuoi: ")
    str2 = input(f"Nhap vao chuoi NEW: ")
    str3 = str1.replace(str1, str2)
    print(f"New Text {i + 1}: {str3}")

# Bài 7. Hiển thị các từ sao cho chúng chỉ xuất hiện duy nhất 1 lần theo đúng thứ tự xuất hiện từ đầu chuỗi đến cuối chuỗi.

n = int(input(f"Nhap vao n: "))
for i in range(n):
    word = [x for x in input(f"Nhap vao chuoi {i + 1}: ").split()]
    s = set()
    print(f"Text {i + 1}: ")
    for j in word:
        if j not in s:
            print(f"{j}", end=" ")
            s.add(j)

# Bài 8. Đếm số lần xuất hiện của các từ có trong chuỗi kí tự cho trước.

