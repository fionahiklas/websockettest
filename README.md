## README

### IMPORTANT

I couldn't get things to work very well with python2.7 and twisted, just kept getting HTTP 500's back from the server for no apparent reason.  Switched to using asyncio and python3.3 (pip install asyncio and pip install autobahn) and things are working better with the server responding and connecting.  However JavaScript still doesn't think webSocket is defined (not connected) so more coding needed.  Will update the code and README when done.

### Overview

Simple test based on the [Autobhan tutorial](http://autobahn.ws/python/tutorials/echo/)

The code is split into three sections

* apache-config - The files needed to forward WebSocket requests from Apache to the server 
* html-page - The html and JavaScript code for the client side of the websockets
* python-wsserver - The code from the [Autobahn tutorial](http://autobahn.ws/python/tutorials/echo/) for a simple echo server

### Development Environment

* I was playing around with this code on a Fedora 19 x86_64 Virtual Machine with the intention of also testing this out on a raspberry Pi running Pidora.

#### Authbahn

* Installed using the following

			pip install autobahn

### Apache Config

Since I wanted to muck around with several bits and pieces locally and don't want to keep su'ing to hack Apache config I enabled the mod_userdir module in userdir.conf so that I could symlink to my working code to play around.

I have SELinux turned on and attempting to acccess the user directory caused an alert which needed to be fixed with the following command

			setsebool -P httpd_read_user_content 1


