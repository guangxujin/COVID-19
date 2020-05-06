# -*- coding: utf-8 -*-                                                         
import random,os
import config
import subprocess
from random import shuffle
#import numpy as np
# import pandas as pd                                                           
import time
import ReadFile
import WriteFileAll
import time,os,sys
import string
import glob
import math
import numpy as np

def q30_m(f,sample):
    cov_data=ReadFile.main(f,0,'\t')
#    cov_data=random.choices(cov_data, k=1000)
    include=0
    L=[]
    fastq=""
    LQ=[]
    for k in range (len(cov_data)):

        if k%4 == 1:
            fastq=cov_data[k][0]
        if k%4 == 3:
            q=list(cov_data[k][0])
            q30_ratio=qscore(q)
            LQ.append(q30_ratio)
        if k > 100000:
                break
    q30_mean=np.quantile(np.array(LQ),0.90)
    return q30_mean

def fa(f,sample,q30_m):
    cov_data=ReadFile.main(f,0,'\t')

    include=0
    L=[]
    fastq=""
    num=0
    for k in range (len(cov_data)):
        if k%4 == 1:
            fastq=cov_data[k][0]
            #print (k)                                                                                                                                                                                      
            #print (k//4 == 1)                                                                                                                                                                              
            #print(fastq)                                                                                                                                                                                   
        if k%4 == 3:
            q=list(cov_data[k][0])
            q30_ratio=qscore(q)
    
            if q30_ratio>=float(q30_m) and q30_ratio>=config.q30_threshold:

                    L.append(['>'+sample+'.'+str(k)])
                    L.append([fastq])
                    #else:
                     #       break
                    num=num+1
    return L

def qscore(L):
        L1=[ord(tmp)-33 for tmp in list(L)]
        num =0
        for tmp in L1:
                if tmp >= 30:
                        num += 1
        ratio=float(num)/float(len(L1))

        return ratio

def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def rmdir(directory): # DO NOT use it and make sure directory is not * or /                                                                                                                                 
    if os.path.exists(directory):
        os.system('rm -r '+directory)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
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
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    stdout.flush()
    stdout.write ('%s |%s| %s%% %s\r' % (prefix, bar, percent, suffix))
    #sys.stdout.write("\r%d%%" % i)                                                                                                                                                                         

    # Print New Line on Complete                                                                                                                                                                            
    if iteration == total:
        print('\r')
