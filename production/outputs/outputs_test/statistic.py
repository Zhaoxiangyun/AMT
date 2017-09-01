f = open('statiscit.txt', 'w')

ST_A = 0
ST_B = 0
ST_C = 0
f.write('hit_id'+' '+ 'all_different' + ' ' +'2 vs. 1' + ' '+ 'all the same')
for i in range(50):
    st_a = 0
    st_b = 0
    st_c = 0
    txt_name = 'output' + str(i) + '.txt'
    txt = open(txt_name,'r')
    lines = txt.readlines()
    line_num = len(lines)
    for j in range(line_num):
        index = 0
        line = lines[j]
        rlt1 = line[0]
        rlt2 = line[2]
        rlt3 = line[4]

        if rlt1 == rlt2:
            index = index + 1
        if rlt2 == rlt3:
            index = index + 1
        if rlt3 == rlt1:
            index = index + 1
        if index == 0:
            st_a = st_a+ 1
        if index == 1:
            st_b = st_b + 1
        if index == 3:
            st_c = st_c + 1

    ST_A = ST_A + st_a
    ST_B = ST_B + st_b
    ST_C = ST_C + st_c

    st_a = st_a/50.0
    st_b = st_b/50.0
    st_c = st_c/50.0
    f.write('hit_id'+str(i)+' '+str(st_a) + ' ' +str(st_b) + ' '+ str(st_c) + '\n')

ST_A = ST_A/2500.0
ST_B = ST_B/2500.0
ST_C = ST_C/2500.0
f.write('average' + ' ' + str(ST_A) + ' ' + str(ST_B) + ' ' + str(ST_C) + '\n')

f.close()




