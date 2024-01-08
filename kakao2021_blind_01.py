def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    for c in new_id:
        if c.isalpha() or c.isdigit():
            answer+=c
        elif c in ['-','_','.']:
            answer+=c
    while ".." in answer:
        answer=answer.replace("..",".")
    if answer and answer[0]==".": answer=answer[1:]
    if answer and answer[-1]==".": answer=answer[:-1]
    if not answer:
        answer="a"
    if len(answer)>=16:
        answer=answer[:15]
    if answer[-1]==".": answer=answer[:-1]
    if len(answer)<=2:
        answer=answer+answer[-1]*(3-len(answer))
        
    return answer

print(solution("=.="))
