from ast import Param
import requests
import json

# def random_joke():
#     url = "http://icanhazdadjoke.com/"
#     response = requests.get(url, headers={"Accept": "application/json"})
#     print(response.content)
    


# if __name__ == "__main__":
#     random_joke()
    
    
def rimeaza():
    url = "http://api.datamuse.com/words"
    response = requests.get(url, params={"rel_rhy":"grape", "ml":"breakfast"})
    print(response.url)
    print(response.content)
    
 
if __name__ == "__main__":
    rimeaza()   
    
    