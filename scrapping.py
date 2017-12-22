	#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup



url="https://www.humblebundle.com/books/be-a-coder-books"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')

tiers=soup.select(".dd-game-row")
tier_dict={}
for tier in tiers:
	#Only for Sections that have a headline
	if tier.select(".dd-header-headline"):
		#Grab tier name and price
		tiername=tier.select(".dd-header-headline")[0].text.strip()
		#grab tier product names
		product_names=[tier.text.strip() for tier in tier.select(".dd-image-box-caption")]
		#Add data to our datastructure		
		tier_dict[tiername]={"products":product_names}



#After we build our datastruction..
for tiername,tierinfo in tier_dict.items():
	print(tiername)
	print("##################################")
	print("\n".join(tierinfo['products']))
	print("\n\n")







"""
# Select Bundle dd-header-headline

tier_headlines=soup.select(".dd-header-headline")
stripped_tier_names=[tier.text.strip() for tier in tier_headlines]

#Product Names
product_names=soup.select(".dd-image-box-caption")
stripped_tiernames=[tier.text.strip() for tier in product_names]


tiers={
"tier1":{
"price":500,"products":["name1","name2"]},
"tier2":{"price":500,"products":["name1","name2"]
}
}


for tiername,tierinfo in tiers.items():
	print(tiername)
	print("priced at " ,tierinfo['price'])
	print("products:")
	print(", ".join(tierinfo['products']))
	print("\n \n")
"""
