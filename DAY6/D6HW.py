# 1. შექმენით ცვლადი შეინახეთ ნებისმიერი მონაცეთმა ტიპი და შეასრულეთ ყველა მონაცემთა ტიპზე კონვერტაციები.
# 2. შექმენით ცვლადები და ყველა შედარების ოპერატორზე გააკეთეთ 2-2 შედარების ოპერაციები.
# 3. მოიძიეთ ინფორმაციებ boolean - ის შესახებ.

#1 davaleba
X = input("Enter a number: ")
X_1 = int(X)
print(type(X_1))

A = input("Enter an information: ")
A_1 = float(A)
print(type(A_1)) 

S = input("Enter an information: ")   #input ავტომატურად გვაძლევებს string ტიპის მონაცემს.
S_1 = str(S)
print(type(S_1))

B = input("Enter an information: ")
B_1 = bool(B)
print(type(B_1))

a = int(99)
b = float(99)
c = str(99)
d = bool(99)
print(a, b, c, d)

#2 davaleba
x = 17
y = 20
print(x == y)
print(x == x)
print(x != y)
print(x != x)
print(x < y)
print(x > x)
print(x > y)
print(x < x)
print(x <= y)
print(y <= y)
print(x >= y)
print(y >= y)

# 3 davaleba:
# boolean არის მონაცმეთა ტიპი, ის გავძლევს მხოლოდ ორ მნიშვნელობა 0=False ან 1=True,