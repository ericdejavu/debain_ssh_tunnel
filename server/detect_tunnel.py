import os, time

is_up = False

PORT = 1022

def isEmpty(n):
        return n != ''

while True:
        r = os.popen('ss -tnl')
        text = r.read()
        scan_res = False
        for line in text.splitlines():
                ds = line.split(' ')
                f = list(filter(isEmpty, ds))
                port = f[3]
                if port[-4:] == str(PORT):
                        scan_res = True
        if is_up and not scan_res:
                is_up = False
                print ('tannel down')
        elif not is_up and scan_res:
                is_up = True
                print ('tannel up')
        time.sleep(2)