#signature verification

import gpg
import time

asc_file = "ex13out.txt.asc"

c = gpg.Context()

try:
    data, result = c.verify(open(asc_file))
    verified = True
except gpg.errors.BadSignatures as e:
    verified = False
    print(e)

if verified is True:
    for i in range(len(result.signatures)):
        sign = result.signatures[i]
        print("""Good signatrue from:
{0}
with key {1}
made at {2}""".format(c.get_key(sign.fpr).uids[0].uid,
        sign.fpr, time.ctime(sign.timestamp)))
else:
    pass
