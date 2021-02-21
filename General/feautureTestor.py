import pandas as pd
import string

data = pd.read_csv(r"C:\Users\cbyle\Desktop\Files\Pishing-Detection\model_1.1\urls.csv", engine= 'python') 
f1 = data['URL']
f2 = data['Label']

bad = 0
good = 0

# Change these variables
numList = ['bk', 'fq', 'jc', 'jt', 'mj', 'qh', 'qx', 'vj', 'wz', 'zh',
            'bq', 'fv', 'jd', 'jv', 'mq', 'qj', 'qy', 'vk', 'xb', 'zj',
            'bx', 'fx', 'jf', 'jw', 'mx', 'qk', 'qz', 'vm', 'xg', 'zn',
            'cb', 'fz', 'jg', 'jx', 'mz', 'ql', 'sx', 'vn', 'xj', 'zq',
            'cf', 'gq', 'jh', 'jy', 'pq', 'qm', 'sz', 'vp', 'xk', 'zr',
            'cg', 'gv', 'jk', 'jz', 'pv', 'qn', 'tq', 'vq', 'xv', 'zs',
            'cj', 'gx', 'jl', 'kq', 'px', 'qo', 'tx', 'vt', 'xz', 'zx',
            'cp', 'hk', 'jm', 'kv', 'qb', 'qp', 'vb', 'vw', 'yq',
            'cv', 'hv', 'jn', 'kx', 'qc', 'qr', 'vc', 'vx', 'yv',
            'cw', 'hx', 'jp', 'kz', 'qd', 'qs', 'vd', 'vz', 'yz',
            'cx', 'hz', 'jq', 'lq', 'qe', 'qt', 'vf', 'wq', 'zb',
            'dx', 'iy', 'jr', 'lx', 'qf', 'qv', 'vg', 'wv', 'zc',
            'fk', 'jb', 'js', 'mg', 'qg', 'qw', 'vh', 'wx', 'zg']
minimum = 2

print("The minimum is: ", minimum)

for i in range(0,549346,1):
    if i %100000 == 0:
        print('At ', i)
    elif i == 549345:
        print("Done... Preparing results")
    
    count = 0
    for x in range (0,len(numList),1):
        count += f1[i].count(numList[x])

    if count >= minimum:
        if f2[i] == 'good':
            good += 1
        else:
            bad += 1

# print to console
print('Good = ', good, '\nBad = ', bad, '\nTotal = ', bad + good, '\nPercent Indication = ', good*100/(bad+good))

#print to file

#add to file
line = str(numList) + "\tMinimum: " + str(minimum) + "\tTotal Links: " + str(good+bad) + "\tGood Samples: " + str(good) + "\tBad Samples: " + str(bad) + "\tPercent Indication: " + str(int(good*10000/(good+bad))/100) + "\n"

fi = open("General\StringResults.txt", "a")
fi.write(line)
fi.close()