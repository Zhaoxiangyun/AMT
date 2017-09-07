import json
from pprint import pprint
import pdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type = str, default = '')
parser.add_argument('--output', type = str, default = '')
args = parser.parse_args()

input_file = args.input
output_file = args.output

txt = open(input_file,'r')
rlt = open(output_file, 'w')
lines = txt.readlines()

data0  = lines[0]
data1 = lines[1]
data2 = lines[2]

output0 = json.loads(data0)['output']
output1 = json.loads(data1)['output']
output2 = json.loads(data2)['output']
l = len(output0)

for j in range(l):
        # pdb.set_trace()
        r0 = output0[j]["select_result"]
        r1 = output1[j]["select_result"]
        r2 = output2[j]["select_result"]
        rlt.write(str(r0)+ ' '+str(r1) + ' '+ str(r2)+ '\n' )