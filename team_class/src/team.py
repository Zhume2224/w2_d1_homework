class Team:
    def __init__(self, input_name,input_players,input_coach):
        self.name=input_name
        self.players=input_players
        self.coach=input_coach
        self.points=0
        # self._teamwin={
        #     'True':3,
        #     'False':0
        # }

    def add_player(self,new_name):
        self.players.append(new_name)

    def has_player(self,new_name):
        for self.name in self.players:
            if self.name==new_name:
                return True
        else:
            return False
    def play_game(self,teamwin):
        if teamwin==True:
            self.points+=3

          

    
    

