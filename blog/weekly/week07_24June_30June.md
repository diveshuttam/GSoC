# Week 7 report:

## Major Things done during this period

### PR's created

- add key pass functionality
  - https://github.com/EasyGnuPG/pgpg/pull/68 

- Update a few tests
  - https://github.com/EasyGnuPG/pgpg/pull/71

- Key gen added
  - https://github.com/EasyGnuPG/pgpg/pull/67

- Add print_key.py
  - https://github.com/EasyGnuPG/pgpg/pull/66

- Fetchuri
  - https://github.com/EasyGnuPG/pgpg/pull/70

- Add contact import
  - https://github.com/EasyGnuPG/pgpg/pull/69

- Try automated testing using travis (closed)
  - https://github.com/EasyGnuPG/pgpg/pull/72

### Issues Worked On:

- Update Key/pass.sh
  - https://github.com/EasyGnuPG/pgpg/issues/48

- Make test pass
  - https://github.com/EasyGnuPG/pgpg/issues/63
    - updated a few more tests, now most all are passing
    - removed split tests for a while. They require change in container.

- Update key/gen.sh
  - https://github.com/EasyGnuPG/pgpg/issues/46

- Update key/list.sh
  - https://github.com/EasyGnuPG/pgpg/issues/47

- update fetchuri.sh
  - https://github.com/EasyGnuPG/pgpg/issues/38

- update contact/import.sh
  - https://github.com/EasyGnuPG/pgpg/issues/39
  
- Toyed with automated testing(travis) [closed]
  - https://github.com/EasyGnuPG/pgpg/issues/73
  - This didn't work out quite well, travis is
  asking for lot many permissions. Also not needed
  for a small project.

## Issues faced

- struggled for quite some time with test script for key/pass.py (t24)
  - thanks to @dashohoxha that it was finally solved, the problem was:
    - we were not reloading gpgagent.
    - the directory for .gnupg folder was also incorrect.

## To be done coming week

The issues planned this week are:
- Contact/export.sh (in progress)
  - https://github.com/EasyGnuPG/pgpg/issues/36

- Contact/fetch.sh (in progress)
  - https://github.com/EasyGnuPG/pgpg/issues/37

- Contact/delete.sh (easy)
  - https://github.com/EasyGnuPG/pgpg/issues/51

- Contact/list.sh (easy)
  - https://github.com/EasyGnuPG/pgpg/issues/40

The following issues are similar and based on keyedit (interact) functionality.
Can probably be handled together.

- key/revcert.sh
  - https://github.com/EasyGnuPG/pgpg/issues/51

- key/renew.sh
  - https://github.com/EasyGnuPG/pgpg/issues/49

- contact/uncertify.sh
  - https://github.com/EasyGnuPG/pgpg/issues/44

- contact/certify.sh
  - https://github.com/EasyGnuPG/pgpg/issues/34

If the above 4 turn out to be easy, I can complete majority
of porting within this week.
