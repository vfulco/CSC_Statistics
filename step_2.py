import numpy as np

print(np.__version__)
# if version < 1.11, please run:
#   sudo pip install --upgrade numpy

## decompose the string
# Method 1: fail
#data = np.genfromtxt('csc_2017_1.txt')
#print(data[:,0])

# Method 2
fid = open('csc_2017_1.txt', 'r')
content = fid.readlines()

nline = len(content)
data = np.zeros(nline, 'int')
data2 = np.zeros(nline, 'int')

for i in range(nline):
  value = content[i].split()
  data[i] = value[0]
  
  data2[i] = (data[i]-201700000000) / 10000  
  
fid.close()
np.savetxt('csc_2017_2.txt', data, fmt='%12d')
np.savetxt('csc_2017_3.txt', data2, fmt='%04d')

print(data)
print(data2)

## count
unique, counts = np.unique(data2, return_counts=True)
data3 = np.asarray((unique, counts)).T
np.savetxt('csc_2017_4.txt', data3, fmt='%04d %d')

## sort
#data4 = np.sort(data3)
temp = data3[:,1] * (-1)
index = np.argsort(temp)
data4 = data3[index,:]
#data4 = data3[data3[:,1].argsort()]
np.savetxt('csc_2017_5.txt', data4, fmt='%04d %d')
print(data4)

