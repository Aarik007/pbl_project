from modules.hash import hash_file, verify_integrity
from modules.encryption import aes_ed, rsa_ed
from modules.password import check_strength, hash_pw, verify_password
from getpass import getpass

def menu():
    print("\nSELECT OPERATION:")
    print("1.hash file")
    print("2.check file integrity")
    print("3.AES encrypt/decrypt")
    print("4.RSA encrypt/decrypt")
    print("5.password manager")
    print("0.exit")

    print("""
Initiating Cryptography Toolkit v1.0...
          
\Welcome, Agent! Your mission, should you choose to accept it:
- Analyze and hash files to detect tampering
- Encrypt and decrypt messages with AES and RSA
- Securely manage passwords and assess their strength
          
All systems online. Data protection protocols active.
Prepare to enter the world of digital secrecy! """)
    
while True:
    menu()
    choice= input("enter choice(0-5):")
    if choice =="0":
        break
    elif choice =="1":
        file_path= input("enter file path:")
        print("\nSHA hash of file is : ",hash_file(file_path))
    elif choice =="2":
        file_path1 = input("Enter file path 1: ")
        file_path2 = input("Enter file path 2: ")
        print(verify_integrity(file_path1, file_path2))
    elif choice =="3":
        message = input ("Enter message: ")

        key, ciphertext, plaintext = aes_ed(message)
        print("AES Key:", key)
        print("AES Ciphertext: ", ciphertext)
        print("AES Plaintext: ", plaintext)
    elif choice =="4":
        message = input("Enter message: ").encode()

        ciphertext, plaintext = rsa_ed(message)


        print("RSA message, encrypted with a public key:", ciphertext )
        print("RSA message, decrypted with a private key:", plaintext)
    elif choice=="5":
        while True:
            password1 = getpass("Enter a password to check strength: ")
            result = check_strength(password1)
            print(result)

            if result.startswith("Weak"):
             print("Please choose a stronger password.\n")
            else:
              break
        hashed_password= hash_pw(password1)
        print("hashed password:",hashed_password)
        attempt = getpass("re-enter the password to verify:")
        print(verify_password(attempt,hashed_password))
    else :
        print("invalid choice")

print("exiting toolkit")

    


    
