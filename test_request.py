import twitter as twit

class RecommendedUsers():
    ''' Given a user's username and password, provides a method for getting
        the friends of the user's friends
    '''
    def __init__(self, username=None, password=None):
        self.user = username
        self.pwd = password
        self.api = twit.Api(self.user,self.pwd)
        self.friends = self.api.GetFriends()
        self.friend_id_list = [u.id for u in self.friends]
        self.names = []

    # create a list of friends of friends
    def getRecommendedUsers(self):
        for id_ in self.friend_id_list:
            users_rec = [u.name for u in self.api.GetFriends(id_)]
            for name in users_rec:
                self.names.append(name)
        
            


