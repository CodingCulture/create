import re
import os
import crypt
import time
import getpass

def colored(str, color):
	start = "\033[1m"
	if(color == "red"):
		start = "\033[91m"
	elif(color == "warning"):
		start == "\033[93m"

 	return start  + str + "\033[0m"


print "##################################"
print "#                                #"
print "#   makeUser::RHEA version 0.1   #"
print "#   author: im@nielsvermaut.eu   #"
print "#                                #"
print "##################################"
print ""

print "This program will create a new user in Rhea, together with the right folders to enable web access"
print colored("This script doesn't make DNS edits!", "warning");
print "Please enter the username for the new user"
username = raw_input().lower();


"""Check if the username contains spaces""" 
if (' ' in username) == True:
	print colored("The username contains an illegal character (space)", "red")
	exit();

"""Check if the username doesn't contain any special chars"""
if not (re.match(r'^\w+$', username)):
	print colored("The username contains illegal characters", "red")
	exit();

"""Ask for the url"""
print "Please enter the url for this user, by which is site will be available"
userurl = raw_input().lower();

homedir = "/home/" + username

"""Ask the users password"""
print "Please enter a nice and strong password"
password = getpass.getpass()
password = crypt.crypt(password, "22")

"""Check if that homedir already exists"""
if os.path.exists(homedir):
	print colored("This username overlaps with a user in the homedir", "red");
	exit();

"""Create the homedir and web dir"""
os.system("useradd -d" + homedir + " -m " + username + " -p " + password)
os.system("chage -d 0 " + username)

if not os.path.exists(homedir):
	print colored("Something went wrong. The user probably exists already", "red")
	exit();
os.makedirs(homedir + "/web")

urldir = "/var/www/" + userurl
"""Check if the url isn't taken already"""
if os.path.exists(urldir):
	print colored("The url has already been taken", "red")

"""Create the urldir"""
os.makedirs(urldir)


"""Create the symlink"""
if not os.path.exists(homedir + "/web"):
	print colored("Something went wrong with the creation of web directory")
	exit();

os.system("ln -s " + homedir + "/web " + urldir + "/public_html")

"""Set the permissions"""
os.system("chown -R " + username + ":" + username + " " + homedir)

"""Create the apache config"""
apacheconfig = "/etc/apache2/sites-available/" + userurl + ".conf"

file = open(apacheconfig, "w")
file.write("<VirtualHost *:80>\n");
file.write("ServerName " + userurl + "\n");
file.write("ServerAlias www." + userurl + "\n");
file.write("ServerAdmin info@codingculture.be\n");
file.write("DocumentRoot /var/www/" + userurl + "/public_html\n")
file.write("ErrorLog ${APACHE_LOG_DIR}/error-" + username + ".log\n")
file.write("CustomLog ${APACHE_LOG_DIR}/access-" + username + ".log combined\n")
file.write("</VirtualHost>\n\n");
file.write("# vim: syntax=apache ts=4 sw=4 sts=4 r noet")
file.close()

while True:
	try:
		with open(apacheconfig, 'rb') as _:
			break
	except IOError:
			time.sleep(3)

os.system("ln -s /etc/apache2/sites-available/" + userurl + ".conf /etc/apache2/sites-enabled/" + userurl + ".conf")
os.system("service apache2 restart")

if not os.path.exists("/etc/apache2/sites-enabled/" + userurl + ".conf"):
	print colored("Something went wrong because the site doesn't report back as enabled")
 
os.system("cp -R ../placeholder/* /home/" + username + "/web")


print "#####################################"
print "#                                   #"
print "#            End result             #"
print "#                                   #"
print "#####################################"
print " \n"
print "Username: " + username
print "Single use password: " + password
print "Website url: " + userurl
print "Website user access: " + homedir + "/web"
print "Website symlink: " + "/var/www/" + userurl + "/public_html/"
print "\n"
print "Happy creating!" 
