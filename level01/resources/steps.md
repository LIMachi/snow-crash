ssh:
- `cat /etc/passwd | grep flag01`
- copy flag01 and the hashed password (`flag01:42hDRfypTqqnw`)

host:
- edit the docker file line 12 so that a file will be created with the copied hashed password between the quotes
- `vim Dockerfile`
- run docker with:
`docker build -t john-ripper .`
`docker run --rm -ti john-ripper`
- copy the cracked password (abcdefg)

TODO: test docker

ssh:
- `su flag01`
- paste the copied password
- `getflag`, copy the flag
- `su level02`, paste the flag as the password