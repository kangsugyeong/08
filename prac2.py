def level_score(score):
    result = ""
    if score >= 81:
        result = "A"
    elif score >= 61:
        result = "B"
    elif score >= 41:
        result = "C"
    elif score >= 21:
        result = "D"
    elif score >= 0:
        result = "E"
    return(result)
score = int(input("점수를 입력하세요.: "))
result = level_score(score)
print(result)