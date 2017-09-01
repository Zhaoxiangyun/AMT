
for f in `seq 0 99`
do
python get_results.py \
      --hit_ids_file=production/hit_ids/hit_ids_train${f}.txt \
       --output_file=production/outputs/train/example_output_train${f}.txt \
       --prod \
       > production/outputs/train/example_output_train${f}.txt

done
