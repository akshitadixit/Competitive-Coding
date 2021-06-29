from sys import maxsize

def subarr(arr):
  max_so_far = -maxsize-1
  max_till_here = 0
  start = 0
  end = 0
  k = 0

  for i, x in enumerate(arr):
      
      max_till_here += x

      if max_till_here>max_so_far:
          max_so_far = max_till_here
          start = k
          end = i

      if max_till_here<0:
          max_till_here = 0
          k = i + 1

  return arr[start:end+1]

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(subarr(a))