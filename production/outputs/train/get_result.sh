for f in `seq 0 99`
do
python test.py  --input example_output_train${f}.txt --output output${f}.txt
done
