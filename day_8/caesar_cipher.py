import caesar_cipher_ascii_art
print(caesar_cipher_ascii_art.logo)

continue_cipher = True

while continue_cipher:
    operation = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
    if operation == "encode":
        print("encoding")
    elif operation == "decode":
        print("decoding")
    else:
        print("Your input is not valid, please try again.")
        continue

    continue_yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    continue_cipher = True if continue_yes_or_no == "yes" else False
