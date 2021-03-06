# This program takes information from the Czech National Insurance Number
# and reads the date of birth and gender.
# you can check the examples of the numbers here:
#https://www.google.com/search?q=rodn%C3%A9+%C4%8D%C3%ADslo&client=firefox-b-d&sxsrf=ALeKk00eVp_hBIHaMocG3wZYwayQrZq89A:1592068900525&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjW4pfqpv_pAhWQyKQKHQiVB0gQ_AUoAXoECBIQAw&biw=1920&bih=966

#this function is called to start the cheking process
def start():
    while True:
        question = input("Do you wish to get information from Czech National Insurance Number? Please answer yes/no and push enter: ")
        if question.lower() == "yes":
            try_again()
            completing_phase()
        elif question.lower() == "no":
            break
        else:
            print("I don't understand. Please type yes or no: ")

#if start() is answered by "yes"
def try_again():
    number_list.clear()
    number = input("Type the number including slash 'xxxxxx/xxx': ")
    for digit in range(11):
        try:
            number_list.append(number[digit])
        except IndexError:
            #if the input has letters, the error is checked in the function numbercheck() later
            pass

# first phase checks, if the input is number, if the number has 10 digits,
# and if the slash is included on the correct place
def conditions():
    while True:
        if ten_digit() + numbercheck() + slash_included() + divisible11() == 4:
            return True

# second phase gets information from the ID if the conditions from first phase are met
def completing_phase():
    conditions()
    ID_find_info()

#everytime the input is incorrect, this function is called
# this function clears and replaces the number list every time the user types a new number
def appendnewlist(copy):
    try:
        number_list.clear()
        for digit in range(11):
            number_list.append(copy[digit])
        conditions()
    except IndexError:
        conditions()

# this function checks if the length of the number is 10
def ten_digit():
    list_length = len(number_list)
    if list_length == 11:
        return (1)
    else:
        check_b = input("Wrong length, the input should have 10 numbers with the slash: ")
        appendnewlist(check_b)
        return (1)

# this function checks if the input is a number (exluding slash)
def numbercheck():
    try:
        number_connected = "".join(number_list)
        conected_numbers = number_connected[0:6] + number_connected[7:11]
    except ValueError:
        check_a = input("There are letters found in your input. Please type the numbers with the slash: ")
        appendnewlist(check_a)
    if conected_numbers.isnumeric() == True:
        return (1)
    else:
        check_c = input("Your input is not numerical! Please type the numbers with the slash: ")
        appendnewlist(check_c)
        return (1)

# this function checks if the slash is included and if it is rightly positioned
def slash_included():
    if number_list[6] == "/":
        return (1)
    else:
        check_d = input("You are missing a slash / on the 7th position: ")
        appendnewlist(check_d)
        return (1)

# this function checks if the number is divisible by number 11
def divisible11():
    try:
        number_connected = "".join(number_list)
        conected_numbers = number_connected[0:6] + number_connected[7:11]
    except ValueError:
        check_a = input("There are letters found in your input. Please type the numbers with the slash: ")
        appendnewlist(check_a)
        return (1)
    if int(conected_numbers) % 11 == 0:
        if int(conected_numbers) / 11 == 0:
            check_g = input("There is no ID card full of zeros :) Please type the ID number: ")
            appendnewlist(check_g)
        return (1)
    else:
        check_e = input("The number should be divisible by 11. Please type the ID number: ")
        appendnewlist(check_e)
        return (1)

#the function finds if there is a 0 in the first number of the day so it deletes it
def day_of_birth():
    if number_list[4] == "0":
        day = number_list[5]
    else:
        day = str(number_list[4]) + str(number_list[5])
    return day

# gender check
def gender():
    if number_list[2] == "5" or number_list[2] == "6":
        gender = "female"
        return gender
    elif number_list[2] == "0" or number_list[2] == "1":
        gender = "male"
        return gender
    else:
        check_h = input("The 3rd number in NIN is incorrect. Please correct and retry: ")
        appendnewlist(check_h)

# create ordinal suffix to the date
def ordinal():
    for number, ord in [("1", "st"), ("2", "nd"), ("3", "rd")]:
        if number_list[5] == number and number_list[4] != "1":
            ordinal = ord
            return ordinal
        else:
            ordinal = "th"
            return ordinal
# translate month number to month letter
def month():
#does a month has 01-31 days?
    month_first = ["0", "1", "2", "3"]
    if number_list[4] not in month_first:
        check_i = input("The 5th number in NIN is incorrect. Please correct and retry: ")
        appendnewlist(check_i)

#female has +5 on the 3rd position
    if gender() == "female":
        month_str = str(int(number_list[2])-5) + number_list[3]
    else:
        month_str = number_list[2] + number_list[3]

    for number, month in month_variations.items():
        if month_str in number:
            return month

# if its a female, then -5 has to be reduced from the number
    if number_list[2] == "0" or number_list[2] == "5":
        return number_list[3]
    elif number_list[2] == "6" or number_list[2] == "7":
        return str(int(number_list[2]) - 5) + number_list[3]
    else:
        return number_list[2]+number_list[3]

def year():
    # year19xx is 1900-1999
    year19xx = []
    for i in range(5,10):
        year19xx.append(str(i))
# checking the first 2 numbers which are revieling the year
# people born from 2000
    if number_list[0] == str(0) or number_list[0] == str(1):
        year = "20{}{}".format(number_list[0], number_list[1])
        return year
# people born before 2000
    elif number_list[0] in year19xx:
        year = "19{}{}".format(number_list[0], number_list[1])
        return year
    else:
        check_f = input("First number in the NIN is incorrect. Please correct and retry: ")
        appendnewlist(check_f)


# by the input information this function will get the date of birth and gender information
def ID_find_info():
    print("This person is born in {}{} {} {} and the gender is {}. ".format(
    day_of_birth(),
    ordinal(),
    month(),
    year(),
    gender()))

#months connected to numbers
month_variations = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06": "June",
"07": "July", "08": "August", "09":"September", "10":"October", "11":"November", "12":"December"}

number_list = []

start()
