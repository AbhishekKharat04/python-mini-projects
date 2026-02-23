from cryptography.fernet import Fernet

key=Fernet.generate_key()
f=Fernet(key)

data=open("file.txt","rb").read()
encrypted=f.encrypt(data)
open("enc.txt","wb").write(encrypted)

decrypted=f.decrypt(encrypted)
open("dec.txt","wb").write(decrypted)
print("Encryption and decryption completed successfully")
