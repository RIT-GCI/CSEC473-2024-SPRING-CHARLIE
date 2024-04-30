import requests

def check_http_service_up(ip_address):
    try:
        response = requests.get(f"http://{ip_address}")
        return response.status_code == 200
    except requests.ConnectionError:
        return False

if __name__ == "__main__":
    http_box_2_ip = '192.168.2.6'  # Blue Team Box 2 IP Address
    service_up = check_http_service_up(http_box_2_ip)
    print(service_up)
