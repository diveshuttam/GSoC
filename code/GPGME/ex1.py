import gpg
import pprint
k = gpg.Context().keylist()
keys = list(k)
pprint.pprint(keys)