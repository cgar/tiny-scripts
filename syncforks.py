#!/usr/bin/python3
# Syncs all git forks inside the Development directory
import os
import subprocess


# Master Forks
root_dir = "/home/cgar/Development/"
linode_docs = "/home/cgar/Development/linode-docs/"
linux = "/home/cgar/Development/linux/"
rust = "/home/cgar/Development/rust/"

master_forks = (linode_docs, linux, rust)

for forks in master_forks:
    os.chdir(forks)
    subprocess.call("git fetch upstream", shell=True)
    subprocess.call("git merge upstream/master", shell=True)
    subprocess.call("git push", shell=True)

# Devel branch
os.chdir(ansible)
subprocess.call("git fetch upstream", shell=True)
subprocess.call("git merge upstream/devel", shell=True)
subprocess.call("git push", shell=True)
