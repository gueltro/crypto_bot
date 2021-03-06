# `cbot`

## What is `cbot`?
cbot allows you to store encrypted data on [r/cryptoparadise] (https://www.reddit.com/r/cryptoparadise) (or somewhere else on reddit). The data is encrypted locally with openssl and posted on reddit as a normal comment.

## Can I run `cbot`?
I tested this on linux debian and OSX, but it should work on any unix machine. In order to make this work, you need openssl and praw.

For example, on debian you can download openssl with:

`sudo apt-get install openssl` 

and praw with:

`sudo pip install praw`


## How do I start using `cbot`?

After cloning this folder, linux users should insert the following into their .bashrc (or .zshrc or similar):

`alias cbot="python $USER/crypto_bot/interface.py"`

Similarly, OSX users should write:

`alias cbot="python $HOME/crypto_bot/interface.py"`

Login as a reddit user:  

`cbot login`

The script will ask you to insert username and password for you reddit account, but it is not necessary if you just want to read files that have already been encrypted and stored on reddit. 

The script will also ask you for a reddit-folder. A reddit-folder is just the name of a post on reddit.com/r/cryptoparadise. If you want to read encrypted file from some post that was previous created, or if you want to store some encrypted file on that post, you should insert the name of the post.

If you want to login as a different user, or you want to change the reddit-folder that you are using you will have to logout with:

`cbot logout`
##How do I store encrypted files on reddit?

The command `write` and `read` are used to read or write from a reddit-folder that was specified in the login procedure.

Store a file in a post that you created:

`cbot write myfile`

Download the file from a post that you created:

`cbot read myfile`

The commands `big-write` and `big-file` are intended to store files with more than 10000 character on them. This will create a new post on /r/cryptoparadise and post multiple comment with your encrypted payload. 


Store a big file in a post in /r/cryptoparadise:

`cbot big-write myfile`

Recover a big file from a post in /r/cryptoparadise:

`cbot big-read myfile`

Note that I do not advise storing large files using this system. It will take a very long time, and it will overload reddit which is a cool and open source site that allows us to interact with it through bots. A pdf or picture will be fine, but please do not upload long videos or other large files.
