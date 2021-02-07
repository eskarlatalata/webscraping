import requests

#da el tiempo de requests
import time


#un diccionario
urls = {
	
	"chedraui":{
	   "base_url": "https://www.chedraui.com.mx/p/{productNumber}",
	   "productNumber":[
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

def main(urls:dict):
	pass


if __name__ == "__main__":
	main(urls)
	



