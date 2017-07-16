import sys
import whoisuse
import json

def date_handler(obj):
	if hashttr(obj, 'isoformat'):
		return obj.iosformat()
	else:
		raise TypeError
num = sys.argv[1]
f=open(sys.argv[2], 'r')
f_result = open("resultwhoisdata.txt", 'w')
for x in range(int(num)):
	data = f.readline()
	print whoisuse.get_whois(str(data))
	json_dump = json.dumps(data, default=date_handler)
	f_result.write(whoisuse.get_whois(str(data)))
f.close()
	
