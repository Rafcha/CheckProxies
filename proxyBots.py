import requests

def is_proxy(ip):
    try:
        target_url = "https://www.google.com"

        proxies = {
            "http": f"http://{ip}",
            "https": f"http://{ip}"
        }

        expected_status_code = 200

        response = requests.get(target_url, proxies=proxies, timeout=10)

        if response.status_code == expected_status_code:
            return True
        else:
            return False

    except requests.exceptions.RequestException:
        return False

ip_list = [
    "1.2.3.4",
    "5.6.7.8",
]

for ip in ip_list:
    if is_proxy(ip):
        print(f"IP-адрес {ip} является прокси-ботом.")
    else:
        print(f"IP-адрес {ip} не является прокси-ботом.")