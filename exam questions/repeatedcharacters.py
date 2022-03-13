Sample_string='thequickbrownfoxjumpsoverthelazydog'
count=0
char=''
for i in Sample_string:
    for j in Sample_string:
        if i[0]==j[1:]:
           count+=1
           char=''+i
           l=int(j)   
    
print(count)           
        
