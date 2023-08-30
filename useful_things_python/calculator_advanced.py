#Calculate the numbers using signs

def is_float(n):
    if ("." or ",") in n:
        float_n = float(n)
        return True
    else:
        try:
            int_n = int(n)
            return False
        except ValueError:
            return False

def Calculator():
    sign = input("1-> '+'     2-> '-'     3-> '*'  4-> '/'    5-> '**' \n   Select your sign using a number: ")
    error_sign = 0
    error_process = 0
    error_process2 = 0
    while sign in ["1", "2", "3", "4", "5"]:
        if error_process == 0 and error_process2 == 0:
            process = input("You selected your sign, please write first number to calculate: ")
        if (process) != "" and (process.isdigit() or is_float(process)):
            if error_process2 == 0:
                process2 = input("Please write another number for calculate: ")
            if (process2) != "" and (is_float(process) or is_float(process2) == True):
                if sign == "1":
                    print("This equals {:.}".format(float(process) + float(process2)))
                    break
                if sign == "2":
                    print("This equals {:.}".format(float(process) - float(process2)))
                    break
                if sign == "3":
                    print("This equals {:.2f}".format((float(process) * float(process2))))
                    break
                if sign == "4":
                    print("This equals {:.2f}".format((float(process) / float(process2))))
                    break
                if sign == "5":
                    print("This equals {:.}".format((float(process) ** float(process2))))
                    break
            elif (process2) == "":
                if error_process2 != 3:
                    process2 = input("Please write a number for calculate: ")  
                    error_process2 += 1
                else:
                    print("Please try again later.")
                    break
            else:
                if sign == "1":
                    print("This equals {:.}".format(int(process) + int(process2)))
                    break
                if sign == "2":
                    print("This equals {:.}".format(int(process) - int(process2)))
                    break
                if sign == "3":
                    print("This equals {:.}".format((int(process) * int(process2))))
                    break
                if sign == "4":
                    print("This equals {:.}".format((int(process) / int(process2))))
                    break
                if sign == "5":
                    print("This equals {:.}".format((int(process) ** int(process2))))
                    break
        elif process == "":
            if error_process < 3:
                process = input("Please write something: ")
                error_process += 1
            elif error_process == 3:
                print("Please try again later.")
                break
        else:
            if error_process > 2:
                print("Please try again later.")
                break
            elif error_process < 3:
                process = input("Please use numbers only: ")
                error_process += 1
    if sign not in ["1", "2", "3", "4", "5"]:
        return "Please try again later."

Calculator()