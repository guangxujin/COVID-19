#!/bin/bash
#SBATCH --output=output.log
#SBATCH --job-name=mpi4py-test   # create a name for your job
#SBATCH -n 100               # total number of tasks 
#SBATCH --cpus-per-task=4 
usr=$2
python=$2anaconda3/bin/python
mpirun=$2anaconda3/bin/mpirun
tasks=$1

$mpirun -n $tasks $python py_mpi.py $tasks $python
