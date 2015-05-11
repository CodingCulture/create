import os
import sys

print "Username"
username = raw_input().lower();

print "url"
url = raw_input().lower();

os.system("rm -R /home/" + username)
os.system("userdel " + username)
os.system("rm -R /var/www/" + url)

os.system("rm /etc/apache2/sites-available/" + url + ".conf")

f = open(os.devnull, "w")
sys.stdout = f
os.system("a2dissite " + url + ".conf")
