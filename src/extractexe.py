from PIL import Image


def decode_exe(image_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGBA")  # Ensure RGBA format
    pixels = list(img.getdata())
    
    # Extract the binary data
    binary_data = ""
    for pixel in pixels:
        r, g, b, a = pixel  # RGBA values
        binary_data += bin(r)[-1]
        binary_data += bin(g)[-1]
        binary_data += bin(b)[-1]
        binary_data += bin(a)[-1]
    
    # Convert binary data to bytes
    data_bytes = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:  # Ignore incomplete bytes
            data_bytes.append(int(byte, 2))
    
    data = bytes(data_bytes)
    # Find the EOF marker
    eof_index = data.find(b"EOF")
    if eof_index != -1:
        data = data[:eof_index]
    else:
        raise ValueError("No hidden file found.")
    
    return data, True

