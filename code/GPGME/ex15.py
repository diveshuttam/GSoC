# create key
import gpg

c=gpg.Context()

c.home_dir = "~/.gnupg"
userid = "Danger Mouse <dm@secret.example.net>"

dmkey = c.create_key(userid, algorithm="rsa4096", expires_in=31536000,
                     sign=True, certify=True, force=True)

print("""
      Fingerprint: {0}
      Primary Key: {1}
      Public key:  {2}
      Secret Key: {3}
      sub key:{4}
      User IDs: {5}""".format(dmkey.fpr, dmkey.primary, dmkey.pubkey, dmkey.seckey,
                              dmkey.sub, dmkey.uid))
