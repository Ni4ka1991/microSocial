#!/usr/bin/env Python3

# MAIN MODULE app.py

 ## imports ######

import math

from data import *

from os import system
from random import randint

 ## ###############

pages = math.ceil( len( users )/USERS_PG )

 ##   VIEW  #######################

def userList( pg ):
 
 system( "clear" )
 
 print( f"THE LIST OF USERS IS {pages} PAGES.\n" )
 
  ###  print a specified interval #######

 for i in range( USERS_PG * ( pg - 1 ), min( USERS_PG * pg, len( users ))): 
  name   = users[i]["name"]
  city   = users[i]["address"]["city"]
  status = "(O)" if users[i]["online"] else "(-)"
  print( f"{( i + 1 ):2} - {name:25} ( {city:15} ) {status}" )

  ###  print a specified interval #######

 print( "-" * 54 )

  ### print a pages number ##############

 for k in range( 1, pages + 1 ):
  if( k == pg ):
   print( "[ %d ]"%k , end = "" )
  else:
   print( " %d "%k , end = "" )
  
 print()

  ### print a pages number ##############

 ##  VIEW  #############################

 ##  LOGIC  ############################

anchor = 1 # which page will be show first

userList( anchor ) # print the first page userList( 1 )

while True:

 navigator = input( "\nEnter p to change page number or < / >  to go to the prev / next pages. Enter x to exit. >>>  " )
 print()
 
 if( navigator == "p" ):
   invite = int( input( f"Select a page from the range 1 to {pages}  >>>  " ))
  
   if( anchor <= invite <= pages ): # if entered number in range 1( anchor ) - 5 ( all pages) 
     userList( invite )             # print list

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
 
 elif( navigator == "x" ):
  print( "By, by!" )
  break

 else:
  print( "Be careful!" ) #lazy check
 
 ## LOGIC #####################################
