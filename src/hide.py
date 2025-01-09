import PIL.Image

def encode_message(image_path, message, output_path):
    try:
        image = PIL.Image.open(image_path, 'r')
        width, height = image.size
        pixels = list(image.getdata())

        if image.mode == "P":
            return "Error: Palette color mode not supported."

        channels = 4 if image.mode == "RGBA" else 3
        
        stop_message = "$ILOVECOOKIE$"
        message += stop_message
        byte_message = ''.join(f"{ord(c):08b}" for c in message)
        bits = len(byte_message)

        if bits > len(pixels) * channels:
            return "Error: Not enough space in the image to hide the message."

        new_pixels = []
        index = 0

        for pixel in pixels:
            new_pixel = list(pixel)
            for j in range(channels):
                if index < bits:
                    # Replace the least significant bit of the channel with the message bit
                    new_pixel[j] = (new_pixel[j] & ~1) | int(byte_message[index])
                    index += 1
            new_pixels.append(tuple(new_pixel))

        # Create a new image with the modified pixels
        result_image = PIL.Image.new(image.mode, (width, height))
        result_image.putdata(new_pixels)
        result_image.save(output_path)
        return True
    except Exception as e:
        return f"Error: {str(e)}"
