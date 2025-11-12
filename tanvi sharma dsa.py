'''marks = int(input("enter your marks:- "))
if marks>=90:
         print("your grade is A+")

elif marks>=80:
          print("your grade is A")
elif marks>=70:
          print("your grade is B+")
elif marks>=60:
          print("your grade is B")
elif marks>=50:
          print("your grade is C")
elif marks>=40:
          print("your grsde is D")

for i in range(1,9,2):
         print(i)
for i in range(1,9,1):
         print(i)
for i in range(10):
         print(i)'''
'''#list
student= ["asdf","sdgf","dfgh","werty"]
for i in student:
         print(i)
#odd even
print("odd number")
for i in range(1,10,2):
      print(i)
print("even number")
for i in range


for i in range(50,550,50):
      print(i)'''
'''a = 3
for i in range(11):
         print(i*a)
a = 2
for  i in range(11):
       print(a*i)
'''
'''a =int(input("enter the number"))
for i in range(11):
    print(a,"*",i,"=",a*i)   
'''
'''a = int(input("enter no. for table"))
for i in range(11):
    print(a,"*",i,"=",a*i)'''
'''for char in "palak shakti rajput":
            print(char)'''
'''i = 1
while i<=5:
    print(i)
    i = i+1'''
'''i = 1
while True:
      prnit(i)
      i=i+1'''
'''def happy():
    print("hello, world")
happy()'''
'''def add(a,b):
   print(a+b)
add(4,5)'''
'''def odd(num):
   if num%2==1:
        print("the num is odd")
   else :
      print("even")

odd(73)'''
'''def calculator( a,b,operator):
   if operator =="+":
       print(a+b)
   elif marks >=75:
      print("B")
   elif marks >=60:
      print("C")
   else:
       print("D")

calculator(4,6,"+")'''
#print("Welcome User")
def run():
    print("PRESS 1 For Continue")
    print("PRESS 2 For Exit")
    a=int(input("PRESS Number to Continue or Exit"))
    if a==1:
        pass
    elif a == 2:
      print("Thanks For Visiting")

run()

def book():
    print("PRESS 1 For Book1")
    print("PRESS 2 For Book2")
    print("PRESS 3 For Book3")
    print("PRESS 4 For Book4")

    b=int(input("enter book number to continue"))
    if b==1:
          print("book1:--book description")
          run() 
    elif b==2:
       run()
    else:
     print("book not found")

book()
    
