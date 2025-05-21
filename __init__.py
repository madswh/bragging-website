from db import Database
from emailer import Emailer
from secret_values import secret_values

database = Database()

emailer = Emailer("smtp.gmail.com",587,secret_values["username"],secret_values["password"])