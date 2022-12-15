import time
f= open("numbers.txt","w+")
t0 = time.perf_counter()
for i in range(100000):
    f.write("%d\n" % (i+1))
print(time.perf_counter()-t0)