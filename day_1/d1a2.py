def main_d1a2(document):
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    final_answer_2 = 0


    def replaceString(element):
        element = element.replace("one","o1e")
        element = element.replace("two","t2o")
        element = element.replace("three","t3e")
        element = element.replace("four","f4r")
        element = element.replace("five","f5e")
        element = element.replace("six","s6x")
        element = element.replace("seven","s7n")
        element = element.replace("eight","e8t")
        element = element.replace("nine","n9e")
        return element

    # go through each element in the document.
    for element in document:
        first_digit = None
        last_digit = None

        # replace words with number characters with numbers
        print(f"{element} --> ",end="")
        element = replaceString(element)
        print(element)
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
        final_answer_2 += final_number


    return final_answer_2

if __name__ == "__main__":
    main_d1a2(open("input.txt","r").read().split("\n"))