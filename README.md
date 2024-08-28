
Read the `README.md` file before using the repo

---

# File Cryptography

## Project Overview

This project involves a Python script that performs encryption and decryption on text files using a Caesar cipher. The script allows users to encrypt a plain text message or decrypt an already ciphered message.

## Project Structure

- **`main.py`**: The main Python script that handles user input and controls the encryption and decryption processes.
- **`module.py`**: Contains the core functions for encrypting, decrypting, and handling files.
- **`cipher.txt`**: The output file where the encrypted message is saved.
- **`message.txt`**: The input file containing the original message for encryption or the decrypted message after running the script.

## How It Works

The Python script in `main.py` allows the user to choose between encryption and decryption:
1. **Encryption**: The script reads the plain text from `message.txt`, encrypts it using a Caesar cipher, and saves the result in `cipher.txt`.
2. **Decryption**: The script reads the ciphered text from `cipher.txt`, decrypts it, and saves the readable message in `message.txt`.

### Steps:

1. **User Instructions**: The script prompts the user to follow guidelines and then proceed with encryption or decryption.
2. **Process Selection**: Choose `E` for encryption or `D` for decryption.
3. **File Handling**: The script reads from `message.txt` or `cipher.txt` depending on the operation, processes the text, and writes the output to the appropriate file.

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Place the plain text in `message.txt` for encryption or the ciphered text in `cipher.txt` for decryption.
4. Run the `main.py` script.
5. The output will be available in `cipher.txt` (for encryption) or `message.txt` (for decryption).

### Running the Script

```bash
python main.py
```

## Example

**Before Running the Script:**
- `message.txt` contains: `Jesus is King!!`
- `cipher.txt` will store the encrypted text.

**After Running the Script:**
- `cipher.txt` contains: `?Zhjh^h@^c\`
- `message.txt` contains the decrypted message.

## Author

This project was created to demonstrate basic file encryption and decryption using a Caesar cipher in Python.

## License

This project is open source and available under the [MIT License](LICENSE).

---
