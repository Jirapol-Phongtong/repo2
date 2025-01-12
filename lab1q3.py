
def time(v):
    a,b,c,d = v.split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if a < 7 or a > 23 or c < 7 or c > 23 or b < 0 or b > 59 or d <0 or d > 59 :
        return("Invalid")
    min = ((c*60)+d)-((a*60) + b)
    if min< 0:
        return("Invalid")

    if min <= 15:
        fee = 0
    if min > 15 and min <= 180:
        fee = 10*(min//60)
        if min % 60 > 0:
            fee = fee+10
    if min > 180 and min <= 240:
        fee = 10*(min//60) + 20
        if min == 240 :
            fee = 10*(min//60) + 10

    if min > 240 and min <= 360 :
        fee = 20*((min//60)-3)+30
        if min % 60 > 0:
            fee = fee+20
    if min > 360 :
        fee = 200
    return(fee)
value = input()
output = time(value)
print(output)
