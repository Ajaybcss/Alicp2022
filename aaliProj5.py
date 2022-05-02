def count(a):
    f= open(a, 'r')
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    alphaD = {}
    
    for letter in alphabet:
        alphaD[letter] = 0
        
    for line in f:
        for char in line:
            alphaD[char.lower()] += 1
            
    for key in alphaD:
        print(key, alphaD[key])
        
count('Proj5.txt')