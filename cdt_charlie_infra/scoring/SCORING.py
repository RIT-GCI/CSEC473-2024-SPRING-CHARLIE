# SCORING.py
import time
import subprocess
from datetime import datetime

t1initial = int(input("Initial points for team 1:"))
t2initial = int(input("Initial points for team 2:"))
scoreround = int(input("Initial round: "))
input("Press any key to start the scoring engine")

service_scores = {
	"DNS/AD": 1,
	"Shop": 3,
	"SMTP": 1,
	"MySQL": 1,
	"SSH": 1,
	"HTTP": 1,
	"SMB": 1,
	"FTP": 1
}

team_scores = {
	"Team 1": t1initial,
	"Team 2": t2initial
}
# Function to read UPTIME.txt and update scores
def update_scores():
	# Read UPTIME.txt
	with open("UPTIME.txt", "r") as uptime_file:
		lines = uptime_file.readlines()

		# Parse each line
		for line in lines:
			line = line.strip()
			if line.startswith("["):
				parts = line.split()
				service = parts[0][1:]
				team = "Team " + parts[2][0]  # Get team number
				status = parts[3]  # Get status
				if status == "UP✅":
					team_scores[team] += service_scores.get(service, 0)
				print(team + " " + service + ": " + status)

	# Print updated scores
	print("\nTeam Scores:")
	for team, score in team_scores.items():
		print(f"{team}: {score} points")

def update_service_status(service_name, team_name, new_status):
	# Read UPTIME.txt
	with open("UPTIME.txt", "r") as uptime_file:
		lines = uptime_file.readlines()

	# Find and update the specified service's status
	updated_lines = []
	for line in lines:
		if line.startswith(f"[{service_name} {team_name}]:"):
			updated_line = f"[{service_name} {team_name}]: {new_status}\n"
			updated_lines.append(updated_line)
		else:
			updated_lines.append(line)

	# Write the updated lines back to UPTIME.txt
	with open("UPTIME.txt", "w") as uptime_file:
		uptime_file.writelines(updated_lines)

def update_team_scores(team1_score, team2_score):
	# Read UPTIME.txt
	with open("UPTIME.txt", "r") as uptime_file:
		lines = uptime_file.readlines()

	# Find and update the lines containing team scores
	updated_lines = []
	for line in lines:
		if line.startswith("Team 1 Score:"):
			updated_line = f"Team 1 Score: {team1_score}\n"
			updated_lines.append(updated_line)
		elif line.startswith("Team 2 Score:"):
			updated_line = f"Team 2 Score: {team2_score}\n"
			updated_lines.append(updated_line)
		else:
			updated_lines.append(line)

	# Write the updated lines back to UPTIME.txt
	with open("UPTIME.txt", "w") as uptime_file:
		uptime_file.writelines(updated_lines)

def get_current_timestamp():
	# Get the current date and time
	timestamp = datetime.now()
	return timestamp

# Run update_scores function
while True:

	#DNS
	try:
		DNSresult1 = subprocess.run(['python3', 'dns1.py'], stdout=subprocess.PIPE, timeout=5)
		if DNSresult1.returncode != 0:
			update_service_status("DNS/AD", "Team 1", "DOWN💀")
		elif DNSresult1.stdout.decode().strip() == "True":
			update_service_status("DNS/AD", "Team 1", "UP✅")
		else:
			update_service_status("DNS/AD", "Team 1", "DOWN💀")
	except Exception as e:
		update_service_status("DNS/AD", "Team 1", "DOWN💀")
	try:
		DNSresult2 = subprocess.run(['python3', 'dns2.py'], stdout=subprocess.PIPE, timeout=5)
		if DNSresult2.returncode != 0:
			update_service_status("DNS/AD", "Team 2", "DOWN💀")
		elif DNSresult2.stdout.decode().strip() == "True":
			update_service_status("DNS/AD", "Team 2", "UP✅")
		else:
			update_service_status("DNS/AD", "Team 2", "DOWN💀")
	except Exception as e:
		update_service_status("DNS/AD", "Team 2", "DOWN💀")

	#SHOP
#	try:
#		SHOPresult1 = subprocess.run(['python3', 'shop1.py'], stdout=subprocess.PIPE, timeout=5)
#		if SHOPresult1.returncode != 0:
#			update_service_status("Shop", "Team 1", "DOWN💀")
#		elif SHOPresult1.stdout.decode().strip() == "True":
#			update_service_status("Shop", "Team 1", "UP✅")
#		else:
#			update_service_status("Shop", "Team 1", "DOWN💀")
#	except Exception as e:
#		update_service_status("Shop", "Team 1", "DOWN💀")
#	try:
#		SHOPresult2 = subprocess.run(['python3', 'shop2.py'], stdout=subprocess.PIPE, timeout=5)
#		if SHOPresult2.returncode != 0:
#			update_service_status("Shop", "Team 2", "DOWN💀")
#		elif SHOPresult2.stdout.decode().strip() == "True":
#			update_service_status("Shop", "Team 2", "UP✅")
#		else:
#			update_service_status("Shop", "Team 2", "DOWN💀")
#	except Exception as e:
#		update_service_status("Shop", "Team 2", "DOWN💀")

	#SMTP
	try:
		SMTPresult1 = subprocess.run(['python3', 'smtp1.py'], stdout=subprocess.PIPE, timeout=5)
		if SMTPresult1.returncode != 0:
			update_service_status("SMTP", "Team 1", "DOWN💀")
		elif SMTPresult1.stdout.decode().strip() == "True":
			update_service_status("SMTP", "Team 1", "UP✅")
		else:
			update_service_status("SMTP", "Team 1", "DOWN💀")
	except Exception as e:
		update_service_status("SMTP", "Team 1", "DOWN💀")
	try:
		SMTPresult2 = subprocess.run(['python3', 'smtp2.py'], stdout=subprocess.PIPE, timeout=5)
		if SMTPresult2.returncode != 0:
			update_service_status("SMTP", "Team 2", "DOWN💀")
		elif SMTPresult2.stdout.decode().strip() == "True":
			update_service_status("SMTP", "Team 2", "UP✅")
		else:
			update_service_status("SMTP", "Team 2", "DOWN💀")
	except Exception as e:
		update_service_status("SMTP", "Team 2", "DOWN💀")

	#MYSQL
	try:
		MYSQLresult1 = subprocess.run(['python3', 'mysql1.py'], stdout=subprocess.PIPE, timeout=5)
		if MYSQLresult1.returncode != 0:
			update_service_status("MySQL", "Team 1", "DOWN💀")
		elif MYSQLresult1.stdout.decode().strip() == "True":
			update_service_status("MySQL", "Team 1", "UP✅")
		else:
			update_service_status("MySQL", "Team 1", "DOWN💀")
	except Exception as e:
		update_service_status("MySQL", "Team 1", "DOWN💀")
	try:
		MYSQLresult2 = subprocess.run(['python3', 'mysql2.py'], stdout=subprocess.PIPE, timeout=5)
		if MYSQLresult2.returncode != 0:
			update_service_status("MySQL", "Team 2", "DOWN💀")
		elif MYSQLresult2.stdout.decode().strip() == "True":
			update_service_status("MySQL", "Team 2", "UP✅")
		else:
			update_service_status("MySQL", "Team 2", "DOWN💀")
	except Exception as e:
		update_service_status("MySQL", "Team 2", "DOWN💀")

	#SSH
	try:
		SSHresult1 = subprocess.run(['python3', 'ssh1.py'], stdout=subprocess.PIPE, timeout=5)
		if SSHresult1.returncode != 0:
			update_service_status("SSH", "Team 1", "DOWN💀")
		elif SSHresult1.stdout.decode().strip() == "True":
			update_service_status("SSH", "Team 1", "UP✅")
		else:
			update_service_status("SSH", "Team 1", "DOWN💀")
	except Exception as e:
		update_service_status("SSH", "Team 1", "DOWN💀")
	try:
		SSHresult2 = subprocess.run(['python3', 'ssh2.py'], stdout=subprocess.PIPE, timeout=5)
		if SSHresult2.returncode != 0:
			update_service_status("SSH", "Team 2", "DOWN💀")
		elif SSHresult2.stdout.decode().strip() == "True":
			update_service_status("SSH", "Team 2", "UP✅")
		else:
			update_service_status("SSH", "Team 2", "DOWN💀")
	except Exception as e:
		update_service_status("SSH", "Team 2", "DOWN💀")

	#HTTP
	try:
		HTTPresult1 = subprocess.run(['python3', 'http1.py'], stdout=subprocess.PIPE, timeout=5)
		if HTTPresult1.returncode != 0:
			update_service_status("HTTP", "Team 1", "DOWN💀")
		elif HTTPresult1.stdout.decode().strip() == "True":
			update_service_status("HTTP", "Team 1", "UP✅")
		else:
			update_service_status("HTTP", "Team 1", "DOWN💀")
	except Exception as e:
		update_service_status("HTTP", "Team 1", "DOWN💀")
	try:
		HTTPresult2 = subprocess.run(['python3', 'http2.py'], stdout=subprocess.PIPE, timeout=5)
		if HTTPresult1.returncode != 0:
			update_service_status("HTTP", "Team 2", "DOWN💀")
		elif HTTPresult2.stdout.decode().strip() == "True":
			update_service_status("HTTP", "Team 2", "UP✅")
		else:
			update_service_status("HTTP", "Team 2", "DOWN💀")
	except Exception as e:
		update_service_status("HTTP", "Team 2", "DOWN💀")

	#SMB
	try:
		SMBresult1 = subprocess.run(['python3', 'smb1.py'], stdout=subprocess.PIPE, timeout=5)
		if SMBresult1.returncode != 0:
			update_service_status("SMB", "Team 1", "DOWN💀")
		elif SMBresult1.stdout.decode().strip() == "True":
			update_service_status("SMB", "Team 1", "UP✅")
		else:
			update_service_status("SMB", "Team 1", "DOWN💀")
	except Exception as e:
		update_service_status("SMB", "Team 1", "DOWN💀")
	try:
		SMBresult2 = subprocess.run(['python3', 'smb2.py'], stdout=subprocess.PIPE, timeout=5)
		if SMBresult2.returncode != 0:
			update_service_status("SMB", "Team 2", "DOWN💀")
		elif SMBresult2.stdout.decode().strip() == "True":
			update_service_status("SMB", "Team 2", "UP✅")
		else:
			update_service_status("SMB", "Team 2", "DOWN💀")
	except Exception as e:
		update_service_status("SMB", "Team 2", "DOWN💀")

	#FTP
	try:
		FTPresult1 = subprocess.run(['python3', 'ftp1.py'], stdout=subprocess.PIPE, timeout=5)
		if FTPresult1.returncode != 0:
			update_service_status("FTP", "Team 1", "DOWN💀")
		elif FTPresult1.stdout.decode().strip() == "True":
			update_service_status("FTP", "Team 1", "UP✅")
		else:
			update_service_status("FTP", "Team 1", "DOWN💀")
	except Exception as e:
		update_service_status("FTP", "Team 1", "DOWN💀")
	try:
		FTPresult2 = subprocess.run(['python3', 'ftp2.py'], stdout=subprocess.PIPE, timeout=5)
		if FTPresult2.returncode != 0:
			update_service_status("FTP", "Team 2", "DOWN💀")
		elif FTPresult2.stdout.decode().strip() == "True":
			update_service_status("FTP", "Team 2", "UP✅")
		else:
			update_service_status("FTP", "Team 2", "DOWN💀")
	except Exception as e:
		update_service_status("FTP", "Team 2", "DOWN💀")


	print("ROUND " + str(scoreround) + " " + str(get_current_timestamp()))
	update_scores()
	update_team_scores(team_scores.get("Team 1"), team_scores.get("Team 2"))
	scoreround += 1
	time.sleep(3) #Scores are set so default should be 36, 32 might work  there is ~ a 4 second delay
