
def F(A):
    isInverted = False
    counter = 0
    for i in A:
        isOn = {
          0: False, 
          1: True
        }[i] ^ isInverted
        if not isOn:
            counter += 1 # counting it on
            isInverted ^= 1 # inverting isInverted
    return counter

a = [0, 0, 1, 0]

r = F(a)
print(r)
