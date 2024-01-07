def med5bil(a,b,c,d,e):
    if a>=b and b>=c and c>=d and d>=e:
        return c
    elif a>=c and c>=b and b>=d and d>=e:
        return b
    elif b>=c and c>=a and a>=d and d>=e:
        return a
    elif a>=b and b>=d and d>=c and c>=e:
        return d
    else:
        return e
print (med5bil(5,6,2,1,3))
print (med5bil(5,3,6,2,9))