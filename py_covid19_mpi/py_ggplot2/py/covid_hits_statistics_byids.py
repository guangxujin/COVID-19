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
data=ReadFile.main(cov_hit,0,'\t')
print(data[1])


ref={}
ref_f="../sequences_columns.txt.country_city.txt"
ref_data=ReadFile.main(ref_f,0,'\t')
for line in ref_data:
	name=line[2]
	ref[name]=line[0]
L=[]
Lsample=[]
keys=ref.keys()
for line in data:
	#print (line[3])
        hit_id=line[2]
	country_name=line[3]
	hit_acc=float(line[4])
	if country_name.find('complete')>-1 and hit_acc==config.hit_acc:
		if hit_id in keys:
			country=ref[hit_id]
                        L.append([country])
print ("input hits, {},found hits, {}".format(len(data),len(L)))
fw=config.uniq_folder
mkdir(fw)
out=fw+'/'+cov_hit.split('/')[-1]+'.country.txt'
#out=fw+'/'+config.cell+'.country.txt'
WriteFileAll.main(out,L,'\t')
cmd="awk -F'\t' '{print $1}' "+out+"|sort |uniq -c|sort -n -k1|tail >"+out+'.uniq'
os.system(cmd)
#maf_id=WAKE_id(maf)
#print maf_id[0:3]
