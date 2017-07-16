#module name : whoisuse.py
import os

def get_whois(url):
	cmd = "whois " + str(url)
	pro = os.popen(cmd)
	res = str(pro.read())

	return res
