home=$3
f=$1
out=$2
python=$4
cd $home"py_statistics/py"
$python covid_hits_statistics_byids.py $f $out
