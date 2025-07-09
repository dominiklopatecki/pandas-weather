import requests

# Oficjalna nazwa kraju
# Nazwa waluty w Polsce
# Nazwa języka w kraju (languages - > pol)
# Czy niepodległy, za pomocą ifa
# Za pomocą pętli, kody wszystkich krajów z którymi graniczy

URL = "https://restcountries.com/v3.1/name/poland"
response = requests.get(URL)
data = response.json()[0]
# 1
country_name =data.get("name").get("official")
print(country_name)
# 2
currence = data.get("currencies").get("PLN").get("name")
print(currence)
# 3
language = data.get("languages").get("pol")
print(language)
# 4
independent = data.get("independent")
if(independent):
    print("Kraj jest niepodległy")
else:
    print("Kraj jest podległy")

# 5
borders = data.get("borders")
print(borders)

for kraje in borders:
    print(kraje)

ALL_URL = "https://restcountries.com/v3.1/all?fields=name"
print(ALL_URL)
all_response = requests.get(ALL_URL)
all_data = response.json()[0]