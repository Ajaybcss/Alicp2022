allCharacters = []


while True:
    print("1 -- Add movie(s)")
    print("\n2 -- Inventory")
    print("\n3 -- Print last entry")
    print("\n4 -- Exit")
    choice = float(input("\nEnter your choice: "))
    if choice == 1:
        notDone = True
        
        while notDone:
           charList=[]
           movie= input("\nName of movie? - ")
           charList.append(movie)
           director= input("\nWho is the director? - ")
           charList.append(director)
           runtime= int(input("\nWhat is the runtime of the movie in minutes? - "))
           hours= runtime//60
           minutes = runtime%60
           print(f"{hours} hours & {minutes} minutes")
           trueRun = (f"{hours} hours & {minutes} minutes")
           charList.append(trueRun)
           genre= input("\nWhat is the genre? - ")
           charList.append (genre)
           rating= input("\nWhat is the movie rating? - ")
           charList.append(rating)
           reviews = str(input("\nWhat were the movie reviews? Put the rating out of ?/10. - "))
           charList.append(reviews)
    
           allCharacters.append(charList)
           print(f"""
           """)

           answer = input('Have you added all your titles? Type "Yes" or "No": ')
           if answer == "Yes":
                  notDone = False
           else:
               print("\nTime for another")
    if choice == 2:
        print(allCharacters)

    if choice == 3:
        print("\nYour latest entry into our catalouge was:")
        print("\n*****************************************")
        print("\nMovie: ", charList[0])
        print("\nDirector: ", charList[1])
        print("\ntrueRun: ", charList[2])
        print("\ngenre: ", charList[3])
        print("\nrating: ", charList[4])
        print("\nreviews: ", charList[5])
        print("\n******************************************")

        answer = input('\nWould you like to go back to the main menu? Type "Yes" or "No": ')
        if answer == ("Yes"):
            notDone = False
            print ("\nOff you go!")
        else:
            print("\nYou're going back to the menu, whether you like it or not.")
    if choice == 4:
         print("\nEnd of program, good bye!")
         exit()
         if choice > 4:
             print("\nInvalid input, please try again. ")
             
    
    
