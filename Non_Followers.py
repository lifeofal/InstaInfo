import os
import pickle
from path_config import cookie_path, list_path, my_path


class non_followers:
    def __init__(self):
        l1 = self.loadFollowers()
        l2 = self.loadFollowing()
        self.list_compair(l1, l2)

    def loadFollowers(self):
        with open((os.path.join(list_path, 'followers_list.txt')), 'rb') as followers:
            listFollowers = pickle.load(followers)
            return listFollowers

    def loadFollowing(self):
        with open((os.path.join(list_path, 'following_list.txt')), 'rb') as following:
            listFollowing = pickle.load(following)
            return listFollowing

    def list_compair(self, l1, l2):
        not_following_back = [user for user in l2 if user not in l1]
        with open('{}/non_followers.txt'.format(list_path), 'w') as f:
            for element in not_following_back:
                f.write(element + '\n')
        print(not_following_back)
