from random import randint

##FUNCTIONS

def level2(numlist):
    numSum = 0

    for num in numlist:
        if num % 3 == 0 or num %5 == 0: #number is either a multiple of 3 or 5
            numSum += num #numSum = numSum + num
            print(num)
    print("Final sum")
    print(numSum)


def level3(numlist):
    primeSum = 0

    #part 1: iterate through the list
    for num in numlist:

        prime = True
        for x in range(2,num):
            if num % x == 0:
                prime = False

        if prime == True:
            print(num)
            primeSum += num

## RUNNING CODE


randomlist = []
for x in range(100):
    randnumber = randint(10,99)
    randomlist.append(randnumber)

level2(randomlist)
