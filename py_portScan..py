from socket import *

def conScan(host, port) :
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((host, port))
        print("[+]%d/tcp open" % port)
        conn.close()
    except:
        print("[-]%d/tcp closed" % port)

def portScan(host, ports):
    try:
        ip = gethostbyname(host)
    except:
        print("[-] Cannot resolve %s" % host)
    
    try:
        name = gethostbyaddr(ip)
        print("\n[+] Scan result of: %s" % name[0])
    except:
        print("\n[+] Scane result of: %s" % ip)
    setdefaulttimeout(1)

    for port in ports:
        print("Scanning port: %d" % port)
        conScan(host, int(port))

if __name__ == '__main__':
    portScan("google.com", [80, 22]) # ("address", [port])