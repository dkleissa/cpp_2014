import sys

# Fill in the missing code!!!!!
# Sections labeled TODO need to be completed before the program will run!!!!
# Sections labeled TODO need to be completed before the program will run!!!!
# REMEMBER TO READ THE ASSIGNMENT PDF!!!
# REMEMBER TO READ THE ASSIGNMENT PDF!!!
# REMEMBER TO READ THE ASSIGNMENT PDF!!!

################
#  Functions   #
################
def caeser(mode, key, message):

    # An empty variable to store our converted string
    converted_str = ''

    # TODO: Complete this for loop statement to loop through
    # each character in the variable `message`, storing each character
    # in the variable `letter`
    for ____:

        #TODO: Finish this if statement that checks if letter contains an
        #alphabetic character
        if ____:

            # TODO: Convert letter to its ASCII integer number
            ascii = 

            # TODO: Add an if statement to do the caeser cipher shift.
            # If the mode is 'encrypt' then add `key` to `ascii`
            # If the mode is 'decrypt' then subtract `key` to `ascii`


            # We need to make sure we handle "wrapping" the shift
            # so we don't end up with an ascii number that is outside the
            # range of our letters
            #
            # TODO: Create an if statement that checks if the letter is either uppercase
            # or lower case.  
            #   If it is uppercase, check to see if the ascii number is greater than the ascii 
            #   number for 'Z'.  If so, subtract 26 from ascii
            #   If it is uppercase, check to see if the ascii number is less than the ascii 
            #   number for 'A'.  If so, add 26 to ascii
            #               
            #   If it is lowercase, check to see if the ascii number is greater than the ascii 
            #   number for 'z'.  If so, subtract 26 from ascii
            #   If it is lowercase, check to see if the ascii number is less than the ascii 
            #   number for 'a'.  If so, add 26 to ascii


            # TODO: convert `ascii` back to a character and add it to `converted_str`
            converted_str = 
        else:
            # TODO: since we are just encrypting letters to keep this simple, simply add letter
            # to converted_str if it is anything else but alphabetic without changing it.
            converted_str = 

    return converted_str


################
# Main Program #
################

def main(argv):
    key = 0 # start the program with the key = 0, which won't encrypt anything
    
    # Program loop
    while True:
        # TODO: Ask the user to encrypt, decrypt, set key, or quit.
        mode = 

        # Check mode
        if mode == 'quit':
            break

        elif mode == "set key":
            # TODO: Ask the user for a new key that is between 0 and 26
            input_key = 
            # TODO: convert the key from a string to an integer
            input_key = 
            # TODO: Check if the new key is greater than 26 or less than 0
            # If it is, tell the user the key is invalid
            # if it isn't, print what the new key is and set the variable `key`
            # equal to the new key value stored in `input_key`

        elif mode == "encrypt":
            # TODO: Ask the user for plaintext
            input_text = 
            # TODO: Call our function caeser() to encrypt!
            encrypted_text = 
            # TODO: Print the ciphertext stored in encrypted_text


        elif mode == "decrypt":
            # TODO: Ask the user for ciphertext
            input_text = 
            # TODO: Call our function caeser() to decrypt!
            decrypted_text = 
            # TODO: Print the plaintext stored in decrypted_text

        else:
            # TODO: Invalid mode.  Print the allowable inputs - encrypt, decrypt, set key, or quit




################
#  Main Check  #
################

# We do this since we are now writing our code so we can use functions in other files.
# This special if statement will check to see if you are running the file itself, or using
# the functions in this file in another program.  If you are running the file itself
# as the main program, Python will call the function main() for us.
if __name__ == "__main__":
    main(sys.argv[1:])

