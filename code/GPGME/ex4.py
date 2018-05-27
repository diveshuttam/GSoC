import gpg

fingerprint = 'CE239E89CACC1112E8D1E21283FE6CC0D0CC01EC'
key = gpg.Context().get_key(fingerprint)
print(key)