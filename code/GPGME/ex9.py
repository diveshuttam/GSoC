import gpg

text = b"""Oh look, another test message.

The same rules apply as with the previous example and more likely
than not, the message will actually be drawn from reading the
contents of a file or, maybe, from entering data at an input()
prompt.

Since the text in this case must be bytes, it is most likely that
the input form will be a separate file which is opened with "rb"
as this is the simplest method of obtaining the correct data
format.
"""

c = gpg.Context(armor=True)
pattern="test.org"
rpattern = list(c.keylist(pattern=pattern, secret=False))
logrus = []

for i in range(len(rpattern)):
    if rpattern[i].can_encrypt == 1:
        logrus.append(rpattern[i])

# The only keyword arguments requiring modification are those for which the default values are changing.
# The default value of sign is True, the default of always_trust is False, the default of add_encrypt_to is False.
ciphertext, result, sign_result = c.encrypt(text, recipients=logrus,
                        always_trust=True,
                        add_encrypt_to=True)

# REM: handle wrong passphrase here (i.e. in case of sign)
with open("secret_plans3.txt.asc", "wb") as afile:
    afile.write(ciphertext)

