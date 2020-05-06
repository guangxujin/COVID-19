# COVID-19
Resource for SARS-CoV-2 datasets and related codes
## Blast single fastq
cd py_covid19_mpi/py_covid

update config.py

python step1.blast.py

## Blast multiple fastqs (Google Cloud Slurm version)

cd py_covid19_mpi

update config.py

python pipeline_covid19_blast.py
