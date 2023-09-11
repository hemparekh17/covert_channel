def encode_to_whitespace(text):
    encoded_text = ""
    for char in text:
        if char.isspace():  # Check if the character is a space or tab
            encoded_text += '1' if char == '\t' else '0'  # Encode space as '0' and tab as '1'
        else:
            encoded_text += char  # Keep non-space/tab characters as is
    return encoded_text

def send_encoded_data(input_text, output_file):
    encoded_text = encode_to_whitespace(input_text)
    with open(output_file, 'w') as file:
        file.write(encoded_text)

if __name__ == "__main__":
    input_text = "Hello World\tPython"
    output_file = "encoded_data.txt"
    send_encoded_data(input_text, output_file)
