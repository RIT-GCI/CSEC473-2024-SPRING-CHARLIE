#!/bin/python3
# importing required libraries
import mysql.connector

def team_two():
    try:
        dataBase = mysql.connector.connect(
          host ="192.168.2.4",
          user ="Greyteam",
          passwd ="P@ssw0rd!",
          connection_timeout =2
        )
        dataBase.close()
        return True
    except:
        return False

print(team_two())
