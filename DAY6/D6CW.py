#კონვერტაცია - მონაცემთ ტიპის შეცვლა.
#int
#float
#str
#bool
x1 = 4
print(x1)
print(type(x1))
print()
x2 = str(x1)
print(x2)
print(type(x2)) 
Guest_number = float(input("How many guests are coming? "))
print(Guest_number)
print(type(Guest_number))
#შედარების ოპერატორები
# ==, !=, >, <, >=, <=
#------------------------------------------------------
#1. შექმენით ცვლადი, სადაც მოათავსებ str - ს, შემდეგ გადააქციეთ integer - ად და ასევე დაუმატეთ 10.
#2. შექმენით ცვლადი, სადაც მოათავსებ float - ს, შემდეგ გადააქციეთ integer - ად.
#3. შექმენით 2 ცვლადი და შეამოწმეთ ერთმანეთ == - ს თუ არ != - ის.

x1 = input("Enter a number: ")
x1 = int(x1)
print(type(x1 + 10))

x2 = float(input("Enter another number: "))
x2 = int(x2)
print(type(x2))

z1 = input("Enter first value: ")
z2 = input("Enter second value: ")
total = z1 == z2
total2 = z1 != z2
print (total, total2)