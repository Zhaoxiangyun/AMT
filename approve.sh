
for f in `seq 0 99`
do
python approve_hits.py --hit_ids_file=production/hit_ids/hit_ids_train${f}.txt \
       --prod

done
