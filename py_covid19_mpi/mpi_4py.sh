#!/bin/bash
#SBATCH --output=output.log
#SBATCH --job-name=mpi4py-test   # create a name for your job
#SBATCH -n 200               # total number of tasks 
#SBATCH --cpus-per-task=4 
python=/home/guangxujin_gmail_com/anaconda3/bin/python
mpirun=/home/guangxujin_gmail_com/anaconda3/bin/mpirun
tasks=$1

Ncore=100
if [ $tasks -lt  $Ncore ]
then
Ncore=$tasks
fi
$mpirun -n $Ncore $python mpi4py.test.py $tasks $python
