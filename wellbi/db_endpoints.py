from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
users = db.collection(u'users')
posts = db.collection(u'posts')
comments = db.collection(u'comments')
tag_coll = db.collection(u'tags')


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
            'comments': [],
            'liked_posts':[],
            'liked_comments':[]
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
def make_post(title, content, username, tags):
    data = {
        'body': content,
        'comments': [],
        'likes': 0,
        'title': title,
        'author': username,
        'tags': [tag for tag in tags if tag is not None],
        'created_at': firestore.SERVER_TIMESTAMP
    }
    postref = posts.document()
    postref.set(data)
    user_ref = users.document(username)
    user_ref.update({u'posts': firestore.ArrayUnion([postref])})

    for tag in tags:
        print(tag)
        # if tag == None:
        #     continue
        tag_list = tag_coll.where('value', '==', tag).get() # .stream() is preferred but doesn't work - look into later
        print(tag_list)
        if not tag_list:
            tag_dict = {
                'value': tag,
                'posts': [postref.id]
            }
            tagref = tag_coll.document(tag)
            tagref.set(tag_dict)
        else:
            tag_list[0].reference.update({'posts': firestore.ArrayUnion([postref.id])})
      
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
    comment_list = []
    for comm_ref in post['comments']:
        comment = comm_ref.get().to_dict()
        if comment:
            comment['id'] = comm_ref.id
            comment_list.append(comment)
        else:
            comment_list.append(None)
    return comment_list

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


def get_posts_with_tag(tag):
    tag_list = tag_coll.where('value', '==', tag).stream()
    title_list = []
    for tag_obj in tag_list:
        id_list = tag_obj.to_dict()['posts']
        title_list = [posts.document(id).get().to_dict()['title'] for id in id_list]
        return id_list, title_list

'''
Likes post with post_id and records which user liked it. If post is already liked, 
instead unlikes it
'''
def like_post(post_id, username):
    post = posts.document(post_id)
    user_ref = users.document(username)
    if post_id in user_ref.get().to_dict()['liked_posts']:
        user_ref.update({u'liked_posts': firestore.ArrayRemove([post_id])})
        post.update({u'likes': firestore.Increment(-1)})
    else:
        user_ref.update({u'liked_posts': firestore.ArrayUnion([post_id])})
        post.update({u'likes': firestore.Increment(1)})

def like_comment(comment_id, username):
    comment = comments.document(comment_id)
    user_ref = users.document(username)
    if comment_id in user_ref.get().to_dict()['liked_comments']:
        user_ref.update({u'liked_comments': firestore.ArrayRemove([comment_id])})
        comment.update({u'likes': firestore.Increment(-1)})
    else:
        user_ref.update({u'liked_comments': firestore.ArrayUnion([comment_id])})
        comment.update({u'likes': firestore.Increment(1)})
    return comment.get().to_dict()['parent-post']

def get_liked_ids(username, post_id):
    user_dict = users.document(username).get().to_dict()
    liked = False
    liked_comm_list = []
    if post_id in user_dict['liked_posts']:
        liked = True
    post = posts.document(post_id).get().to_dict()
    comments = post['comments']
    for i in range(len(comments)):
        if comments[i].id in user_dict['liked_comments']:
            liked_comm_list.append(i)
    return liked, liked_comm_list 

def delete_post(id, username):
    posts.document(id).delete()
    users.document(username).update({'posts': firestore.ArrayRemove([posts.document(id)])})

def delete_comment(id, username):
    comments.document(id).delete()
    users.document(username).update({'comments': firestore.ArrayRemove([comments.document(id)])})

def get_tags():
    tags = tag_coll.get()
    return sorted([tag.id for tag in tags], key=str.lower)
