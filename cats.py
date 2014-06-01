import urllib
import os



def main():
    file = open('cats.txt', 'r+')
    file.write( "Cats are okay at best\n I'm not a fan")
    file.close()

if __name__=='__main__':
    main()