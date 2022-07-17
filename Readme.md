Hi Fellow Pentesters Presenting you Ip-Hunt the All-in-one Ip tool suite [Still under development]


██╗██████╗░░░░░░░██╗░░██╗██╗░░░██╗███╗░░██╗████████╗
██║██╔══██╗░░░░░░██║░░██║██║░░░██║████╗░██║╚══██╔══╝
██║██████╔╝█████╗███████║██║░░░██║██╔██╗██║░░░██║░░░
██║██╔═══╝░╚════╝██╔══██║██║░░░██║██║╚████║░░░██║░░░
██║██║░░░░░░░░░░░██║░░██║╚██████╔╝██║░╚███║░░░██║░░░
╚═╝╚═╝░░░░░░░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░

"It's l!k3 the W!ld W3st , the Int3rn3t - Th3r @re n0 rul3Z"

Done by Mohammed Sharoz 

Features Present:
-----------------

1)Configure the nmap scan for automatic scanning - cutomizable scan where you can scan a large number of IP's with different scan automatically and get the open ports under a separate file in txt format .

Features to be added:
---------------------

1)Manual scan by selection combination of different options 
2)Ip tracing 
3)Ip spoofing 
and so on 

Configuration and Installation:
-------------------------------

1)In you github account create the following files for configuring the scans 
2)Get you github API Token open the ConfigFolder and open the ip_Hunt.py script 
3)Search for the word "curl" replace {YOUR TOKEN HERE} with your github API Token 
4)Replace the {YOUR GITHUB USERNAME HERE} with your github username account 
5)For the First Time you need to create the ConfigFolder and under that create the "host_IP_scan_list.txt"
6)Always the IP-Hunt tool with the "sudo" command in-case you configured any nmap commands that require root privileges and for updating the tool 
7)Better use the "sudo" command followed by "python3 ip_Hunt.py {Specify-your-option-Here}"
8)The option can be "-d"  or "-w" , where the -d specifies the ip_hunt tool to use the daily config files and the -w specifies to use the weekly config files 
9)The "daily_cmd_run.txt" -contains the commans to be run daily (uselful when we need it as a cron job) the "weekly_cmd_run.txt" file will contain aggressive commands that can be run once in a week 
10)The daily_cmd_run and the weekly_cmd_run files will be "automatically created" by merging the configuration files that we have created 
11)To make any changes in the daily and the weekly cmd files you need to alter the main configuration files on the GitHub 
12)IMPORTANT: Make sure there are no trailing new lines "\n" in the configuration files  or the Host_IP_configuration file since it will interfere with the command execution and you will receieve an error .

You are good to go !!!!





