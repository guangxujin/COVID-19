folder=$1
python=$2
cd $1
tasks=$3
usr=$4
job_name=$5
cores=$6
$python update_slurm.py $tasks $job_name $cores
sbatch mpi_4py_updated.sh $tasks $usr


