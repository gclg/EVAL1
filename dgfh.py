class student:
    def __int__(self):
        self.stu={}
    def add_student(self,name,classe,height,weight,psport,grade):
        self.stu={"name":name,"class":classe,"height":height,"weight":weight,"psport":{"own":psport,"rec":[]},"abilities":None,"grade":grade}
    def add_abilities(self,solving,agility,speed,strength):
        self.stu["abilities"]={"prb_solving":solving,"agility":agility,"speed":speed,"strength":strength}
    def app_sport(self):
        if(self.stu["abilities"]["prb_solving"]>80):
            print("chess")
            self.stu["psport"]["rec"].append("chess")
            if(self.stu["abilities"]["agility"]>50 and self.stu["abilities"]["speed"]>70):
                print("football")
                self.stu["psport"]["rec"].append("football")
        if(self.stu["abilities"]["strength"]>70 and self.stu["abilities"]["speed"]>50):
            print("cricket")
            self.stu["psport"]["rec"].append("cricket")
        if(self.stu["abilities"]["strength"]>80 and self.stu["abilities"]["speed"]>70):
            print("javelin throw")
            self.stu["psport"]["rec"].append("javelin")
            
    def diet_rec(self):
        if(self.stu["height"]<80 or self.stu["weight"]<80):
            print("eat food rich in calcium and protein")
        if(self.stu["weight"]<100):
            print("eat food low in carbs and control calories.\n consume balance diet")
        if("football" in self.stu["psport"]["rec"]):
            print("always consume electrolytes and eat protein")
        if("chess" in self.stu["psport"]["rec"]):
            print("eat food nutritious in vitamins and low carbs")
            

s=student()
print("enter student details")
name=input("enter name: ")
classe=int(input("enter class: "))
height=int(input("enter height: "))
weight=int(input("enter weight: "))
# s.add_student(class)
z=[] 
i=1
while i:
    x=input("enter sport")
    z.append(x)
    i=int(input("enter 1 to continue and 0 to end"))
grade=int(input("enter grade: "))
s.add_student(name,classe,height,weight,z,grade)
solving=int(input("enter solving: "))
agility=int(input("enter AGI: "))
speed=int(input("enter spee: "))
strength=int(input("enter stren: "))
s.add_abilities(solving,agility,speed,strength)
s.app_sport()
s.diet_rec()
