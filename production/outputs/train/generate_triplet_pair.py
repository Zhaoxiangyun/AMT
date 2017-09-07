import cv2
import os
import pdb

list_file = open('smile_pair_train.txt', 'r')
list_lines = list_file.readlines()
dir = 'images'
data_path ='/mnt/ilcompf6d1/user/haoxli/WS0/datasets/CelebA/crops/attrib/'
out = open('fine_grained_train.txt', 'w')

for i in range(100):
    f = open('output{}.txt'.format(i), 'r')
    lines = f.readlines()
    line_num = len(lines)
    for j in range(line_num):

        index = 0
        start_index = (i*50 + j)*3
        line = lines[j]
        rlt1 = line[0]
        rlt2 = line[2]
        rlt3 = line[4]
        if rlt1 == rlt2:
            index = index + 1
            pos_index = rlt1

        if rlt2 == rlt3:
            index = index + 1
            pos_index = rlt2

        if rlt3 == rlt1:
            index = index + 1
            pos_index = rlt3
        pos_index = int(pos_index)
        if index ==0:
            continue
        else:
            if index > 2:
                anchor_name = list_lines[start_index][0:10]
                pos_name = list_lines[start_index + pos_index][0:10]
                if pos_index == 1:
                    neg_index = 2
                else:
                    neg_index = 1
                neg_name = list_lines[start_index + neg_index][0:10]
                anchor_image = cv2.imread(os.path.join(data_path,anchor_name))
                pos_image = cv2.imread(os.path.join(data_path,pos_name))
                neg_image = cv2.imread(os.path.join(data_path,neg_name))

                out.write(anchor_name + '\n')
                out.write(pos_name + '\n')
                out.write(neg_name + '\n')


                cv2.imwrite(os.path.join(dir, str(i) + '_' + str(j) + 'anchor.jpg'), anchor_image)
                cv2.imwrite(os.path.join(dir, str(i) + '_' + str(j) + 'pos.jpg'), pos_image)
                cv2.imwrite(os.path.join(dir, str(i) + '_' + str(j) + 'neg.jpg'), neg_image)

            # else:
            #     anchor_name = list_lines[start_index + 1][0:10]
            #     pos_name = list_lines[start_index + 2][0:10]
            #     neg_name = list_lines[start_index][0:10]
            #
            #     anchor_image = cv2.imread(os.path.join(data_path, anchor_name))
            #     pos_image = cv2.imread(os.path.join(data_path, pos_name))
            #     neg_image = cv2.imread(os.path.join(data_path, neg_name))
            #
            #     cv2.imwrite(os.path.join(dir, str(i) + '_' + str(j) + 'anchor.jpg'), anchor_image)
            #     cv2.imwrite(os.path.join(dir, str(i) + '_' + str(j) + 'pos.jpg'), pos_image)
            #     cv2.imwrite(os.path.join(dir, str(i) + '_' + str(j) + 'neg.jpg'), neg_image)

