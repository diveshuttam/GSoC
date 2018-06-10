# Week 3 report:

## Major Things done during this period

### PR's created
- pgpg script for revoking the certificate (in-progress)
  - https://github.com/EasyGnuPG/pgpg/pull/56

### Issues Worked On:

- Update seal.sh calls
  - https://github.com/EasyGnuPG/pgpg/issues/32

- Update open.sh calls
  - https://github.com/EasyGnuPG/pgpg/issues/31

- Update key/rev.sh
  - https://github.com/EasyGnuPG/pgpg/issues/50

### Problems faced

I was stuck with seal and open scripts, though the sealing and
opening(decrypting) part is easy and documented, there is problem in retriving
the keys from keyserver, The bindings are not very well documented, I tried 
to understand these through the working of the c bindings, But could not work 
out.

I asked this on the gnupg-devel list which can be found here -  
https://lists.gnupg.org/pipermail/gnupg-devel/2018-June/033764.html

The solution proposed was to retrive the keys form the keyserver using request
library. And then we can get this done. Currently I have paused the issue for
a couple of days and by that time working on others. Will get back after I 
know about it.

## To be done coming week
Whatever was proposed last week could not be completed due to issues faced
above. My main aim is to work out the retriving key part form the keyserver,
as It is required in quiet a few other commands. Since it is taking time, I will
side by side be working on other issues, that don't require the keyserver and
are documented. Mostly from the key commands as proposed last week.

