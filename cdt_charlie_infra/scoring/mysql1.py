#!/bin/python3
# importing required libraries
import mysql.connector

def team_one():
    try:
        dataBase = mysql.connector.connect(
          host ="192.168.1.4",
          user ="Greyteam",
          passwd ="P@ssw0rd!",
          connection_timeout =2
        )
        dataBase.close()
        return True
    except:
        return False

print(team_one())

