import random

def random_ranges(*ranges):
    return random.choice(random.choice(ranges))
n = 0
f = open("PESEL.txt", "w")
while n < 10:
    year=str(random.randint(0,99))
    month=random_ranges(range(1, 12), range(21, 32))
    gender=str(random.randint(0,9))
    number=str(random.randint(0,999))
    if month=="02" or month=="22":
        day="28"
    elif month%2==0 and (7<month<22 or month>27): 
        day=str(random.randint(1,31))
    elif month%2!=0 and (month<8 or month<27):
        day=str(random.randint(1,31))
    else:
        day=str(random.randint(1,30))

    PESEL = (year.zfill(2)+str(month).zfill(2)+day.zfill(2)+number.zfill(3)+gender)


    num_PESEL = [int(i) for i in PESEL]
    sum_PESEL=num_PESEL[0]+3*num_PESEL[1]+7*num_PESEL[2]+9*num_PESEL[3]+num_PESEL[4]+3*num_PESEL[5]+7*num_PESEL[6]+9*num_PESEL[7]
    +num_PESEL[8]+3*num_PESEL[9]

    if sum_PESEL%10==0:
        control_number = 0
    else:
        control_number = 10 - sum_PESEL%10
    PESEL+=str(control_number)
    n+=1
    f.write(PESEL+"\n")
f.close()