#Calculate the numbers using signs
import re

def is_float(n):
    if "." in n:
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
    error_process = 0
    error_process2 = 0
    error_login = 0
    sign_progress = False
    while sign in ["1", "2", "3", "4", "5"] or sign_progress == True:
        if error_process == 0 and error_process2 == 0:
            process = input("You selected your sign, please write first number to calculate: ")
        if (process) != "" and (process.isdigit() or is_float(process)):
            if error_process2 == 0:
                process2 = input("Please write another number for calculate: ")
            try:
                if ((process2) != "") and (is_float(process) or is_float(process2) == True):
                    if sign == "4" and float(process) % float(process2) == 0:
                        if float(process) % float(process2) == 0 and not float(process2) % float(process) == 0:
                            print("This equals {:,}".format(int(float(process) / float(process2))))
                            break
                        else:
                            print("This equals {:,}".format(int(float(process) / float(process2))))
                            break
                    if sign == "1":
                        print("This equals {:.2f}".format(float(process) + float(process2)))
                        break
                    if sign == "2":
                        print("This equals {:.2f}".format(float(process) - float(process2)))
                        break
                    if sign == "3":
                        print("This equals {:.2f}".format((float(process) * float(process2))))
                        break
                    if sign == "4":
                        print("This equals {:.2f}".format((float(process) / float(process2))))
                        break
                    if sign == "5":
                        print("This equals {:.2f}".format((float(process) ** float(process2))))
                        break
                elif (process2) == "":
                    if error_process2 != 3:
                        process2 = input("Please write a number for calculate: ")  
                        error_process2 += 1
                    else:
                        print("Please try again later.")
                        break
                else:
                    if sign == "4" and (int(process) % int(process2) or int(process2) % int(process) == float):
                            if int(process) % int(process2) == 0 and int(process2) % int(process) != float:
                                print("This equals {:,}".format(float(int(process) / int(process2))))
                                break
                            else:
                                print("This equals {:,}".format(float(int(process) / int(process2))))
                                break
                    if sign == "1":
                        if re.search(r"\d+\.\d{2,}$", str(int(process) + int(process2))):
                            print("This equals {:.2f}".format((float(process) + float(process2))))
                            break
                        else:
                            print("This equals {:,}".format(int(int(process) + int(process2))))
                            break
                    if sign == "2":
                        if re.search(r"\d+\.\d{2,}$", str(int(process) - int(process2))):
                            print("This equals {:.2f}".format((float(process) - float(process2))))
                            break
                        else:
                            print("This equals {:,}".format(int(int(process) - int(process2))))
                            break
                    if sign == "3":
                        if re.search(r"\d+\.\d{2,}$", str(int(process) * int(process2))):
                            print("This equals {:.2f}".format((float(process) * float(process2))))
                            break
                        else:
                            print("This equals {:,}".format(int(int(process) * int(process2))))
                            break
                    if sign == "4":
                        if re.search(r"\d+\.\d{2,}$", str(int(process) / int(process2))):
                            print("This equals {:.2f}".format((float(process) / float(process2))))
                            break
                        else:
                            print("This equals {:,}".format(int(int(process) / int(process2))))
                            break
                    if sign == "5":
                        if re.search(r"\d+\.\d{2,}$", str(int(process) ** int(process2))):
                            print("This equals {:.2f}".format((float(process) ** float(process2))))
                            break
                        else:
                            print("This equals {:,}".format(int(int(process) ** int(process2))))
                            break
            except ZeroDivisionError:
                    print("Cannot divide by zero.")
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
        error_login += 1
        answer = input("You made an incorrect entry, do you want to try again? (yes/no): ")
        if answer.lower() != ("yes" or "no"):
            error_login += 1
        if answer.lower() == "no":
            print("You know best. See you soon!")
        if answer.lower() == "yes":
            Calculator()
        if answer.lower() == "no":
            pass
        else:
            if error_login == 2:
                print("You made an incorrect again, please try again later!")

Calculator()