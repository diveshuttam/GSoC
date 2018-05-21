# Week 1 report:

I had my exams during bonding period, so this week went mostly into trying out
thing that were proposed during the bonding period. 

## Major Things done during this period

### PR's created
- https://github.com/EasyGnuPG/egpg/pull/40
- https://github.com/EasyGnuPG/egpg-ds/pull/7
- https://github.com/EasyGnuPG/egpg-ds/pull/8

### ISSUES WORKED ON
- https://github.com/EasyGnuPG/pgpg/issues/7
  - read the wikibook and ch 24-28 from the book
- https://github.com/EasyGnuPG/pgpg/issues/9
  - build a test + dev env for egpg, tried various examples and tried finding
    bugs
- https://github.com/EasyGnuPG/pgpg/issues/3
  - while working with above (#9) tried to understand the egpg code and its 
    working to find issues/bugs
- https://github.com/EasyGnuPG/pgpg/issues/8
  - read about various bindings for GPGME. Finally decided to go with the
    official bindings
- https://github.com/EasyGnuPG/egpg-ds/issues/4
  - installed `man` in the test enviroenment

### Other research/ findings
- We can't package the official bindings into a pip package.
  ([reference](http://files.au.adversary.org/crypto/GPGMEpythonHOWTOen.html#do-not-use-pypi))
- Thought about the structure of the package
- Read the guide to [structuring python code](http://docs.python-guide.org/en/latest/writing/structure/) 

## To be done coming week
- Get done with the structure of the pip package and division into modules.
- Get the basic init, seal, sign, commands working.

