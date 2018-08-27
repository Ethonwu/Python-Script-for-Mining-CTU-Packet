#!/usr/bin/env python
import sys
import string
import re
import os
from optparse import OptionParser
import linecache
import operator
def GetInfo(txt_File):
    num_of_packet_frame = 0
    packet_line = 1
    packet_info = list()
    protocol_info = dict()
    flag = False
    i = 1
    with open(txt_File,'rb') as f:
        for line in f:
            s = line.strip('\n')
            #print "Now Doing Line:",packet_line
            
            #if flag is True:
            #    print s
           # OutputFile(s,txt_File,i)
                #proto = s.split()[5]
                #if proto not in protocol_info:
                #    print "Add new proto:"+str(proto)
                #    protocol_info[proto] = 1
                #else:
                #    protocol_info[proto] = protocol_info[proto] + 1
                #flag = False
            """if flag is True:    
                source_ip = "src_ip-"+info[3]
                dst_ip = "dst_ip-" + info[4]
                protocol = "proto-" + info[5]
                packet_info.append(source_ip)
                packet_info.append(dst_ip)
                packet_info.append(protocol)
                flag = False
            """
            #if s[0:3]=="No.":
            if s[0:5]=="Frame":
                if len(packet_info) ==5:
		    print "I'm here"
                    print packet_info
                    OutputFile(packet_info,date)
                    packet_info = list()
                    date,source_ip, dst_ip , src_port , dst_port, protocol = "","","","","",""
                    
                packet_info = list() 
                print "Doing No.",i,"packet!!"
		name=str(i)
                #OutputFile(s,name,i)
                flag = True
                i = i + 1
            if "Destination: " in s:
                if len(s.split()[1].split(".")) ==4:
                    dst_ip = "dst_ip-"+s.split()[1]
                    packet_info.append(dst_ip)
            if "Source: " in s:
                if len(s.split()[1].split(".")) == 4:
                    source_ip = "src_ip-"+s.split()[1]
                    packet_info.append(source_ip)
            if "Protocols in frame" in s:
                pt = s.split()
                protocol = "proto-"+pt[3][:-1]
                packet_info.append(protocol)
            if "Arrival Time:" in s:
                o = s.split()
                date = o[2] + o[3][:-1]
            if "Source Port:" in s:
                src_port = "src_port-"+s[17:]
                packet_info.append(src_port)
            if "Destination Port" in s:
                dst_port = "dst_port-"+s[22:]
                packet_info.append(dst_port)

            #OutputFile(s,name,i)
            #if packet_line==2:
            #    print s.split()
            #space_dect = s.split()
            #packet_line = packet_line + 1
            """
            if not s.strip() and "No." in linecache.getline(txt_File,packet_line+1):
                #print s 
                print "*******"
                print "Line space is",packet_line
                #print linecache.getline(txt_File,packet_line+1)
                print "*******"
                packet_line = 0
                print "Now is",num_of_packet_frame
            """
           # print s
            #print "==="

            #packet_line = packet_line + 1
            #if packet_line==100:
            #    break

    #return protocol_info
def OutputFile(Data,name):
    log_file = "output/"+name +".txt"
    #print "Test:"+ log_file
    f = open(log_file, 'a+')
    #log_text = "No."+str(num)+" ,The info is: "+Data
    s = " ".join(str(x) for x in Data)
    f.write(s)
    f.write('\n')
    f.close()
if __name__=="__main__":
    optparser = OptionParser("useage: %prog"+"-f <input dataset File>")
    optparser.add_option('-f', '--inputFile',dest='input',help='filename',default=None)
    (options, args) = optparser.parse_args()
    if options.input is None:
        print sys.usage
        sys.exit()
    else:
        inFile=options.input
    
    filename = ""
    """ 
    f = open(inFile,'rb')
    i = 0
    for line in f:
        s = line.strip('\n')
        print s 
        i = i + 1
        if i==5:
            break
    """
     
    """ filename="Bang_file_all_info_display_all_expand"
    first_input = filename + ".txt"
    GetInfo(first_input)
    for j in range(1,7):
        print "Now Run",j,"File!!"
        second_file = filename + str(j) + ".txt"
        GetInfo(second_file)
        """
    print inFile
    GetInfo(inFile)
    #sorted_result = sorted(result.items(), key=operator.itemgetter(0))
    #print "Final Result:"
    #print sorted_result
