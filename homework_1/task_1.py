import re


def domain_name(url):
    domain = re.search(r'(https?://)?(www.)?([A-Za-z_0-9-]+).*', url)
    return domain[3]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
