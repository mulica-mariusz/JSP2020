def conversion(r,g,b):
    Cmax = max(r/255,g/255,b/255)
    Cmin = min(r/255,g/255,b/255)
    delta = Cmax - Cmin
    v= Cmax
    s=0
    h=0
    if Cmax==0:
        s=0
    else:
        s=delta/Cmax
    if delta==0:
        h=0
    elif Cmax==(r/255):
        h=60*((g/255-b/255)/delta % 6)
    elif Cmax==(g/255):
        h=60*((b/255-r/255)/delta +2)
    elif Cmax==(b/255):
        h=60*((r/255-g/255)/delta +4)
    return "S: "+str(100*round(s,3))+"% V: "+str(100*round(v,3))+"% H: "+str(round(h))

print(conversion(222,133,51))