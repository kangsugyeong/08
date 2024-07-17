# for num in range(2, 10):
#     for ber in range(1,10):
#         print(num, "x", ber,"=",num*ber )

# def print_mul_table(num):
#     print(num)
#     for i in range(1,10):
#         num2 = num * i
#         print(num,'X',i,'=',num2)
# print_mul_table(5)

def price(a):
    # 요금을 반환하기 위해서 변수 설정(초기화)
    result = 0     #결과 저장
    b = len(a)
    if b <= 20:
        result = 50
        print("50원")
    else:
        result = 100
        print("100원")
        return result
price("으악 너무너무너무 어렵자나요")

#1.문자메시지 길이 파악 text = input(~) print(len(text))
#2.문자메시지 길이 <=20, 50원 >20, 100원
#3.사용자로부터 문자메시지 입력 받아
#4.함수로 만들어서 요금을 반환
