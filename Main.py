BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(data):
    if isinstance(data, str):
        data = data.encode("utf-8")

    result = []

    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]

        padding = 3 - len(chunk)

        # Convert the chunk into one 24-bit number
        number = 0
        for byte in chunk:
            number = (number << 8) | byte

        number = number << (padding * 8)

        # Split the 24-bit number into four 6-bit values
        indexes = [
            (number >> 18) & 63,
            (number >> 12) & 63,
            (number >> 6) & 63,
            number & 63
        ]

        # Convert 6-bit values to Base64 characters
        for j in range(4 - padding):
            result.append(BASE64_CHARS[indexes[j]])

        # Add '=' padding
        for _ in range(padding):
            result.append("=")

    return "".join(result)

def base64_decode(encoded):



    encoded = "".join(char for char in encoded if not char.isspace())

    if len(encoded) % 4 != 0:
        raise ValueError("Invalid Base64 input length")

    result = bytearray()

    # Process 4 Base64 characters at a time
    for i in range(0, len(encoded), 4):
        block = encoded[i:i + 4]

        padding = block.count("=")

        number = 0

        for char in block:
            if char == "=":
                value = 0
            else:
                if char not in BASE64_CHARS:
                    raise ValueError(f"Invalid Base64 character: {char}")
                value = BASE64_CHARS.index(char)

            number = (number << 6) | value


        bytes_from_block = [
            (number >> 16) & 255,
            (number >> 8) & 255,
            number & 255
        ]


        for j in range(3 - padding):
            result.append(bytes_from_block[j])

    return bytes(result)


def base64_decode_to_text(encoded):

    return base64_decode(encoded).decode("utf-8")

def print_base64_map():

    print("\nBase64 Character Map")
    print("--------------------")

    columns = 4
    rows = len(BASE64_CHARS) // columns

    for row in range(rows):
        for col in range(columns):
            index = row + col * rows
            char = BASE64_CHARS[index]

            print(f"{char} -> {index:2}", end="    ")

        print()

