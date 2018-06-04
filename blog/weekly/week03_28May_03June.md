# Week 3 report:

## Major Things done during this period

### PR's created
- Update dev environment for pgpg (pgpg-ds)
  - https://github.com/EasyGnuPG/pgpg-ds/pull/6 (merged)
  - https://github.com/EasyGnuPG/pgpg-ds/pull/5 (merged)

- Create python script for signing
  - https://github.com/EasyGnuPG/pgpg/pull/24 (merged)

- Create python script for verifying
  - https://github.com/EasyGnuPG/pgpg/pull/53 (open, in progress)

### Issues Worked On:
- ch 33-36 from the book the linux command line 
  - https://github.com/EasyGnuPG/pgpg/issues/7 (closed)

- Try a few examples in GPGME 
  - These can be found
  [here](https://github.com/diveshuttam/GSoC18/tree/gh-pages/code/GPGME)
    - https://github.com/EasyGnuPG/pgpg/issues/4 (closed)

- Try with egpg
  - https://github.com/EasyGnuPG/pgpg/issues/3 (closed)
    - mostly worked with this while and after creating tasks as per the new
      plans

- Some minor issues due to change of plan
  - Updation of tasks
    - https://github.com/EasyGnuPG/pgpg/issues/27 (closed)
  - Update container for pgpg
    - https://github.com/EasyGnuPG/pgpg/issues/19 (closed)
  - https://github.com/EasyGnuPG/pgpg/issues/52 (closed)

- Python script for signing a file
  - https://github.com/EasyGnuPG/pgpg/issues/23 (closed)

- Update verify.sh calls
  - https://github.com/EasyGnuPG/pgpg/issues/33 (open, in progress)


## Pending
- Most of the initial prepration issues have been wrapped off this week
Only [#9](https://github.com/EasyGnuPG/pgpg/issues/9) is still pending.

## Change of plans
- We have tried another approach towards this project, instead of a complete
rewrite, we are currently replacing calls to `gpg` with calls to python
scripts which use GPGME library internally and achieve the same funcitonality.  

  - This still achieves the main purpose of the project which is to make `egpg` 
  stable
    - REASON: As discussed with mentor prior to proposal, The instablity arises
      from the output and options of `gpg` CLI which change relatively 
      frequently. If we base it on calls to GPGME library whose interface and
      output are stable, we can offer much more stability.

## To be done coming week
- Python scripts related to Open, sign, and most of key commands
  - I currently plan to pick atleast one issue daily between issue 28 to 51.
  Will try to push it to couple of issues daily by the end of this week. I 
  intend to finish with these in couple of weeks proceeding in this order:
    - open, seal
    - key commands (gen, list, delete, pass, renew, rev, revcert)
    - contact commands
    - other files which are left (auxilary.sh, bash-complete.sh)

  - I am now feeling a bit comfortable with gpgme library, in best case I expect
  to finish open, sign and all of key commands by the end of week 4

- [#9](https://github.com/EasyGnuPG/pgpg/issues/9)(testing egpg2.2),
  - I had been delaying this because I was also learning bash scripting along.
    I guess I am ready to complete this now.
  - Also I plan to run this in parallel to the above updating part, as
    I update a (bash) file with python script, I ensure its working with `gpg2`
    also. 
    - This makes sense as while trying examples from GPGME library as well as 
    working with sign and verify I found myself comparing my scripts output to
    actual output for which I had to test output of egpg commands quite a few 
    times.
