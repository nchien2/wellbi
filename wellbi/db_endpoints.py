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
def get_user(username, password, update=False):
    user_list = users.where('username', '==', username).get() # .stream() is preferred but doesn't work - look into later
    if not user_list:
        data = {
            'username': username,
            'password': password,
            'posts': [],
            'comments': []
        }
        if update:
            users.document(username).set(data)
        return None, data
    for user in user_list:
        return user.id, user.to_dict()

def get_user_by_id(id):
    user = users.document(id).get()
    if user.exists:
        return user.to_dict()
    return None

# def make_post()