from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Function to fetch information and calculate scores
def get_information():
    # Initialize variables to store team status and scores
    team1_status = {}
    team2_status = {}
    team1_score = 0
    team2_score = 0

    # Read data from the UPTIME.txt file
    with open('UPTIME.txt', 'r') as file:
        lines = file.readlines()

    # Extract team status from the file contents
    for line in lines:
        line = line.strip()
        if line.startswith('['):  # Team status line
            team_name, status = line[1:].split(': ')
            status = status.split()[0]
            if 'Team 1' in team_name:
                team1_status[team_name.split()[0]] = status
            elif 'Team 2' in team_name:
                team2_status[team_name.split()[0]] = status
        elif line.startswith('Team 1 Score:'):
            team1_score = int(line.split(': ')[1])
        elif line.startswith('Team 2 Score:'):
            team2_score = int(line.split(': ')[1])

    return team1_status, team2_status, team1_score, team2_score

@app.route('/')
def index():
    team1_status, team2_status, team1_score, team2_score = get_information()
    return render_template('index.html', team1_status=team1_status, team2_status=team2_status, team1_score=team1_score, team2_score=team2_score)

@app.route('/data')
def get_data():
    team1_status, team2_status, team1_score, team2_score = get_information()
    return jsonify({
        'team1_status': team1_status,
        'team2_status': team2_status,
        'team1_score': team1_score,
        'team2_score': team2_score
    })

if __name__ == '__main__':
    app.run(debug=True)

