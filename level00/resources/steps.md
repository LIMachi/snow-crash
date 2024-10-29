ssh:
- `cat /rofs/usr/sbin/john`
- copy the output

host:
- go to https://www.dcode.fr/caesar-cipher
- paste in the cipher text box
- hit decrypt (bruteforce)
- copy the first result on the left (`nottoohardhere`, using 11 shifts, is the correct answer)

ssh:
- `su flag00`
- paste `nottoohardhere` as the password
- `getflag`, copy the flag
- `su level01`, paste the flag as the password