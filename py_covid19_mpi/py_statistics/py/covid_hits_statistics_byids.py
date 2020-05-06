from load import *
import ReadFile
import WriteFileAll
import sys
'''
@author 
Guangxu Jin, wake forest school of medicine.
Processing covid hits
'''

####input and output

#cov_hits=config.cov_hits #"/home/guangxujin/covid-19/SARS-COV2_raw/1_US_WI_blast_1000/*blast"

cov_hit=sys.argv[1]
gc_out=sys.argv[2]
#data=ReadFile.main(cov_hit,0,'\t')
#print(data[1])
fr=open(cov_hit,'r')

ref={}
ref_f="../sequences_columns.txt.country_city.txt"
ref_data=ReadFile.main(ref_f,0,'\t')
for line in ref_data:
	name=line[2]
	ref[name]=line[0]
L=[]
L97=[]
Lsample=[]
keys=ref.keys()
#for line in data:
while 1:
        line=fr.readline()
        if not line: 
                break
        line=line.split('\n')[0].split('\t')
        hit_id=line[2]
        country_name=line[3]
        hit_acc=float(line[4])
        if hit_acc==100:
             if hit_id in keys:
                 country=ref[hit_id]
                 L.append([country])
        if hit_acc>=97.5:
             if hit_id in keys:
                 country=ref[hit_id]
                 L97.append([country])
fr.close()
print ("found hits, {}".format(len(L)))
fw='/tmp/'+cov_hit.split('/')[-1]+'_statistics'
mkdir(fw)
out=fw+'/'+cov_hit.split('/')[-1]+'.country.txt'
#out=fw+'/'+config.cell+'.country.txt'
WriteFileAll.main(out,L,'\t')
cmd="awk -F'\t' '{print $1}' "+out+"|sort |uniq -c|sort -n -k1|tail >"+out+'.uniq'
os.system(cmd)

fw='/tmp/'+cov_hit.split('/')[-1]+'_statistics'
mkdir(fw)
out=fw+'/'+cov_hit.split('/')[-1]+'.975.country.txt'
#out=fw+'/'+config.cell+'.country.txt'                                          
WriteFileAll.main(out,L97,'\t')
cmd="awk -F'\t' '{print $1}' "+out+"|sort |uniq -c|sort -n -k1|tail >"+out+'.uniq'
os.system(cmd)
os.system('mv '+cov_hit+' '+fw+'/')
cmd='gsutil -m cp -r '+fw+' '+gc_out+'/'
print (cmd)
os.system(cmd)
#sleep(300)
os.system('rm -r '+fw) 
#maf_id=WAKE_id(maf)
#print maf_id[0:3]