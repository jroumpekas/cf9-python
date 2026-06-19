def decrypt_message(message: str) -> str:
    decrypted_message = " "
    for char in message:
        if not char.isnumeric():
            decrypted_message += char
    return decrypted_message  
  
    pass

def main():
    strange_message = "432H3525el523l52o5 523C532F52"

    print(decrypt_message(strange_message))

if __name__ == "__main__":
    main()