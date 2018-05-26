import gpg

a_key = "CE239E89CACC1112E8D1E21283FE6CC0D0CC01EC"
text = b"""Some text to test with.

Since the text in this case must be bytes, it is most likely that
the input form will be a separate file which is opened with "rb"
as this is the simplest method of obtaining the correct data
format.
"""

c = gpg.Context(armor=True)
rkey = list(c.keylist(pattern=a_key, secret=False))
ciphertext, result, sign_result = c.encrypt(text, recipients=rkey, sign=False)

with open("secret_plans.txt.asc", "wb") as afile:
    afile.write(ciphertext)