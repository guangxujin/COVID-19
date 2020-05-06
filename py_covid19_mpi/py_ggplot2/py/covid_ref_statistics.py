from load import *
'''
@author 
Guangxu Jin, wake forest school of medicine.
Processing covid reference
'''

####input and output

cov_ref="../sequences_columns.txt"
data=ReadFile.main(cov_ref,1,'\t')
print(data[1])

L=[]
Lsample=[]
for line in data:
	country=line[1].split(':')[0]
	country_split=country.split('"')
	if len(country_split) > 1:
		country=country_split[1]
	city=""
	if len(line[1].split(':'))>1:
		city=line[1].split(':')[1]	
	
	L.append([country,city]+line)
print ("input samples, {},found samples, {}".format(len(data),len(L)))
fw='./'
out=fw+cov_ref+'.country_city.txt'
WriteFileAll.main(out,L,'\t')
#maf_id=WAKE_id(maf)
#print maf_id[0:3]