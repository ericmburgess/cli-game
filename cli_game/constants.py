import os
from posixpath import expanduser

DATA_DIR = expanduser("~/.cli-game")
FS_DIR = os.path.join(DATA_DIR, "fs")
