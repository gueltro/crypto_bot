import praw
import os
import hashlib

temp_folder = "/tmp/redtrunk/"
conf_file = temp_folder+".rc"

def login():
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    if not os.path.isfile(conf_file):
        f = open(conf_file,'a')
        f.write(raw_input("Insert your reddit_username (OPTIONAL):  ")+"\n")
        f.write(raw_input("Insert your reddit_password (OPTIONAL): ")+"\n")
        f.write(raw_input("Insert your trunk (MANDATORY): ")+"\n")

def get_info():
    f = open(conf_file)
    r_username = f.readline()[:-1]
    r_password = f.readline()[:-1]
    r_trunk = f.readline()[:-1]
    return [r_username, r_password,r_trunk]

    

def post_cipher(cipher_text,r_username,r_password,r_trunk):
    user_agent = ("crypto_angel")
    r = praw.Reddit(user_agent = user_agent)
    r.login(r_username, r_password)
    subreddit = r.get_subreddit("cryptoparadise")

    to_send = filter(None,cipher_text)
    for submission in subreddit.get_hot(): 
        if submission.title == r_trunk:
            submission.add_comment(cipher_text)


def read_cipher(cipher_name,r_trunk):
    user_agent = ("crypto_angel")
    r = praw.Reddit(user_agent = user_agent)
    subreddit = r.get_subreddit("cryptoparadise")
    for submission in subreddit.get_hot(): 
        if submission.title == r_trunk:
            for comment in submission.comments:
                lines =  comment.body.split("\n")
                if lines[0] == cipher_name:
                    return lines[1] 


def post_file(filename):
    [r_username,r_password,r_truck]  = get_info() 
    
    cipher_name = hashlib.sha224(filename).hexdigest() 
    
    temp_file = temp_folder+cipher_name
    os.system("openssl aes-256-cbc -in "+filename+" -a -out " + temp_file)
    
    cipher_text = cipher_name+ "\n" +open(temp_file).read()
    post_cipher(cipher_text, r_username, r_password, r_truck)

def read_file(filename):
    [r_username,r_password,r_truck]  = get_info()
    cipher_name = hashlib.sha224(filename).hexdigest()
    cipher_text = read_cipher(cipher_name,r_truck)    
    
    temp_file = temp_folder + cipher_name

    f = open(temp_file,'w')
    print cipher_text
    f.write(cipher_text+"\n")
    f.close()

    os.system("openssl aes-256-cbc -d -in "+temp_file+" -a -out " + filename)
