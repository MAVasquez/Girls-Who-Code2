print ("I am the age wizard. What is your name?")
name = input()

print ("what is your age")
age = input()

#print(type(age))

age2 = int(age)

if age2 >= 100:
    print("wow, you old as hell")
elif age2 > 12 and age2 < 20:
    print("you are a teenager")
else:
    print("Under 100 years old? Quite the youngin'")
    
print("I'm going to tell you something about you..")
print("your name is %s and your age is %d" %(name,age2))
