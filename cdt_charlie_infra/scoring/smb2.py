import uuid
from smbprotocol.connection import Connection, Dialects
from smbprotocol.session import Session

def check_smb(target_ip):
    try:
        # Establish connection 
        connection = Connection(uuid.uuid4(), target_ip, 445)
        connection.connect(Dialects.SMB_3_0_2)

        # Start a session
        session = Session(connection, username="ansible", password="P@ssw0rd!")
        session.connect()

        print("True")
    except Exception as e:
        print("False")
    finally:
        if 'connection' in locals():
            connection.disconnect(True)

if __name__ == "__main__":
    target_ip = "172.16.2.1" 
    check_smb(target_ip)

