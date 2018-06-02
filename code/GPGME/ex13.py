import gpg
logrus = input("Enter the email address or string to match the sigining keys to:")
hancock = gpg.Context().keylist(pattern=logrus,secret=True)
sig_src=list(hancock)

text0 = """Declartion of --- something.
"""

text = text0.encode()
c=gpg.Context(armor=True, signers=sig_src)

signed_data, result= c.sign(text, mode=gpg.constants.sig.mode.CLEAR)

with open("ex13out.txt.asc","w") as afile:
    afile.write(signed_data.decode())

