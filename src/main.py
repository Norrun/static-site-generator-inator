# from textnode import *
from handle_static import static_copy
import os


        

def main():
    working = os.getcwd()
    origin = os.path.join(working,"static")
    dest = os.path.join(working,"public")
    static_copy(origin, dest)
main()