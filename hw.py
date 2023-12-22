# a= int(input("enter number a"))
# b= int(input("enter number b"))

# if a==b:
#     print("1")
# elif a>b:
#     print("2")
# else:
#     print("3")


# a= int(input("enter number a"))
# b= int(input("enter number b"))
# c= int(input("enter number c"))
# d= int(input("enter number d"))
# if a==b:
#     print("hello")
# elif c==d:
#     print("hello")



# a= int(input("enter number a"))
# b= int(input("enter number b"))
# c= int(input("enter number c"))
# d= int(input("enter number d"))
# if a==b and c==d:
#     print("hello")


# a= int(input("enter number a"))
# if a>0:
#     print("true")
# elif a<0:
#     print("false")
# else :
#     print("zero")

# a= int(input("enter number a"))
# if a/2==0:
#     print("even")
# elif a/2 != 0:
#     print("odd")

# a= int(input("enter number a"))
# if a > 69 :
#     print("distinction")
# elif a>59 :
#     print ("first")
# elif a>39 :
#     print ("pass")
# else :
#     print ("fail")

    
# 7. What is the output of ‘APPLE’ > ‘apple’?


# 8. Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
# Cost price(in Rs)                  Tax
# >100000		          15%
# >50000 and <=100000      10%
# <=50000                                   5%

# a= int(input("enter the cost price of the bike in RS :  "))
# if a>100000:
#     print("the road tax to be paid according to the following criteria is 15%")
# elif a>50000 and a<=100000:
#     print("the road tax to be paid according to the following criteria is 10%")
# elif a <= 50000:
#     print("the road tax to be paid according to the following criteria is 5%")




# 9. Accept the age of 4 people and display the youngest one.


# a= int(input("age of first person  "))
# b= int(input("age of second person  "))
# c= int(input("age of third person  "))
# d= int(input("age of fourth person  "))

# youngest_age= min (a,b,c,d)
# print("youngest person is ", youngest_age,"yrs old")



# 10. Accept the age of 4 people and display the oldest one.

# a= int(input("age of first person  "))
# b= int(input("age of second person  "))
# c= int(input("age of third person  "))
# d= int(input("age of fourth person  "))

# eldest_age= max (a,b,c,d)
# print("eldest person is ", eldest_age,"yrs old")



# 11. Accept the percentage from the user and display the grade according to the following criteria:
# Below 25 --D
# 25 to 45  -- C
# 45 to 50 -- B
# 50 to 60 --B+
# 60 to 80 -- A
# Above 80 -- A+

# a= int(input("please insert your percentage  :  "))
# if a< 25 :
#     print ("D")
# elif a>=25 and 45>a:
#     print ("c")
# elif a>=45 and 50>a:
#     print ("b")
# elif a>=50 and 60>a:
#     print ("b+")
# elif a>=60 and 80>a:
#     print ("a")
# elif a>80:
#     print ("a+")

# 12. A company decided to give bonus to employee according to following criteria:
# Time period of service     Bonus
# More than 10 years	        10%
# >=6 and <=10                       8%
# Less than 6 years                 5%


# a=int(input("enter your time period of service in years : "))
# if a>10:
#     print("bonus ia 10%")
# elif a>=6 and a<=10  :
#     print("bonus is 8%")
# elif a<6:
#     print("bonus is 5%")




# 13. Accept three numbers from the user and display the second largest number.

# a=float(input("enter the first numbeer : "))
# b=float(input("enter the second numbeer : "))
# c=float(input("enter the third numbeer : "))

# second_largest = sorted([a,b,c])[1]

# print ("second largest number is : ",second_largest)


# 14. Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day
# Six to ten days: Rs 3/day
# 11 to 15 days: Rs 4/day
# After 15 days: Rs 5/day

# a=int(input("the number of days  :  "))
# if a<5 :
#     print ("total amount is rs : " ,a*2)
# if a>5 and a<=10 :
#     print (" total amount is rs :",5*2+a*3)
# if a<=15 and a>10 :
#     print ("total amount is rs  :",5*2+5*3+a*4 )
# if a>15 :
#     print ("total amount is rs : ",5*2+5*3+5*4+a*5)

# 15. A company decided to give bonus of 5% to employee if his/her year of service is more than 5years.
# Ask user for their salary and year of service and print the net bonus amount.

# a= int(input("enter your time of service : "))
# if a>5 :
#     print("your bonus is 5% ")
# else :
#     print("no bonus for you")

# 16. Write a program to check two strings are anagram or not.
# def are_anagrams(str1, str2):
    
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

    
#     return sorted(str1) == sorted(str2)

# # Example usage:
# string1 = "Listen"
# string2 = "Silent"

# if are_anagrams(string1, string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")


# 18. Write a Python program to display your details like name, age, address in three different lines.
# print("Name: Your Name")
# print("Age: Your Age")
# print("Address: Your Address")


# 19. Write a python program which accepts the radius of circle from user and compute the area.
# a=int(input("enter the radius of circle :  "))
# area= 22/7*a**2
# print("area = ", area)


# 20. A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks that
# can be purchased. The program should read three integers: the number of students in each of the 
# #three 

# class_a_students = int(input("Enter the number of students in class A: "))
# class_b_students = int(input("Enter the number of students in class B: "))
# class_c_students = int(input("Enter the number of students in class C: "))


# desks_class_a = (class_a_students + 1) // 2
# desks_class_b = (class_b_students + 1) // 2
# desks_class_c = (class_c_students + 1) // 2


# total_desks = desks_class_a + desks_class_b + desks_class_c


# print(f"The smallest possible number of desks needed is: {total_desks}")


# 27. N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket. How many apples will each single student
# get? How many apples will remain in the basket? The program reads the numbers N and K. 
#It should print the two answers for the questions above.
 
# N = int(input("Enter the number of students: "))
# K = int(input("Enter the number of apples: "))

# apples_per_student = K // N
# remaining_apples = K % N

# print(apples_per_student)
# print(remaining_apples)

# 28. A company decided to give bonus to employee according to following criteria:
# Time period of service     Bonus
# More than 10 years	        10%
# >=6 and <=10                       8%
# Less than 6 years                 5%


# a=int(input("enter your time period of service in years : "))
# if a>10:
#     print("bonus ia 10%")
# elif a>=6 and a<=10  :
#     print("bonus is 8%")
# elif a<6:
#     print("bonus is 5%")


# 29. Accept three numbers from the user and display the second largest number.

# a=float(input("enter the first numbeer : "))
# b=float(input("enter the second numbeer : "))
# c=float(input("enter the third numbeer : "))

# second_largest = sorted([a,b,c])[1]

# print ("second largest number is : ",second_largest)


# 30. Write a program to check whether a person is eligible for voting or not. (accept age from user)
# a=int(input("enter your age : "))
# if a>17:
#     print("you are alowed to vote")
# else:
#     print("you are not allowed to vote")

# 31. Write a program to check whether a number is divisible by 7 or not.
# number = int(input("Enter a number: "))
# if number % 7 == 0:
#     print(number, "is divisible by 7.")
# else:
#     print(number, "is not divisible by 7.")

# 32. Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur 
#                              Jal Mahal

# city = input("Enter a city: ")

# if city.lower() == "delhi":
#     print("Monument of Delhi:", "Red Fort")
# elif city.lower() == "agra":
#     print("Monument of Agra:", "Taj Mahal")
# elif city.lower() == "jaipur":
#     print("Monument of Jaipur:", "Jal Mahal")
# else:
#     print("Monument for", city, "is not available in the program.")


# 33. Write a program to whether a number (accepted from user) 
# is divisible by 2 and 3 both.
# a=int(input("enter your number"))
# if a==2 and a==3:
#     print("it is divisible by 2 and 3")
# else : 
#     print("it is not")

# 34. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter the operator (+, -, *, /): ")

# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Cannot divide by zero"
# else:
#     result = "Invalid operator"

# print("Your Answer is:", result)

# 35. Write a program to check whether a number entered is 
# three digit number or not.
# a=int(input("enter a number"))
# if a>99 and a<1000:
#     print ("it has 3 digit")
# else:
#     print(" it is not")


# 36. Accept the following from the user and calculate the percentage of class attended:
# a. Total number of working days
# b. Total number of days for absent
# After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam.



# total_working_days = int(input("Enter the total number of working days: "))
# days_absent = int(input("Enter the total number of days absent: "))
# attendance_percentage = ((total_working_days - days_absent) / total_working_days) * 100

# print("Percentage of class attended:", round(attendance_percentage, 2), "%")

# if attendance_percentage >= 75:
#     print("The student is eligible to sit in the exam.")
# else:
#     print("The student is not eligible to sit in the exam.")


# 37. Write a program to accept percentage and display the category according to the following criteria:
# Percentage                                   Category
# <40		               Failed
# >=40 and <55                             Fair
# >=55 and <65	               Good
# >=65		               Excellent	

# a= int(input("enter number a"))
# if a > 69 :
#     print("distinction")
# elif a>59 :
#     print ("first")
# elif a>39 :
#     print ("pass")
# else :
#     print ("fail")

# 38. Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
# Age		Sex	Wage/day
# >=18 and <30	M	700
# 		F	750
# >=30 and <=40	M	800
# 		F	850

# age = int(input("Enter age: "))
# sex = input("Enter sex ('M' or 'F'): ")
# days_worked = int(input("Enter the number of days worked: "))

# wage_rates = {'M': {18: 700, 30: 800}, 'F': {18: 750, 30: 850}}

# wage = 0
# for threshold_age, rate in wage_rates[sex].items():
#     if age >= threshold_age:
#         wage = rate * days_worked
#         break

# print("Wage for the given parameters:", wage)


# 39. Accept three numbers from the user and display the second largest number.


# a=float(input("enter the first numbeer : "))
# b=float(input("enter the second numbeer : "))
# c=float(input("enter the third numbeer : "))

# second_largest = sorted([a,b,c])[1]

# print ("second largest number is : ",second_largest)

# 40. Evaluate the following statements:
# a=True
# b=True
# c=True
# d=True

# 1.print(c)
# 2.print(d)
# 3.print(not a)
# 4.print(not b)
# 5.print(not c)
# 6.print(not d)
# 7.print(a and b)
# 8.print(a or b)
# 9.print(a and b or c)
# 10.print(not a or b or c)
# 11. print(not a or not b or not c)
# 12.print(not(not a or not b or not c))

a = True
b = True
c = True
d = True

print(c)
print(d)
print(not a)
print(not b)
print(not c)
print(not d)
print(a and b)
print(a or b)
print(a and b or c)
print(not a or b or c)
print(not a or not b or not c)
print(not(not a or not b or not c))