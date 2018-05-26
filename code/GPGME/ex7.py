import gpg

a_key = "CE239E89CACC1112E8D1E21283FE6CC0D0CC01EC"

with open("secret_plans.txt", "rb") as afile:
    text = afile.read()

c = gpg.Context(armor=True)
rkey = list(c.keylist(pattern=a_key, secret=False))
ciphertext, result, sign_result = c.encrypt(text, recipients=rkey,
            sign=True, always_trust=True, add_encrypt_to=True)

with open("secret_plans1.txt.asc", "wb") as afile:
    afile.write(ciphertext)