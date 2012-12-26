from fabric.api import *
from fabric.contrib.files import exists, append, contains
from fabric.decorators import hosts, task
from fabric.operations import local
from fabtools.vagrant import vagrant

@task
def setup():
    sudo("apt-get update")
    sudo("apt-get install unzip")
    sudo("apt-get install -y emacs23")
    sudo("apt-get install -y ipython")
    sudo("apt-get install -y git-core")
    sudo("apt-get install -y python-setuptools")
    sudo("easy_install pip")
    sudo("pip install virtualenv")
    sudo("pip install Flask")
    sudo("pip install flask-bootstrap")

def create_project(myproject):
    sudo("mkdir " + myproject)
    with cd(myproject):
        sudo("virtualenv venv")

# . venv/bin/activate
