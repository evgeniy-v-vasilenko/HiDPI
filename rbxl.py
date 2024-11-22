import os

def BlockRoblox():
    rbxl=['128.116.21.3','128.116.50.3','128.116.32.3','128.116.32.4','128.116.99.4','128.116.123.4','128.116.127.4','128.116.127.4','128.116.102.3','128.116.123.3','128.116.127.4','128.116.127.4','128.116.102.3','128.116.119.4','128.116.63.3','128.116.21.4','128.116.97.3','128.116.51.4','128.116.116.4']
    for ip in rbxl:
        os.system(f'netsh advfirewall firewall add rule name="BLOCK IP ADDRESS - {ip}" dir=out action=block remoteip={ip}')
def UnblockRoblox():
    os.system('netsh advfirewall reset')
