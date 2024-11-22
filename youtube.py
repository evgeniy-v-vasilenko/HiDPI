import os

def BlockYoutube():
    yout=['142.251.40.206','142.251.41.14','142.251.40.174','142.250.176.206','142.251.40.110','142.250.65.174','142.251.40.206']
    for ip in yout:
        os.system(f'netsh advfirewall firewall add rule name="BLOCK IP ADDRESS - {ip}" dir=out action=block remoteip={ip}')

def UnblockYoutube():
    os.system('netsh advfirewall reset')
