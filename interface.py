import sys 
from bot import *

command = sys.argv[1]


if command == "login":
    login()

if command == "logout":
    logout()

if command == "write":
    file_in = sys.argv[2]
    post_file(file_in)

if command == "read":
    file_in = sys.argv[2]
    read_file(file_in)

if command == "big-write":
    file_in = sys.argv[2]
    new_post(file_in)

if command == "big-read":
    file_in = sys.argv[2]
    read_post(file_in)

