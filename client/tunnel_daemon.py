import os, time


PORT = 2001

def isEmpty(n):
        return n != ''

def check_tannel():
    r = os.popen('ss -tnl')
    text = r.read()
    for line in text.splitlines():
        ds = line.split(' ')
        f = list(filter(isEmpty, ds))
        port = f[3]
        if port[-4:] == str(PORT):
            return True
    return False

def start_tannel():
    r = os.popen('/usr/bin/autossh -M 2001 -fCNR 1022:localhost:22 -i /home/eric/.ssh/id_rsa root@domain.com')
    text = r.read()


while True:
    is_up = check_tannel()
    if not is_up:
        start_tannel()
    time.sleep(20)