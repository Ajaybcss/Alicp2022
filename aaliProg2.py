def product(a):
    f= open(a, "r")
    
    product = 1
    for line in f:
        product = product * int(line)
        
        
    print(product)
     
    f.close()