L = [ 51, 19, 3]

myMax = 0
for x in L :
    if x % 2 == 1 :
        print myMax
        if x > myMax:
            print "Setting myMax to ", x
            myMax = x
if myMax > 0:
    print "Largest odd is ", myMax
else:
    print "No odds"
    


