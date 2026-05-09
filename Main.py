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

