import praw
import shutil
import os
import hashlib

temp_folder = "/tmp/redtrunk/"
conf_file = temp_folder+".rc"

def login():
    ##Create a temp fodler with authentication information
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    if not os.path.isfile(conf_file):
        f = open(conf_file,'a')
        f.write(raw_input("Insert your reddit_username (just if you want to post):  ")+"\n")
        f.write(raw_input("Insert your reddit_password (just if you want to post: ")+"\n")
        f.write(raw_input("Insert your reddit-folder (just if you want to read from this folder): ")+"\n")

def logout():
    shutil.rmtree(temp_folder)

def get_info():
    ##Recover the information for the current login
    f = open(conf_file)
    r_username = f.readline()[:-1]
    r_password = f.readline()[:-1]
    r_trunk = f.readline()[:-1]
    return [r_username, r_password,r_trunk]

   
##post_chiper and read cipher are the function that directly write or
## read the encrypted payload from reddit 
#(The encrypted payload must have less than 10000 character that is the maximum length of a reddit comment )

def post_cipher(cipher_text,r_username,r_password,r_trunk):
    ##Connect to user_agent
    user_agent = ("crypto_angel")
    r = praw.Reddit(user_agent = user_agent)
    r.login(r_username, r_password)
    subreddit = r.get_subreddit("cryptoparadise")
   
   ## Find the right reddit-folder and post your encrypted file there
    to_send = filter(None,cipher_text)
    for submission in subreddit.get_hot(): 
        if submission.title == r_trunk:
            submission.add_comment(cipher_text)


def read_cipher(cipher_name,r_trunk):
    ##Connect to user_agent
    user_agent = ("crypto_angel")
    r = praw.Reddit(user_agent = user_agent)
    subreddit = r.get_subreddit("cryptoparadise")
    
    ##Find the first comment whose name corresponds to your cipher_name and return the
    ##body of the comment
    for submission in subreddit.get_hot(): 
        if submission.title == r_trunk:
            for comment in submission.comments:
                lines =  comment.body.split("\n")
                if lines[0] == cipher_name:
                    return "\n".join(lines[1:]) 


##High level interface to post a file in the current reddit-folder

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

##The following functions allows you to post a file with more than 10000 character 
##by submitting a new post 

def new_post(filename):
	[r_username,r_password,r_truck]  = get_info() 
	cipher_name = hashlib.sha224(filename).hexdigest() 
	
	temp_file = temp_folder+cipher_name

    	os.system("openssl aes-256-cbc -in "+filename+" -a -out " + temp_file)

	cipher_text = open(temp_file).read()
	user_agent = ("crypto_angel 4")
    	r = praw.Reddit(user_agent = user_agent)
    	r.login(r_username, r_password)
    	subreddit = r.get_subreddit("cryptoparadise")
	step = 5000	
	ciphers = [cipher_text[i:i+step] for i in range(0, len(cipher_text), step)]
	subreddit.submit(cipher_name,"a pic")	

	for submission in subreddit.get_hot():
		if submission.title == cipher_name:
			for cipher in ciphers:
				submission.add_comment(cipher)			 

def read_post(filename):
	[r_username,r_password,r_truck]  = get_info() 
	cipher_name = hashlib.sha224(filename).hexdigest() 
	
	temp_file = temp_folder+cipher_name
	user_agent = ("crypto_angel 4")
    	r = praw.Reddit(user_agent = user_agent)
    	r.login(r_username, r_password)
    	subreddit = r.get_subreddit("cryptoparadise")
	
	## Collect the comments in the interested post
	cipher_text = ""	

	for submission in subreddit.get_hot():
		if submission.title == cipher_name:
                        submission.replace_more_comments(limit=None, threshold=0)
			for comment in submission.comments: 
				cipher_text += comment.body 

	##Write the encrypted file in the temp folder
	temp_file = temp_folder + cipher_name

    	f = open(temp_file,'w')
    	f.write(cipher_text+"\n")
   	f.close()

	##Decrypt the file and store it in current folder
   	os.system("openssl aes-256-cbc -d -in "+temp_file+" -a -out " + filename)


