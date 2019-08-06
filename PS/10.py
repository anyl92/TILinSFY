#codewars - RGB To Hex Conversion

def rgb(r, g, b):
    rgb_list = [r, g, b]
    rgb_range = list(range(0, 256))
    hex_str = ''
    hex_list = []

    for i in rgb_list:
        if len(i) == 1:
            hex_list.append('0x0' + hex(i))

        if i in rgb_range:
            hex_list.append(hex(i))
        elif i > 255:
            hex_list.append('0xFF')
        elif i < 0:
            hex_list.append('0x00')
        
    for i in range(len(rgb_list)):
        map(str, hex_list)
        hex_str += hex_list[i][2:]
        
    return hex_str.upper()

    # if hex_list[i] in range:
    #     for i in range(len(hex_list)):
    #         if not hex_list[i][-1] == '0':
    #             hex_str += hex_list[i][2:]
    #         else:
    #             hex_list.pop(i)
    #             zero = '00'
    #             hex_list.insert(i,zero)
    #             hex_str += zero
    # return hex_str.upper()

print(rgb(0,0,0)) # "000000"