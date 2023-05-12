from Crypto.Cipher import AES
import base64
cpassword=input("Cipher Password : ") # cipher password with AES
decoded_password = base64.b64decode(cpassword)
key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'# AES Windows key
decryption_suite = AES.new(key, AES.MODE_CBC, iv=b'\x00'*16)
plain_text = decryption_suite.decrypt(decoded_password)
password_list = (plain_text.decode().split('\x00')) # removing null bytes
password = ''.join(str(i) for i in password_list) # list to string
print(password)