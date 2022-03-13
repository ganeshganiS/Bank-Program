week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
sum=0
count=0
for i in week_temps_f.split(','):
    sum+=float(i)
    count+=1
avg_temp=sum/count
print("{:.2f}".format(avg_temp))
