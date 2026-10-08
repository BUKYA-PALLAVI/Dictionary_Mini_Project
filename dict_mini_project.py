dictionary={}
while True:
    print("\ndictionary management system")
    print("1.add a word")
    print("2.search for meaning")
    print("3.display all words")
    print("4.update meaning")
    print("5.delete word")
    print("6.exit")
    choice = input("enter your chioce: ")
    if choice == "1":
        word = input("enter the word: ").lower()
        meaning = input("enter the meaning: ")
        dictionary[word] = meaning
        print("word successfully added.....")
    elif choice == "2":
        word = input("enter the word to search: ")
        if word in dictionary:
            print("meaning:",dictionary[word])
        else:
            print("word not found in the dictionary.")
    elif choice == "3":
        if dictionary:
            print("words and their meanings:")
            for word,meaning in dictionary.items():
                print(f"{word}:{meaning}")
        else:
            print("dictionary is empty.")
    elif choice == "4":
        word = input("enter the word to update: ").lower()
        if word in dictionary:
            new_meaning = input("enter the new meaning:")
            dictionary[word] = new_meaning
            print("meaning updated successfully....")
            print("updated meaning:",dictionary[word])
        else:
            print("word not found in the dictionary")
    elif choice == "5":
        word = input("enter the word to delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print("word deleted successfully...")
        else:
            print("word not found in the dictionary")
    elif choice == "6":
        print("exiting from the dictionary...")
        break
    else:
        print("invalid choice please enter valid option to proceed.")