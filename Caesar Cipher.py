alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Caesar Cipher code")


    
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#This code allows for the user to input a shift of greater than 26, then we just divied that number by 26 and use the remainder 
#This allows for an accurate shift even with large numbers
shift = shift % 26 


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= 26:
                new_position = new_position - 26
            elif new_position < 0:
                new_position = new_position + 26
            end_text += alphabet[new_position]
        else: 
            end_text += char
        
    print(f"The {cipher_direction}d is {end_text}")
    

caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

keep_asking = True
while keep_asking:
    again = input("Do you have another message you would like to encode/decode? ").lower()
    if again != "no":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    else: 
        keep_asking = False


