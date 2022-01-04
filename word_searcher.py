def search(words, wordLength, excludedLetters, includedLetters, includedLettersWithExcludedPositions, includedLettersWithIncludedPositions):
    resultWords = []
    for word in words:
    
        if len(word) != wordLength:
            continue
            
        word = word.lower()
        
        tempIncludedPool = []
        viable = True
        for letter in excludedLetters:
            try:
                word.index(letter)
                viable = False
                break
            except ValueError:
                continue
            
        if not viable: 
            continue
            
        for key in includedLettersWithExcludedPositions:
            #tempIncludedPool.append(key)
            for pos in includedLettersWithExcludedPositions[key]:
                if word[pos] == key:
                    viable = False
                    break
            if not viable:
                break
            
            try:
                word.index(key)
            except ValueError:
                viable = False
                break
            
        if not viable:
            continue
        
        for key in includedLettersWithIncludedPositions:
            #tempIncludedPool.append(key)
            for pos in includedLettersWithIncludedPositions[key]:
                if word[pos] != key:
                    viable = False
                    break
            if not viable:
                break
            
        if not viable:
            continue
           
        for letter in includedLetters:
            try:
                word.index(letter)
            except ValueError:
                viable = False
                break
            
        if not viable:
            continue
    
        resultWords.append(word)
    return resultWords
    
    
def main():
    #credit to https://github.com/dwyl/english-words for the provided dictionary
    #If you want to use a different word list, change the value of $filename
    filename = "words_alpha.txt"
    f = open(filename, "r")
    words = f.read().split()
    maxlen = 0
    for word in words:
        if len(word) > maxlen:
            maxlen = len(word)

    choice = "-1"

    wordLength = -1
    excludedLetters = []
    includedLetters = []
    includedLettersWithExcludedPositions = {}
    includedLettersWithIncludedPositions = {}
    
    print("Welcome to the word searcher program.\nYou will be asked to input parameters and given instructions for formatting which are important.\nPlease note that the provided word bank contains only alphabetical words\n and as a result the word searcher does not natively support searching with numeric or symbolic string data.\n")
    
    while choice != "exit":
        choice = input("Please enter desired word length to search for.\n If you input nothing or any other non positive integer value, all word lengths will be considered in the search.\n At any time you may input \"exit\" without quotes to exit the program.\n")
        choice_int = -1
        try: 
            choice_int = int(choice)
            if choice_int > 0:
                if choice_int > maxlen:
                    print(f"Entered int is higher than the length of the longest word in the provided dictionary.\n Automatically reducing to the maximum value of the dict ({maxlen})\n")
                    wordLength = maxlen
                else:
                    wordLength = choice_int
        except ValueError:
            if choice == "exit":
                break
        
        print(f"Word Length to search for set to {wordLength}\n")
        
        exit = False
        while True:
            choice = input("(optional) Please enter any letters to exclude from search results, separated by a space.\n")
            if choice == "exit": 
                exit = True
                break
                
            if len(choice) == 0:
                break
             
            excludedLetters = choice.split()
            for letter in excludedLetters:
                if len(letter) > 1:
                    print(f"Excluded letters incorrectly specified for letter {letter} (Seems like its more than one letter). Please try again\n")
                    break
                
                if letter.lower() < 'a' or letter.lower() > 'z':
                    print(f"Excluded letters incorrectly specified for letter {letter} (Seems like theres a non-letter included). Please try again\n")
                    break
                       
        if exit:
            break
        
        while True:
            choice = input("(optional) Please enter any letters to include in search results at set positions.\nTo format, please separate the letters and positions with commas and separate each set of letters and indices with a space.\nE.g.: If you want to search words with an \'i\' in index 2 (0 based indexing) and an 'r' in indices 1 and 4\nyou would type \"i,0 r,1,4\" (without the quotes)\n")
            if choice == "exit":
                exit = True
                break
            
            if len(choice) == 0:
                break
            
            chunks = choice.split()
            cdex = 0
            for chunk in chunks:
                separatedChunk = chunk.split(',')
                letter = separatedChunk[0].lower()
                if len(separatedChunk[0]) != 1 or letter < 'a' or letter > 'z':
                    print(f"Chunk index {cdex} contains a non-letter in the 0th index. Please reformat and try again.\n")
                    continue
                    
                positions = []
                for dex in range(1, len(separatedChunk)):
                    pos = separatedChunk[dex]
                    posint = -1
                    try:
                        posint = int(pos)
                    except ValueError:
                        print(f"Chunk index {cdex} contains a non integer position value at subindex {dex}\n(or {dex+1} if you count the letter at the beginning of the chunk)\nPlease reformat and try again.\n")
                        continue
                    if posint < 0 or (wordLength > 0 and posint >= wordLength):
                        print(f"Chunk index {cdex} contains a negative integer position value or one which exceeds the provided wordLength at subindex {dex}\n(or {dex+1} if you count the letter at the beginning of the chunk)\nPlease reformat and try again.\n")
                        continue
                    else:
                        positions.append(posint)
                  
                includedLettersWithIncludedPositions[letter]=positions
                cdex += 1  
        if exit:
            break
            
        while True:
            choice = input("(optional) Please enter any letters to include in search results with positions at which to exclude those letters.\nTo format, please separate the letters and positions with commas and separate each set of letters and indices with a space.\nE.g.: If you want to search words with an \'i\' not at index 2 (0 based indexing) and an 'r' not at indices 1 or 4\nyou would type \"i,0 r,1,4\" (without the quotes)\n")
            if choice == "exit":
                exit = True
                break
                
            if len(choice) == 0:
                break
            
            chunks = choice.split()
            cdex = 0
            for chunk in chunks:
                separatedChunk = chunk.split(',')
                letter = separatedChunk[0].lower()
                if len(separatedChunk[0]) != 1 or letter < 'a' or letter > 'z':
                    print(f"Chunk index {cdex} contains a non-letter in the 0th index. Please reformat and try again.")
                    continue
                    
                positions = []
                for dex in range(1, len(separatedChunk)):
                    pos = separatedChunk[dex]
                    posint = -1
                    try:
                        posint = int(pos)
                    except ValueError:
                        print(f"Chunk index {cdex} contains a non integer position value at subindex {dex}\n(or {dex+1} if you count the letter at the beginning of the chunk)\nPlease reformat and try again.\n")
                        continue
                    if posint < 0 or (wordLength > 0 and posint >= wordLength):
                        print(f"Chunk index {cdex} contains a negative integer position value or one which exceeds the provided wordLength at subindex {dex}\n(or {dex+1} if you count the letter at the beginning of the chunk)\nPlease reformat and try again.\n")
                        continue
                    else:
                        positions.append(posint)
                  
                includedLettersWithIncludedPositions[letter]=positions
                cdex += 1  
                
        if exit:
            break
            
        while True:
            choice = input("(optional) Please enter any letters to include in search results with unspecified locations.\nLetters duplicated from the excluded letters list and the included letters list which has explicitly excluded positions are not allowed.\n")
            if choice == "exit":
                exit = True
                break
                
            if len(choice) == 0:
                break
   
            includedLetters = choice.split()
            for letter in includedLetters:
                if len(letter) > 1:
                    print(f"Included letters incorrectly specified for letter {letter} (Seems like its more than one letter). Please try again\n")
                    break
                
                if letter.lower() < 'a' or letter.lower() > 'z':
                    print(f"Included letters incorrectly specified for letter {letter} (Seems like theres a non-letter included). Please try again\n")
                    break
                    
                if letter in excludedLetters:
                    print(f"Included letter found in excluded list. Please remove it or exit to restart the search process.\n") 
                    break
                    
                if letter in includedLettersWithExcludedPositions:
                    print(f"Included letter found in included list with excluded positions. Please remove it or exit to restart the search process.\n")
                    break

        if exit:
            break
        
        result = search(words, wordLength, excludedLetters, includedLetters, includedLettersWithExcludedPositions, includedLettersWithIncludedPositions)
        print(f"The results of your search will follow. There are {len(result)} words of length {wordLength} and the other provided search options.\n")
        choice = input("Enter just the letter x (non case-sensitive) to view the rest of the search parameters.\nAny other input, excluding the exit command, will reveal the results without reviewing those parameters.\n")
        if choice == "exit":
            break
            
        if choice.lower() == "x":
            print(f"excludedLetters: {excludedLetters}\nincludedLettersWithExcludedPositions: {includedLettersWithExcludedPositions}\nincludedLettersWithIncludedPositions: {includedLettersWithIncludedPositions}")
        
        print(result)

if __name__ == "__main__": 
    main()
     
