import array as arr

f = arr.array('i',[-1] * 20)

def fib_mem_init():
  f = arr.array('i',[-1] * 20)

#template<typename T>
def fib_mem(n):
  if f[n] == -1:  # if f[n] is default, compute
    if (n == 0) or (n == 1): # base case
      return 1
    else:
      f[n] = fib_mem(n-1) + fib_mem(n-2)
      return f[n]    
  else:
    return f[n]

fib_mem_init()
print(fib_mem(25))
