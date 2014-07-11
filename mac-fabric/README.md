Support Loft Control System
===========================

This script adds a few useful commands for controlling
our mac (support-mini.jaalam.net). 

## Requirements:

Python and [Fabric](http://www.fabfile.org/installing.html).

# Set up:

You need a working SSH config for the host 'support-mini'.
Generate a fresh keypair and copy it over to the mac with 
username/pass.

```
$ ssh-keygen -f ~/.ssh/id_mac
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in ~/.ssh/id_mac.
Your public key has been saved in ~/.ssh/id_mac.pub.
The key fingerprint is:
a8:21:e5:47:88:17:df:20:1d:58:ed:79:fc:ac:48:8c user@localhost
The key's randomart image is:
+--[ RSA 2048]----+
|    o++o         |
|   ..=.o.        |
|  . + o..o       |
|   + . .o o      |
|  . o ooS. o     |
|   . +E o   o    |
|    .  . . .     |
|        . .      |
|                 |
+-----------------+

$ ssh-copy-id -i ~/.ssh/id_mac.pub support@support-mini
```

Add the following to ~/.ssh/config.

```
Host support-mini
    Hostname support-mini
    User support
    IdentityFile ~/.ssh/id_mac
```

If you can run `ssh support-mini` with no futher prompts you're
good.

If you don't want to have fabfile.py hanging around in your
home directory create a ~/.fabricrc file and add this.

```
fabfile = /home/<whatever>/shenanigans/mac-fabric/fabfile.py
```

## Syntax: 
    fab <command>:<arg>

## Commands:

* pizza, manaman, lobster, happy
  * play a selected youtube video

* random
  * play a random youtube video

* snap
  * Take a photo and download it to your machine

* vol OR vol:`<NUMBER>`
  * Retrive current volume setting
  * Set the volume, valid integers are 0-100

* say:"some words"
  * Speak something out loud (ohgodwhy)