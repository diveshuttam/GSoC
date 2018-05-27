# Week 2 report:

## Major Things done during this period

### PR's created
- Create a basic pip setup and install instructions
  - https://github.com/EasyGnuPG/pgpg/pull/18

- Create a dev environment for pgpg (pgpg-ds)
  - https://github.com/EasyGnuPG/pgpg-ds/pull/1
  - https://github.com/EasyGnuPG/pgpg-ds/pull/2
  - https://github.com/EasyGnuPG/pgpg-ds/pull/3

- Fix a small bug in gnupg-2.2 branch
  - https://github.com/EasyGnuPG/egpg/pull/48

- Basic blueprint for the project (in progress)
  - https://github.com/EasyGnuPG/pgpg/pull/22

### Issues Worked On:
- ch 28-32 from the book the linux command line
  - https://github.com/EasyGnuPG/pgpg/issues/7

- Tested more of gnupg2.2 branch 
  - https://github.com/EasyGnuPG/egpg/issues/27
  - created the following issues
    - https://github.com/EasyGnuPG/egpg/issues/42
    - https://github.com/EasyGnuPG/egpg/issues/41 (also solved this)

- build a test + dev env for pgpg (see
  [pgpg-ds](https://github.com/EasyGnuPG/pgpg-ds))
  - https://github.com/EasyGnuPG/pgpg/issues/19

- Tried a few examples in GPGME which can be found
  [here](https://github.com/diveshuttam/GSoC18/tree/gh-pages/code/GPGME)
  - https://github.com/EasyGnuPG/pgpg/issues/4

- Created a basic blueprint (functions) that handle commandline
  - https://github.com/EasyGnuPG/pgpg/issues/21

### Other research/ findings
- GPGME binidngs are not availible in Ubuntu<=16.04 repositories
  - https://github.com/EasyGnuPG/pgpg/issues/20
    - will add pointers to installing these from source towards the end of this
      project.
    - For now we can continue developement and testing in the docker containers.
      got these bindings in the buster as well as bionic repositories and are 
      working inside the [containers](https://github.com/EasyGnuPG/pgpg-ds).


## Pending/Change of Plan
I had planned to work on pgpg init, sign and seal but as following was suggested
by mentors I have changed it: 
- creating commands the way they are invoked by the user is better
    - I will work with `pgpg init` and `pgpg key gen` first and following the
      order of examples in man pages, will make the job lot easier. 
- It would be good to use oop for key and management 
    - will have to study a bit of code and create a key class first.

## To be done coming week
- Issues [#7](https://github.com/EasyGnuPG/pgpg/issues/7)(bash scripting),
  [#9](https://github.com/EasyGnuPG/pgpg/issues/9)(testing egpg2.2),
  [#3](https://github.com/EasyGnuPG/pgpg/issues/3)(experiment egpg),
  [#4](https://github.com/EasyGnuPG/pgpg/issues/4)(trying a few gpgme examples)
  are pending for long. They are alomst done. Close them by the end of this week.

- Create a class for Key 
  - as discussed in [pgpg/pull#18](https://github.com/EasyGnuPG/pgpg/pull/18),
  It would be good to use oop for the key and user management (User Management
  will be dealt later when/if necessary).

- initial checking of keys on invocation.
  this would check for the existance of the .egpg folder and keys as per the
  context defined by enviroment variable EGPG_DIR 

- egpg init
  As I have genereated basic structure for the project, this envolves adding
  code to the core/cmd/init.py (as per pgpg/pr#18)

- egpg key gen
  generate key pair for the user. This just involves simple calls to GPGME
  library with few error checking.

As I am new to GPGME bindings I expect these to take some time in initial
phase hence adding less code work for this week will speed up by the coming week.
