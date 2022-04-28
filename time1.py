from unittest import result


class time :
    def __init__(self ,h,m,s) :
        self.hour=h
        self.minute=m
        self.second=s
    def show(self)   :
        print(self.hour, ":",self.minute, ":",self.second) 
    def sub(self,A,b) :
        result=time(0,0,0)   
        result.hour=A.hour-b.hour
        result.minute=A.minute-b.minute
        result.second=A.second-b.second
        return result
    def fix(self):
        if self.second>=60:
            self.second -=60
            self.minute +=1
        if self.minute >=60:
            self.minute -=60
            self.hour+= 1    

t1=time(2,44,30)
t2=time(3,15,12)

t1.show() 
t2.show()    
output=t1.sub(t1,t2)   
output.show()