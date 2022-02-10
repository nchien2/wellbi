from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('wellbi/key.json')
default_app = initialize_app(cred)
db = firestore.client()
users = db.collection(u'users')
posts = db.collection(u'posts')
comments = db.collection(u'comments')

'''
Given a username and password, retrieves and returns user information from the database.
If there is no matching user and update=True, creates a new one and returns it.

params: 
  username (string): username
  password (string): password
  update (bool): True if new user should be created. False if you just want to retrieve user data.
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

'''
Returns a user with a specific id. User id should be the same as their username
'''
def get_user_by_id(id):
    user = users.document(id).get()
    if user.exists:
        return user
    return None


'''
Adds a post to the database and returns its id. 

params:
  title (String)   : Title of post
  content (String) : Content for body of post
  username (ref): Username of user who created post. 
'''
def make_post(title, content, username):
    data = {
        'body': content, 
        'comments': [],
        'likes': 0,
        'title': title,
        'author': username,
        'created_at': firestore.SERVER_TIMESTAMP
    }
    postref = posts.document()
    postref.set(data)
    user_ref = users.document(username)
    print(user_ref)
    user_ref.update({u'posts': firestore.ArrayUnion([postref])})
    return postref

def get_post_by_id(id):
    post = posts.document(id).get()
    return post.to_dict()

'''
Adds a comment to the database and returns its id. 

params:
content (String) : Content for body of comment
username (String): Username of user who 
post_id (String) :
'''
def make_comment(content, username, post_id):
    post_ref = posts.document(id).get()
    data = {
        'body': content,
        'author': username,
        'parent-post': post_ref, 
        'likes': 0,
        'post-time': firestore.SERVER_TIMESTAMP
    }
    comm_ref = comments.document()
    comm_ref.add(data)
    return comm_ref.id