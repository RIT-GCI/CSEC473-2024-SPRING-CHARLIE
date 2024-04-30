import requests

def check_frontend(target_host, target_port=5173):
    """
    Attempts to connect to the frontend HTTP service.
    Returns True if HTTP status code is 200, otherwise False.
    """
    url = f"http://{target_host}:{target_port}"
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    frontend_host = "192.168.1.2"

    # Check frontend
    frontend_success = check_frontend(frontend_host)

    if frontend_success:
        print("Frontend is up")
    else:
        print("Frontend is down")

if __name__ == "__main__":
    main()
