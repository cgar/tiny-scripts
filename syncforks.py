#!/usr/bin/python3
# Syncs all git forks inside the Development directory
import os
import subprocess


# Master Forks
root_dir = "/home/cgar/Development/"
codespell = "/home/cgar/Development/codespell/"
flask = "/home/cgar/Development/flask/"
jekyll = "/home/cgar/Development/jekyll/"
linode_docs = "/home/cgar/Development/linode-docs/"
linux = "/home/cgar/Development/linux/"
pelican = "/home/cgar/Development/pelican/"
pep8 = "/home/cgar/Development/pep8/"
ProjectToxCore = "/home/cgar/Development/ProjectToxCore/"
vagrant = "/home/cgar/Development/vagrant/"
ansible = "/home/cgar/Development/ansible/"

# CCP folder
brennivin = "/home/cgar/Development/CCP/brennivin"
eveodoc = "/home/cgar/Development/CCP/eveonline-third-party-documentation"
pypackage = "/home/cgar/Development/CCP/pypackage"
pypicloud = "/home/cgar/Development/CCP/pypicloud-tools"
rescache = "/home/cgar/Development/CCP/rescache"

master_forks = (codespell, flask, jekyll, linode_docs, linux, pelican, pep8,
                ProjectToxCore, vagrant)

ccp_forks = (brennivin, eveodoc, pypackage, pypicloud, rescache)

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


# CCP folder
for forks in ccp_forks:
    os.chdir(forks)
    subprocess.call("git fetch upstream", shell=True)
    subprocess.call("git merge upstream/master", shell=True)
    subprocess.call("git push", shell=True)
