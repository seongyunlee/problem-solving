import requests as rq
import json

url = "https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api/"

class callApi:
    def __init__(self,scene):
        self.key=rq.post(url+'start',headers={'X-Auth-Token':'39772e460b369006a1a7ae176ad89636','Content-Type': 'application/json'},data=json.dumps({'problem':scene})).json()["auth_key"]
        self.problem=scene
    def newRequest(self):
        result =  rq.get(url+'new_requests',headers={"Authorization":self.key,'Content-Type': 'application/json'}).json()
        #print('nR',result)
        return result["reservations_info"]
    def sendReply(self,data):
        rq.put(url+"reply",headers={"Authorization":self.key,'Content-Type': 'application/json'},data=json.dumps({'replies':data})).json()
        #print('sR',data,rq.put(url+"reply",headers={"Authorization":self.key,'Content-Type': 'application/json'},data=json.dumps({'replies':data})).json())
    def simulate(self,data):
        result= rq.put(url+"simulate",headers={"Authorization":self.key,'Content-Type': 'application/json'},data=json.dumps({'room_assign':data})).json()
        #print('sim',result["fail_count"])
        return result['day']
    def getScore(self):
        result =  rq.get(url+'score',headers={"Authorization":self.key,'Content-Type': 'application/json'}).json()
        print('score',result)
class Hotel:
    def __init__(self,scene,api):
        self.today=1
        self.rate=100
        self.api=api
        if scene==1:
            self.n_days=200
            self.n_floors=3
            self.n_rooms=20
            self.target=60
            self.threshold=10
        else:
            self.n_days=1000
            self.n_floors=10
            self.n_rooms=200
            self.target=75
            self.threshold=30
        self.req=[]
        self.rooms=[[[True]*self.n_rooms for _ in range(self.n_floors)] for _ in range(self.n_days)]
        self.room_cnt=[[self.n_rooms]*self.n_floors for _ in range(self.n_days)]
        self.book=[[] for _ in range(self.n_days)]
    def calcEff(self,chk_in,chk_out,floor,number):
        day_eff=[]
        for day in range(chk_in,chk_out):
            n_p=[0]*self.n_rooms
            prev=None
            for room in range(self.n_rooms):
                if prev==None and self.rooms[day][floor][room] and room<number:
                    prev=room
                if prev!=None and (not self.rooms[day][floor][room] or prev<=number<=room):
                    for i in range(prev,room):
                        n_p[i]=room-i
                        prev=None
            day_eff.append(max(n_p))
        return sum(day_eff)/len(day_eff)
    def chkRooms(self,chk_in,chk_out,amount):
        found=[]
        for floor in range(self.n_floors):
            psb=[True]*self.n_rooms
            for date in range(chk_in-1,chk_out-1):
                fr=None
                for to in range(self.n_rooms):
                    if self.rooms[date][floor][to]:
                        if fr==None:fr=to
                    else:
                        for ok in range(fr,min(fr+amount,to))
                        fr==None
                    if number+amount>self.n_rooms:break
                    if all([all(self.rooms[date][floor][number:number+amount]) for date in range(chk_in-1,chk_out-1)]):
                        k=[self.cnt_rooms[date][floor] for date in range(chk_in-1,chk_out-1)]
                        found.append([-sum(k),chk_in,chk_out,floor,number])
        found.sort()
        return found[0][1:] if found else []
    def assignRooms(self,id,amount,chk_in,chk_out,floor,number):
        for date in range(chk_in,chk_out):
            for a in range(amount):
                self.rooms[date][floor][number+a]=False
                self.rooms[date][floor][number+a]=False
            self.room_cnt[date][floor]-=amount
        self.book[chk_in-1].append({"id":id,"room_number":int(str(floor+1)+str(number+1).zfill(3))})
    def chkRequests(self):
        if self.today%1==0:print('\n',self.today)
        reply=[]
        for r in self.api.newRequest():
            r['day']=self.today
            self.req.append(r)
        self.req.sort(key=lambda x:[self.today>=min(x['day']+14,x['check_in_date']-1),x['amount']])
        for i in range(len(self.req)-1,-1,-1):
            id,amount,chk_in,chk_out,day = self.req[i].values()
            if self.today>=min(day+14,chk_in-1) or amount>=self.threshold:
                result = self.chkRooms(chk_in,chk_out,amount)
                if result:
                    self.assignRooms(id,amount,*result)
                    reply.append({ "id": id, "reply": "accepted"})
                else:
                    reply.append({ "id": id, "reply": "refused"})
                self.req.pop(i)
        if reply:
            self.api.sendReply(reply)
    def simulate(self):
        self.today=self.api.simulate(self.book[self.today-1])
def solve():
    for i in [2]:
        call = callApi(i)
        hotel= Hotel(i,call)
        while hotel.today<=hotel.n_days:
            hotel.chkRequests()
            hotel.simulate()
        hotel.api.getScore()
solve()

'''
score {'accuracy_score': 80.0, 'efficiency_score': 10.0, 'penalty_score': 446.01671184390335, 'score': 143.98328815609665} th:1 (50,10,5,1)
score {'accuracy_score': 80.0, 'efficiency_score': 4.940239043824701, 'penalty_score': 517.3034790205875, 'score': 67.63676002323723}
score {'accuracy_score': 80.0, 'efficiency_score': 4.940239043824701, 'penalty_score': 520.455879387979, 'score': 64.48435965584565} th:5
score {'accuracy_score': 80.0, 'efficiency_score': 4.940239043824701, 'penalty_score': 466.33952373485073, 'score': 118.60071530897397}
score {'accuracy_score': 80.0, 'efficiency_score': 0.8207171314741035, 'penalty_score': 304.6799883509935, 'score': 276.14072878048063}


'''

'''

score {'accuracy_score': 80.0, 'efficiency_score': 10.0, 'penalty_score': 177.21844244281246, 'score': 412.7815575571875}
score {'accuracy_score': 80.0, 'efficiency_score': 10.0, 'penalty_score': 277.3493002471533, 'score': 312.6506997528467}
score {'accuracy_score': 80.0, 'efficiency_score': 1.096798043564807, 'penalty_score': 215.1069210109948, 'score': 365.98987703257}
score {'accuracy_score': 80.0, 'efficiency_score': 1.153955525223227, 'penalty_score': 208.6480798482816, 'score': 372.50587567694157}



'''