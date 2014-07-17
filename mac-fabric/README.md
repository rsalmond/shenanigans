Support Loft Control System
===========================

This script adds a few useful commands for controlling
our mac (support-mini.jaalam.net). 

## Requirements:

Python and [Fabric](http://www.fabfile.org/installing.html).

# Mac Set up:

Put everything from the 'support-mini' dir into ~/Shenanigans
on the mac.

# Local Set up:

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

* yt:<video>
  * play a selected youtube video
  * omit video name to play a random video
  * `fab yt:list` to show available videos

* snap
  * Take a photo and post it in the support chat

* vol
  * Retrive current volume setting `fab vol`
  * Set the volume `fab vol:<num>` valid range 0-100
  * Increase or decrease volume by amount `fab vol:+<num>` or `fab vol:-<num>`

* say:"some words"
  * Speak something out loud (ohgodwhy)

* temperature
  * Speak current readings from coffeecam temp probe

* freshpots
  [Fresh Pots!](https://www.youtube.com/watch?v=fhdCslFcKFU)
