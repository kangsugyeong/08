def num(a):
    result = ""
    if a % 2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result

a = int(input("숫자를 입력하세요.:"))
print(num(a))