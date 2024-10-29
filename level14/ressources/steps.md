ssh:
- `gdb /bin/getflag`

gdb:
- `b *0x0804898e`
- `r`
- `set $eax = 0`
- `b *0x08048b0a`
- `c`
- `set $eax = 0x0bc6`
- `c`, copy the flag
- `q`

ssh:
- `su flag14`, paste the flag as the password
- WE IN IT BOYZ!!