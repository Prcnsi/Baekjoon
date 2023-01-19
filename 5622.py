dial={'ABC':3,'DEF':4,'GHI':5,'JKL':6,'MNO':7,'PQRS':8,'TUV':9,'WXYZ':10}
key_list=list(dial.keys())
#print('D' in key_list[0])

word=input()
dial_time=0
for i in range(len(word)):
    for j in range(len(key_list)):
        if word[i] in key_list[j]:
            dial_time+=dial[key_list[j]]
print(dial_time)    
