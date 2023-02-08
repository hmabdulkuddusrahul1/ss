import requests
from bs4 import BeautifulSoup

filename = input("Enter Range File : ")
domain_coun = 0
with open(filename) as file:
  contents = file.read()
  lines = contents.split("\n")
  for line in lines:
    domain_count = 0
    url = "https://rapiddns.io/s/" + line + "?full=1&down=1#result"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    domains = [td.text.strip() for td in soup.find_all("td") if td.text.strip() != "A"]
    with open("results.txt", "a") as file:
      for domain in domains:
        if '.' in domain:
          file.write(domain + "\n")
          domain_count += 1
          domain_coun += 1
    print ("[ + ] "+line+" -» "+str(domain_count))
print("[ + ] Total Links -» " + str(domain_coun))
