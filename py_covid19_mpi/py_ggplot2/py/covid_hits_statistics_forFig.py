from load import *
import ReadFile
import WriteFileAll
import sys
import numpy as np
'''
@author 
Guangxu Jin, wake forest school of medicine.
Processing high-confidence hits and analyzing the hit countries
'''
def remove_blank(line):
    while("" in line) : 
        line.remove("")
    name=""
    if len(line) == 2:
        name=line[1]
    if len(line) > 2:
        name='-'.join(line[1:len(line)])
    return name,line[0]   
config.Rfig_piden=sys.argv[1]
ref={}
ref_f="../covid_ref.count.txt"
ref_data=ReadFile.main(ref_f,0,' ')
#print (ref_data[0:2])
for line in ref_data:
    #print (line)
    name,n=remove_blank(line)
    #print (name,n)
    ref[name]=int(n)
L=[]
Lcountry=[]
keys=ref.keys()
uniq_folder='/tmp/'+config.cell
mkdir(uniq_folder)
if float(config.Rfig_piden) == 100:
    cmd='gsutil -m cp -r '+config.gc_blast_out+'/*/*blast.country*'+' '+uniq_folder+'/'
    print (cmd)
    os.system(cmd)
if float(config.Rfig_piden) == 97.5:
    cmd='gsutil -m cp -r '+config.gc_blast_out+'/*/*blast.975.country*'+' '+uniq_folder+'/'
    os.system(cmd)

for f in glob.glob(uniq_folder+'/*.uniq'):
        
    data=ReadFile.main(f,0,' ')
    Ltmp=[]
    for line in data:
        name,n=remove_blank(line)
        n_ref=ref[name]
        ratio=float(0)
        if name in keys:
            ratio=float(n)/float(n_ref)
        Ltmp.append([name,n,n_ref,ratio])
    if len(Ltmp) > 0:
        total=0
        for line in Ltmp:
            total=float(total)+float(line[3])
        for line in Ltmp:
            new_line=line+[float(line[3])/float(total)]
            L.append(new_line)
            if line[0] not in Lcountry:
                Lcountry.append(line[0])
print ("input samples, {},found countries, {}".format(len(glob.glob(uniq_folder+'/*.uniq')),len(Lcountry)))
print('rm -r '+uniq_folder)
os.system('rm -r '+uniq_folder)
#print maf_id[0:3]
out=config.hit_country
mkdir(out)
fw=out+'/'+config.cell+'_'+str(config.Rfig_piden)+'.country.statistics'
WriteFileAll.main(fw,L,'\t')
L1=[]
for country in Lcountry:
    Ltmp=[]
    for line in L:
        if country == line[0]:
            Ltmp.append(line[4])
    m=np.mean(Ltmp)
    L1.append([country,m])
fw1=out+'/'+config.cell+'_'+str(config.Rfig_piden)+'.country.mean.statistics'
WriteFileAll.main(fw1,L1,'\t')

cmd='Rscript '+config.HOME+'/py_ggplot2/Rcode/draw.boxplot.R '+config.cell+'_'+str(config.Rfig_piden)+' '+fw+' '+fw1+' '+config.hit_country
os.system(cmd)
