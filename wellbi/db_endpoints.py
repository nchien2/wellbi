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
username (String): Username of user who is commenting
post_id (String) : id of post comment is under
'''
def make_comment(content, username, post_id):
    data = {
        'body': content,
        'author': username,
        'parent-post': post_id,
        'likes': 0,
        'post-time': firestore.SERVER_TIMESTAMP
    }
    comm_ref = comments.document()
    comm_ref.set(data)
    user_ref = users.document(username)
    post_ref = posts.document(post_id)

    user_ref.update({u'comments': firestore.ArrayUnion([comm_ref])})
    post_ref.update({u'comments': firestore.ArrayUnion([comm_ref])})
    return comm_ref.id

'''
Returns all the comments under a given post
'''
def get_comments(post_id):
    post = posts.document(post_id).get().to_dict()
    content_list =[]
    author_list = []
    for comm_ref in post['comments']:
        comment = comm_ref.get()
        content_list.append(comment.to_dict()['body'])
        author_list.append(comment.to_dict()['author'])
    return content_list, author_list

'''
Returns a list of top posts
'''
# TODO: Update to only get top few posts by certain criteria... once we decide the criteria
def get_top_posts():
    title_list =[]
    id_list = []
    for post in posts.stream():
        title_list.append(post.to_dict()['title'])
        id_list.append(post.id)
    return title_list,id_list
