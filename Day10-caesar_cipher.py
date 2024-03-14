alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
from logo import logo
print(logo)


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceaser(start_text, shift,cipher_direction):

     text=""
     if cipher_direction == "decode":
         shift=shift*(-1)
     for letter in start_text.lower():
         if letter  in alphabet:
             position = alphabet.index(letter)
             new_position = position + shift
             new_letter = alphabet[new_position]
             text += new_letter
         else:
             text += letter



     print(f"Here is the {cipher_direction} result {text}")

while True:
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    start_text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    ceaser(start_text,shift,cipher_direction)
    respond = input("Type 'Yes' if you wnat to  again, otherwise type 'No' ")
    if respond.lower() == "no":
        print('Goodbye!')
        break
##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
