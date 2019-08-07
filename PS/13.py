# codewars - What's in a name?

def name_in_str(stri, name):
    result=''
    name = name.lower()
    stri = stri.lower()
    for i in name:
        for j in stri:
            if j == i:
                stri = stri[stri.find(j)+1:]
                result += i
                break
    if result == name:
        return True
    return False

print(name_in_str("pippippi","Pippi"))
print(name_in_str("pipipp","Pippi"))



def name_in_str(str, name):
    it = iter(str.lower())
    return all(c in it for c in name.lower())


def name_in_str(text, name):
    for c in text.lower():
        if c == name[0].lower():
            name = name[1:]
            if not name:
                return True
    return False