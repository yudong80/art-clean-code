def if_confusion(x, y):
    if x > y:
        if x-5 > 0:
            x = y
            if y == y+y:
                return "A"
            else:
                return "B"
        elif x+y > 0:
            while x > y:
                x = x-1
            while y > x:
                y = y-1
            if x == y:
                return "E"
        else:
            x = 2 * x
            if x == y:
                return "F"
            else:
                return "G"
    else:
        if x-2 > y-4:
            x_old = x
            x = y * y
            y = 2 * x_old
            if (x-4)**2 > (y-7)**2:
                return "C"
            else:
                return "D"
        else:
            return "H"

print(if_confusion(2, 8))
