from py_load import *
import config
from load import *

task_id=int(sys.argv[1])
cov_input=glob.glob(config.fastq_folder+'/'+config.cell+'/*.fastq')
os.system('rm '+'/tmp/*.fa')
for cov_sample in [cov_input[task_id]]:
    sample_name=cov_sample.split('/')[-1].split('.')[0]
    q30_mean=q30_m(cov_sample,sample_name)
    
    blast_input=fa(cov_sample,sample_name,q30_mean)
    out=config.fastq_folder+'/'+config.cell+"_blast/"
    mkdir(out)
    out_blast='/tmp/'+sample_name+'.blast'
    fw='/tmp/'+sample_name+'.fa'
    WriteFileAll.main (fw,blast_input,'\t')
    fw1='/tmp/'+sample_name+'.q30'
    WriteFileAll.main (fw1,[[q30_mean]],'\t')
    print('{}| Fastq data processed ...'.format(gettime()))
    out_blast='/tmp/'+sample_name+'.blast'
    db=config.HOME+"covid-19-assembly/Betacoronavirus"
    os.system('cp -r '+db+' '+'/tmp/')
    dbtmp='/tmp/Betacoronavirus/Betacoronavirus'
    blast=config.blast
    cmd = blast+ \
      ' -db '+dbtmp+ \
      ' -query '+fw+ \
      ' -out '+out_blast+ \
      ' -perc_identity '+str(config.perc_identity)+ \
      ' -num_threads '+ str(config.threads)+ \
      ' -max_target_seqs ' +str(config.hits)+ \
      ' -outfmt "6 qseqid sseqid sallacc stitle pident ppos gaps gapopen mismatch length qstart qend sstart send evalue bitscore score"'
    print('{}| Blast starts ...'.format(gettime()))
    print('{}| Blast cmd:: {}'.format(gettime(),cmd))
    os.system(cmd)
#    os.system('rm '+fw)
    #sleep(300)
#    os.system('rm '+out_blast)
    fw=out+'/'+sample_name+'.final'
    WriteFileAll.main (fw,[['complete']],'\t')
    print('{}| Blast is completed ...'.format(gettime()))    

    print('{}| statistics on Blast output ...'.format(gettime()))
    os.system('bash step2.sh '+out_blast+' '+config.gc_blast_out+' '+config.HOME+' '+config.python_dir)
'''
ppos      Percentage of positive-scoring matches                                                                                                                                                            
frames    Query and subject frames separated by a '/'                                                                                                                                                       
qframe    Query frame                                                                                                                                                                                       
sframe    Subject frame                                                                                                                                                                                     
btop      Blast traceback operations (BTOP)                                                                                                                                                                 
staxids   Subject Taxonomy ID(s), separated by a ';'                                                                                                                                                        
sscinames Subject Scientific Name(s), separated by a ';'                                                                                                                                                    
scomnames Subject Common Name(s), separated by a ';'                                                                                                                                                        
sblastnames Subject Blast Name(s), separated by a ';'   (in alphabetical order)                                                                                                                             
sskingdoms  Subject Super Kingdom(s), separated by a ';'     (in alphabetical order)                                                                                                                        
stitle      Subject Title                                                                                                                                                                                   
salltitles  All Subject Title(s), separated by a '<>' 
supported format specifiers are:
qseqid    Query Seq-id
qgi       Query GI
qacc      Query accesion
qaccver   Query accesion.version
qlen      Query sequence length
sseqid    Subject Seq-id
sallseqid All subject Seq-id(s), separated by a ';'
sgi       Subject GI
sallgi    All subject GIs
sacc      Subject accession
saccver   Subject accession.version
sallacc   All subject accessions
slen      Subject sequence length
qstart    Start of alignment in query
qend      End of alignment in query
sstart    Start of alignment in subject
send      End of alignment in subject
qseq      Aligned part of query sequence
sseq      Aligned part of subject sequence
evalue    Expect value
bitscore  Bit score
score     Raw score
length    Alignment length
pident    Percentage of identical matches
nident    Number of identical matches
mismatch  Number of mismatches
positive  Number of positive-scoring matches
gapopen   Number of gap openings
gaps      Total number of gaps
ppos      Percentage of positive-scoring matches
frames    Query and subject frames separated by a '/'
qframe    Query frame
sframe    Subject frame
btop      Blast traceback operations (BTOP)
staxids   Subject Taxonomy ID(s), separated by a ';'
sscinames Subject Scientific Name(s), separated by a ';'
scomnames Subject Common Name(s), separated by a ';'
sblastnames Subject Blast Name(s), separated by a ';'   (in alphabetical order)
sskingdoms  Subject Super Kingdom(s), separated by a ';'     (in alphabetical order)
stitle      Subject Title
salltitles  All Subject Title(s), separated by a '<>'
sstrand   Subject Strand
qcovs     Query Coverage Per Subject
qcovhsp   Query Coverage Per HSP
'''
