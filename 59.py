from itertools import permutations


def decode_message(encrypted_codes):
    for key in permutations("abcdefghijklmnopqrstuvwxyz", 3):
        message = []

        for i, code in enumerate(encrypted_codes):
            decrypted_code = int(code) ^ ord(key[i % 3])
            message.append(chr(decrypted_code))

        if all(x in "".join(message) for x in ["the", "and", "be", "to"]):
            ascii_sum = sum(ord(c) for c in message)
            return key, ascii_sum, "".join(message)
    return "Unable to decode."

with open("p059_cipher.txt", "r") as f:
    encrypted_codes = f.read().strip().split(",")

print decode_message(encrypted_codes)
