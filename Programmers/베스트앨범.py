def solution(genres, plays):
    d = {}
    answer=[]
    
    #사전 자료형에 저장
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i],0) + plays[i]
    
    #사전 자료형을 value 기준 내림차순으로 정렬
    d= sorted(d.items(),key= lambda x:x[1],reverse=True)
    
    #d(2차원 리스트)에 있는 모든 key,value에 대하여
    for key,value in d:
        lst=[]
        
        #genres[i]와 key값이 같을때, plays[i]와 i를 lst에 넣는다.
        for i in range(len(genres)): 
            if genres[i] == key:
                lst.append([plays[i],i])
        
        #lst를 plays기준 내림차순으로 정렬한다.
        lst = sorted(lst,key=lambda x:x[0],reverse=True)
        
        #i값을 answer 배열에 넣어준다. (장르에 속한 곡이 하나일 수 있으니, 두번째 곡은 조건문으로 검사한 후 넣는다.)
        answer.append(lst[0][1])
        if len(lst)>1:
            answer.append(lst[1][1])
            
    return answer