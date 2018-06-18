# Week 5 report:

## Major Things done during this period

### PR's created
- Add Key Delete:
  - https://github.com/EasyGnuPG/pgpg/pull/58
- Seal.py
  - https://github.com/EasyGnuPG/pgpg/pull/60 

### Issues Worked On:

- Update seal.sh calls
  - https://github.com/EasyGnuPG/pgpg/issues/32

- Update open.sh calls
  - https://github.com/EasyGnuPG/pgpg/issues/31

- Update key/delete.sh
  - https://github.com/EasyGnuPG/pgpg/issues/45

- Update key/rev.sh
  - modified to use env variable debug to geneerate error messges
    - https://github.com/EasyGnuPG/pgpg/issues/50

### Problems faced
Seal and open commands required use of keyserver to retrive keys. 
Worked and learnt `requests` solve these, but solving these with 
all the error checking is difficult and will decrease the stability if 
done without error checking, For now I am relying on gpg cli for 
retriving these so that we can move forward. Later maybe if we have 
time left or after GSoC, we may implement a keyserver retrival with 
`requests` library


## To be done coming week

- Key/open.sh
  - https://github.com/EasyGnuPG/pgpg/issues/31
- Key/list.sh
  - https://github.com/EasyGnuPG/pgpg/issues/47
- Key/gen.sh
  - https://github.com/EasyGnuPG/pgpg/issues/46
- import.sh
  - https://github.com/EasyGnuPG/pgpg/issues/39
- fetchuri.sh
  - https://github.com/EasyGnuPG/pgpg/issues/38
- fetch.sh
  - https://github.com/EasyGnuPG/pgpg/issues/37

