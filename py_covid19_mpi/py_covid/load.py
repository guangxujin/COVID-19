# -*- coding: utf-8 -*- 
import time,os,sys
import glob
from datetime import datetime
import subprocess
import config
def gettime():
                now = datetime.now()
                date_time = now.strftime("%m/%d/%Y-%H:%M:%S")
                return date_time
def cp_config(folder):
                os.system('cp config.py '+folder+'/')

def get_active_jobs():
                cmd="squeue|awk -F' ' '{print $5}'|grep R| wc -l"
                out=subprocess.check_output(cmd,shell=True)
                n=out.decode("utf-8").split('\n')[0]
                #print('{}|Running jobs # is {}...'.format(gettime(),n))
                return n

def update_config(cell1,cell2):
                str1='="'+cell1+'"'
                str2='="'+cell2+'"'
                os.system('cp -f config.py.bk config.py')
                cmd="sed -i 's/"+str1+'/'+str2+"/g'"+" config.py"
                os.system(cmd)
                print (cmd)
def check_output(out_dir):
                n=glob.glob(out_dir+'/*/*')
                n=len(n)
                if out_dir.find('gs')>-1:
                                n=get_folder_num(out_dir)
                return n
def check_output_files(out_dir):
                n=glob.glob(out_dir+'/*')
                if out_dir.find('feature')>-1:
                                n=glob.glob(out_dir+'/*.counts.txt')
                if out_dir.find('count')>-1:
                                n=glob.glob(out_dir+'/*.genes.statistics')
                n=len(n)
                if out_dir.find('gs')>-1:
                                n=get_folder_num(out_dir)
                return n

def get_input_num(input_dir):
                cmd='gsutil ls '+input_dir+'*/sam*| wc -l'
                out=subprocess.check_output(cmd,shell=True)
                n=out.decode("utf-8").split('\n')[0]
                return n
def get_folder_num(input_dir):
                cmd='gsutil ls '+input_dir+'*| wc -l'
                out=subprocess.check_output(cmd,shell=True)
                n=out.decode("utf-8").split('\n')[0]
                return n
def print_bar(tasks,out_dir):
                start=time.time()
                while 1:
                                num=check_output(out_dir)
                                
                                time.sleep(10)
                                n=get_active_jobs()
                                #print (num)
                                printProgressBar(int(num), int(tasks), prefix = 'Progress:'+str(num), suffix = 'Complete', length = 60)
                                if float(num)/float(tasks) >0.5 and int(n)==0:
                                                break
                                time_lapse=time.time()-start
                                if time_lapse > 1500 and float(num)/float(tasks) < 1 and int(n)==0 :
                                                print('Something Wrong with the mpi process, please check threads and file system')
                                                break
def print_bar_gc(tasks,out_dir):
                start=time.time()
                while 1:
                                cmd='gsutil ls '+out_dir+'/*| wc -l'
                                out=subprocess.check_output(cmd,shell=True)
                                num=out.decode("utf-8").split('\n')[0]


                                time.sleep(10)
                                n=get_active_jobs()
                                #print (num)                                                                                                                                         
                                printProgressBar(int(num), int(tasks), prefix = 'Progress:'+str(num), suffix = 'Complete', length = 60)
                                if float(num)/float(tasks) >0.5 and int(n)==0:
                                                #break
                                                printProgressBar(int(num), int(tasks), prefix = 'Progress:'+str(num), suffix = 'Complete', length = 60)
                                                break
                                time_lapse=time.time()-start
                                if time_lapse > 1500 and float(num)/float(tasks) < 1 and int(n)==0 :
                                                print('Something Wrong with the mpi process, please check threads and file system')
                                                break




def print_bar_files(tasks,out_dir):
                start=time.time()
                ns=0
                while 1:
                                num=check_output_files(out_dir)

                                time.sleep(10)
                                n=get_active_jobs()
                                if int(n) > 0 and ns ==0:
                                                ns=1
                                                print('{}|job started...'.format(gettime()))  
                                printProgressBar(int(num), int(tasks), prefix = 'Progress:'+str(num), suffix = 'Complete', length = 60)
                                if int(num) >= int(tasks)*0.99 and int(n)==0:
                                                print('{}|job completed...'.format(gettime()))
                                                break
                                time_lapse=time.time()-start
                                if time_lapse > 1500 and float(num)/float(tasks) < 1 and int(n)==0:
                                                print('Something Wrong with the mpi process, please check threads and file system')
def print_bar_files_reduced(tasks,out_dir):
                start=time.time()
                ns=0
                while 1:
                                num=check_output_files(out_dir)

                                time.sleep(10)
                                n=get_active_jobs()
                                if int(n) > 0 and ns ==0:
                                                ns=1
                                                print('{}|job started...'.format(gettime()))
                                printProgressBar(int(num), int(tasks), prefix = 'Progress:'+str(num), suffix = 'Complete', length = 60)
                                if int(num) > 0 and int(n)==0:
                                                print('{}|job completed...'.format(gettime()))
                                                break
                                time_lapse=time.time()-start
                                if time_lapse > 1500 and float(num)/float(tasks) < 1 and int(n)==0:
                                                print('Your data may be in low quality and the targeted cell number cannot be reached.')

def delete_mk_output(out_dir):
                print('{}|check output: {}...'.format(gettime(),out_dir))
                if os.path.exists(out_dir):
                   if out_dir.find(config.sam_out_dir)>-1:
                                   os.system('rm -r '+out_dir)
                                   mkdir(out_dir)
                                   print('{}|Cleaning output from previous run: {}...'.format(gettime(),out_dir))
def print_bar_sbatch(tasks,out_dir):
                start=time.time()
                ns=0
                while 1:
                                num=check_output_files(out_dir)

                                time.sleep(10)
                                n=get_active_jobs()
                                if int(n) > 0 and ns ==0:
                                                ns=1
                                                print('{}|job started...'.format(gettime()))
                                printProgressBar(int(num), int(tasks), prefix = 'Progress:'+str(num), suffix = 'Complete', length = 60)
                                if float(num)/float(tasks)>0.0001 and int(n)==0:
                                                break
                                time_lapse=time.time()-start

from sys import stdout
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """                                                                                                                                                                                 Call in a loop to create terminal progress bar                                                                                                                                      @params:                                                                                                                                                                                iteration   - Required  : current iteration (Int)                                                                                                                            
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

def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
