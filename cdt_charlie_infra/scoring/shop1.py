import requests
import socket

def check_frontend(target_host, target_port=5173):
    """
    Attempts to connect to the frontend HTTP service.
    Returns True if HTTP status code is 200, otherwise False.
    """
    url = f"http://{target_host}:{target_port}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Frontend is up")
            return True
        else:
            print(f"Frontend returned status code {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Error connecting to frontend: {e}")
        return False

def check_backend(host, port=3000):
    """
    Checks if the backend service is running on the specified host and port.
    Returns True if the port is open, False otherwise.
    """
    try:
        with socket.create_connection((host, port), timeout=5):
            print("Backend is running on port 3000")
            return True
    except Exception as e:
        return False

def main():
    host = "192.168.1.2"

    # Check frontend
    frontend_success = check_frontend(host)

    # Check database
    backend_success = check_backend(host)

    if frontend_success and backend_success:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
