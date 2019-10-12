import statistics
import numpy
import sys

file = open(sys.argv[1])
file_read = file.read().splitlines()
file.close()

transform_file = [int(index) for index in file_read]

for i in transform_file:
    if i > 32767 or i < -32768:
        print('Числа в файле за пределами: -32 768 до 32 767')

    elif len(transform_file)>1000:
        print('В файле более 1000 строк')
     
print('{:.2f}'.format(numpy.percentile(transform_file,90)),
      '{:.2f}'.format(statistics.median(transform_file)),
      '{:.2f}'.format(max(transform_file)),
      '{:.2f}'.format(min(transform_file)),
      '{:.2f}'.format(sum(transform_file)/len(transform_file)),sep="\n")
