ssh:
- `gdb ./level13`

gdb:
- `b main`
- `r`
- `set {char}0x0804859f = 0xeb`
- `c`, copy the flag
- `q`

ssh:
- `su level14`, paste the flag as the password