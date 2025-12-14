def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    
    STEP-BY-STEP PROCESS:
    
    Step 1: Initialize empty result string
    Step 2: Adjust shift direction (negative for decryption)
    Step 3: Loop through each character in the text
    Step 4: Check if character is a letter
    Step 5: Determine ASCII offset (65 for 'A', 97 for 'a')
    Step 6: Convert character to position (0-25)
    Step 7: Apply shift and wrap around using modulo 26
    Step 8: Convert back to character
    Step 9: Append to result
    Step 10: Return the final encrypted/decrypted message
    
    Args:
        text: The message to encrypt or decrypt
        shift: The number of positions to shift (1-25)
        mode: 'encrypt' or 'decrypt'
    
    Returns:
        The encrypted or decrypted message
    """
    # STEP 1: Initialize empty result string
    result = ""
    
    # STEP 2: Adjust shift for decryption (reverse direction)
    if mode == 'decrypt':
        shift = -shift
    
    # STEP 3: Process each character in the text
    for char in text:
        # STEP 4: Check if the character is a letter
        if char.isalpha():
            # STEP 5: Determine ASCII offset based on case
            # 'A' = 65, 'a' = 97 in ASCII
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # STEP 6-7: Convert to 0-25, apply shift, wrap with modulo
            # Example: 'C' with shift 3
            # ord('C') = 67, ascii_offset = 65
            # (67 - 65 + 3) % 26 = 5
            shifted = (ord(char) - ascii_offset + shift) % 26
            
            # STEP 8: Convert back to character
            # 5 + 65 = 70 = 'F'
            result += chr(shifted + ascii_offset)
        else:
            # STEP 9: Keep non-alphabetic characters unchanged
            result += char
    
    # STEP 10: Return the final result
    return result


def main():
    print("=" * 50)
    print("       CAESAR CIPHER ENCRYPTION/DECRYPTION")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '3':
            print("\nThank you for using Caesar Cipher!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue
        
        # Get user input
        message = input("\nEnter your message: ")
        
        while True:
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 1 and 25!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Perform encryption or decryption
        mode = 'encrypt' if choice == '1' else 'decrypt'
        result = caesar_cipher(message, shift, mode)
        
        # Display result
        print("\n" + "-" * 50)
        print(f"Original message: {message}")
        print(f"Shift value: {shift}")
        print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} message: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()