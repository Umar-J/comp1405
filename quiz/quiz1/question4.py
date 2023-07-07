print("Choose from the following words: PLUCKY, TUCKER, ATKINS, MUSKOXEN, GRIMES, or SQUAWK.\n")

def question (ask):
    answer = input(ask).upper()
    return answer == "YES"

if question("is k in the word "):
    if question("is O in the word? "):
        print("the word is muskoxen ")
    else:
        if question("is E in the word? "):
            print("the word is trucker ")
        else:
            if question("is A in the word "):
                if question("is Q in the word "):
                    print("the word is squawk ")
                else:
                    print("the word is atkins ")
            else:
                print("the word is plucky ")           
else:
    print("the word is grimes ")
