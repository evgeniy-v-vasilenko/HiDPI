from rich import print as p
from rbxl import *
from youtube import *
p('--Hi DPI V.1.0 by kotodobr--')
p('[green]1[/green] - Block Roblox')
p('[green]2[/green] - Block YouTube')
p('[green]3[/green] - Unblock YouTube')
p('[green]4[/green] - Unblock roblox')
while True:
    option=input('Option: ')
    if option=='1':
        p('[yellow] Blocking roblox... [/yellow]')
        BlockRoblox()
        p('[green] Roblox blocked! [/green]')
    elif option=='2':
        p('[yellow] Blocking youtube... [/yellow]')
        BlockYoutube()
        p('[green] YouTube blocked! [/green]')
    elif option=='3':
        p('[yellow] Unblocking youtube... ')
        UnblockYoutube()
        p('[green] YouTube already unblocked![/green]')
    elif option=='4':
        p('[yellow] Unblocking roblox...[/yellow]')
        UnblockRoblox()
        p('[green] Roblox already unblocked![/green]')
    else:
        p('[red] Invalid option! [/red]')
