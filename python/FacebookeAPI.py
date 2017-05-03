# To import Facebook SDK, do :
# virtualenv facebookenv
# source facebookenv/bin/activate
# pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk


# myFacebook = FacebookAPI(access_token = my_token)
# my_likes = myFacebook.getNamesFromFacebookLikes()
# my_likes = myFacebook.get_user_facebook_likes()

import facebook
import requests
from pprint import pprint
import json


class FacebookAPI:
    def __init__(self, access_token, userid='me'):
        self.access_token = access_token
        self.user_id = userid
        self.graph = facebook.GraphAPI(access_token)

    # Debug display of the json data
    def printdatarecovered(self, dataRecovered):
        print(json.dumps(dataRecovered, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))

    # Get the name of all the pages the user has liked
    def getNamesFromFacebookLikes(self):
        facebook_likes = self.get_user_facebook_likes()
        list_of_names = list()
        for facebook_like in facebook_likes:
            list_of_names.append(facebook_like['name'])
        return list_of_names

    # Get the basic Facebook user profile
    def get_user_facebook_profile(self):
        profile = self.graph.get_object(self.user_id)
        return profile

    # Get Complete informations about all likes from a list of their ids
    def get_pages_from_ids(self):
        ids = self.getIdsFromFacebookLikes()
        list_of_pages = list()
        for i in range(0, len(ids)//50 + 1 ):
            if len(ids) > (i+1) * 50:
                sublist_ids = ids[i*50:(i+1)*50]
            else:
                sublist_ids = ids[i*50:len(ids)]

            #self.printdatarecovered(sublist_ids)
            pages = self.graph.get_objects(ids=sublist_ids, fields='name,about,description,category')
            list_of_pages.append(pages)
        return list_of_pages
			
    # Get all the likes the user has liked (all pages)
    def get_user_facebook_likes(self):
        likesPages = self.graph.get_all_connections(id=self.user_id, connection_name='likes')
        result = list()
        for likePage in likesPages:
            result.append(likePage)
        return result 
        

