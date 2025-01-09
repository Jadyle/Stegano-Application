# Stegano

### Authors
- **Lina Rashdan**

## Description
The Stegano program allows hiding messages or files within images using steganography techniques. It supports RGB and RGBA formats for encoding messages and files. The program uses the **Least Significant Bit (LSB)** technique to ensure that the integration of data remains discrete and does not alter the visual quality of the image. A graphical user interface is available, and an executable file is provided.

## Preview
A preview of the process for hiding and extracting a secret message from an image.

![0109](https://github.com/user-attachments/assets/fca1c3ea-fe3b-4b25-a20d-35d789091ed2)

## Features
The program offers 4 main features:
- **Hide a message in an image**
- **Extract a message from an image**
- **Hide an .exe file in an image**
- **Extract an .exe file from an image**

### Compatibility
- Language: Python - 3.12.8
- This program is recommended for use on Windows.
    - It was developed and tested exclusively on Windows, ensuring better compatibility and stability on this operating system.

### Dependencies
- **Pillow**: Used for image processing.
  - You can install the library via pip:
  ```bash
  pip install Pillow
  ```

### Installation and Usage
#### Prerequisites
Before running the program, ensure Python is installed (version 3.10 recommended). You can download Python here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

#### Installation Steps:
1. Clone this repository or download the files.
2. Install the required dependencies:
   ```bash
   pip install Pillow
   ```
3. Run the `main.py` file to launch the graphical user interface.

#### Usage:
1. Start the Python file using the following command in the project's `src` directory:
    ```bash
   python main.py
   ```

2. The graphical interface will appear, allowing you to:
   - Select an image to hide a message or a file.
   - Extract a hidden message or file from an image.
