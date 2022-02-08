from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('wellbi/key.json')
default_app = initialize_app(cred)
db = firestore.client()
users = db.collection(u'users')
posts = db.collection(u'posts')
comments = db.collection(u'comments')

'''
Given a username and password, retrieves and returns user information from the database.
If there is no matching user, creates a new one and returns it.

params: 
  username (string): username
  password (string): password
'''
def get_user(username, password):
    user_list = users.where('username', '==', username).get() # .stream() is preferred but doesn't work - look into later
    if not user_list:
        data = {
            'username': username,
            'password': password,
            'posts': [],
            'comments': []
        }
        users.add(data)
        return data
    for user in user_list:
        return user.id, user.to_dict()

def get_user_by_id(id):
    user = users.document(id)
    return user.to_dict()

# def make_post()