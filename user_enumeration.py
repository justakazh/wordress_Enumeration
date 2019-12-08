# WP ENUMERATE
# PYTHON 3.6.7
# CODED BY AKAZH ID

import requests
import json
import threading

print("""

 __      ____________ 
/  \    /  \______   \
\   \/\/   /|     ___/
 \        / |    |    
  \__/\  /  |____|    
       \/           Enumeration


Coded by : Akazh ID
Facebook : fb.com/justakazh
""")

def get(url):
	try:

		header = {
		"user-agent":""
		}
		target = url+"/wp-json/wp/v2/users"
		r = requests.get(target, headers=header)
		res = r.text
		j1 = json.loads(res)
		if "slug" in res:
			name = j1[0]['name']
			slug = j1[0]['slug']
			print("[+] Found! ---> ",url," || Name : ",name," || Slug : ",slug)
		else:
			print("[-] Unknown! ---> ",url)

	except:
		pass


i = input("List >> ")
o = open(i, "r").readlines()
for x  in o:
	try:
		y = x.strip()
		y = y.replace("https", "http")
		t1 = threading.Thread(target=get, args=(y,))
		t1.start()
	except:
		pass
