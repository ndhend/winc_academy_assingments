
def computepay(h, r):
    if h <= 40:
       up_to_40 = h*r
       return up_to_40
    if h > 40:
       over_40 = (40*r)+(h-40)*(r*1.5)
       return over_40
print(computepay(45, 10.5))