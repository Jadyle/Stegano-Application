from PIL import Image

def encode_exe(image_path, output_path, file_to_hide):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGBA")  # Ensure RGBA format
    pixels = list(img.getdata())
    
    # Read the file to hide
    with open(file_to_hide, "rb") as file:
        data = file.read()
    # Add a delimiter to mark the end of the file
    data += b"EOF"
    
    # Convert data to binary
    binary_data = ''.join(format(byte, '08b') for byte in data)
    
    # Check if the data fits in the image
    if len(binary_data) > len(pixels) * 4:  # 4 channels in RGBA
        raise ValueError("File size is too large to hide in the provided image.")
    
    # Embed the binary data into the image
    new_pixels = []
    data_index = 0
    for pixel in pixels:
        r, g, b, a = pixel  # RGBA values
        
        if data_index < len(binary_data):
            r = (r & 0xFE) | int(binary_data[data_index])
            data_index += 1
        if data_index < len(binary_data):
            g = (g & 0xFE) | int(binary_data[data_index])
            data_index += 1
        if data_index < len(binary_data):
            b = (b & 0xFE) | int(binary_data[data_index])
            data_index += 1
        if data_index < len(binary_data):
            a = (a & 0xFE) | int(binary_data[data_index])
            data_index += 1
        
        new_pixels.append((r, g, b, a))
    
    # If there's no more data, append the rest of the original pixels
    new_pixels.extend(pixels[len(new_pixels):])
    
    # Save the new image
    img.putdata(new_pixels)
    img.save(output_path)
    print(f"File hidden successfully in {output_path}")
