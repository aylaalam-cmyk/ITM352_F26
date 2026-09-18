#get url from the user, clean it, and extract the domain name and TLD (top-level domain)
#name: Ayla Alameida
#date: 9/18/2026

url = input("Enter a URL: ")

cleaned_url = url.replace("http://", "")
cleaned_url = cleaned_url.replace("/", "")
print("Cleaned URL :", cleaned_url)


# Extact the domain name and TLD 

parts = cleaned_url.split(".")
print("The parts are: ", parts)

domain_name = parts[1]
TLD = parts[2]
print("Domain Name: ", domain_name)
print("TLD: ", TLD)
