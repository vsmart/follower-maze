Overview: 

* Elements 

** Socket Server
** Event Source 
** User Client []

* Element Methods

** Socket Server 
*** ?Reads events from event_source
*** !forwards them to x of [user_client]

** Event Source
*** !Sends stream of events to socket_server

** User Client
*** ?Receives notifications for events relevant to user self

* Protocol Meta
** String based 
** Each msg terminated by `CRLF`
** strings encoded in UTF-8

* Protocol
** event_source 
*** connects on 9090 
*** starts sending events as soon as connection is established

** user_clients
*** connect on 9099
*** send server ID of represented user 
*** wait for events for that user id
 
