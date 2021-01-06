try:
    f = open("PESEL.txt","r")
    g = open("PESEL_DATA.txt", "w")
    for line in f:
        PESEL = line.strip()
        num_PESEL = [int(i) for i in PESEL]
        print(num_PESEL)
        sum_PESEL = num_PESEL[0]+3*num_PESEL[1]+7*num_PESEL[2]+9*num_PESEL[3]+num_PESEL[4]+3*num_PESEL[5]+7*num_PESEL[6]+9*num_PESEL[7]
        +num_PESEL[8]+3*num_PESEL[9]
        sum_PESEL += num_PESEL[10]
        
        if sum_PESEL%10==0:
            
            num_plec = num_PESEL[9]
            if num_plec%2==0:
                plec = "kobieta"
            else:
                plec = "mężczyzna"
            y = str(num_PESEL[0])+str(num_PESEL[1])
            m = str(num_PESEL[2])+str(num_PESEL[3])
            d = str(num_PESEL[4])+str(num_PESEL[5])
            if int(m)>12:
                m = str(int(m)-20).zfill(2)
                y = "20"+y
            else:
                y = "19"+y
            g.write(f"nr {PESEL}: \n data urodzenia {d}-{m}-{y};\t płeć {plec} \n")
        else:
            print("Ostatnia cyfra numeru PESEL jest nieprawidłowa")
        print(PESEL)
    g.close()
except IOError:
    print("Plik niedostępny")
finally:
    f.close()