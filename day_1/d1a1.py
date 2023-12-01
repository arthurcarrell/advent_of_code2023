def main_d1a1(document):
    # parse the input of the text file into a list.
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    final_answer_1 = 0

    # go through each element in the document.
    for element in document:
        first_digit = None
        last_digit = None
        # now go through each character in the string.
        for character in element:
            if character in numbers:
                # this is a number. so lets check if it is the first digit.
                if first_digit == None: first_digit = int(character)
                else:
                    # if the first digit is not none, then we can set this as the last digit.
                    last_digit = int(character)
        # if the last digit is None. then set the last digit to the first digit.
        if last_digit == None: last_digit = first_digit
        final_number = int(f"{first_digit}{last_digit}")
        final_answer_1 += final_number


    return final_answer_1

if __name__ == "__main__":
    main_d1a1(open("input.txt","r").read().split("\n"))