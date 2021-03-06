#!/usr/bin/python3
import sys, socket
from datetime import datetime as date
from sys import exc_info

def main(target, verbose=False):
    """
    Main component of pymap
    @params:
        target:         - Required  :   ip/hostname of the scan target (str)
        verbose:        - Optional  :   prints loading bar if True (bool)
        outputfile:     - Optional  :   print result of scan in outputfile (str)
    """
    flag=False
    # SMTP, HTTP, HTTPS, FTP, TELNET, IMAP, RDP, SSH, DNS, DHCP, POP3
    default_ports=[25,80,443,20,21,23,143,3389,22,53,67,68,110]
    print("-"*30)
    print("ONIMAP 1.2")
    print("Scanning target: "+target)
    print("Time started: "+str(date.now()))
    print("-"*30)
    try:
        for port in default_ports:
            s=socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            s.close()
            if verbose:
                #print("[*] - Testing port {}...".format(port))
                printProgressBar(default_ports.index(port),len(default_ports))
            if result==0:
                flag=True
                print("[!] - Port {} is open".format(port))
    except KeyboardInterrupt:
        print("[!] - Leaving program")
        sys.exit(1)
    except socket.gaierror:
        print("[!] - Host not found")
        sys.exit(1)
    except socket.error:
        print("[!] - Couldn't connect to server")
        sys.exit(1)
    except:
        print(exc_info())
    if flag==False:
        print("[***] - No ports open")
        sys.exit(1)


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print("\n\n")

def helper():
    print("onimap")
    print("Usage: ./onimap [flag] [host]")
    print("host is an ip address or name")
    print("Available flags:")
    print("-v    displays verbose")
#debug


if len(sys.argv)>=2:
    target=socket.gethostbyname(sys.argv[len(sys.argv)-1])
    if len(sys.argv)==2:
        main(target)
    elif len(sys.argv)==3:
        if sys.argv[len(sys.argv)-2]=="-v" :
            main(target,True)
else:
    print("[!] - No argument parsed");
    helper()
    sys.exit(1)
