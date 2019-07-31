# codewars - Regex validate PIN code

def validate_pin(pin):

    # try:
    #     int(pin)
    #     if (len(pin) == 4 or len(pin) == 6) and ('-', '+' not in pin):
    #         return True
    #     else:
    #         return False
    # except:
    #     return False

# li='-121'.split()
# print(li)

    lst = []
    num_lst = list(range(0,10))
    str_lst = str(num_lst)
    try:
        for i in pin:
            if i not in str_lst:
                break
                return False

            if len(pin) == 4 or len(pin) == 6:
                return True
            else:
                return False
    except:
        return False


print(validate_pin('112221'))
