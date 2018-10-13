#! usr/bin/python
# ----------------------------------------------------------------------------------------------
# FYP - Fuck You Phisher
#
# this tool sends fake data to phishers' websites. Read the Readme.md file to know more.
#
# Author :  Mirko Viviano , version 1.0
# ----------------------------------------------------------------------------------------------
import requests
import glob
from itertools import zip_longest
import random
import string

#global params
url = ''
emailField = ''
passwordField = ''
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
firstnames_list = []
lastnames_list = []
providers_list = []


# generates a first names array
def get_firstnames_list():
    global firstnames_list
    firstnames_file = open("first_names_list.txt", "r")
    for fn in firstnames_file:
        firstnames_list.append(fn.strip().lower())
    
    return(firstnames_list)

# generates a first names array
def get_lastnames_list():
    global lastnames_list
    lastnames_file = open("last_names_list.txt", "r")
    for ln in lastnames_file:
        lastnames_list.append(ln.strip().lower())
    
    return(lastnames_list)

# generates a providers array
def get_providers_list():
    global providers_list
    providers_file = open("providers_list.txt", "r")
    for ln in providers_file:
        providers_list.append(ln.strip().lower())
    
    return(providers_list)

# define emailField, passwordField and url
def getParams():
	global emailField, passwordField, url
	emailField = input("Enter email field name...\n")
	passwordField = input("Enter password field name...\n")
	url = input("Enter website url (e.g. http(s)://website.com\n")

def main():
	global chars, emailField, passwordField, url
	get_firstnames_list()
	get_lastnames_list()
	get_providers_list()

	for i in range(0, 3000): #choose how many users you want to send
		email = "{}{}@{}".format(random.choice(firstnames_list), random.choice(lastnames_list), random.choice(providers_list))
		password = ''.join(random.choice(chars) for i in range(random.randint(8, 15)))

		r = requests.post(url, data = {
			emailField: email,
			passwordField: password
		})

		print("Sending request with email {} and password {} -- {} / {}".format(email, password, r.status_code, r.reason))


if __name__ == '__main__':
	getParams()
	main()