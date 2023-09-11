def decode_from_whitespace(encoded_text):
    decoded_text = ""
    binary_str = ""
    for char in encoded_text:
        if char == '0' or char == '1':
            binary_str += char
        else:
            if binary_str:
                try:
                    ascii_value = int(binary_str, 2)
                    decoded_text += chr(ascii_value)
                except ValueError:
                    decoded_text += '?'  # Handle invalid binary as a placeholder
            decoded_text += char  # Append any non-binary character
            binary_str = ""
    if binary_str:
        try:
            ascii_value = int(binary_str, 2)
            decoded_text += chr(ascii_value)
        except ValueError:
            decoded_text += '?'  # Handle invalid binary as a placeholder
    return decoded_text

def receive_encoded_data(input_file):
    with open(input_file, 'r') as file:
        encoded_text = file.read()
        decoded_text = decode_from_whitespace(encoded_text)
        return decoded_text

if __name__ == "__main__":
    input_file = "encoded_data.txt"
    decoded_data = receive_encoded_data(input_file)
    print("Decoded Data:")
    print(decoded_data)
