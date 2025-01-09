import PIL.Image


def decode_message(image_path):
    
    try:
        # Open the image file
        image = PIL.Image.open(image_path, 'r')
        pixels = list(image.getdata())

        if image.mode == "P":  # If the color mode is palette
            print("Not supported")
            exit()

        channels = 4 if image.mode == 'RGBA' else 3

        # Extract the least significant bits for each pixel's RGB channels
        secret_bits = []
        for pixel in pixels:
            for j in range(channels): 
                secret_bits.append(bin(pixel[j])[-1])

        # Group the bits into bytes (8 bits each)
        secret_bits = ''.join(secret_bits)
        byte_chunks = [secret_bits[i:i + 8] for i in range(0, len(secret_bits), 8)]

        # Convert the bytes into characters
        secret_message = ''.join(chr(int(byte, 2)) for byte in byte_chunks)

        # Stop message used to identify the end of the hidden message
        stop_message = "$ILOVECOOKIE$"

        # Extract and display the secret message
        stop_message in secret_message
        extracted_message = secret_message[:secret_message.index(stop_message)]

        return True, extracted_message
    
    except Exception as e:
        return f"Error: {str(e)}"