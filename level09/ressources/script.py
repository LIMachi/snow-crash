import sys

def decode_text(file_path):
    with open(file_path, 'r') as file:
        encoded_text = file.read()
    
    decoded_chars = []
    for index, char in enumerate(encoded_text):
        decoded_value = ord(char) - index
        # Ensure the decoded value is within the valid ASCII range
        if decoded_value < 0:
            decoded_value += 256  # Wrap around using modulo
        decoded_char = chr(decoded_value)
        decoded_chars.append(decoded_char)
    
    decoded_text = ''.join(decoded_chars)
    return decoded_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decode_script.py <file_path>")
    else:
        file_path = sys.argv[1]
        decoded_text = decode_text(file_path)
        print("Decoded text:")
        print(decoded_text)
