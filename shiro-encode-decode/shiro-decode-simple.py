import sys
import base64
import uuid
from random import Random
import subprocess
from Crypto.Cipher import AES


def decode_remember(remember):
    iv = base64.b64decode(remember)[:16]
    file_body = base64.b64decode(remember)[16:]
    key = "ikB3y6O9BpimrZLB3rca0w=="
    mode = AES.MODE_CBC
    decryptor = AES.new(base64.b64decode(key), mode, iv)
    result = decryptor.decrypt(file_body)
    print(result)


with open("xray.cookie", "r") as f:
    remember = f.readline().strip()

# print(remember)
decode_remember(remember)
