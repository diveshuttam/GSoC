import gpg

k=gpg.Context().keylist(pattern="test.org")
keys=list(k)
print(keys)