# PAX v0.6
# Password generator / profiler
# Video by Fukrey Hacker's Team: https://youtu.be/1pBMvFmqm7U
#
# Good wordlist: www.wpwhitesecurity.com/downloads/wpw_pwd_dictionary.zip

import argparse

def logo():
	print("PAX v0.6              ")
        print("By MichaelDim.")
def interface():
	print("-s Start   -i Info")
def about():
	print("PAX Generator 0.6 - Simple Password List Generation Tool v0.6")
	print("MichaelDim // Greece // 2017\n\n")
	print("This tool creates a dictionary / wordlist with simple passwords based on the information that you have.")
	print("Later the wordlist can be used to crack down the victim's password. (With another piece of software)")
	print("This tool is not meant to create every possible password, but instead a small list of the most likely ones.\n")
	print("Passwords will be exported into a txt file with filename the name of the victim. If there already is a file with that name. it will get replaced")
	print("If the field is not required you can hit space to skip it. However, if it is required (There is a [r]) then it cannot be left blank\n")
	print("It is reocmmened that you write only in lower case, since most passwords do not contain capital letters. Ctrl+C to exit.")
	print("Video by Fukrey Hacker's Team: https://youtu.be/1pBMvFmqm7U\n\n")
def InfoCol():
	name = raw_input("[?] [r] Name: ")
	last_name = raw_input("[?] [r] Last name: ")
	birthday = raw_input("[?] Birthday (DDMMYYYY): ")
	year = raw_input("[?] Year of birth: ")
	number1 = raw_input("[?] Phone number: ")
	kw_str = raw_input("[?] [r] Keywords (with commas/no spaces - Required at least one): ")
	kw_list = kw_str.split(",")
	limit = raw_input("[?] [r] Limit for numbers after the keywords: ")
	limit = int(limit)
	bool_dots = raw_input("[?] [r] Include dots (.)? [y/n]: ")
	if bool_dots == "y":
		dots = True
	else:
		dots = False
	bool_dashes = raw_input("[?] [r] Include dashes (-)? [y/n]: ")
	if bool_dashes == "y":
		dashes = True
	else:
		dashes = False
	bool_unders = raw_input("[?] [r] Include underscores (_)? [y/n]: ")
	if bool_unders == "y":
		unders = True
	else:
		unders = False
	generator(name,last_name,birthday,year,number1,kw_list, limit, dots, unders, dashes)
def generator(name,last_name,birthday,year,number1,kw_list, limit, dots, unders, dashes):
	#OPENING THE FILE#
	f = open(str(name) ,'w+')
	#GENERATOR#
	f.write(str(name) + "\n")
	f.write(str(last_name) + "\n")
	name_sur = name + last_name + "\n"
	if birthday != "":
		f.write(str(birthday) + "\n")
		name_birthday = name + birthday	+ "\n"
		name_sur_bday = name + last_name + birthday + "\n"
		f.write(str(name_birthday))
		f.write(str(name_sur_bday))
		if dots == True:
			name_birthday_with_dot = name + "." + birthday	+ "\n"
			name_sur_bday_with_dot = name + "." + last_name + birthday + "\n"
			f.write(str(name_birthday_with_dot))
			f.write(str(name_sur_bday_with_dot))
		if unders == True:
			name_birthday_with_us = name + "_" + birthday	+ "\n"
			name_sur_bday_with_us = name + "_" + last_name + birthday + "\n"
			f.write(str(name_birthday_with_us))
			f.write(str(name_sur_bday_with_us))
		if dashes == True:
			name_birthday_with_dash = name + "-" + birthday	+ "\n"
			name_sur_bday_with_dash = name + "-" + last_name + birthday + "\n"
			f.write(str(name_birthday_with_dash))
			f.write(str(name_sur_bday_with_dash))
	if year != "":
		name_sur_year = name + last_name + year + "\n"
		sur_year = last_name + year + "\n"
		sur_birthday = last_name + year + "\n"
		f.write(str(year) + "\n")
		name_year = name + year	+ "\n"
		f.write(str(name_sur_year))
		f.write(str(name_year))
		f.write(str(sur_year))
		if dots == True:
			name_sur_year_dot_1 = name + "." + last_name + year + "\n"
			name_sur_year_dot_2 = name + last_name + "." + year + "\n"
			name_sur_year_dot_3 = name + "." + last_name + "." + year + "\n"
			f.write(str(name_sur_year_dot_1))
			f.write(str(name_sur_year_dot_2))
			f.write(str(name_sur_year_dot_3))
		if unders == True:
			name_sur_year_us_1 = name + "_" + last_name + year + "\n"
			name_sur_year_us_2 = name + last_name + "_" + year + "\n"
			name_sur_year_us_3 = name + "_" + last_name + "_" + year + "\n"
			f.write(str(name_sur_year_us_1))
			f.write(str(name_sur_year_us_2))
			f.write(str(name_sur_year_us_3))
		if dashes == True:
			name_sur_year_dash_1 = name + "-" + last_name + year + "\n"
			name_sur_year_dash_2 = name + last_name + "-" + year + "\n"
			name_sur_year_dash_3 = name + "-" + last_name + "-" + year + "\n"
			f.write(str(name_sur_year_dash_1))
			f.write(str(name_sur_year_dash_2))
			f.write(str(name_sur_year_dash_3))
		sur_year = last_name + year + "\n"
		sur_birthday = last_name + year + "\n"
		f.write(str(sur_year))
		f.write(str(sur_birthday))
	if number1 != "":
		f.write(str(number1) + "\n")
		name_sur_num = name + last_name + number1 + "\n"
		name_num = name + number1 + "\n"
		f.write(str(name_num))
		sur_num = last_name + number1 + "\n"
		f.write(str(name_sur_num))
		f.write(str(name_sur_num))
		if dots == True:
			name_num_dot = name + "." + number1 + "\n"
			sur_num_dot = last_name + "." + number1 + "\n"
			f.write(str(name_num_dot))
			f.write(str(sur_num_dot))	
		if unders == True:
			sur_num_us = last_name + "_" + number1 + "\n"
			name_num_us = name + "_" + number1 + "\n"
			f.write(str(name_num_us))
			f.write(str(sur_num_us))
		if dashes == True:
			sur_num_dash = last_name + "-" + number1 + "\n"
			name_num_dash = name + "-" + number1 + "\n"
			f.write(str(name_num_dash))
			f.write(str(sur_num_dash))
	f.write(str(name_sur))
	for item in kw_list:
		f.write(item + last_name + "\n")
		f.write(item + name + "\n")
		f.write(name + item + "\n")
		f.write(last_name + item + "\n")
		if unders == True:
			f.write(item + "_" + name + "\n")
			f.write(item + "_" + last_name + "\n")
			f.write(name + "_" + item + "\n")
			f.write(last_name + "_" + item + "\n")
		if dashes == True:
			f.write(item + "-" + name + "\n")
			f.write(item + "-" + last_name + "\n")
			f.write(name + "-" + item + "\n")
			f.write(last_name + "-" + item + "\n")
		if dots == True:
			f.write(name + "." + item + "\n")
			f.write(item + "." + name + "\n")
			f.write(item + "." + last_name + "\n")
			f.write(last_name + "." + item + "\n")
	for item in kw_list:
        	f.write(item + "\n")
		if birthday != "":
			f.write(item + birthday + "\n")
		if year != "":
			f.write(item + year + "\n")
	num = 0
	for item in kw_list:
		if number1 != "":
			f.write(item + number1 + "\n")
		if year != "":
			f.write(item + year + "\n")
		if birthday != "":
			f.write(item + birthday + "\n")
	while (num <= limit):
			f.write(name + str(num) + "\n")
			num = num + 1
	num = 0
	while (num <= limit):
		f.write(last_name + str(num) + "\n")
		num = num + 1
	num = 0
	for item in kw_list:
		while (num <= limit):
			f.write(item + str(num) + "\n")
			num = num + 1
	num = 0
	for item in kw_list:
		while (num <= limit):
			f.write(item + last_name + str(num) + "\n")
			num = num + 1
	num = 0
	for item in kw_list:
		while (num <= limit):
			f.write(item + name + str(num) + "\n")
			num = num + 1
	num = 0
	if len(kw_list) > 0:
        	for item in kw_list:
        	        for item_ in kw_list:
				f.write(item + item_ + "\n")
				while (num <= limit):
        	                	f.write(item + item_ + str(num) + "\n")
        	                	num += 1
        			num = 0

# WITH DOTS
	if dots == True:
		for item in kw_list:
	        	f.write(item + "\n")
			if birthday != "":
				f.write(item + "." + birthday + "\n")
			if year != "":
				f.write(item + "." + year + "\n")
		num = 0
		for item in kw_list:
			if number1 != "":
				f.write(item + "." + number1 + "\n")
			if year != "":
				f.write(item + "." + year + "\n")
			if birthday != "":
				f.write(item + "." + birthday + "\n")
		while (num <= limit):
				f.write(name + "." + str(num) + "\n")
				num = num + 1
		num = 0
		while (num <= limit):
			f.write(last_name + "." + str(num) + "\n")
			num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + "." + str(num) + "\n")
				num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + "." + last_name + str(num) + "\n")
				f.write(item + last_name + "." + str(num) + "\n")
				f.write(item + "." + last_name + "." + str(num) + "\n")
				num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + name + str(num) + "\n")
				f.write(item + "." + name + "." +str(num) + "\n")
				f.write(item + name + "." + str(num) + "\n")
				f.write(item + "." + name + str(num) + "\n")
				num = num + 1
		num = 0
		if len(kw_list) > 0:
	        	for item in kw_list:
	        	        for item_ in kw_list:
					f.write(item + item_ + "\n")
					while (num <= limit):
	        	                	f.write(item + "." + item_ + "." + str(num) + "\n")
						f.write(item + "." + item_ + str(num) + "\n")
						f.write(item + item_ + "." + str(num) + "\n")
	        	                	num += 1
	        			num = 0

# WITH DASHES 
	if dashes == True:
		for item in kw_list:
	        	f.write(item + "\n")
			if birthday != "":
				f.write(item + "-" + birthday + "\n")
			if year != "":
				f.write(item + "-" + year + "\n")
		num = 0
		for item in kw_list:
			if number1 != "":
				f.write(item + "-" + number1 + "\n")
			if year != "":
				f.write(item + "-" + year + "\n")
			if birthday != "":
				f.write(item + "-" + birthday + "\n")
		while (num <= limit):
				f.write(name + "-" + str(num) + "\n")
				num = num + 1
		num = 0
		while (num <= limit):
			f.write(last_name + "-" + str(num) + "\n")
			num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + "-" + str(num) + "\n")
				num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + "-" + last_name + str(num) + "\n")
				f.write(item + last_name + "-" + str(num) + "\n")
				f.write(item + "-" + last_name + "-" + str(num) + "\n")
				num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + name + str(num) + "\n")
				f.write(item + "-" + name + "-" +str(num) + "\n")
				f.write(item + name + "-" + str(num) + "\n")
				f.write(item + "-" + name + str(num) + "\n")
				num = num + 1
		num = 0
		if len(kw_list) > 0:
	        	for item in kw_list:
	        	        for item_ in kw_list:
					f.write(item + item_ + "\n")
					while (num <= limit):
	        	                	f.write(item + "-" + item_ + "-" + str(num) + "\n")
						f.write(item + "-" + item_ + str(num) + "\n")
						f.write(item + item_ + "-" + str(num) + "\n")
	        	                	num += 1
	        			num = 0
	# WITH UNDERSCORES
	if unders == True:
		for item in kw_list:
	        	f.write(item + "\n")
			if birthday != "":
				f.write(item + "_" + birthday + "\n")
			if year != "":
				f.write(item + "_" + year + "\n")
		num = 0
		for item in kw_list:
			if number1 != "":
				f.write(item + "_" + number1 + "\n")
			if year != "":
				f.write(item + "_" + year + "\n")
			if birthday != "":
				f.write(item + "_" + birthday + "\n")
		while (num <= limit):
				f.write(name + "_" + str(num) + "\n")
				num = num + 1
		num = 0
		while (num <= limit):
			f.write(last_name + "_" + str(num) + "\n")
			num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + "_" + str(num) + "\n")
				num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + "_" + last_name + str(num) + "\n")
				f.write(item + last_name + "_" + str(num) + "\n")
				f.write(item + "_" + last_name + "_" + str(num) + "\n")
				num = num + 1
		num = 0
		for item in kw_list:
			while (num <= limit):
				f.write(item + name + str(num) + "\n")
				f.write(item + "_" + name + "_" +str(num) + "\n")
				f.write(item + name + "_" + str(num) + "\n")
				f.write(item + "_" + name + str(num) + "\n")
				num = num + 1
		num = 0
		if len(kw_list) > 0:
	        	for item in kw_list:
	        	        for item_ in kw_list:
					f.write(item + item_ + "\n")
					while (num <= limit):
	        	                	f.write(item + "_" + item_ + "_" + str(num) + "\n")
						f.write(item + "_" + item_ + str(num) + "\n")
						f.write(item + item_ + "_" + str(num) + "\n")
	        	                	num += 1
	        			num = 0
	print("[+] Passwords exported at " + name)
parser = argparse.ArgumentParser()
parser.add_argument("-s", help="Start", action="store_true")
parser.add_argument("-i", help="Info", action="store_true")
logo()
if parser.parse_args().s:
	InfoCol()
elif parser.parse_args().i:
	about()
else:
	interface()
