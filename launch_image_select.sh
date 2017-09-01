
for f in `seq 0 99`
do
python launch_hits.py \
      --html_template=image_select.html \
      --hit_properties_file=hit_properties/image_select.json \
      --input_json_file=production/inputs/example_input_train${f}.txt \
      --hit_ids_file=production/hit_ids/hit_ids_train${f}.txt\
      --prod
done
