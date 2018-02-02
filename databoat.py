# Carol Joplin
# Emma Delucchi
# project.py
# Databoat

import mysql.connector
import config

def displayMenu():
	while True:
		print ""
		print "1. Athlete Information\n2. Workout by Date\n3. Workout by Type\n4. PRs (2k, 6k, 10k)\n5. More Options\n6. Exit"
		print ""
		choice = int(raw_input("What would you like to do? "))

		if choice == 1:
			athleteInformation()
		if choice == 2:
			workoutByDate()
		if choice == 3:
			workoutByType()
		if choice == 4:
			pr()
		if choice == 5:
			more()
		if choice == 6:
			quit()
		else:
			print "Not a valid choice. Please enter any number and try again"

def athleteInformation():
	try:
		# connection info
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = 'cjoplin_DB'

		# take user input
		choice = raw_input("A. Display All Athlete Information\nB. Display Specific Athlete Information\nC. Display Fastest Athlete Test Time\D. Add an Athlete\nE. Return to main menu\nWhat would you like to do (A-D): ")
		# Fastest Time Query: SELECT a.first_name, a.last_name, MIN(t.total_time) FROM athlete a JOIN test t ON (a.athlete_id = t.athlete) GROUP BY t.total_time LIMIT 1
		# Selects all details about an athlete
		# Functional as of Fri 12/8 9:46pm
		if choice == 'A':
			# create a connection
			con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

			# create the result set
                        rsA = con.cursor()

			queryA = 'SELECT * FROM athlete'

			rsA.execute(queryA)

			for (athlete_id, first_name, last_name, weight, team) in rsA:
                                print 'ID: {}\nAthlete: {} {}\nWeight: {}\nTeam: {}\n'.format(athlete_id, first_name, last_name, weight, team)
                        rsA.close()
                        con.close()
                        displayMenu()
			print ""

		if choice == 'B':
			# create a connection
			con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

			# create the result set
			rsB = con.cursor()

			# get athlete details from user
			user_first = raw_input("First Name: ")
			user_last = raw_input("Last Name: ")
			print ""

			# gets all athlete details from athlete table
			query = 'SELECT first_name, last_name, athlete_id, weight, team FROM athlete WHERE first_name=%s AND last_name=%s'

			rsB.execute(query, (user_first, user_last))

			# print the results
			# prints one entry three times
			# prints "Not a valid choice. Please enter any number and try again"
			for (first_name, last_name, athlete_id, weight, team) in rsB:
				print 'Athlete: {} {}\nID: {}\nWeight: {}\nTeam (T/F): {}\n'.format(first_name, last_name, athlete_id, weight, team)
			rsB.close()
			con.close()
			displayMenu()
			print ""

		if choice == 'C':
			# create a connection
			con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

			# take user input on athlete details
			user_id = raw_input("Athlete ID: ")
			user_first = raw_input("First Name: ")
			user_last = raw_input("Last Name: ")
			user_height = raw_input("Weight: ")
			user_team = raw_input("Team (1/0): ")

			# create the id flag
			athlete_flag = False

			# create the first result set
			rsC1 = con.cursor()

			# query to determine if entered athlete is in the database
			query1 = 'SELECT athlete_id, first_name FROM athlete'

			# execute the query
			rsC1.execute(query1)

			# determine if entered athlete is in the database
			# not setting code flag to true when taking in an athlete already in table
			for athlete_id, first_name in rsC1:
				if athlete_id == user_id:
					athlete_flag = True
			rsC1.close()

			if athlete_flag == True:
				print "Athlete already in database"
			else:
				try:
					# create a new connection for second query
					rsC2 = con.cursor()

					# insert the athlete into the database
					insert = 'INSERT INTO athlete VALUES(%s, %s, %s, %s)'

					# let user know athlete was successfully added
					print "Athlete Added!"
					print ""
					con.commit()
					rsC2.close()
				except mysql.connector.Error as err:
					print err

			con.close()
			displayMenu()
			print ""

		if choice == 'D':
			displayMenu()
			print ""

	except mysql.connector.Error as err:
		print err

def workoutByDate():
	try:
		# connection info
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = 'cjoplin_DB'

		# create a connection
		con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

		# create the result set
		rsD = con.cursor()

		# get athlete date from user
		user_date = raw_input("Date (YYYY-MM-DD): ")

		# create and execute the query
		queryD = "SELECT a.first_name, a.last_name, t.test_date, t.workout_type FROM athlete a JOIN test t ON (a.athlete_id = t.athlete) WHERE t.test_date = %s"

		rsD.execute(queryD, (user_date))

		# print the results
		for first_name, last_name, test_date, workout_type in rsD:
			 print 'Athlete: {} {}\nDate: {}\nWorkout Type: {}\n'.format(first_name, last_name, test_date, workout_type)

		rsD.close()
		con.close()
		displayMenu()

	except mysql.connector.Error as err:
		print err
 
def workoutByType():
	try:
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = 'cjoplin_DB'

                # create a connection
                con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

                # create the result set
                rs = con.cursor()

		user_type = raw_input("Workout Type: ")

                query = "SELECT workout_type, workout_name, length_duration FROM workout_type WHERE workout_type = %s"

		rs.execute(query, (user_type))
		# prints up to here

		# this for loop isn't working
                for workout_type, workout_name, length_duration in rs:
               		print "Workout Type: {}\nWorkout Name: {}\nWorkout Duration: {}\n".format(workout_type, workout_name, length_duration)
               		#print "inside type for"
		# prints right here
		rs.close()
                con.close()
                displayMenu()
		print ""

	except mysql.connector.Error as err:
		print err

def more():
	try:
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = 'cjoplin_DB'

		choice = raw_input("A. Display Top Athletes by Workout Split\nB. Display Top Athletes by Date\nC. Display Top Athletes by Workout Type\nD. Find Athletes Who Just PR'ed\nWhat would you like to do (A-D): ")

		if choice == 'A':
			con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)
			rsA = con.cursor()

			# take user input for split and workout
			user_split = raw_input("Athletes Faster than Split: ")
			user_workout = raw_input("On Workout Type: ")

			queryA = 'SELECT a.athlete_id, a.first_name, a.last_name, wt.workout_name, t.average_split, t.total_time FROM workout_type wt JOIN test t USING (workout_type) JOIN athlete a ON a.athlete_id = t.athlete WHERE t.average_split < \'%s\' AND wt.workout_name = \'%s\''

			rsA.execute(queryA, (user_split, user_workout))

			for athlete_id, first_name, last_name, workout_type, average_split, total_time in rsA:
				print 'Athlete ID: {}\nAthlete: {} {}\nWorkout: {}\nSplit: {}\nTime: {}\n'.format(athlete_id, first_name, last_name, workout_type, average_split, total_time)
			rsA.close()
			con.close()
			displayMenu()

		if choice == 'B':
			con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)
			rsB = con.cursor()

			user_date = raw_input("Test Date: ")

			queryB = 'SELECT a.athlete_id, a.first_name, a.last_name, wt.workout_name, t.test_date, t.total_time FROM workout_type wt JOIN test t USING (workout_type) JOIN athlete a ON a.athlete_id = t.athlete WHERE t.test_date = \'%s\''

			rsB.execute(queryB, (user_date))

			for athlete_id, first_name, last_name, workout_name, test_date, total_time in rsB:
				print 'Athlete ID: {}\nAthlete: {} {}\nWorkout: {}\nTest Date: {}\nTime: {}\n'

			rsB.close()
			con.close()
			displayMenu()

		# prints one time, one athlete name and all three workout types
		if choice == 'C':
			con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)
			rsC = con.cursor()

			queryC = 'SELECT DISTINCT a.athlete_id, a.first_name, a.last_name, wt.workout_name, t.total_time FROM workout_type wt JOIN test t USING (workout_type) JOIN athlete a ON a.athlete_id = t.athlete GROUP BY a.athlete_id, a.first_name, a.last_name, wt.workout_name, t.total_time HAVING COUNT(*) <= ALL (SELECT COUNT(DISTINCT t.total_time) FROM workout_type wt JOIN test t USING (workout_type) JOIN athlete a ON a.athlete_id = t.athlete GROUP BY t.total_time)'

			rsC.execute(queryC)

			for athlete_id, first_name, last_name, workout_name, total_time in rsC:
				print 'Athlete ID: {}\nAthlete: {} {}\nWorkout: {}\nTime: {}\n'.format(athlete_id, first_name, last_name, workout_name, total_time)
			rsC.close()
			con.close()
			displayMenu()
		if choice == 'D':
			con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

			rsD = con.cursor()

			queryD = 'SELECT a.first_name, a.last_name, FROM athlete a JOIN workout'

	except mysql.connector.Error as err:
		print err

def main():
	displayMenu()

if __name__ == '__main__':
	main()
