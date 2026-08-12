import json 

def load_data(file_path):                   #data load function for json files#

    with open(file_path , "r") as file:
        return json.load(file) 

def save_data(file_path , data):             #data save function for json files#

    with open(file_path , "w") as file:
        json.dump(data , file , indent= 4 )