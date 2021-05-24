# Name:- Arjun Chauhan
# Instagram Handle:- @python.programe

import instaloader
insta=instaloader.Instaloader()
pp=input("Enter Instagram Username:- ")
insta.download_profile(pp,profile_pic_only=True)