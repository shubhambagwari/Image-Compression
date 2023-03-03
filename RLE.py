from PIL import Image
# import comp34

def run_length_encode(image):
    """
    Run-length encode a grayscale image.

    Parameters:
        image (PIL.Image): The input grayscale image.

    Returns:
        bytes: The encoded image data.
    """
    data = bytearray()
    width, height = image.size
    run = 0
    prev = None

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel == prev:
                run += 1
            else:
                if prev is not None:
                    data.append(run)
                    data.append(prev)
                prev = pixel
                run = 1

        # Flush the last run of pixels for the current row.
        data.append(run)
        data.append(prev)
        prev = None
        run = 0

    return bytes(data)


def run_length_decode(data, width, height):
    """
    Run-length decode a grayscale image.

    Parameters:
        data (bytes): The encoded image data.
        width (int): The width of the original image.
        height (int): The height of the original image.

    Returns:
        PIL.Image: The decoded grayscale image.
    """
    image = Image.new('L', (width, height))
    x = 0
    y = 0
    i = 0

    while i < len(data):
        run = data[i]
        value = data[i + 1]
        i += 2

        for j in range(run):
            image.putpixel((x, y), value)
            x += 1
            if x >= width:
                x = 0
                y += 1

    return image
