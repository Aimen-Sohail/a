
#program that takes a student's score as input and prints their
#  Marksheet on predefined grading criteria.
name=(input("Enter your name: "))
Percentage=int(input
( "Enter your Percentage: "))
if Percentage >= 90:
    print("Percentage:", Percentage, "%")
    print("Grade: A+")
elif Percentage >= 80:
    print("Percentage:", Percentage)
    print("Grade: A")
elif Percentage >= 60:
      print("Percentage:",Percentage)
      print("Grade: B")
elif Percentage >= 50:
            print("Percentage:", Percentage)
            print("Grade: C")
elif Percentage >= 40:
            print("Percentage:", Percentage)
            print("Grade: D")
else:
        print("Percentage:", Percentage) 
        print("Grade:Fail")           

#Create a program that checks if a given year is a leap year and prints the result.

Year=int(input("Enter the year: "))
if (Year % 400==0) and (Year % 100==0): 
 print(Year, "is a Leap year")
elif (Year % 4==0) and ("Year 100!=0"):
  print(Year, "is a Leap year")
else:
  print(Year, "is not a Leap year")
#Write a program that converts temperatures between Celsius and Fahrenheit based on user input. 
#  : F=59×C+32
# :  C=95×(F−32)
# : K=C+273.15  
print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
choice = int(input(
"Enter your choice (1,2, ог 3): "))
if choice == 1:
        C= float(input(
"Enter temperature in Celsius: "))
        F=95*C + 32
        print(f" (C)°C is equal to (F)*F")
elif choice == 2:
       F=float(input(
"Enter temperature in Fahrenheit: "))
       C=59*(F-32)
       print(f"{F}°F is equal to (C)C")
elif choice == 3:
       C= float(input(
"Enter temperature in Celsius: "))
       K=C+ 273.15
       print(f" (C)°C is equal to (k)*k")
else:
       print("Invalid choice. Please try again.")
#Develop a program that takes three sides of a triangle as input and determines whether the triangle
#  is equilateral,isosceles, or scalene using conditional statement
A =float(input( "Enter side 1 of your Triangle: "))
B =float(input( "Enter side 2 of your Triangle: "))
C =float(input( "Enter side 3 of your Triangle: "))
if A==B==C:
  print("Your Triangle is 'Equilateral'.")
elif A == B or B==C or A==C:
  print("Your Triangle is Isosceles'."
)
else:
   print("Your Triangle is 'Scalene'.")