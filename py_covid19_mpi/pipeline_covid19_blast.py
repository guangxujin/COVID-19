from load import *
import config
import sys
###############################################                                                 
# BLAST of SARS-CoV-2 sequences to BetaCoronavirus                                                 
###############################################                                                                                                                                                            

'''
#@ author                                                                                                                                                                                                 
#Guangxu Jin, Ph.D.                                                                                                                                                                                        
#Wake Forest School of Medicine                                                                                                                                                                 
# Email: guangxujin@gmail.com                                                                                                                                                                              
'''                           
print('###############################################')
print('BLAST of SARS-CoV-2 sequences to BetaCoronavirus')
print('###############################################') 

print('{}|Identifying fastq files from {} ...'.format(gettime(),config.fastq_data_dir))
import config
os.system('chmod +x '+config.blast)
mkdir(config.fastq_folder)
cmd='gsutil -m cp -r '+config.fastq_data_dir+' '+config.fastq_folder+'/'
directory=config.fastq_folder+'/'+config.cell
if not os.path.exists(directory):
    os.system(cmd) 

print('{}|Checking genome database from {} ...'.format(gettime(),config.))
database=config.Betacorona+'.n*'
if not os.path.exists(directory):
    cmd='tar -xvf '+config.Betacorona+'.tar.gz'

tasks=len(glob.glob(config.fastq_folder+'/'+config.cell+'/*fastq')) #folder for sams
codes=config.HOME+"py_covid"
cp_config(codes)

print
print('{}|1::Blast sequences to Betacoronavirus for the samples in {}...'.format(gettime(),config.cell))
print

import config
out=config.fastq_folder+'/'+config.cell+"_blast/"
delete_mk_output(out)
os.system('bash step1.sh '+codes+' '+config.python_dir+' '+str(tasks)+' '+config.usr+' '+config.cell+' '+str(config.cores)) ### change column number for sam file                 
print_bar_sbatch(tasks,out)

print
print('{}|3::Draw boxplot for samples in {}...'.format(gettime(
),config.cell))
print
codes=config.HOME+"py_ggplot2/py"
cp_config(codes)
hit_acc=100
os.system('bash step3.sh '+codes+' '+config.python_dir+' '+str(hit_acc))
hit_acc=97.5
os.system('bash step3.sh '+codes+' '+config.python_dir+' '+str(hit_acc))

cmd='gsutil -m cp -r '+config.hit_country+' '+config.Rfig_gc+'/'
os.system(cmd)
