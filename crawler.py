import requests

#da el tiempo de requests
import time


#un diccionario
stores = {
	
	"chedraui":{
	   "url": "https://www.chedraui.com.mx/p/{productNumber}",
	   "productNumbers":[
	     {"product":"Media Crema Nestlé Lata 225g",
          "productNumber":"000000000003019751"
	     }
	   ]
	}
}


# la flechita no es necesaria
def get_url(url:str) -> str:
	"""
	Input:
	  url to visit
	Output:
	  source code of the visited url
	"""
	pass

def  save_result(file_name:str,source_code:str) -> str:
	"""
	Input:
	   source_code tobe stored in the file name
	Output:
	   path of saved file
    """
	pass

def main(stores:dict):
	for store in stores:
		base_url = stores[store]['url']

		for product in stores[store]['productNumbers']:
			url = base_url.format(**product)
			print(url)



if __name__ == "__main__":
	main(stores)




