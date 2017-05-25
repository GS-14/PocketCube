f1 = open('Pocket Cube - God\'s Lookup Table.txt','r')
f2 = open('Pocket Cube - God\'s Lookup Table (with Colors).txt','w')

#f1 = open('Pocket Cube - 3 or less steps.txt','r')
#f2 = open('Pocket Cube - 3 or less steps (with Colors).txt','w')

ColorMap = {'0':'r', '1':'r','2':'r','3':'r', '4':'w', '5':'w', '6':'w', '7':'w', '8':'b', '9':'b', '10':'b', '11':'b', '12':'y', '13':'y', '14':'y', '15':'y', '16':'g', '17':'g', '18':'g', '19':'g', '20':'o',  '21':'o', '22':'o', '23':'o'}



def Color(line):
    line = line.split("\t")
    line[0] = line[0].split(",")
    for i in range(0,24):
        line[0][i] = ColorMap[line[0][i]]
    line[0] = ",".join(line[0])
    return "\t".join(line)

for line in f1.readlines():
    f2.write(Color(line))

f1.close()
f2.close()