from art import *

print(logo)


def caesar(plain_text, shift_amount, shift_direction):
    message = ""
    if shift_direction == "decode":
        shift_amount *= -1
    for position in range(len(plain_text)):
        if plain_text[position] in alphabet:
            message += alphabet[(alphabet.index(plain_text[position]) + shift_amount) % 26]
        else:
            message += plain_text[position]
    print(f"The {shift_direction}d text is: {message}")


stop_program = False
while not stop_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, shift_direction=direction)
    restart_program = input("Do you want to restart the cipher program? Type 'yes' "
                            "if you want to go again. Otherwise type 'no'").lower()
    if restart_program == "no":
        stop_program = True
        print("Good bye!")
