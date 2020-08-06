A Simple Flask based Web Application
<hr>
Outlines the project structure to get started with building a Python Flask Web application and includes the steps to be followed to deploy the application on Apache Web Server using mod_wsgi.

## Server Setup
An EC2 Instance is used as the Server for the application.<br/>

Operating System: <b>Ubuntu 18.04</b></br>
Python Version: <b>Python 3.6.9</b>

### Install pip
Pip is required for installing Python modules from the PyPI repository. Additionally, install the development packages for python
```
~$ sudo apt-get install python3-pip python-dev
```

### Enable HTTP and HTTPS Ports
By default, ports 80 and 8080 are not blocked on AWS provided Ubuntu AMIs. 
In case they are not open, run these commands below
```
~$ sudo ufw allow from any to any port 8080 proto tcp
~$ sudo ufw allow from any to any port 80 proto tcp
```

### Install Apache
```
~$ sudo apt-get install apache2
```
To check if Apache is installed, direct your browser to your instance's Public IP address `http://<Public-DNS>/`

### Install mod_wsgi
WSGI (Web Server Gateway Interface) is an interface between web servers and web applications for python. <br/>
<b><i>mod_wsgi</i></b> is an Apache HTTP server mod that enables Apache to serve Flask applications.
```
~$ sudo apt-get install libapache2-mod-wsgi-py3
```
Enable <b>mod_wsgi</b>
```
~$ sudo a2enmod wsgi
```

## Deploy Application
Clone this repository to the apache's <i>/var/www/</i> directory.<br/>
```
~$ cd /var/www/
~$ git clone https://github.com/franklinsijo/flask-simple-webapp.git
~$ ls /var/www/
    flask-simple-webapp
```
Now, We have the application files in the server. <br/>
Let us install the application's dependencies
```
~$ cd /var/www/flask-simple-webapp/
~$ pip3 install -r pip.requirements
```

Next, Serve the application using Apache.
```
~$ sudo cp /var/www/flask-simple-webapp/app.conf /etc/apache2/sites-available/app.conf
```
Update the `app.conf` file with the EC2 instance's public DNS. Or,
```
~$ export EC2_PUBLIC_DNS=<YOUR_EC2_INSTANCE_PUBLIC_DNS>
```
<br/>
Disable the default apache homepage and enable `app`

```
~$ sudo a2dissite 000-default
~$ sudo a2ensite app
```
Finally, restart apache service
```
~$ sudo service apache2 restart
```

Access the application: `http://<Public-DNS>/`
