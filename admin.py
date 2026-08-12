from utils import get_int_input
from data_manager import save_data , load_data

admins = load_data("data/admins.json")

def admin_login(): #login menu function for admins#

    while True:
    
        admin_email = input("Please enter your email: ")
        admin_password = input("Please enter your password: ")

        for admin_id, admin_info in admins.items():

            if admin_info["email"] == admin_email and admin_info["password"] == admin_password:
                return admin_id , admin_info
            
        
        print("Email or password is incorrect. Please try again.")

            



