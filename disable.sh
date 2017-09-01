
for f in `seq 0 199`
do
python disable_hits.py --hit_ids_file=production/hit_ids/hit_ids_train${f}.txt \
       --prod

done
