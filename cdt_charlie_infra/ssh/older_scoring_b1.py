import paramiko
import requests

def check_ssh(target_ip, username, password):
    try:
        # SSH Connection
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(target_ip, username=username, password=password)
        # If SSH is successful, service is up
        return True
    except paramiko.AuthenticationException:
        # If authentication fails, service is down
        return False
    except Exception as e:
        # Other exceptions indicate service down or connection issues
        return False
    finally:
        client.close()

def send_to_scoring_engine(message):
    scoring_engine_url = "http://192.168.4.2/score"
    payload = {"message": message}
    try:
        response = requests.post(scoring_engine_url, json=payload)
        if response.status_code == 200:
            print("Message sent to scoring engine successfully.")
        else:
            print("Failed to send message to scoring engine.")
    except Exception as e:
        print("Error:", e)

def main():
    target_ip = "192.168.1.5"
    username = "Grey_Team"
    password = "P@ssw0rd123!"

    ssh_success = check_ssh(target_ip, username, password)
    if ssh_success:
        print("SSH connection to target successful.")
    else:
        print("SSH connection to target failed.")

    try:
        send_to_scoring_engine("Service Up" if ssh_success else "Service Down")
    except Exception as e:
        print("Failed to send status to scoring engine. Error:", e)

if __name__ == "__main__":
    main()
