for f in `seq 0 49`
do
python test.py  --input example_output${f}.txt --output output${f}.txt
done