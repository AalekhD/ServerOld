file = open('fft_x_axis.txt','r')
data = file.readlines()
file.close()
line_labels = [i+1 for i in range(len(data))]
line_values = [d.strip() for d in data]
print(line_labels)
print(line_values)