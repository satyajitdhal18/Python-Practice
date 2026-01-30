# print("my name is satya.\tmy age is 28")
# print("my name is satya.\nmy age is 28")
# a="satya"
# b="jit"
# c=a+" "+b
# print(c,len(c))
# a="satya jit"
# print(a[5])
# a="satya"
# print(a[-4:-1])

# a="i am a boy"
# print(a.endswith("by"))
# a="i am a boy"
# print(a.capitalize())
# print(a)

# a="i play ball"
# print(a.replace("ball","cricket"))

# name=(input("user's first name:"))
# print(len(name))


# a="hin $is a Good$ but $not"
# print(a.count("$"))

# a=16
# if(True):
#     print("can vote and apply for license")

# light="pink"
# if(light == "green"):
#     print("go")
# elif(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("wait")
# else:
#     print("light is broken")

# age=14
# if(age>=18):
#     print("can vote")
# else:
#     print("can not vote")

# mark=int(input("Enter Your Mark:"))
# if(mark>=90):
#     grade = "A"
# elif(mark>=80 and mark<90):
#     grade= "B"
# elif(mark>=70 and mark<80):
#     grade= "C"
# elif(mark>=60 and mark<70):
#     grade= "D"
# else:
#     grade= "F"

# print("grade of student->", grade)


# age=90
# if(age>=18):
#     if(age>=80):
#         print("cant drive")
#     else:
#         print("Can Drive")
# else:
#     print("cant drive")

# num=int(input("Enter a number:"))

# if(num%2==0):
#     print("Even number")
# else:
#     print("Odd Number")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if(a>=b and a>=c):
    print("a is greatest",a)
elif(b>=c):
    print("b is greatest",b)
else:
    print("c is greatest",c)