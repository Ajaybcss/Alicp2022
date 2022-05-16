#Only operates if original file is fully capitalized.

def encrypt(a):
    f = open(a, 'r')
    code = ""
    for line in f:
        string = line
    for shift in range(27):
        for c in string:
            if c.isupper() or c.islower():
                c_index = ord(c) - ord("A")
                new_index = (c_index + shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                code = code + new_character
            else:
                code += c
        print(f'\nWe revealed the encryption to be {code}.', end = '')
        code = ''
        
encrypt('textRR.txt')