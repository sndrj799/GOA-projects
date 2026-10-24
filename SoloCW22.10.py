#შექმენი ცვლადები, გააკეთე ორი დავალება ჯერ ყველა შედარების ოპერატორებზე შეასრულე შედარების ოპერაციები შემდეგ ცვლადებში კი ყველა ლოგიკურ ოპერატორებზე შეასრულე ლოგიკური ამოცანები.
#დაწერე რას გამოიტანს print(True and False or False and True or True or False and True and True or True or False and True or False)
v_1 = 12
v_2 = 7
result = v_1 > v_2
print(result)

v_3 = 5
v_4 = 3
result = v_3 < v_4
print(result)

v_5 = 88
v_6 = 55
result = v_5 == v_6
print(result)

v_7 = 88
v_8 = 55
result = v_7 != v_8
print(result)

v_9 = 44
v_10 = 7
result = v_9 <= v_10
print(result)

v_11 = 9
v_12 = 32
result = v_11 >= v_12
print(result)

T = 12
G = 32
print(T + G > 22)

T = 22
G = 88
H = 122
print(T * G == 2)

R = True
K = False
print(R and K)

R = True
K = False
print(R or K)

R = True
K = True
print(R and K)

R = False
K = True
print(R and K)

R = True
K = True
print(R or K)

R = False
K = True
print(R or K)

R = False
K = False
print(R or K)

R = False
K = False
print(R and K)

print(True and False or False and True or True or False and True and True or True or False and True or False)
# პასუხი არის TRUE რადგან ჯერ სრულდება and ოპერატორი, რადგან აქვს მეტი პრივილეგია და შემდგომ OR ოპერატორი. ამ შემთხვევაში ჯერ ვიღებთ True-ს და შემდგომ სრულდება or ოპერატორი რაც გავძლევს საბოლოო შედეგს True