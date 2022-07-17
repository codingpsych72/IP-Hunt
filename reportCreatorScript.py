import re
import os
import sys
import datetime
from datetime import datetime

def reportCreator(fileNam,current_Dir):
    working_dir=current_Dir+'/ScanResult'
    file_name=fileNam
    def check_ReportFolder():
        print("\n")
        print("Inside the check output dir function\n")
        print("checking if the dir [ReportFolder] is present\n")
        if (os.path.isdir("ReportFolder")):
            print("\nReportFolder found in the current dir")
        else:
            print("\n")
            print("OOps!! the ReportFolder is not present\n")
            print("Creating the ReportFolder for you :)\n")
            os.system('mkdir ReportFolder')
            print("\n")
            print("Directory created\n")
            print("\nRechecking for confirmation")
            if (os.path.isdir('ReportFolder')):
                print("\nSucces ReportFolder presence confirmed proceeding to scanning.....")
            else:
                print("\nOOOps Error look into the folder for file creation\n")
    def Open_port_splitter(u,port_element_buffer):
        host_ip=u
        port_element_buffer_carrier=port_element_buffer
        if port_element_buffer=='' or port_element_buffer==None:
            print("\nThere are no open Ports\n")
            open_port_stats="No Open Ports FOund"
            no_Open_Port_Report_printer(host_ip,open_ports_stats)
        a=port_element_buffer_carrier.split("reason=\"")
        temp_list=[]
        for i in range(0,len(a)):
            if "/><service" in a[i]:
                temp_list.append(a[0])
                b=a[i].split("/><service ")
                #print("\nSplitted with the service\n")
                #print("Printing the value of b ")
                #print(b)
                #print("\n")
                for i in b:
                    temp_list.append(i)
        temp_list_holder=[]
        temp_list_holder.append(temp_list[0])
        temp_list_holder.append(temp_list[2])
        list_file_writer=''
        for i in temp_list_holder:
            if "><state" in i:
                c=i.replace("><state",'')
                c=c.replace("<port ",'')
                list_file_writer=c
                i=list_file_writer
            if "method=" in i:
                d=i.split(" method")
                d=d[0]
                list_file_writer=list_file_writer+''+d
                i=list_file_writer
            if "product=" in i:
                e=i.split(" product=")
                e=e[0]
                list_file_writer=e
        list_file_writer=list_file_writer.replace("\"","")
        list_file_writer=list_file_writer.replace('=',',')
        list_file_writer=list_file_writer.replace(' ',',')
        list_file_writer=list_file_writer.replace(' Product=\"Apache https\"','')
        lst=[]
        dict_list=[]
        lst=list_file_writer.split(",")
        dict_of_values=Convert_list_to_Dict(lst)
        return dict_of_values
    
    with open(file_name)as f:
        xml_reader=f.readlines()
    port_search_key_element='portid'
    port_table_element_list=[]

    def no_Open_Port_Report_printer(host_ip,open_ports_stats,file_name,working_dir):
        main_dir=working_dir
        hostIp=host_ip
        file_name_buffer=file_name
        no_open_port_var=open_ports_stats
        openPort_header='''
********************
        Open Ports
********************
    ''' 
        host_format_var='''
******************************************************************
**********Scan Results for {ip_placeholder} *************************
******************************************************************
        '''.format(ip_placeholder=hostIp)
        check_ReportFolder()
        folder_shift=os.getcwd()
        print("\nno open port function folder shift {foldr}".format(foldr=folder_shift))
        folder_shift=folder_shift+'/ReportFolder'
        os.chdir(folder_shift)
        with open(file_name_buffer,'w')as fn:
            fn.write(host_format_var)
            fn.write("\n")
            fn.write(openPort_header)
            fn.write("\n")
            fn.write(no_open_port_var)
        os.chdir(main_dir)
        print("Current Dir")
        print(os.getcwd())
        print("\n")
            
        
    def report_Printer(u,list_of_dict,file_name,working_dir):
        main_dir=working_dir
        file_name_buffer=file_name
        hostIp=u
        temp_list=list_of_dict
        openPort_header='''
********************
        Open Ports
********************
    '''
        closedPort_header='''
********************
        Closed Ports
********************
    ''' 
        host_format_var='''
******************************************************************
**********Scan Results for {ip_placeholder} *************************
******************************************************************
        '''.format(ip_placeholder=hostIp)
        check_ReportFolder()
        folder_shift=os.getcwd()
        folder_shift=folder_shift+'/ReportFolder'
        os.chdir(folder_shift)
        with open(file_name_buffer,'w')as fn:
            fn.write(host_format_var)
            fn.write("\n")
            fn.write(openPort_header)
            fn.write("\n")
            for i in temp_list:
                if i['state']=='open':
                    fn.write(i['portid'])
                    fn.write("\n")
            fn.write(closedPort_header)
            for i in temp_list:
                if i['state']=='closed':
                    fn.write("\n")
                    fn.write(i['portid'])
                else:
                    fn.write("\n")
                    fn.write("No Open Ports Detected")
                    break
        os.chdir(main_dir)
        print("Current Dir")
        print(os.getcwd())
        print("\n")
        print("\nWORKING DIRECTORY IS {WD}".format(WD=working_dir))
    host_search_key_element='nmaprun scanner'
    host_table_element=''
    for e in xml_reader:
        if (host_search_key_element) in e:
            host_table_element=e
    def Convert_list_to_Dict(lst):
         resulting_dict={lst[i]:lst[i+1] for i in range(0,len(lst),2)}
         return resulting_dict
    for i in xml_reader:
        if (port_search_key_element) in i:
            port_table_element_list.append(i)
    IP_grabber_pattern=re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
    ip_=IP_grabber_pattern.search(host_table_element)
    print(str(ip_.group()))
    z=str(ip_.group())
    time_now=datetime.now()
    time_file_format_extension=time_now.strftime("Date:_%d_%m_%y___Time:_%H_%M_%S__")
    file_name1=str(z).replace('.','_')
    file_name1='IP:_'+file_name1
    file_name1=file_name+'_'+time_file_format_extension+'.txt'
    file_name1=file_name+'_'+file_name1
    file_name=file_name1
    port_element_buffer=''
    if (len(port_table_element_list)==0):
        print("\nNo Open Ports Detected\n")
        no_op_var="No Open Ports Detected all are either filtered or closed or in ignored state"
        no_Open_Port_Report_printer(z,no_op_var,file_name,working_dir)
        print("\n")
        print("*"*100)
        print("\n")
        os.chdir(working_dir)
        
    else:
        list_of_dict=[]
        for i in port_table_element_list:
            if 'portused' in i:
                continue
            port_element_buffer=i
            print("\nPrinting the port element buffer before calling the Open SPlitter\n")
            print(port_element_buffer)
            splitter_op_buffer=Open_port_splitter(z,port_element_buffer)
            print(type(splitter_op_buffer))
            print(splitter_op_buffer)
            print("\nAppending the splitter_op_buffer to the list_of_dict\n")
            list_of_dict.append(splitter_op_buffer)
            print("Printing the List of dict\n")
            print(list_of_dict)
            print("\nPrinting the list of the dictionary that can be used to print the report\n")
            print(list_of_dict)
            host_Header_holder_buffer=''
            Open_port_holder_buffer=''							
            print("\nPrinting the Open_port_holder_buffer\n")
            report_Printer(z,list_of_dict,file_name,working_dir)
            print("\nREPORT CREATED SCRIPT COMPLETED")
            os.chdir(working_dir)
            
if __name__=="__main__":
    reportCreator() 


