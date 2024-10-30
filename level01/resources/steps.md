ssh:
- `cat /etc/passwd | grep flag01`
- we will need to copy `flag01:42hDRfypTqqnw` into `utils`

utils:
- `echo "flag01:42hDRfypTqqnw" > /tmp/crack`
- `sudo john /tmp/crack`
- `sudo cat /root/.john/john.pot` or `cat ~/.john/john.pot` (depends on how john was installed/run and privileges)
- the cracked password is found: `abcdefg`, copy it

ssh:
- `su flag01`, paste the password
- `getflag`, copy the flag
- `su level02`, paste the flag as the password