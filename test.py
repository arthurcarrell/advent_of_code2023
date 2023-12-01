from colorama import Fore, Back, Style
from day_1.d1a1 import main_d1a1
from day_1.d1a2 import main_d1a2


def test(function,expectedresult):
    output = function
    if output == expectedresult:
        print(f"{Style.BRIGHT}[ {Fore.GREEN}PASSED{Fore.RESET} ]{Style.RESET_ALL} returned {output}")
    else:
        print(f"{Style.BRIGHT}[ {Fore.RED}FAILED{Fore.RESET} ]{Style.RESET_ALL} returned {output} expected {expectedresult}")

# -- DAY 1 --
default_values = open("day_1/defaultinput.txt","r").read().split("\n")
input_values = open("day_1/input.txt","r").read().split("\n")

test(main_d1a1(input_values),55386)
test(main_d1a2(input_values),54824)
