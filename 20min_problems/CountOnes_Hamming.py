# counting number of 1's in the 64-bit int

def CountOnes(A):
    A = (A & 0x5555555555555555) + ((A >> 1) & 0x5555555555555555)
    A = (A & 0x3333333333333333) + ((A >> 2) & 0x3333333333333333)
    A = (A & 0x0f0f0f0f0f0f0f0f) + ((A >> 4) & 0x0f0f0f0f0f0f0f0f)
    A = (A & 0x00ff00ff00ff00ff) + ((A >> 8) & 0x00ff00ff00ff00ff)
    A = (A & 0x0000ffff0000ffff) + ((A >> 16) & 0x0000ffff0000ffff)
    A = (A & 0x00000000ffffffff) + ((A >> 32) & 0x00000000ffffffff)
    return A