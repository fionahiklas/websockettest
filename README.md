## README

### IMPORTANT

I couldn't get things to work very well with python2.7 and twisted, just kept getting HTTP 500's back from the server for no apparent reason.  Switched to using asyncio and python3.3 (pip install asyncio and pip install autobahn) and things are working better with the server responding and connecting.  It may work fine with python2.7 etc but I've shifted over to python3 for now.

### Overview

Simple test based on the [Autobhan tutorial](http://autobahn.ws/python/tutorials/echo/)

The code is split into three sections

* apache-config - The files needed to forward WebSocket requests from Apache to the server 
* html-page - The html and JavaScript code for the client side of the websockets
* python-wsserver - The code from the [Autobahn tutorial](http://autobahn.ws/python/tutorials/echo/) for a simple echo server

### Development Environment

* I was playing around with this code on a Fedora 19 x86_64 Virtual Machine with the intention of also testing this out on a Raspberry Pi running Pidora (see later for attempts to get this working).

#### Python

* I needed to install the following with yum

			yum install python3
			yum install python3-pip
			yum install python3-devel

* Installed using the following

			python3-pip install asyncio
			python3-pip install autobahn
			python3-pip install --upgrade setuptools
			python3-pip install autobahn

* I'm not sure what's going on with the setuptools.  
* When I install autobahn first I get this error:

			[root@hermione ~]# python3-pip install autobahn
			Downloading/unpacking autobahn
			  Downloading autobahn-0.8.6.zip (164kB): 164kB downloaded
			  Running setup.py egg_info for package autobahn
			    
			    The required version of setuptools (>=2.1) is not available,
			    and can't be installed while this script is running. Please
			    install a more recent version first, using
			    'easy_install -U setuptools'.
			    
			    (Currently using setuptools 0.6c11 (/usr/lib/python3.3/site-packages))
			    Complete output from command python setup.py egg_info:
			    
			
			The required version of setuptools (>=2.1) is not available,
			
			and can't be installed while this script is running. Please
			
			install a more recent version first, using
			
			'easy_install -U setuptools'.
			
			
			
			(Currently using setuptools 0.6c11 (/usr/lib/python3.3/site-packages))
			
			----------------------------------------
			Command python setup.py egg_info failed with error code 2 in /tmp/pip-build-root/autobahn
			Storing complete log in /root/.pip/pip.log

* I also tried upgrading the setuptools *before* installing autobahn but that doesn't seem to make any difference
* Anyway, after all the above the server should start


### Apache Config

Since I wanted to muck around with several bits and pieces locally and don't want to keep su'ing to hack Apache config I enabled the mod_userdir module in userdir.conf so that I could symlink to my working code to play around.  After my editing the file /etc/httpd/conf.d/userdir.conf it looks like this (sans comments)

			<IfModule mod_userdir.c>
			    UserDir enabled 
			    UserDir public_html
			</IfModule>
			
			<Directory "/home/*/public_html">
			    AllowOverride FileInfo AuthConfig Limit Indexes
			    Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
			    Require method GET POST OPTIONS
			</Directory>


I have SELinux turned on (on the Fedora VM) and attempting to acccess the user directory caused an alert which needed to be fixed with the following command

			setsebool -P httpd_read_user_content 1


After all the of the above is done then you can copy the files under apache-config to the relevant direcories under /etc/httpd/ and restart Apache using the command

			systemctl httpd restart


### Testing

The server will happily run a non-root.

I link files from my working directory (~/wd/wstest) to ~/public_html and make sure that the permissions for ~/public_html (and indeed ~) are permissive enough to let the apache user access them.

Open a browser window on http://localhost/~<user>/index.html (or morecomplex.html)



### Messaging

#### Setup

* Install qpid and qmf

			yum install qpid-cpp-server qpid-qmf

* Install qpid for Python3





