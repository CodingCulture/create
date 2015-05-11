create
======

Create is just a repo where we will manage and store our scripts for daily ops tasks
that would be considered tedious. The footprint of these scripts are relatively small, you'll just need python, apache2 and of course Linux.

## Why is this Open Source (or just published)

We believe that our code will get better if it is published out in the open, indeed sunlight is the best disinfectant. The other philosophical reason why we publish this, is because we have learned much from other people, and we hope that we can enlighten some new folks that are just discovering the world of web and everything that comes with managing that.

##Convention over configuration

This script is written following some clear conventions

- It makes user accounts, grants those user access in their home folders and makes a web folder where the code should be stored that is accessible via Apache2.
- The web folder gets symlinked into a folderstructure in the default LAMP location (/var/www/)

If you have found a way to improve this script, let us know by e-mailing us, or just making a pull request.
