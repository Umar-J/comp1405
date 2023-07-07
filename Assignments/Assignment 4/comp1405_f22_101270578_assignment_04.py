# Umar Jan 101270578 
from re import L


def question(ask):
    result = input(ask).upper()
    return result == "YES"

if question("Do you need instructions?"):
    print("This is a guessing game where this program tries to guess what movie youre thinking of")

actionMovie = question("is your movie a Pop-Action movie?")
parts = question("is your movie part 1 out of 2?")
    
if actionMovie:
    #action movie
    if question("does your movie have tom cruise as an actor"):
        if question("does your movie have fighter jets"):
            if parts:
                #Tom cruise, fighter jets
                print("your movie is top gun (1986) is the name of the movie")
            else:
                print("your movie is top gun maverick (2022) is the name of the movie")
        else:
            if question("is the movie about being an IMF spy?"):
                #Tom cruise, IMF Spy
                if parts:
                    #part 1
                    print("Your movie is mission impossible 1 (1996) is the name of the movie")
                else:
                    #part 2
                    print("your movie is mission impossible 2 (2000) is the name of the movie")
            else:
                #Tom cruise, crime investegtion
                question("is your movie about investigating crimes")
                if parts:
                    #part 1
                    print("your movie is jack reacher 1 (2012) is the name of the movie")
                else:
                    #part 2
                    print("Your movie is jack reacher 2 (2016) is the name of the movie")
    #not tom cruise
    else:
        if question("does your movie have Sylvester Stallone as an actor"):
            if parts:
                #Sylvester Stallone, part 1
                print("your movie is  (1982) is the name of the movie")
            else:
                #Sylvester Stallone, part 2
                print("your movie is rambo 2 (1985) is the name of the movie")
        else:
            # not Sylvester Stallone
            if parts:
                #part 1
                print("your movie is Mad Max (1979) is the name of the movie")
            else:
                #Sylvester Stallone, part 2
                print("Your movie is mad max 2 (1981) is the name of the movie")

#if not Pop-Action movie (Classic Horror movie)
else:
    if question("is your movie about a doll?"):
        #has doll
        if question("does your movie contain a nun?"):
            # Conjuring, doll, nun
            if parts:
                #part 1
                print("your movie is The Conjuring (2013) is the name of the movie")
            else:
                #part 2
                print("Your movie is The Conjuring 2 (2016) is the name of the movie")
        else:
            # Anabelle, doll, no nun
            if parts:
                #part 1
                print("Your movie is anabelle 1 (2014) is the name of the movie")
            else:
                #Part 2
                print("Your movie is Annabelle: Creation (2017) is the name of the movie")
    else:
        if question("does your movie contain a ouija board?"):
            #has ouija board
            if question("does your movie revolve around a young girl?"):
                # Exorcist - young girl and ouija board
                if parts:
                    #part 1
                    print("Your movie is exorcist (1973) is the name of the movie")
                else:
                    #part 2
                    print("Your movie is excorsit 2 (1977) is the name of the movie")
            else:
                # Whichboard - no young girl, ouija board
                if parts:
                    print("Your movie is Witchboard (1986) is the name of the movie")
                else:
                    print("Your movie is Witchboard 2 (1993) is the name of the movie")

        if question("Is it about a ghost that possesses?"):
            # has possesive ghost
            if question("Does the movie take place in Japan?"):
                # Grudge - japan and has posessive ghost
                if parts:
                    #part 1
                    print("Your movie is The Grudge (2002) is the name of the movie")
                else:
                    #part 2
                    print("Your movie is The Grudge 2 (2006) is the name of the movie")
            else:
                # Poltergeist - Possesive ghost, not in japan
                if parts:
                    #part 1
                    print("Your movie is Poltergeist (1982) is the name of the movie")
                else:
                    #part 2
                    print("Your movie is Poltergeist II (1986) is the name of the movie")
        