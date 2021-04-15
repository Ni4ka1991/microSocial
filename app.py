#!/usr/bin/env Python3

# MAIN MODULE
import math

from data import *

from os import system
from random import randint


pages = math.ceil( len( users )/USERS_PG )


def userList( pg ):
 
 system( "clear" )
 
 print( f"THE LIST OF USERS IS {pages} PAGES.\n" )
 
 if( pg != pages ):
  for i in range( USERS_PG * ( pg - 1 ), USERS_PG * pg ): 
   name   = users[i]["name"]
   city   = users[i]["address"]["city"]
   status = "(O)" if users[i]["online"] else "(-)"
   print( f"{( i + 1 ):2} - {name:25} ( {city:15} ) {status}" )
 else:
  for i in range( USERS_PG * ( pg - 1 ), len( users )): 
   name   = users[i]["name"]
   city   = users[i]["address"]["city"]
   status = "(O)" if users[i]["online"] else "(-)"
   print( f"{( i + 1 ):2} - {name:25} ( {city:15} ) {status}" )

 print( "-" * 54 )

 for k in range( 1, pages + 1 ):
  if( k == pg ):
   print( "[ %d ]"%k , end = "" )
  else:
   print( " %d "%k , end = "" )
  
 print()

 ####### PRINT USER LIST #########

anchor = 1

userList( anchor ) 

while True:

 navigator = input( "\nEnter p to change page number or < / >  to go to the prev / next pages. Enter x to exit. >>>  " )
 print()
 if( navigator == "p" ):
   invite = int( input( f"Select a page from the range 1 to {pages}  >>>  " ))
  
   if( anchor <= invite <= pages ):   
     userList( invite )

   else:
     print( "Such page is not in the list" )
     input( "hit ENTER to continue" )

 elif( navigator == "<"):
   if( anchor > 1):
    anchor -= 1
    userList( anchor )
   else:
    print( "You are already  on the first page." )
    input( "hit ENTER to continue" )

 elif( navigator == ">"):
   if( anchor < pages ):
    anchor += 1
    userList( anchor )
   else:
    print( f"You are already  on the last < {pages} > page." )
    input( "hit ENTER to continue" )
 elif( navigator == "x"):
  print( "By, by!" )
  break
 else:
  print( "Be careful!" )
 











 
# ####### PRINT USER LIST #########

