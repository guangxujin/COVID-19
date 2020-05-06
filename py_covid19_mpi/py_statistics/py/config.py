usr="/home/guangxujin/"
HOME='/home/guangxujin/covid-19/'

#configs for BC uniq and count
python_dir=usr+"anaconda3/bin/python"
cell="1_US_WI" ### sample
#cell="19_NTS_Wuhan"
fastq_data_dir="gs://bigdata_backup/covid-19/raw_data/"+cell ### input for step1-9
fastq_folder=HOME+"SARS-COV2_raw"
cov_hits=fastq_folder+'/'+cell+"_blast/*blast"
uniq_folder=fastq_folder+'/'+cell+"_blast_uniq"
hit_acc=100
