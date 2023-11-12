import hashlib
import os

def hash_append(hash):
    os.makedirs("hash_append", exist_ok=True)
    fichier_name = open("hash_append\hash.txt", "a")
    fichier_name.write(str("\n"+hash))
    fichier_name.close()

def hash_and_password_append(hash, password, type_of_hash):
    os.makedirs("hash_append", exist_ok=True)
    fichier_name = open("hash_append\hash_and_password.txt", "a")
    fichier_name.write(str("\n"+hash+" ("+type_of_hash+")=> "+password))
    fichier_name.close()

def hash():
    password = str(input("\nEntrez le mdp a hacher : "))
    print("\n-----TYPE-OF-HASH-ALGORITHME----------------------------------------")
    print("2    => blak2b")
    print("5    => md5")
    print("256  => sha256")
    print("512  => sha512")
    print("--------------------------------------------------------------------")
    option = int(input("\nEnter the type of hash algorithme : "))
    if option == 2:
        type_of_hash = "blak2b"
        password_encode = password.encode("utf-8")
        password_hash = hashlib.blake2b(password_encode)
        result_hash_hexadecimal = password_hash.hexdigest()
    if option == 5:
        type_of_hash = "md5"
        password_encode = password.encode("utf-8")
        password_hash = hashlib.md5(password_encode)
        result_hash_hexadecimal = password_hash.hexdigest()
    if option == 256:
        type_of_hash = "sha256"
        password_encode = password.encode("utf-8")
        password_hash = hashlib.sha256(password_encode)
        result_hash_hexadecimal = password_hash.hexdigest()
    if option == 512:
        type_of_hash = "sha512"
        password_encode = password.encode("utf-8")
        password_hash = hashlib.sha512(password_encode)
        result_hash_hexadecimal = password_hash.hexdigest()
    hash_append(result_hash_hexadecimal)
    hash_and_password_append(result_hash_hexadecimal, password, type_of_hash)
    return result_hash_hexadecimal

if __name__=="__main__":
    while True:
        print(hash())
