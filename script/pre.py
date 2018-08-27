#!/usr/bin/env python
import sys
import string
import re
import os
from snakebite.minicluster import MiniCluster
from snakebite.client import Client
from optparse import OptionParser
def AnalyseInputFile(inputFile,pro_symbol):
    Convert_list = dict()
    j = 1
    with open(inputFile,'r') as f:
        for line in f.readlines():
            s = line.strip('\n')
            cp_l = ""
            symbol_index = []
            for symbol in pro_symbol:
                for i in range(0,len(s)):
                    if s[i] == symbol:
                        symbol_index.append(i)
            s_tmp = ""
            s_tmp = s[0:symbol_index[0]]
            if s_tmp not in Convert_list:
                Convert_list[s_tmp] = j
                j = j + 1
                cp_l = str(Convert_list[s_tmp])
            else:
                cp_l = str(Convert_list[s_tmp])
            for i in range(1,len(symbol_index)):
                s_tmp = ""
                s_tmp = s[symbol_index[i-1]+1:symbol_index[i]]
                if s_tmp not in Convert_list:
                    Convert_list[s_tmp] = j
                    j = j + 1
                    cp_l = cp_l + " " + str(Convert_list[s_tmp])
                else:
                    cp_l = cp_l + " " + str(Convert_list[s_tmp])
            s_tmp = ""
            s_tmp = s[symbol_index[i]+1:len(s)]
            if s_tmp not in Convert_list:
                Convert_list[s_tmp] = j
                j = j + 1
                cp_l = cp_l + " " + str(Convert_list[s_tmp])
            else:
                cp_l = cp_l + " " + str(Convert_list[s_tmp])
            OutputFile(cp_l)
        #    print cp_l
    return Convert_list
def OutputFile(Data):
    f = open(filename, 'a+')
    f.write(Data)
    f.write('\n')
    f.close()
def HDFS_Upload(uploadfile):
    if uploadfile:
        connect = MiniCluster(None, start_cluster=False)  
        result = connect.ls("/")
        cluster = MiniCluster("/")
        if result:
            #raise Exception("An active Hadoop cluster is found! Not running tests!")
            if cluster.exists(uploadfile):
                hadoop_home = os.getenv('HADOOP_HOME')
                if hadoop_home is None:
                    print "Can't find hadoop path!!!"
                    cluster.terminate()
                    sys.exit()
                upload_command =  hadoop_home + "/bin/hadoop" + " dfs -put " + filename + " " + uploadfile
                #print upload_command
                os.system(upload_command)
            else:
                cluster.terminate()
                print "No path in HDFS"
        else:
            print "Hadoop is not running"
        cluster.terminate()
    else:
        sys.exit()
if __name__ =="__main__":
    get_Table = dict()
    global filename
    optparser = OptionParser("useage: %prog"+"-f <input dataset File>"+"-o <output covert dataset path>"+"-D <output convert dataset to HDFS>")
    optparser.add_option('-f', '--inputFile',dest='input',help='filename',default=None)
    optparser.add_option('-o','--output',dest='output',help='Output filename',default='Output.txt')
    optparser.add_option('-D','--outputHDFS',dest='HDFSOutput',help='Output filename',default=None)
    optparser.add_option('-s','--getfileSymbol',dest='symbol',help="Enter your file's symbol",default=' ')
    (options, args) = optparser.parse_args()
    if options.input is None:
        print sys.usage
        sys.exit()
    elif options.input is not None:
        inFile = options.input
    else:
        print options.usage
        sys.exit('Bye bye see you baby <3')
    filename = options.output
    dictfile = 'Table_' + filename
    if os.path.exists(filename) or os.path.exists(dictfile):
        print "Here already have file"
        sys.exit()
    print "Now do pre process from file.........."
    get_symbol = options.symbol
    get_Table = AnalyseInputFile(inFile,get_symbol)
    d = open(dictfile,'a+')
    print "Your dataset list table is:"
    for key, value in sorted(get_Table.iteritems(), key=lambda (k,v): (v,k)):
        #print "%s: %s" % (key, value)
        d.write(key + " " + str(value) + '\n')
    d.close()
    print "Convert Successfully!!!"
    HDFS_Upload(options.HDFSOutput)
