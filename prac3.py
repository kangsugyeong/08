def avg_sum(list):
    b = 0
    for a in list:
        b = b + a
    c = len(list)
    x = b/c
    return x

list = [1,2,3,4,5,6,7]
print(avg_sum(list))
