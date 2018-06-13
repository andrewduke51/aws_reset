#! /usr/bin/env python
from __future__ import print_function
import subprocess
import awscli
class Bash2Py(object):
  __slots__ = ["val"]
  def __init__(self, value=''):
    self.val = value

print("Hello, set your new password for the aws console :-)?")
PASSWORD = Bash2Py(raw_input())
print("Tell me your username")
USERNAME = Bash2Py(raw_input())
print("What is your profile?")
PROFILE = Bash2Py(raw_input())
_rc0 = subprocess.call(["aws", "iam", "update-login-profile", "--user-name", str(USERNAME.val), "--password", str(PASSWORD.val), "--profile", str(PROFILE.val)])
print(_rc0)
print("You are all set and you can login to the aws console using your new password now!")
exit(0)
