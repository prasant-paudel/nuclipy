from random import choice
from .colors import Colors

BANNERS = '''
                     ___            
   ____  __  _______/ (_)___  __  __
  / __ \/ / / / ___/ / / __ \/ / / /
 / / / / /_/ / /__/ / / /_/ / /_/ / 
/_/ /_/\__,_/\___/_/_/ .___/\__, /  
                    /_/    /____/   

---split---
                         __    _                   
                        [  |  (_)                  
 _ .--.  __   _   .---.  | |  __  _ .--.   _   __  
[ `.-. |[  | | | / /'`\] | | [  |[ '/'`\ \[ \ [  ] 
 | | | | | \_/ |,| \__.  | |  | | | \__/ | \ '/ /  
[___||__]'.__.'_/'.___.'[___][___]| ;.__/[\_:  /   
                                 [__|     \__.'    
---split---
 ▄▄    ▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ 
█  █  █ █  █ █  █       █   █   █   █       █  █ █  █
█   █▄█ █  █ █  █       █   █   █   █    ▄  █  █▄█  █
█       █  █▄█  █     ▄▄█   █   █   █   █▄█ █       █
█  ▄    █       █    █  █   █▄▄▄█   █    ▄▄▄█▄     ▄█
█ █ █   █       █    █▄▄█       █   █   █     █   █  
█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█▄▄▄█     █▄▄▄█  
---split---
                 _  _  _ __  _  _ 
 _ _   _  _  __ | |(_)| '_ \| || |
| ' \ | || |/ _|| || || .__/ \_. |
|_||_| \_._|\__||_||_||_|    |__/ 
---split---
            ╔╗            
            ║║            
╔═╗ ╔╗╔╗╔══╗║║ ╔╗╔══╗╔╗ ╔╗
║╔╗╗║║║║║╔═╝║║ ╠╣║╔╗║║║ ║║
║║║║║╚╝║║╚═╗║╚╗║║║╚╝║║╚═╝║
╚╝╚╝╚══╝╚══╝╚═╝╚╝║╔═╝╚═╗╔╝
                 ║║  ╔═╝║ 
                 ╚╝  ╚══╝ 
---split---
 / \---------------, 
 \_,|              | 
    |    nuclipy   | 
    |  ,-------------
    \_/____________/ 

  ___             ___  
 (o o)           (o o) 
(  V  ) nuclipy (  V  )
--m-m-------------m-m--
'''
ABOUT = """
nuclipy - Template based vulnerability scanner inspired by Nuclei
https://github.com/prasant-paudel/nuclei-python
"""
COLORS = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]

print(
    choice(COLORS) 
    + choice(BANNERS.split('---split---'))
    + '\n' + ABOUT
    + Colors.RESET)

