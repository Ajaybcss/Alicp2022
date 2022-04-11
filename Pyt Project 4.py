NotNumber = True
while NotNumber:
    
    try:
      def encrypted(string,shift):
        ciper=''
        for char in string:
          if char==' ' :
            ciper = ciper+char
          elif char.isupper():
            ciper=ciper+chr((ord(char)+shift-65)%26+65)
          else:
            ciper = ciper + chr((ord(char)+shift-97)%26+97)
        return ciper
        
        
      text = input(str("Enter the text - "))
      s = int(input("enter the Shift key - "))
      print("your original text is:", text)
      print("your Encryptrf text is:", encrypted(text,s))
        
      NotNumber = False
    except ValueError:
      print("Invalid, please enter a Number \n")