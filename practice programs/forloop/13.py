sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e=0
for i in sentence.split():
    if ('a' in i) or ('e' in i):
        num_a_or_e+=1
print(num_a_or_e)        
