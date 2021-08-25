class gun:

    def __init__(self):
        self
    def rounds(self,rounds=6):
        self.rounds=rounds
        print(self.rounds,'Rounds available')

    def shoot_1(self):
        if self.rounds>0:
            self.rounds -=1
            print('Shot fired')
            print(self.rounds,'Rounds remaining')
        else:
            print('Gun is empty')

    
