def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        elif char.isdigit():
            shift_amount = shift if encrypt else -shift
            result += str((int(char) + shift_amount) % 10)
        else:
            result += char
    return result

# --- Main ---
msg = input("Enter message: ")
shift = int(input("Shift value: "))

enc = caesar_cipher(msg, shift)
print("Encrypted:", enc)

choice = input("Do you want to decrypt the message? (yes/no): ").strip().lower()
if choice in ['yes', 'y']:
    dec = caesar_cipher(enc, shift, encrypt=False)
    print("Decrypted:", dec)
else:
    print("Exiting without decryption.")
