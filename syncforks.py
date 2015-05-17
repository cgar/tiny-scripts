#!/usr/bin/python3
# Syncs all git forks inside the Development directory
import os
import subprocess


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
ansible = "/home/cgar/Development/ansible"


master_forks = (codespell, flask, jekyll, linode_docs, linux, pelican, pep8,
                ProjectToxCore, vagrant)
# devel_forks = (ansible, test_fork1, test_fork2)


for forks in master_forks:
    os.chdir(forks)
    subprocess.call("git fetch upstream", shell=True)
    subprocess.call("git merge upstream/master", shell=True)
    subprocess.call("git push", shell=True)


os.chdir(ansible)
subprocess.call("git fetch upstream", shell=True)
subprocess.call("git merge upstream/devel", shell=True)
subprocess.call("git push", shell=True)
