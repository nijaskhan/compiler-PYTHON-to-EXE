import os
import subprocess
import time

os.system('cls')

blue = '\x1b[34m'
green = '\x1b[32m'
red = '\x1b[41m'
cyan = '\x1b[36m'
stop = '\x1b[0m'

print(f"""{blue} ____  ____  _     ____  _  _    _________      _______  _   _____  ____    ________  ______
/   _\/  _ \/ \__//  __\/ \/ \  /  __/  __\    /  __\  \//  /__ __\/  _ \  /  __/\  \//  __/
|  /  | / \|| |\/||  \/|| || |  |  \ |  \/|    |  \/|\  /     / \  | / \|  |  \   \  /|  \  
|  \__| \_/|| |  ||  __/| || |_/\  /_|    /    |  __// /      | |  | \_/|  |  /_  /  \|  /_ 
\____/\____/\_/  \\_/   \_/\____|____\_/\_\    \_/  /_/       \_/  \____/  \____\/__/\\____\
                                                                                             {stop}

{red}THIS SOFTWARE ONLY WORKS IF PYTHON IS INSTALLED ON THIS COMPUTER{stop}""")
print('\n')

while True:
    yes = input(f'{cyan}Do you want to convert this python file To exe [yes, no] :{stop} ')
    print('\n')
    pyNu = input(f'''{cyan}
[1] pyinstaller 
[2] nuitka

which method : {stop}''')

    if pyNu == '1':
        name = input(f'{green}PythonFile [path]: {stop}')
        try:
            print(f"""{red}inorder to convert this to exe you needed python installed{stop}""")
            try:
                subprocess.run(f'pyinstaller --onefile {name}', shell=True)
                cwd = os.getcwd()
                print(f'{green}compiled EXE saved on {cwd} {stop}')
                print('\n')
                next = input(f'{cyan}Do you want to convert another python file [press any key]{stop}')
            except Exception:
                print(f'{red}pyinstaller not installed{stop}')
                print(f'{blue}installing pyinstaller{stop}')
                subprocess.run('pip install pyinstaller', shell=True)
                print(f'{green}pyinstaller installed{stop}')
                print('\n')
                subprocess.run(f'pyinstaller --onefile {name}', shell=True)
                print(f'{green}compiled EXE saved on {cwd} {stop}')
                print('\n')
                next = input(f'{cyan}Do you want to convert another python file [press any key]{stop}')
        except Exception as e:
            print(f'{red}{e}{stop}')
    elif pyNu == '2':
        name = input(f'{green}PythonFile [path]: {stop}')
        try:
            print(f"""{red}inorder to convert this to exe you needed python installed{stop}""")
            try:
                subprocess.run(f'py -m nuitka --mingw64 {name} --standalone --onefile', shell=True)
                cwd = os.getcwd()
                print(f'{green}compiled EXE saved on {cwd} {stop}')
                print('\n')
                next = input(f'{cyan}Do you want to convert another python file [press any key]{stop}')
            except Exception:
                print(f'{red}nuitka not installed{stop}')
                print(f'{blue}installing nuitka{stop}')
                subprocess.run('pip install nuitka', shell=True)
                print(f'{green}nuitka installed{stop}')
                print('\n')
                subprocess.run(f'py -m nuitka --mingw64 {name} --standalone --onefile', shell=True)
                print(f'{green}compiled EXE saved on {cwd} {stop}')
                print('\n')
                next = input(f'{cyan}Do you want to convert another python file [press any key]{stop}')
        except Exception as e:
            print(f'{red}{e}{stop}')
    else:
        print(f'{blue}compiler exiting.... Thank You !!{stop}')
        time.sleep(4)
