import math

def converter(deg=None, rad=None): 
    result = 0
    if deg != None:
        result = math.radians(deg)
        return f'{result} rad'
    if rad != None:
        result = math.degrees(rad)
        return f'{result} deg'
        
print(converter(rad=3))
print(converter(deg=35))