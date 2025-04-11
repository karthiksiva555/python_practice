import caesar_cipher_ascii_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesar_cipher_ascii_art.logo)


def invoke_caesar_cipher():
    continue_cipher = True

    while continue_cipher:
        operation = input("Type 'encode' to encrypt, 'decode' to decrypt: ").lower()
        if operation == "encode" or operation == "decode":
            encode_or_decode(operation)
        else:
            print("Your input is not valid, please try again.")
            continue

        continue_yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        continue_cipher = True if continue_yes_or_no == "yes" else False


def encode_or_decode(operation):
    message = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number: "))

    result_message = ""

    for ch in message:
        if ch in alphabet:
            index = (alphabet.index(ch) + shift) % 26 if operation == "encode" else alphabet.index(ch) - shift
            result_message += alphabet[index]
    print(f"Here's the {operation}d result: {result_message}")


invoke_caesar_cipher()