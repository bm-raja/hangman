import random

#list av Ord som spelare behöver gissa
wordlist = ['sweden','finland','norway','germany','denmark']

#spel kommer välja själv från listan.
Word = random.choice(wordlist)

#alla försökt kommer spara i den variable.
guessed = ""

#räknar fel försok, 
nooftries = 6

while nooftries > 0:

    guess = input("Enter a Letter: ")

    if guess in Word:

        print(f"Rätt! Det finns en eller fler bokstaf {guess} i Ord")
    else:
        nooftries -= 1
        print(f"fel, den ord {guess} fins inte i ord {nooftries} turn(s) left")

    guessed = guessed + guess
    wrongCount = 0

    for letter in Word:
        if letter in guessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongCount += 1


    if wrongCount == 0:
        print(f"Gratis! Ord var {Word}. you won!") 
        break
    
print(f"You have use maximum tries! ord var {Word}")
  
