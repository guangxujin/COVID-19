f=../sequences_columns.txt.country_city.txt
c=../covid_ref.count.txt
awk -F'\t' '{print $1}' $f|sort|uniq -c| sort -n -k1 > $c