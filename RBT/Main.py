import Dictionary

if __name__ == '__main__':
    dictionary = Dictionary.Dictionary("EN-US-Dictionary")
    while True:
        print("1.Insert word\n2.Search for a word\n3.Print dictionary size\n4.Exit")
        choice = int(input(f"Choose your desired operation: "))
        match choice:
            case 1:
                word = input("Enter the desired word: ")
                dictionary.insert(word.strip())
            case 2:
                word = input("Enter the desired word: ")
                dictionary.search(word.strip())
            case 3:
                dictionary.printSize()
            case 4:
                break
