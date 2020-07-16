
#!usr/bin/env python3
import sys
import os
import subprocess
import time

os.system("clear")

print ("hi friends its new ")

print ("--------------------------------------------------")

print ("")
print ("")
print ("")
print ("")
print ("")
print ("copy paste 1st or 2nd 192.168.0.1/24  and 192.168.1.1/24")

def own(text):
    print ("hello guys " + text)

own("i am unknown")

ip = input("enter router ip:")

subprocess.call("nmap -sn " + ip , shell=True)
print ("")
print ("")
 
print ("IF U WANT MAC ADDR OF IP'S TYPE SUDO AND AFTER TYPE network_scanner.py")
							       
