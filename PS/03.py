# codewars - Format a string of names like 'Bart, Lisa & Maggie'.

def namelist(names):
    total = l_name = r_name = ''

    if len(names) == 0:
        pass
    elif len(names) == 1:
        total = names[0].get('name')
    else:
        l_name = names[-2].get('name')
        r_name = names[-1].get('name')
        print(l_name, r_name)

        for i in names:
            if i.get('name')!=r_name and i.get('name')!=l_name:
                get_name = i.get('name')
                total += get_name + ', '
            elif names == []:
                continue

        total = total + l_name + ' & ' + r_name
    return total