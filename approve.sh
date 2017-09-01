
for f in `seq 0 49`
do
python approve_hits.py --hit_ids_file=production/hit_ids/hit_ids${f}.txt \
       --prod

done
