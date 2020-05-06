from mpi4py import MPI
import sys
import os
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
comm = MPI.COMM_WORLD

tasks=int(sys.argv[1])
python=sys.argv[2]
data=[item for item in range (0,tasks)]
if rank == 0:
   print ('we will be scattering:',data)
else:
    data = None
   
data = comm.scatter(data, root=0)
#for task_id in data:
os.system(python+' step1.blast.py '+str(data))
