#!/bin/python3
# importing required libraries
import mysql.connector

def team_one():
    try:
        dataBase = mysql.connector.connect(
          host ="192.168.1.4",
          user ="Greyteam",
          passwd ="P@ssw0rd!",
          connection_timeout =1
        )
        dataBase.close()
        return True
    except:
        return False

def team_two():
    try:
        dataBase = mysql.connector.connect(
          host ="192.168.2.4",
          user ="Greyteam",
          passwd ="P@ssw0rd!",
          connection_timeout =1
        )
        dataBase.close()
        return True
    except:
        return False

print("Team1:",team_one())
print("Team2:",team_two())
