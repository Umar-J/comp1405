print("Choose from the following words: SOLITUDE, SNYDER, STARDOM, CALUMNY, SHROUD, or DESTROY.")

def question (sual):
    answer = input(sual).upper()
    return answer == "YES"



endE = input("does your word end with an e?").upper()
if endE =="YES":
    print("your word is solitude")
else:
    #wordD = input("is there D in the word?").upper()
    if question("is there D in your word "):
       # wordU = input("is there u in the word").upper()
        if question("does your word have u? "):
            print("your word is shroud")
        else:
         #   wordA = input("is a in your word?").upper()
            if question("is a in your word? "):
                print("Your word is stardom")
            else:
            #    wordO = input(" is O in your word?").upper()
                if question("is there o in your word? "):
                    print("your word is destroy")
                else:
                    print("Your word is snyder")
    else:
        print("your word is Calumny")

