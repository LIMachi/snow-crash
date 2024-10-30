IMPORTANT:
-
ip address of the vm's aren't guaranteed to be the same as the ones used in the steps, use `ifconfig` or `ip address` to check the valid ip and change them as needed in the steps

\
\
first start Virtual Box


- make sure there is a local network setup:
- - recent version: go to file->tools->network manager
- - old version: go to file->preferences->network manager


- then if there is no host only network available create a new one (new version will be automatic, old version might require some settings).
by default it is 192.168.56.1, and the first vm will usually be assigned the ip 192.168.56.101 (and if you use another vm, it probably will be at 192.168.56.102).


- now go back to the main vb page and click new, put any name, select any folder (preferably not on your home as vms can be quite large),
finally select the iso image (all the other options below should be grayed),
click next, let the default (2gb ram, 1 processor), click next, you can lower the disk size or let it be, next then finish.


- once created, select it and go to settings->network and switch the adapter to host-only, using the one you created before or the one by default if it was already there.


start the vm, if everything worked the vm should show an ip that starts similar to the host only network adapter (ex: 192.168.56.101).

now you can start a ssh connection to the vm on any terminal outside the vm by using `ssh -p 4242 level00@192.168.56.101` and inputting level00 as the password when prompted.

for the rest of the evaluation, `host` will refer to the host machine running vm, `ssh` a terminal connected to the vm running snow_crash via ssh, and `utils` is a secondary vm to run `john-the-ripper` and `wireshark`.

`host` is always expected to be running in the resources folder of the current level