usr="/home/guangxujin_gmail_com/"
HOME=usr+'py_covid19_mpi_batch/'
blast=HOME+'ncbi-blast-2.10.0+/bin/blastn'
#configs for python and folders
python_dir=usr+"anaconda3/bin/python"
#cell="1" ### sample
#cell="19_NTS_Wuhan"
#cell="18_RNA-Seq_san_Diego"
#cell="4_amplicon_malaysia_nanopore"
cell="9_RNA_Australia_nanopore"
gs_raw_data="gs://bigdata_backup/covid-19_0.8/1_RNA_seq"
fastq_data_dir=gs_raw_data+'/'+cell ### fastq location
fastq_folder=HOME+"SARS-COV2_raw"
cov_hits=fastq_folder+'/'+cell+"_blast/*blast"
#configs for blastn
threads=8
q30_threshold=0.5
hits=1000
perc_identity=97.5
gc_blast_out="gs://bigdata_backup/covid-19_sampled/BLAST_RNA/"+cell+'_blast' ### results
#configs for cluster
cores=8
#config for Rcode
hit_country=fastq_folder+'/'+cell+"_blast_uniq_country"
Rfig_gc="gs://bigdata_backup/covid-19_sampled/Rfig_RNA/"+cell+'_blast'
Rfig_piden=100
