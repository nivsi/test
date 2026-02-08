import requests

class ApiClient:

    def __init__(self, base_url):
        self.__base_url = base_url

    def get_user_by_id(self, id: int):
        try:
            user_id = int(id) 
            params = {"id": user_id}
        except ValueError:
            return {"error": "must be int num"}
        try:
            res = requests.get(f'{self.__base_url}/id',params=params)
            res.raise_for_status()  
            return res.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def create_user(self, id: int, email: str):
        try:
            user_id = int(id)
            user_email = str(email)
            body = {"id": user_id,"email": user_email}
        except ValueError:
            return {"error": "must be int num"} 
        
        try:
            res = requests.post(f'{self.__base_url}/createUser', json = body)
            res.raise_for_status()
            return res.json()
        except requests.exceptions.RequestException as e:
            return{"mssg": str(e)}