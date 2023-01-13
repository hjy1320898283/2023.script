#!/usr/bin/python
#####以depth为优先，如果要以width为优先可以更换list_width和list_depth的位置

lst1 = [248,16,22.16]
lst2 = [152,16,20.29]

list_all = [lst1.lst2]
list_depth = [lst1[1],lst2[1]]

def main (wideth,depth):
    output = []
    list_width = []
    print ('the size you choose is width : %d , depth is %d ' % (width,depth))   #1.tell you the size you apply
    depth_i = min(list_depth, key=lambda x:abs(x-depth))                         #2.select the most similar value to width
    for item in list_all:                                                        #3.Traversal database
        if item [1] == depth_i:                                                  #4.search the data in step2
            list_width.append(item[0])                                           #5.make the satisfied depth a new list
            output.append(item)                                                  #6.make a new list that satisfy width
    wideth_i = min(list_width, key=lambda x:abs(x-wideth))                       #7.select the most similar value to depth
    for need in output:                                                          #8.Traversal database
        if need[0] ==wideth_i:                                                   #9.mathc data
            print ('the simliar mem is width is : %d , depth is : %d , persentage = %.2f %%' % (need[0],need[1],need[2]))