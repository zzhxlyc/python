list = ['DS', 'OS']

len(list)

list.append('ADS')

list.insert(1, 'CS')

list.remove('ADS')
list.pop()
list.pop(1)

#extend
list += ['ADS']
list.extend(['Math'])   #no return value

list.index('ADS')

list.count('DS')

#sort
list.sort(lambda x,y : cmp(x, y))
list.reverse()

#tuple only have index() and count()

for index, value in enumerate(list): pass  

#range(start, end(exclude), step = 1), range(num) = range(0, num, 1)
range(5), #[0, 1, 2, 3, 4]
range(-1 ,-5 ,-1) #[-1, -2, -3, -4]

#range create the complete list in onetime in memory, quick but waste memory
#xrange create one element each time, slow and save memory
#in python 3+, xrange is no longer used

#list jiexi is faster than for loop as 2 times
[x ** 2 for x in range(10)]
[x ** 2 for x in range(10) if x % 2] 

M = N = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

#[1, 16, 49, 4, 25, 64, 9, 36, 81]
[M[row][col] * N[row][col] for col in range(3) for row in range(3)]

#[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]

