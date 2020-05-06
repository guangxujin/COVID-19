from load import *
import ReadFile
import WriteFileAll
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
	name=line[-1].split('"')
	name=name[0]
	if len(name)>1:
		name=name[1]
	ref[name]=line[0]
L=[]
Lsample=[]
keys=ref.keys()
for line in data:
	#print (line[3])
	country_name=line[3]
	hit_acc=float(line[4])
	if country_name.find('complete')>-1 and hit_acc==config.hit_acc:
		if country_name in keys:
			country=ref[country_name]

		else:
			if len(country_name.split('/'))>2:
				country=country_name.split('/')[2]
				if country == "2020, complete genome":
						country=country_name.split('/')[1].split('-')[0]
			else:
				if country_name.find('SZ')>-1 \
				or country_name.find('WHU')>-1 \
				or country_name.find('HZ')>-1 \
				or country_name.find('Wuhan')>-1 \
				or country_name.find('HZ')>-1:
					country='CHN'
				else:
					print (country_name)
		L.append([country])
print ("input samples, {},found samples, {}".format(len(data),len(L)))
fw=config.uniq_folder
mkdir(fw)
#out=fw+'/'+cov_hit.split('/')[-1]+'.country.txt'
out=fw+'/'+config.cell+'.country.txt'
WriteFileAll.main(out,L,'\t')
cmd="awk -F'\t' '{print $1}' "+out+"|sort |uniq -c|sort -n -k1|tail >"+out+'.uniq'
os.system(cmd)
#maf_id=WAKE_id(maf)
#print maf_id[0:3]
