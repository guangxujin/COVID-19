from load import *
import config
def change_field(f,f1,n,n1):
    with open(f, "rt") as fin:
        with open(f1, "wt") as fout:
            for line in fin:
                fout.write(line.replace(n, n1))
tasks=sys.argv[1]
job_name=sys.argv[2]
cores=sys.argv[3]
change_field('mpi_4py.sh','mpi_4py_jbn.sh',"--job-name=mpi4py-test","--job-name="+job_name)
change_field('mpi_4py_jbn.sh','mpi_4py_cores.sh',"-n 100","-n "+tasks)
change_field('mpi_4py_cores.sh','mpi_4py_updated.sh',"--cpus-per-task=4","--cpus-per-task="+cores)
