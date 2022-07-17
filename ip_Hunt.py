import os
import sys
import time
import csv
import re
import threading
from datetime import datetime
import inputimeout
import subprocess
from inputimeout import inputimeout, TimeoutOccurred
from subprocess import run 
import getopt	
from reportCreatorScript import reportCreator	
os.system('clear')
def prRed(skk): print("\033[91m {}\033[00m".format(skk))
def prGreen(skk): print('\033[92m {}\033[00m'.format(skk))
def prYellow(skk): print('\033[93m {}\033[00m'.format(skk))
def prLightPurple(skk): print('\033[94m {}\033[00m'.format(skk))
def prPurple(skk): print('\033[95m {}\033[00m'.format(skk))
def prLightGray(skk): print('\033[96m {}\033[00m'.format(skk))
def prCyan(skk): print('\033[97m {}\033[00m'.format(skk))
def prBlack(skk): print('\033[98m {}\033[00m'.format(skk))
def prRRed(skk): print("\033[91m {}\033[00m".format(skk),end='')
def prLLightPurple(skk): print('\033[94m {}\033[00m'.format(skk),end='')
def prrGreen(skk): print('\033[92m {}\033[00m'.format(skk),end='')
print("\n")

prRed('██╗██████╗░░░░░░░██╗░░██╗██╗░░░██╗███╗░░██╗████████╗')
prGreen('██║██╔══██╗░░░░░░██║░░██║██║░░░██║████╗░██║╚══██╔══╝')
prYellow('██║██████╔╝█████╗███████║██║░░░██║██╔██╗██║░░░██║░░░')
prPurple('██║██╔═══╝░╚════╝██╔══██║██║░░░██║██║╚████║░░░██║░░░')
prLightPurple('██║██║░░░░░░░░░░░██║░░██║╚██████╔╝██║░╚███║░░░██║░░░')
prYellow('╚═╝╚═╝░░░░░░░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░')
print("\n")
prGreen("It\'s l!k3 the W!ld W3st , the Int3rn3t - Th3r @re n0 rul3Z")
prRRed("Done by Mohammed Sharoz")
for i in range (0,29):
    prRRed("#")
PowerFlag=0
print("\n")
class Error(Exception):
    """Base Error class"""
    pass
class NoArgumentPassed(Error):
    """Please Enter atleast one auto_mode [-D for daily] [-W for weekly] [ -I to ignore the automode ]"""
    pass
def make_daily_cmd_run():
    nmp='nmap'
    temp_daily_cmd_list=[]
    temp_var2=''
    with open('daily_config.txt') as f:
        daily_config_reader=f.readlines()
    with open('host_IP_scan_list.txt') as g:
        host_IP_reader=g.readlines()
    for i in daily_config_reader:
        i=i.strip('\n')
        i=nmp+' '+i
        for j in host_IP_reader:
            j=i+' '+j
            temp_daily_cmd_list.append(j.strip('\n'))
    #print("\n")
    #print("The daily command to be run is as follows\n")
    #print(temp_daily_cmd_list)    
    #print("*"*100)
    with open('command_prepend.txt') as h:
        command_prepend_reader=h.readlines()
    with open('host_IP_scan_list.txt') as g:
        host_IP_reader=g.readlines()
    for k in command_prepend_reader:
        k=k.strip('\n')
        k=nmp+' '+k
        for l in host_IP_reader:
            l=k+' '+l
            temp_daily_cmd_list.append(l.strip('\n'))
    print('\n')
    #print("The updated Daily command List is as follows\n")
    #print(temp_daily_cmd_list)
    with open('daily_cmd_run.txt','+w')as p:
        for o in temp_daily_cmd_list:
            p.write(o)
            p.write('\n')
def make_weekly_cmd_run():
    nmp='nmap'
    temp_weekly_cmd_list=[]
    temp_var2=''
    with open('weekly_config.txt') as f:
        daily_config_reader=f.readlines()
    with open('hots_IP_scan_list.txt') as g:
        host_IP_reader=g.readlines()
    for i in daily_config_reader:
        i=i.strip('\n')
        i=nmp+' '+i
        for j in host_IP_reader:
            j=i+' '+j
            temp_weekly_cmd_list.append(j.strip('\n'))
    with open('weekly_cmd_run.txt','+w')as p:
        for o in temp_weekly_cmd_list:
            p.write(o)
            p.write('\n')
def auto_store_automated_result():
    print("\nInside the auto store automated result\n")
    current_Dir=os.system("pwd")
    print("\nThe Script is running in the ")
    pass
def config_Files_Checker():
    print("\nInside Config Files Checker\n")
    count=4
    while (count==4):
        config_files_list=['daily_config.txt','weekly_config.txt','command_prepend.txt']
        for q in config_files_list:
            if os.path.isfile(q):
                print("File {d} found ".format(d=q))
                print("\nProceeding to update the files....")
                file_Remove_Cmd_Var='rm '+q
                os.system(file_Remove_Cmd_Var)
        for t in config_files_list:
            if os.path.isfile(t):
                print("file {c} found ".format(c=t))
                count=0
            else:
                print("\nfile {c} not found".format(c=t))
                print("\nDonwloading the config files for you\n")
                url='curl -H \'Authorization: token {YOUR TOKEN HERE} \' -H \'Accept: application/vnd.github.v3.raw\' -O -L https://raw.githubusercontent.com/{YOUR GITHUB USERNAME HERE}/IP-Hunt/main/'+str(t)
                #print(url)
                os.system(url)
                print("\n")
                print("*"*100)
            count=0 
def get_CurrentTime():
    #print("Inside Get Current Time function\n")
    time_now=datetime.now()
    time_now_with_sec=time_now.strftime("__%d-%m-%y__%H-%M-%S_")
    return str(time_now_with_sec)
def check_ScanFolder():
    prGreen("\nInside the check output dir function\n")
    prRed("checking if the dir [ScanResult] is present\n")
    if (os.path.isdir("ScanResult")):
        prYellow("\nScanResult Folder found in the current dir\n")
    else:
        prLightPurple("OOps!! the ScanResult Foledr is not present\n")
        prPurple("Creating the ScanResult Folder for you :)\n")
        os.system('mkdir ScanResult')
        prGreen("Directory created\n")
        print("\nRechecking for confirmation")
        if (os.path.isdir('ScanResult')):
            print("\nSucces ScanFolder presence confirmed proceeding to scanning.....")
        else:
            print("OOOps Error look into the folder for file creation")
def check_ConfigFolder():
    #print("Inside the config folder check\n")
    prLightPurple("Checking if the [ConfigFolder] is present\n")
    if (os.path.isdir('ConfigFolder')):
        prYellow("ConfigFolder is present\n")
    else: 
        prRed("OOps Config folder is not found\n")
        prGreen("Creating the COnfigFOlder For you\n")
        os.system("mkdir ConfigFolder")
        prYellow("Confirming if the ConfigFolder is created\n")
        if (os.path.isdir("ConfigFolder")):
            prPurple("Success the ConfigFolder is found\n")
        else: 
            prLightPurple("There's a problem with the configFolder Creation please look into it\n")
def command_config_File_Pull():
    print("\nInside the command config file pull function\n")
    pass
def daily_File_Config_Pull():
    print("\nInside the daily file config Pull function")
    pass
def week_FIle_Config_pull():
    print("\nInside the weekly file config Pull function")
    pass
def nmap_scan_automode(am):
    main_working_dir=os.getcwd()
    print("\n")
    prPurple("We are currently working from the following directory:\t"+"main_working_dir")
    final_auto_cmd_list=[]
    print("\n")
    prYellow("Executing predefined nmap automated script\n")
    prGreen("\nThe curren running version of nmap is displayed below\n")
    version="nmap --version"
    os.system(version)
    print("\n")
    #read the ports to be scanned from the file 
    tmp_cmd_var_list=[]
    os.chdir(main_working_dir)
    prCyan("\nChecking if the config folder is present or not\n")
    check_ConfigFolder()
    os.chdir('./ConfigFolder')
    config_Files_Checker()
    auto_mode_type=am
    if (auto_mode_type=="D"):
        auto_mode_file_name="daily_cmd_run.txt"
        make_daily_cmd_run()
    elif (auto_mode_type=="W"):
        auto_mode_file_name="weekly_cmd_run.txt"
        make_weekly_cmd_run()
    with open(auto_mode_file_name,"r")as cmdfile:
        reader=csv.reader(cmdfile,delimiter='\n')
        for i in reader:
            tmp_cmd_var_list.append(str(i)) 
        tmp_cmd_var=[]
        zero=0
    for i in tmp_cmd_var_list:
        temp_cmd_holder_var1=i.replace("[",'')
        temp_cmd_holder_var1=temp_cmd_holder_var1.replace("\'",'')
        temp_cmd_holder_var2=temp_cmd_holder_var1.replace("]",'')
        final_auto_cmd_list.append(temp_cmd_holder_var2)
    print("\n")
    fileName=''
    prLightPurple("\nEntering into the command execution Process\n")
    prPurple("The present working dir is :\t"+os.getcwd())
    print("\n")
    #print("\nMoving back to the main folder") 
    os.chdir(main_working_dir)
    prCyan("\nChecking if the scan folder is present or not") 
    check_ScanFolder()
    os.chdir('./ScanResult')
    #print("\nThe directory changed to :\t"+os.getcwd())
    print("\n")
    for i in final_auto_cmd_list:
        auto_command=i # getting the command from the cmd list 
        file_extension_time_var=get_CurrentTime() # adding time to the file 
        fileName=auto_command.replace('--stats-every 1s','') # replacing the unnecesar items in the command 
        fileName=fileName.replace(' ','_') #removing the space fot the purpose of formatting 
        fileName=fileName+file_extension_time_var+'.xml' #here we do ot need the file extension 
        if ('"') in fileName:
            fileName=fileName.replace('"','')
            #print("\nThe quotes replaces filename is {fname}".format(fname=fileName))
            #print("\nsssss")
        auto_command=auto_command+" -oX "+fileName #the command will be saved without the file extension 
        os.system(auto_command)
        #The file must be passed to the other function  that accepts the filename as input and processes that 
        print("\n")
        prRed("command:-->"+auto_command+"  Executed")
        print("\n")
        prPurple("*"*100)
        prRed("#---MOVING TO REPORT GENERATOR SCRIPT---#")
        reportCreator(fileName,main_working_dir)
        print("\n")
    prGreen("<--<Automated scan completed>-->\n")
    

    #print("\nMoving back to the main folder") 
    os.chdir(main_working_dir)
    prYellow("Current Directory: "+os.getcwd())
    prLightGray("\nExiting")
    sys.exit()
def scan_techniques():
    print("\n Inside Scan Techniques")
    pass  
def host_Discovery():
    print("\nInside Host Discovery")
    pass   
def scan_all_ports():
    print("\nInside All ports scan")
    pass
def netbios_scan():
    print("\nInside netbios scan")
    pass 
def service_Version_Detection():
    print("\nInside Version Detection")
    pass
def script_Scan():
    print("\nInside Script Version Scan")
    pass
def nmap_scan_manual_mode():
    prLightPurple("\n00ops M4nu4l M0d3 sc4nn!ng !s und3r c0n5tru(t!0n Y0u h4v3 2 w4!t !:) till n3xt v3rs!0n r3l34s3 by333 ")
    sys.exit()
    print("\nIn the nmap manual scan mode")    
    print('''
    Press 1--> Scan Techniques
    Press 2--> Host Discovery 
    Press 3--> Scan All ports
    Press 4--> Netbios Scan
    Press 5--> Service Version Detection
    Press 6--> Script Scan 
    Press 7--> OS Detection  
    ''')
    print("\nexiting")
    pass 
def nmap_scan():
    print("\n")
    print("Inside nmap scan Options")
    print("\n")
    n_loop=0
    while (n_loop==0):
        print("Inside N_loop")
        print("\n")
        print('''
        Enter z for normal  scan
        Enter x for stealth scan
        Enter c for Xmas    scan 
        Enter v for No Ping scan 
        
        ''')
        print("Do you want to add firewall evesion Technique to the current method You have 5 seconds to choose")
        temp_n=int(input("enter 1 to stop n_loop"))
        n_loop=temp_n
def whois_scan():
    print("\n")
    print("Inside the whois_scan function ")
def file_creation():
    print("\n")
    print("Inside file creation function")
def dir_creation():
    print("\n")
    print("Inside dir creation function")
def file_updation():
    print("\n")
    print("Inside the file updation FUnction")
def dir_update():
    print("\n")
    print("Inside dir updation funtion")
def my_device_ip():
    #print("\nInside my_device_ip")
    prYellow("\nYour local system IP is below\n")
    os.system("hostname -I")
    prLightPurple("\n!!No VPN or Socks proxy used from this machine!!")
    print("\n")
    pass
def main_menu():
    print("\n")
    print("Inside tha main_menu function")
def out_of_time_function():
    time_elapsed=True    
while (PowerFlag==0):
    mode_decision_time=5
    my_device_ip()
    mode_='A'
    time_elapsed=False
    #print("\nInside the main while loop\n")
    prPurple("Waiting to get the decision input Enter [M] for manual test\n")
    time_prompt="You have 5 seconds to choose: "
    argumentList=sys.argv[1:]
    options="dw"
    long_options=["daily","weekly"]
    am='' #auto mode value variable
    try:
        arguments,values=getopt.getopt(argumentList,options,long_options)
        for currentArgument,currentValue in arguments:
            if currentArgument in ("-d","--daily"):
                am='D'
            elif currentArgument in ("-w","--weekly"):
                am='W'
    except NoArgumentPassed:
        print("No arguments Passed")
    try:
        mode_=inputimeout(time_prompt,mode_decision_time)
    except TimeoutOccurred:
        print("\nyour 5 seconds are over")
        pass
    if mode_=='M':
        prRed("\n[Proceeding with manual mode scan]")
        nmap_scan_manual_mode()
    elif mode_=='A':
        print("\nProceeding with the automation script\n")
        nmap_scan_automode(am)
    temp_option_var=input(''' 
    For Nmap type   type :"n"
    For Whois scan  type :"w"
    For Simple ping type :"p"
    ''')
    print("\n")
    if temp_option_var=="n":
        nmap_scan()
    print("\n")
    main_menu()
    print("\n")
    print("Test Loop")
    a=int(input("enter 1 to break Loop: "))
    PowerFlag=a
    
# Get the output normally in the xml format rather than the txt format 
# now call the other script as a function  by using it as a package 
# This package must do its duty of converting the file from the txt format to the report format
  
 
    
    
