#2) მომხმარებელს შეაყვანინეთ ასაკი და შეამოწმეთ არის თუ არა 13 ზა მეტი და 18 ის ტოლი
#3) მომხმარებელს შეაყვანინეთ რიცხვი და შეამოწმეთ არის თუ არა რიცცხვი 10 ზე ნაკლები
#4) მომხმარებელს შეაყვანინეთ სახელი და შეამოწმეთ არის თუ არა ეგ თქვენი სახელი

#2
User_Age = int(input("Enter your age: "))
Age_check = User_Age >= 13 and User_Age == 18
print(Age_check)
#3
Number_1 = int(input("Enter a number: "))
Number_check = Number_1 < 10
print(Number_check)
#4
User_Name = input("Enter your name: ")
Name_Check = User_Name == "SANDRO"
print(Name_Check)