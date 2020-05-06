from load import *
import ReadFile
import WriteFileAll
'''
@author 
Guangxu Jin, wake forest school of medicine.
Processing covid hits
'''

####input and output

cov_hits=config.cov_hits #"/home/guangxujin/covid-19/SARS-COV2_raw/1_US_WI_blast_1000/*blast"
Ldata=[]
for cov_hit in glob.glob(cov_hits):
#cov_hit=glob.glob(cov_hits)[0]
        print(cov_hit)
        cmd='python covid_hits_statistics_byids.py'+' '+cov_hit
        os.system(cmd)
