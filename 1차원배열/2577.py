a = int(input())
b = int(input())
c = int(input())

sum = str(a * b * c)                #숫자를 곱해서 str 형으로 변환

for number in range(10):
    count = sum.count(str(number))  #str형으로
    print(count)