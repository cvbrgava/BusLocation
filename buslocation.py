#!/usr/bin/env python
import urllib2, urllib
import ast
import time
import os
import dbus
import time
import gobject
from dbus.mainloop.glib import DBusGMainLoop

# Dbus variables
bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface( obj, "im.pidgin.purple.PurpleInterface" )

# Proxy authentication for pining the Civil Dept server
proxy = urllib2.ProxyHandler({'http': 'http://ee08b037:M@draa55@hproxy.iitm.ac.in:3128'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)


# Send message function for pidgin only.

def sendmessage(group,string):
    for online in purple.PurpleFindBuddies( (purple.PurpleAccountsGetAllActive())[0], '' ):
        if ( purple.PurpleBuddyGetAlias( online ) in group):
            conv = purple.PurpleConversationNew(1, (purple.PurpleAccountsGetAllActive())[ 0 ] , purple.PurpleBuddyGetName( online ) )
            purple.PurpleConvImSend(purple.PurpleConvIm(conv), string)
        
# List of all the aliases in your pidgin chat list

lab = ['IronButt Iyer','Shiny shoulder shekar','Sudharshan Viswanathan','Nigga Sarkari','Pardouche Gupto','Elbarato Mustachio','Ammi Jaan']
me = ['bhargava']

 

# Ping the server once every minute to check the co-ordinates of the bus.

while( True ):
	msgsent = 0
	conn = urllib2.urlopen("http://115.115.108.122//buses_json.php")
	bus_list = ast.literal_eval( conn.read())
	for bus in bus_list:
		if bus['routeid'] == 12 and bus['Moving'] == 1:
			print "Bus to Hostel -- moving"
			if bus['lng'] <= 80.2240 :
				sendmessage( lab, "Bus at velachery!!" )
				msgsent = 1
				break
	if msgsent ==1 :
		break
	time.sleep( 60 )
