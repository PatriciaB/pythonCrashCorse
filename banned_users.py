"""
consider a list of users who are banned from commenting in a forum. You can check whether a user
"""
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")