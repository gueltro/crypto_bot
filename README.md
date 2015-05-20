Insert this in yout .bashrc:

`alias cbot="python $USER/crypto_bot/interface.py"`

cbot will allow you to store encrypted file on reddit. During the login phase the program will ask for a truck. A truck is just the name of a post in /r/cryptoparadise, and you can think about it as a folder. In order to be able to use the write or read command you must insert a truck during login

Login as a reddit user:  

`cbot login`

Store a file in a post that you created:

`cbot write myfile`

Download the file from a post that you created:

`cbot read myfile`

Store a big file in a post in /r/cryptoparadise:

cbot big-write myfile

Recover a big file from a post in /r/cryptoparadise:

`cbot big-read myfile`
