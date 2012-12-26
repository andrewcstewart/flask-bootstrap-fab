flask-bootstrap-fab
===================

flask-bootstrap-fabric deployment

Deploy to Vagrant
-----------------
    $ vagrant init
    $ vagrant up
    $ fab vagrant setup
    $ fab vagrant create:myapp

Deploy to target host
---------------------
    $ fab user@host:port setup
    $ fab user@host:port create:myapp
