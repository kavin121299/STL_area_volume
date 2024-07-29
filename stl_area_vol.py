#Please change the file path for your stl file...
file = open("C:\\Users\\kavinp\\Downloads\\2020_corner_bracket.stl","r")
lines = file.readlines()
tlst = []
for i in lines:
    if "vertex" in i:
        dd = i.split()
        tlst.append(dd[1:4])
normal = []
for i in lines:
    if "normal" in i:
        ss = i.split()
        normal.append(ss[2:5])       
AAA = 0.0
index = 0
count = 0
Volume = 0.0
a = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
cent = [0.0,0.0,0.0]
N = [0.0,0.0,0.0]
index1 = 0
for i in tlst:
    index = 0
    for j in i:
        a[count][index] = float(j)
        index += 1
    count += 1
    if count == 3:
        count = 0
        aa = ((a[1][0] - a[0][0])**2 + (a[1][1] - a[0][1])**2 + (a[1][2] - a[0][2])**2)**(0.5)
        bb = ((a[2][0] - a[1][0])**2 + (a[2][1] - a[1][1])**2 + (a[2][2] - a[1][2])**2)**(0.5)
        cc = ((a[2][0] - a[0][0])**2 + (a[2][1] - a[0][1])**2 + (a[2][2] - a[0][2])**2)**(0.5)
        ss = (0.5)*(aa+bb+cc)
        AA = (ss*(ss-aa)*(ss-bb)*(ss-cc))**(0.5)
        AAA += AA
        N[0] = float(normal[index1][0])
        N[1] = float(normal[index1][1])
        N[2] = float(normal[index1][2])
        dS = [kk*AA for kk in N]
        index1 += 1
        cent[0] = (a[0][0] + a[1][0] + a[2][0])/3
        cent[1] = (a[0][1] + a[1][1] + a[2][1])/3
        cent[2] = (a[0][2] + a[1][2] + a[2][2])/3
        dot = sum([x*y for x,y in zip(dS,cent)])
        Volume += (1/3)* dot
print("Area : ",AAA)
print("Volume : ",Volume)