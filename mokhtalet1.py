class c_num :
    def __init__(self, haghighi=None, mohoom=None):
        self.r = haghighi
        self.i = mohoom
    def sub(self, other):
        result=c_num()
        result.r= self.r - other.r
        result.i= self.i - other.i
        return result
    def sum(self, other):
        result=c_num()
        result.r= self.r + other.r
        result.i= self.i + other.i
        return result
    def mul(self, other):
        result=c_num()
        result.r= self.r * other.r - self.i * other.i
        result.i= self.r * other.i - self.i * other.r
        return result
    def show(self):
        return str(self.r )+'+('+str(self.i) +')i'
haghighi1=int(input('bakhshe haghighi adad aval mokhtalet ra vared konid :'))
mohoom1=int(input('bakhshe mohoom adad aval mokhtalet ra vared konid  :'))
haghighi2=int(input('bakhshe haghighi dovom  mokhtalet ra vared konid : '))
mohoom2=int(input('bakhshe haghighi dovom  mokhtalet ra vared konid  :'))
mokhtalet1 = c_num(haghighi1,mohoom1)
mokhtalet2 = c_num(haghighi2,mohoom2)
print('+:',(mokhtalet1.sum(mokhtalet2)).show())
print('-:',(mokhtalet1.sub(mokhtalet2)).show())
print('*:',(mokhtalet1.mul(mokhtalet2)).show())