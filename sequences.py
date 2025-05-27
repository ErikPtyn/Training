def sequence(n):
    u = 3
    for i in range(n):
        u = 4 * u - 6
    return u
    
print(sequence(13))
