# Bruce Reyes 
# INST126

#define constant variables

LastLetterCode = 90 # the last number value of ASCII conversion for the alphabet
FirstLetterCode = 65 # the first number value of ASCII conversion for the alphabet
LetterRange = LastLetterCode - FirstLetterCode + 1


def CaeserCipher(message, shift):
    
    #var that is a place holder for the result to print
    result = ""

    #loop that goes through all of the letters in the string
    for letter in message.upper(): #convert to uppercase because lowercase has another numbering system
        if letter.isalpha(): #if it is an alphabetical number
            #convert to ASCII
            LetterCode = ord(letter)
            NewLetterCode = LetterCode + shift #adds shift to the number that it is on

            if NewLetterCode > LastLetterCode:
                NewLetterCode -= LetterRange 

            if NewLetterCode < FirstLetterCode:
                NewLetterCode += LetterRange

            NewLetter = chr(NewLetterCode) #converts back into a letter
            result  +=  NewLetter #adds all the letters to the blank slate of the result var
        else:
            result += letter
            
    print(result.upper())

#prompt user for message and ask for the shift
UserPhrase = input("Message to encrypt or decrypt?: ")
UserShift = int(input("Shift by how much?"))

#print the caeser cipher
CaeserCipher(UserPhrase, UserShift)




