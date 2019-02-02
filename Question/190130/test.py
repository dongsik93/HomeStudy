class Change:
    def __init__(self,**kwargs):
        self.password = kwargs["password"]
        self.password_confirmation = kwargs["password_confirmation"]

    def change(self, c_password):
        if(self.password == c_password and self.password_confirmation == c_password):
            print("접속완료")
        else:
            print("비밀번호가 틀립니다")

my_id = Change(password="1122",password_confirmation="1122")
my_id.change("1123")
my_id.change("1122")