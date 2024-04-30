import ftplib

def ftp_login(host, username, password):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(host)
        # Attempt to log in
        ftp.login(username, password)
        # If login is successful, print a success message
        print("Login successful!")
        # It's a good practice to logout after your work is done
        ftp.quit()
        return True
    except ftplib.all_errors as e:
        # If login fails, print the error
        print(f"FTP login failed: {e}")
        return False

# Replace 'your_username' and 'your_password' with the FTP account credentials
if __name__ == "__main__":
    HOST = "172.16.2.2"
    USERNAME = "Grey_Team"
    PASSWORD = "P@ssw0rd123!"
    
    # Attempt to log in
    ftp_login(HOST, USERNAME, PASSWORD)

