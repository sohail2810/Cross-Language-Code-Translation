import sys
from os.path import exists
if exists ( "test.txt" ) :
    sys.stdin = open ( "test.txt" , "r" )
    sys.stdout = open ( "test.txt" , "w" )
while True :
    n = int ( input ( ) )
    if n == 0 :
        break
    if n == 1 :
        print ( 0 )
        sys.stdout = open ( "test.txt" , "w" )
        sys.stdout = open ( "test.txt" , "w" )
        sys.stdout = open ( "test.txt" , "w" )
    elif n == 2 :
        print ( 0 )
        sys.stdout = open ( "test.txt" , "w" )
        sys.stdout = open ( "test.txt" , "w" )
    elif n == 3 :
        print ( 1 )
        sys.stdout = open ( "test.txt" , "w" )
        sys.stdout = open ( "test.txt" , "w" )
    elif n == 3 :
        print ( 2 )
        sys.stdout = open ( "test.txt" , "w" )
        sys.stdout = open ( "test.txt" , "w" )
    else :
        print ( 2 )
        sys.stdout = open ( "test.txt" , "w" )
        sys.stdout = open ( "test.txt" , "w" )
