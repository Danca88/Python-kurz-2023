import math

original_number = input("Zadej telefonni cislo: ")
number = original_number.replace(" ","")

def check(number: int):
    if len(number) == 9:
        return True
    elif (len(number) == 13) and (number[0:4] == "+420"):
        return True
    else:
        return False

if check(number):
    message = input("Zadej zpravu: ")
    SMSprice = 3
    message_price = math.ceil(len(message)/180)*SMSprice
    print(f"Cena zpravy je {message_price} Kc.")
else:
    print("Neplatne telefonni cislo.")