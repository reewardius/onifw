#!/usr/bin/python

import os
import socket

from os import makedirs as mkdir
from os import path
from core.gui import color as color
from time import gmtime, strftime

def clearScr():
    os.system('cls||clear')


alreadyInstalled = "Already Installed"
continuePrompt = "\nClick [Return] to continue"

installDir = os.path.dirname(os.path.abspath(__file__)) + '/../'
toolDir = installDir + 'tools/'


### CLASS ###
class microsploit:
    def __init__(self):
        self.installDir = toolDir + "microsploit"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("bash %s/Microsploit" % (self.installDir))

class poet:
    def __init__(self):
        self.installDir = toolDir + "poet"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("python2 %s/server.py" % (self.installDir))

class weeman:
    def __init__(self):
        self.installDir = toolDir + "weeman"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("cd %s/ && python2 weeman.py" % (self.installDir))

class sb0x:
    def __init__(self):
        self.installDir = toolDir + "sb0x"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))


    def run(self):
        os.system("cd %s/ && python2 %s/sb0x.py" % (self.installDir, self.installDir))

class nxcrypt:
    def __init__(self):
        self.installDir = toolDir + "nxcrypt"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))


    def run(self):
        os.system("sudo python2 %s/NXcrypt.py --help" % (self.installDir))

class revsh:
    def __init__(self):
        self.installDir = toolDir + "revsh"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))


    def run(self):
        os.system("chmod +x %s/revsh.c" % self.installDir)
        os.system("cd %s/ && %s/revsh" % (self.installDir, self.installDir))

class nmap:
    def __init__(self, installDir):
        self.installDir = toolDir + "nmap"
        self.normalDir = installDir
        self.targetPrompt = color.LOGGING + "nmap > Enter Target IP/Subnet/Range/Host: " + color.WHITE

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")

        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def run(self):
        target = input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        print("   Nmap scan for: %s\n" % target)
        print("   1 - Ping scan         [-sP]")
        print("   2 - Syn scan          [-sS]")
        print("   3 - UDP scan          [-sU]")
        print("   4 - Version detection [-sV]")
        print("   5 - OS detection      [-O]")
        print("   6 - Aggressive scan   [-A]")
        print("   7 - Scan for vulns    [--script vuln]")
        print("   c - Custom")
        print("   99 - Return \n")
        response = input(color.LOGGING + "nmap > " + color.WHITE)
        clearScr()
        logPath = "{}logs/nmap-".format(self.normalDir) + strftime("%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("nmap -sP -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "2":
                os.system("nmap -sS -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "3":
                os.system("nmap -sU -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "4":
                os.system("nmap -sV -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "5":
                os.system("sudo nmap -O -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "6":
                os.system("nmap -A -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "7":
                os.system("nmap --script vuln -oN %s %s" % (logPath, target))
                response = input(continuePrompt)
            elif response == "c":
                flags = input("Which options: ")
                os.system("nmap %s -oN %s %s" % (flags, logPath, target))
                response = input(continuePrompt)
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

class xsstrike:
    def __init__(self):
        self.installDir = toolDir + "xsstrike"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
            clearScr()
        else:
            response = input(color.LOGGING + "xsstrike > Enter a command (leave blank if unsure) :" + color.WHITE)
            self.run(response)
        

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self, response):
        if not len(response):
            os.system("python3 %s/xsstrike.py -h" % (self.installDir))
        else :
            os.system("python3 %s/xsstrike.py %s" % (self.installDir, response))

class doork:
    def __init__(self):
        self.installDir = toolDir + "doork"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
            clearScr()
        else:
            target = input(color.LOGGING + "doork > Enter a Target: " + color.WHITE)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self, target):
        if not "http://" in target:
            target = "http://" + target
        logPath = "logs/doork-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        try:
            os.system("python2 %s/doork.py -t %s -o %s" %
                      (self.installDir, target, logPath))
        except KeyboardInterrupt:
            pass

class crips:
    def __init__(self):
        self.installDir = toolDir + "crips"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")

        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir) or os.path.isdir("/usr/share/doc/Crips"))

    def run(self):
        try:
            os.system("python2 %s/crips.py" % self.installDir)
        except:
            pass

class wpscan:
    def __init__(self):
        self.installDir = toolDir + "wpscan"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            target = input(color.LOGGING + "wpscan > Enter a Target: " + color.WHITE)
            self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def menu(self, target):
        print("   WPScan for: %s\n" % target)
        print("   1- Username Enumeration [--enumerate u]")
        print("   2 - Plugin Enumeration [--enumerate p]")
        print("   3 - All Enumeration Tools [--enumerate]\n")
        print("   r - Return to information gathering menu \n")
        response = input(color.LOGGING + "wpscan > " + color.WHITE)
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner --random-agent --url %s" % target
        try:
            if response == "1":
                os.system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate u --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "2":
                os.system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate p --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "3":
                os.system(
                    "ruby tools/wpscan/lib/wpscan.rb %s --enumerate --log %s" % (wpscanOptions, logPath))
                response = input(continuePrompt)
            elif response == "r":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)

class setoolkit:
    def __init__(self):
        self.installDir = toolDir + "setoolkit"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        print("%ssetoolkit/setoolkit" % toolDir)
        print(os.path.isfile("%s/setoolkit/setoolkit" % (toolDir)))
        return (os.path.isfile("%s/setoolkit/setoolkit" % (toolDir)))

    def run(self):
        os.system("sudo %ssetoolkit/setoolkit" % (toolDir))

class apwps:
    def __init__(self):
        self.installDir = toolDir + "apwps"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:   
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("python2 %s/autopixie.py" % self.installDir)

class snmp:
    def __init__(self):
        self.installDir = toolDir + "snmp"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        target = input("Enter Target IP: ")
        os.system("python2 %s/snmpbrute.py -t %s" % (self.installDir,target))

class pyphi:
    def __init__(self):
        os.system("wget http://pastebin.com/raw/DDVqWp4Z --output-document=pypisher.py")
        clearScr()
        os.system("mv pypisher.py %spypisher.py" % (toolDir))
        os.system("python2 %spypisher.py" % (toolDir))

class stmp:
    def __init__(self):
        os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
        clearScr()
        os.system("mv smtp.py %ssmtp.py" % (toolDir))
        os.system("python2 %ssmtp.py" % (toolDir))

class sslstrip:
    def __init__(self):
        self.installDir = toolDir + "sslstrip"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        target = input("Enter Target IP: ")
        os.system("python2 %s/sslstrip.py %s" % (self.installDir, target))

class cupp:
    
    def __init__(self):
        self.installDir = toolDir + "cupp"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("python3 %s/cupp.py -i" % self.installDir)

class brutex:
    def __init__(self):
        self.installDir = toolDir + "brutex"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        target = input(color.LOGGING + "BruteX > " + color.WHITE + "Enter Target IP: ")
        os.system("brutex %s" % target)

class leviathan:
    
    def __init__(self):
        self.installDir = toolDir + "leviathan"

        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("python2 %s/leviathan.py -i" % self.installDir)

class nikto:
    def __init__(self):
        self.installDir = toolDir + "nikto"
        self.targetPrompt = color.IMPORTANT + "Nikto > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            clearScr()
            self.run()
    def installed(self):
        return (os.path.isfile("%s/program/nikto.pl" % self.installDir))

    def run(self):
        target = input(self.targetPrompt)
        self.menu(target)
    def menu(self, target):
        os.system("perl %s/program/nikto.pl -h %s" % (self.installDir, target))
               
class rscan:
    def __init__(self):
        self.installDir = toolDir + "rapidscan"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            self.targetPrompt = color.LOGGING + "rscan > "  + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
            target=input(self.targetPrompt)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self, target):
        os.system("python2 %s/rapidscan.py %s" % (self.installDir, target))

class arachni:
    def __init__(self):
        self.installDir = toolDir + "arachni"
        if not os.path.isdir(self.installDir):
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:self.run()

    def run(self):
        target = input(color.LOGGING + "Arachni > " + color.LOGGING + "Enter Target Hostname/URL: ")
        os.system("sudo arachni %s" %(target))

class sqlmap:
    def __init__(self):
        self.installDir = toolDir + "sqlmap"
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else : self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("python2 %s/sqlmap.py --wizard" % (self.installDir))

class slowloris:
    def __init__(self):
        self.installDir = toolDir + "slowloris"
        self.targetPrompt = color.LOGGING + "slowloris > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            target = input(self.targetPrompt)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self,target):
        os.system("python3 %s/slowloris.py %s" % (self.installDir, target))

class pwnloris:
    def __init__(self):
        self.installDir = toolDir + "pwnloris"
        self.targetPrompt = color.LOGGING + "pwnloris > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:
            target = input(self.targetPrompt)
            self.run(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self,target):
        os.system("python3 %s/pwnloris.py %s" % (self.installDir, target))

class atscan:
    def __init__(self):
        self.installDir = toolDir + "atscan"
        self.targetPrompt = color.LOGGING + "ATscan > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")

        else:self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("perl %s/atscan.pl --interactive" % (self.installDir))

class hyde:
    def __init__(self):
        self.installDir = toolDir + "hyde"
        self.targetPrompt = color.LOGGING + "Hyde > " + color.WHITE + "Enter Target IP/Subnet/Range/Host: "
        if not self.installed():
            print("[*] - Tool not installed.\n[*] - Please use pkg -i [pkg] to install it.")
        else:self.run()

    def installed(self):
        return (os.path.isdir(self.installDir))

    def run(self):
        os.system("python3 %s/hyde/main.py" % (self.installDir))


# Default 
'''
hashcheck
viewtraffic
netmanager
onimap
'''

class ipfind:
    def __init__(self):
        host = input(color.LOGGING +
                     "onifw/IPfinder > Enter URL: " + color.WHITE)
        ip = socket.gethostbyname(host)
        print("[*] - The IP of %s is: %s" % (host, ip))

class hashcheck:
    def __init__(self,logDir):
        filepath=input(color.LOGGING+"Enter path of file: ")
        print("Hash checker")
        print("1 - MD5")
        print("2 - sha1")
        print("3 - sha224")
        print("4 - sha256")
        print("99 - exit")
        hashtype = input("onifw/hashcheck> ")
        if hashtype=="1":
            os.system("md5sum {}".format(filepath))
        elif hashtype == "2":
            os.system("sha1sum {}".format(filepath))
        elif hashtype=="3":
            os.system("sha224sum {}".format(filepath))
        elif hashtype == "4":
            os.system("sha256sum {}".format(filepath))

class servicestatus:
    def __init__(self,logDir):
        self.logDir=logDir
        if not path.isdir(self.logDir):mkdir(self.logDir)  # Make folder
        print(color.LOGGING)
        os.system("ps -ef > {}/services.out".format(self.logDir))
        print(color.END + color.NOTICE + "[*] - Log saved in the .onifw/src/logs/ dir")
        print(color.END)


class firewall:
    def __init__(self,logDir):
        self.logDir = logDir
        if not path.isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print(color.LOGGING)
        print("FIREWALL SETUP")
        print("1 - Export firewall current setup")
        print("2 - Edit firewall table")
        print("3 - Apply iptable")
        print("99 - exit")
        print(color.END)
        choice = input("onifw/firewall > ")
        if choice == "1":
            os.system("iptables-save > {}/firewall.out".format(self.logDir))
        elif choice == "2":
            os.system("iptables-save > {}/firewall.out".format(self.logDir))
            os.system("vi {}/firewall.out".format(logDir))
        if choice == "3":
            os.system("iptables-restore < {}/firewall.out".format(self.logDir))


class viewtraffic:
    def __init__(self,logDir):
        self.logDir = logDir
        if not path.isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print("TRAFFIC ANALYSIS")
        print("1 - Tcpdump")
        print("2 - Tshark")
        choice = input("onifw/trafficanalyzer > ")
        if choice == "1":
            os.system("sudo tcpdump -A -vv > {}/tcpdump.out".format(self.logDir))
        elif choice == "2":
            os.system("sudo tcpdump -w {}/tshark.pcap".format(self.logDir))


class networkmanaged:
    def __init__(self,logDir):
        self.logDir = logDir
        if not path.isdir(self.logDir):
            mkdir(self.logDir)  # Make folder
        print("wireless monitoring")
        print("1 - Enable monitoring mode")
        print("2 - Disable monitoring mode")
        print("99 - Exit ")
        ans = input(color.LOGGING+"onifw/netmanager > "+color.END)
        if ans == "1":
            inter_name = input("interface name: ")
            try:
                os.system("sudo iwconfig {} down".format(inter_name))
                os.system("sudo iwconfig {} mode monitor".format(inter_name))
                os.system("sudo iwconfig {} up".format(inter_name))
            except:
                print(
                    color.IMPORTANT+"[!] - An error occurred, check if iwconfig is installed and the name of the interface"+color.END)
        elif ans == "2":
            inter_name = input("interface name: ")
            try:
                os.system("sudo iwconfig {} down".format(inter_name))
                os.system("sudo iwconfig {} mode managed".format(inter_name))
                os.system("sudo iwconfig {} up".format(inter_name))
            except:
                print(
                    color.IMPORTANT+"[!] - An error occurred, check if iwconfig is installed and the name of the interface"+color.END)


class onimap:
    def __init__(self,installDir,logDir):
        self.logDir = logDir
        self.installDir = installDir
        print("Which target to scan")
        target = input("onifw/onimap > ")
        os.system("{0}core/onimap {1}".format(self.installDir,target))
