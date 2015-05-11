import os
import sys
from optparse import OptionParser

version = "0.2";

"""Read the parameters"""
parser = OptionParser();
parser.add_option("-u", "--username", dest="username", help="Defines a username before interaction", default="unset");
parser.add_option("-f", "--url", dest="url", help="Defines the url of the to be removed user", default="unset");

options, args = parser.parse_args();
options_dict = vars(options);
"""Set the username"""
username = options_dict["username"]
if options_dict["username"] == "unset":
	print "Username";
	username = raw_input().lower();

"""Set the url"""
url = options_dict["url"];
if options_dict["url"] == "unset":
	print "url";
	url = raw_input().lower();

os.system("rm -R /home/" + username);
os.system("userdel " + username);
os.system("rm -R /var/www/" + url);

os.system("rm /etc/apache2/sites-available/" + url + ".conf");

f = open(os.devnull, "w");
sys.stdout = f;
os.system("a2dissite " + url + ".conf");
