word=list(input().upper())
cnt={x:0 for x in word}
for w in word:
    cnt[w]+=1
cnt_list=[[x,y] for x,y in cnt.items()]
cnt_list.sort(key=lambda x:x[1],reverse=True)
if len(cnt_list)>1:print(cnt_list[0][0] if cnt_list[1][1]!=cnt_list[0][1] else "?")
else:print(cnt_list[0][0])