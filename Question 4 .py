
# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

import json

d1={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
}
b=open("Meraki q4.json","w")
b.write((json.dumps(d1,sort_keys=True,indent=4)))
b.close()


