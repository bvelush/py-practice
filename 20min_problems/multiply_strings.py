# multiply two integers represented by strings without str2int function

a = '01234567890'
b = '65'

def char2int(a):
    return ord(a)-48 # ASCII codes of 0..9 are 48..58

list(map(lambda a: print(char2int(a)), a))