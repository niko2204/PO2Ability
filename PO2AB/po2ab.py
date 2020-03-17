#학습성과 - 핵심 역량 매핑 함수

#PO2AB = {'PO1':'w4','PO2':'w2,w4','PO3':'w1','PO4':'s4','PO5':'s1', 'PO6':'s5','PO7':'w3,s6','PO8':'s2,w3,w8','PO9':'w7,s9','PO10':'w3,w4'}
PO2AB = {'PO1':['w4'],'PO2':['w2','w4'],'PO3':['w1'],'PO4':['s4'],'PO5':['s1'], 'PO6':['s5'],'PO7':['w3','s6'],'PO8':['s2','w3','w8'],'PO9':['w7','s9'],'PO10':['w3','w4']}
result = []
s = input('학습성과를 입력하세요: (ex.PO2 PO3 PO5)').split()
for i in s:
    result.append(PO2AB[i])
    #print(PO2AB[i])
    #result.extend(PO2AB[i])
#print(result)
result.sort()

print(result)