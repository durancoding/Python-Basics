city = ("Antalya", "Bursa", "Samsun", "Kastamonu", "Ankara")
number1 = 0
for i in city:
    number1 += 1
    print(number1, "-" , i)



input_for_num = int(input("Enter a number between 1-5: "))
city = ("Antalya", "Bursa", "Samsun", "Kastamonu", "Ankara")
number1 = 0
for i in city:
    number1 += 1
    if input_for_num == number1:
        print(number1, "-", i)

while True:
    input_for_num = int(input("Enter a number between 1-5: "))
    if 1 <= input_for_num <= 5:
        break
    else:
        print("Invalid input. Please try again.")