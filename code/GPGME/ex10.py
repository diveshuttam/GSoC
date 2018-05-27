import gpg

ciphertext = input("Enter path and filename of encrypted file: ") # secret_plans.txt.asc
newfile = input("Enter path and filename of file to save decrypted data to: ") # decrypt.txt

with open(ciphertext, "rb") as cfile:
    plaintext, result, verify_result = gpg.Context().decrypt(cfile)

with open(newfile, "wb") as nfile:
    nfile.write(plaintext)