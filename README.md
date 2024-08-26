Read the  `README.md` file before using the repo

---

# Cipher Message Decoder

## Project Overview

This project involves a simple Python script that decodes a ciphered message from a given text file. The script takes a message encrypted using a basic substitution cipher and decodes it into readable text. 

## Project Structure

- **`main.py`**: The main Python script that handles the decoding process.
- **`cipher.txt`**: Contains the encrypted message that needs to be decoded.
- **`message.txt`**: Contains the decoded message after running the script.

## How It Works

The Python script in `main.py` reads the ciphered text from `cipher.txt`, applies the decoding algorithm, and then writes the decoded message into `message.txt`.

### Steps:

1. **Read Ciphered Text**: The script reads the encrypted message from the `cipher.txt` file.
2. **Decode Message**: It applies the decoding logic to translate the ciphered text into a readable message.
3. **Output**: The decoded message is saved to the `message.txt` file.

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Place the ciphered text in `cipher.txt`.
4. Run the `main.py` script.
5. The decoded message will be available in `message.txt`.

### Running the Script

```bash
python main.py
```

## Example

**Before Running the Script:**
- `cipher.txt` contains: `_z+q}tpyo~+p}p+~ttyr+ty+sp+~nszzw...`

**After Running the Script:**
- `message.txt` contains: `"Two friends were sitting in the school cafeteria..."`

## Author

This project was created to demonstrate a basic example of working with ciphers in Python.

## License

This project is open source and available under the [MIT License](LICENSE).

---

