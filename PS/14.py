# codewars - Bit Counting

def countBits(n):
    return bin(n).count('1')

print(countBits(0))  #, 0);
print(countBits(4))  #, 1);
print(countBits(7))  #, 3);
print(countBits(9))  #, 2);
print(countBits(10))  #, 2);