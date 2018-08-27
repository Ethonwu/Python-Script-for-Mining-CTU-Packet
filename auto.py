#!/usr/bin/env python
import os
import sys
def getFileSize(path):
    command = "ls " + str(path) + " | grep .pcap"
    pcap_name = os.popen(command).read().split('\n')[0:-1]
    os.chdir(path)
    print pcap_name
    os.system('mkdir output')
    tshark_output = []
    for name in pcap_name:
        output_name = "tsharkOutput_" + name[0:-5] + ".txt"
        command = "tshark -r " + name + " -Vx > output/" + output_name
        output_file_path = "output/" + output_name
        tshark_output.append(output_file_path)
        os.system(command)
    os.chdir("output")
    return tshark_output
def getAllDir(pwdpath):
    command = "ls " + str(pwdpath[0]) + " |grep CTU"
    pacp_path = os.popen(command).read().split('\n')[0:-1]
    return pacp_path
def runSplit(tshark_out_list):
    split_output_name = []
    for name in tshark_out_list:
        print "name is:"+name[7:]
        packet_num_file = "packet_num_" + name[7:]
        command = "cat " + name[7:] + ' | grep "bytes on wire" | wc -l > ../' + packet_num_file
        os.system(command)
        command = "python2.7 ~/packet/script/split.py -f " + name[7:]
        os.system(command)
        path = "output_" + name[7:]
        print "Path is:"+path
        split_output_name.append(path)
    return split_output_name
def Mining(file_path):
    for name in file_path:
        os.chdir(name)
        command = "sh ~/packet/script/Mining.sh"
        os.system(command)
        os.chdir("../")
        command = "mv " + name + " ../"
        os.system(command)
if __name__=="__main__":
    work_path = os.popen('pwd').read().split('\n')[0:-1]
    pacp_path = getAllDir(work_path)
    tshark_output = []
    split_outputPath = []
    for paths in pacp_path:
        tshark_output = getFileSize(paths)
        split_outputPath = runSplit(tshark_output)
        Mining(split_outputPath)
        os.chdir(work_path[0])
        command = "rm -r " + paths + "/output/"
        os.system(command)

