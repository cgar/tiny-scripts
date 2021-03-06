#!/usr/bin/python3
# Syncs all git forks inside the Development directory
import os
import subprocess


# Original
linux = "/home/cgar/Development/linux/"
openbsd = "/home/cgar/Development/OpenBSD/"

original = (linux, openbsd)

# Master branch
rust = "/home/cgar/Development/rust/"
python = "/home/cgar/Development/cpython/"
bedrock = "/home/cgar/Development/mozilla_org_bedrock/"
devguide = "/home/cgar/Development/python_devguide/"
django = "/home/cgar/Development/django/"
servo = "/home/cgar/Development/servo/"
flask = "/home/cgar/Development/flask/"

masterForks = (rust, python, bedrock, devguide, django, servo, flask)

# Devel branch
ansible = "/home/cgar/Development/ansible/"

develForks = (ansible)

# Start sync
for forks in original:
    os.chdir(forks)
    subprocess.call("git pull", shell=True)

for forks in masterForks:
    os.chdir(forks)
    subprocess.call("git fetch upstream", shell=True)
    subprocess.call("git merge upstream/master", shell=True)
    subprocess.call("git push", shell=True)


# for forks in develForks:
os.chdir(ansible)
subprocess.call("git fetch upstream", shell=True)
subprocess.call("git merge upstream/devel", shell=True)
subprocess.call("git push", shell=True)
