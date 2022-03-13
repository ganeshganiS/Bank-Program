original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_words_list=[]
for i in original_str.split():
    l=len(i)
    num_words_list.append(l)
print(num_words_list)    
