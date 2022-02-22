import os 
import csv
import time
import random






def login_or_exit():
	log_or_ex=input("To log in, enter \"Login\". To log out, enter \"Exit\":\n").lower().strip()
	os.system("cls||clear")

	while True:
		if log_or_ex=="login":
			log_in_system()
			break

		elif log_or_ex=="exit":  
			print("The program is completed!") 
			break

		else:
			print("Error! Try again!") 
			login_or_exit()
			break






def csv_reader(filename):       
	with open(filename) as File:          
		reader=csv.DictReader(File, delimiter=",") 
		info_array=[]

		for row in reader:
			info_array.append(row)

	return info_array






def csv_dictreader(filename):
	with open(filename) as File:
		reader=csv.DictReader(File, delimiter=",")
		info_dict={}

		for row in reader:
			name=row.get("Full name")
			info_dict.setdefault(name, row)
			
	return info_dict






def log_in_system():
	global fullname, account_type
	fullname=None
	fails=0
	check=False
	
	while True:
		account_type=input("Select your account type:\n1) HR-Manager\n2) Worker\n3) Director\n").lower().strip() 
		if account_type=="1":
			account_type="hr-manager"

		elif account_type=="2":
			account_type="worker"

		elif account_type=="3":
			account_type="director"
		
		if account_type not in ("hr-manager", "worker", "director"):
			os.system("cls||clear")
			print("Wrong account type!")
		
		else:
			login=input("Enter your login:\n").strip()
			password=input("Enter your password:\n").strip()
			
			info_array=csv_reader("workers_logins_passwords_names.csv")

			for i in info_array:                                                        
				if i.get("Account type")==account_type and i.get("Login")==login and i.get("Password")==password:
					fullname=i.get("Full name") 
					check=True
					break


			if check==True:
				os.system("cls||clear")
				print("Welcome, {}!".format(fullname))

				if account_type=="hr-manager":
					menu_for_hrmanager()

				elif account_type=="worker":
					menu_for_worker()

				elif account_type=="director":
					menu_for_director()
				break    

			else:
				if fails==3:
					print("Too many login attempts! Try again later!") 
					break
				os.system("cls||clear")
				print("Invalid login or password! Try again") 
				fails+=1






def menu_for_hrmanager():
	while True:
		menu=input("""To work with the program, enter the number of the corresponding option.
		List of options:
		1) Show a list of all employees
		2) Add an employee
		3) Delete an employee
		4) Change the position of the employee
		5) Show the work schedule of all employees
		6) Change the employee's work schedule
		7) Show my account information
		8) Change my login
		9) Change my password
		If you want to exit the program, enter 0\n""").strip()

		if menu=="0":
			os.system("cls||clear")
			print("You are out of the program! It will be nice to have you back!") 
			login_or_exit()
			break

		elif menu=="1":
			os.system("cls||clear")
			workers_list(False)
			break

		elif menu=="2":
			os.system("cls||clear")
			add_worker()
			break

		elif menu=="3":
			os.system("cls||clear")
			delete_worker()
			break

		elif menu=="4":
			os.system("cls||clear")
			change_post()
			break

		elif menu=="5":
			os.system("cls||clear")
			employee_schedule()
			break

		elif menu=="6":
			os.system("cls||clear")
			change_timesheet()
			break
		
		elif menu=="7":
			os.system("cls||clear")
			account_info()
			break

		elif menu=="8":
			os.system("cls||clear")
			change_my_lp(True)
			break

		elif menu=="9":
			os.system("cls||clear")
			change_my_lp(False)
			break

		else:
			os.system("cls||clear")
			print("Error! Try again!")






def menu_for_worker():
	while True:
		menu=input("""To work with the program, enter the number of the corresponding option.
		List of options:
		1) Show my position in the list of employees
		2) Show my work schedule
		3) Show my premium
		4) Show my salary
		5) Show my salary for the year
		6) Show my account information
		7) Change my login
		8) Change my password
		If you want to exit the program, enter 0\n""").strip()

		if menu=="0":
			os.system("cls||clear")
			print("You are out of the program! It will be nice to have you back!")
			login_or_exit()
			break

		elif menu=="1":
			os.system("cls||clear")
			my_position()
			break

		elif menu=="2":
			os.system("cls||clear")
			timesheet()
			break

		elif menu=="3":
			os.system("cls||clear")
			my_addition()
			break

		elif menu=="4":
			os.system("cls||clear")
			my_salary(1)
			break

		elif menu=="5":
			os.system("cls||clear")
			my_salary(12)
			break 
		
		elif menu=="6":
			os.system("cls||clear")
			account_info()
			break

		elif menu=="7":
			os.system("cls||clear")
			change_my_lp(True)
			break

		elif menu=="8":
			os.system("cls||clear")
			change_my_lp(False)
			break

		else:
			os.system("cls||clear")
			print("Error! Try again!")






def menu_for_director():
	while True:
		menu=input("""To work with the program, enter the number of the corresponding option.
		List of options:
		 1) Show a list of all employees
		 2) Increase the employee's salary
		 3) Lower the employee's salary
		 4) Show the salary of all employees for one month
		 5) Show the employee with the highest salary
		 6) Show the employee with the lowest salary 
		 7) Show the average salary level among employees
		 8) Show a list of premiums of all employees
		 9) Give a premiums to an employee
		10) Open the calculator
		11) Show my account information
		12) Change my login
		13) Change my password
		If you want to exit the program, enter 0\n""").strip()

		if menu=="0":
			os.system("cls||clear")
			print("You are out of the program! It will be nice to have you back!")
			login_or_exit()
			break

		elif menu=="1":
			os.system("cls||clear")
			workers_list(True)
			break
		
		elif menu=="2":
			os.system("cls||clear")
			change_salary(True)
			break

		elif menu=="3":
			os.system("cls||clear")
			change_salary(False)
			break

		elif menu=="4":
			os.system("cls||clear")
			salary_sum()
			break

		elif menu=="5":
			os.system("cls||clear")
			biggest_salary()
			break

		elif menu=="6":
			os.system("cls||clear")
			smallest_salary()
			break

		elif menu=="7":
			os.system("cls||clear")
			salary_sum(True)
			break

		elif menu=="8":
			os.system("cls||clear")
			list_of_additions()
			break

		elif menu=="9":
			os.system("cls||clear")
			add_addition()
			break
		
		elif menu=="10":
			os.system("cls||clear")
			calculator()
			break
		
		elif menu=="11":
			os.system("cls||clear")
			account_info()
			break

		elif menu=="12":
			os.system("cls||clear")
			change_my_lp(True)
			break

		elif menu=="13":
			os.system("cls||clear")
			change_my_lp(False)
			break

		else:
			os.system("cls||clear")
			print("Error! Try again!")          






def back_to_menu():
	print("-----------------------------------")
	print("To return back to the menu, enter 0")

	while True:
		backmenu=input("").strip()

		if backmenu=="0":
			if account_type=="hr-manager":
				os.system("cls||clear")
				menu_for_hrmanager()
				break

			elif account_type=="worker":
				os.system("cls||clear")
				menu_for_worker()
				break

			elif account_type=="director":
				os.system("cls||clear")
				menu_for_director()
				break

		else:
			os.system("cls||clear")
			print("Error! To return back to the menu, enter 0")






def save_csv(info, filename, fdname): 
	with open(filename, "w", newline="") as File:
		fieldnames=fdname
		writer=csv.DictWriter(File, fieldnames=fdname)
		writer.writeheader()
		writer.writerows(info)






def workers_list(d=False): #director
	info=csv_reader("workers_info.csv")

	for i in info:
		if d==True:
			for key, value in i.items():
				print(key, "-", value)
			print("")

		else:
			if i["Post"]=="Director":
				continue

			else:
				for key, value in i.items():
					print(key, "-", value)
				print("")

	back_to_menu()






def lp_generator(): #lp-login and password
	lower="qwertyuiopasdfghjklzxcvbnm"
	upper="QWERTYUIOPASDFGHJKLZXCVBNM"
	numbers="0123456789"

	all=lower+upper+numbers
	password="".join(random.sample(all, 8))

	return password






def add_worker():
	info_array=csv_reader("workers_info.csv")
	timesheet=csv_reader("timesheet.csv")
	lp=csv_reader("workers_logins_passwords_names.csv")
	additions=csv_reader("additions.csv")
	
	info_dict=csv_dictreader("workers_info.csv")
	
	name=input("Enter the full name of the new employee:\n").strip()
	for i in info_dict:
		if i==name:
			print("This name is already taken!")
			break
		
		elif name=="":
			print("Error!")
			break

	else:
		post=input("Enter the position that the employee will hold:\n").strip()
		if post=="Director" or post=="director":
			print("You can't appoint an employee to the position of director!")
		
		elif post=="":
			print("Error!")

		else:
			account=input("Select the account type for the employee: \n1) HR-Manager \n2) Worker\n").lower().strip()
			if account in ("1", "2") or account in ("hr-manager", "worker"):
				if account=="1":
					account="hr-manager"

				elif account=="2":
					account="worker"
				
				date=input("Enter the date of employment (dd.mm.YYYY):\n").strip()
				if date=="":
					todays_date=time.localtime()
					date=time.strftime("%d.%m.%Y", todays_date)

				if "." not in date:
					print("The date was entered incorrectly!")
				
				else:
					try:
						salary=input("Enter the salary that the employee will receive:\n$").strip()

						if salary=="" or int(salary)<0:
							salary=0
					
						new_worker={"Full name":name, "Post":post, "Date of employment":date, "Salary":"$"+str(salary)}
						info_array.append(new_worker)
						print("Employee was added!")

						save_csv(info_array, "workers_info.csv", ["Full name", "Post", "Date of employment", "Salary"]) #Добавляем сотрудника в файл с общей информацией о сотрудниках

						timesheet.append({"Full name":name, "Monday":"9:00-16:00", "Tuesday":"9:00-16:00", "Wednesday":"9:00-16:00", "Thursday":"9:00-16:00", "Friday":"9:00-16:00", "Saturday":"Non-working day"}) #Добавляем сотрудника в файл с расписанием
						save_csv(timesheet, "timesheet.csv", ["Full name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

						additions.append({"Full name":name, "January":"$0", "February":"$0", "March":"$0", "April":"$0", "May":"$0", "June":"$0", "July":"$0", "August":"$0", "September":"$0", "October":"$0", "November":"$0", "December":"$0"}) #Добавляем сотрудника в файл с премией
						save_csv(additions, "additions.csv", ["Full name", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

						login=lp_generator() #Генерируем логин и пароль для сотрудника
						password=lp_generator()
						os.system("cls||clear")
						print("Employee's login and password: \nLogin - {} \nPassword - {}".format(login, password))

						lp.append({"Account type":account, "Login":login, "Password":password, "Full name":name})  
						save_csv(lp, "workers_logins_passwords_names.csv", ["Account type", "Login", "Password", "Full name"]) #Добавляем сотрудника в файл с паролями

					except Exception:
						print("The salary was entered incorrectly!")		
			else:
				print("Wrong account type!")


	back_to_menu()






def delete_worker():
	info_dict=csv_dictreader("workers_info.csv")
	timesheet_dict=csv_dictreader("timesheet.csv")
	lp_dict=csv_dictreader("workers_logins_passwords_names.csv")
	additions_dict=csv_dictreader("additions.csv")

	print("List:")
	counter=1
	for i in info_dict.values():
		if i.get("Full name")=="Petr Palych":
			continue

		else:
			print("{}) {}".format(counter, i.get("Full name")))
			counter+=1

	print("----------------------------------------------------------------")
	workers_name=input("Enter the name of the employee you want to remove from the list:\n").strip()
	if workers_name=="Petr Palych":
		print("You can't delete the director!")
	
	else:
		try:
			info_dict.pop(workers_name) 
			info_array=list(info_dict.values())

			timesheet_dict.pop(workers_name)
			timesheet=list(timesheet_dict.values())

			lp_dict.pop(workers_name)
			lp=list(lp_dict.values())

			additions_dict.pop(workers_name)
			additions=list(additions_dict.values())

			os.system("cls||clear")
			print("Employee was removed!")

			save_csv(info_array, "workers_info.csv", ["Full name", "Post", "Date of employment", "Salary"])
			save_csv(timesheet, "timesheet.csv", ["Full name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
			save_csv(lp, "workers_logins_passwords_names.csv", ["Account type", "Login", "Password", "Full name"])
			save_csv(additions, "additions.csv", ["Full name","January","February","March","April","May","June","July","August","September","October","November","December"])

		except:
			os.system("cls||clear") 
			print("Employee wasn't found!")
				
	back_to_menu()






def change_post():
	info_dict=csv_dictreader("workers_info.csv")

	print("List:")
	counter=1
	for i in info_dict.values():
		if i.get("Full name")=="Petr Palych":
			continue

		else:
			print("{}) {} \nPost - {}\n".format(counter, i.get("Full name"), i.get("Post")))
			counter+=1

	print("-----------------------------------------------------------------")
	name=input("Enter the name of the employee whose position you want to change:\n").strip()
	worker_dict=info_dict.get(name, None)
	if worker_dict==None:
		print("Employee not found!")
	
	else:
		post=input("Enter a new position of the employee:\n").strip()
		if worker_dict["Post"]==post:
			print("The employee already holds this position!")

		elif post=="Director":
			print("You can't change the position of an employee to the position of director!")
		
		elif post=="":
			print("Error!")

		elif name=="Petr Palych":
			print("You can't change the position of the director!")

		else:
			worker_dict["Post"]=post
			info_dict[name]=worker_dict
			info_array=list(info_dict.values())
			os.system("cls||clear")
			print("The position has been changed!")

			save_csv(info_array, "workers_info.csv", ["Full name", "Post", "Date of employment", "Salary"])

	back_to_menu()






def employee_schedule():
	schedule=csv_reader("timesheet.csv")
	for i in schedule:
		for key, value in i.items():
			print(key, "-", value)
		print("")

	back_to_menu()






def change_timesheet():
	info_dict=csv_dictreader("timesheet.csv")

	print("List:")
	counter=1
	for i in info_dict:
		print("{}) {}".format(counter, i))
		counter+=1

	print("----------------------------------------------------------------------")
	name=input("Enter the name of the employee whose work schedule you want to change:\n").strip()
	work_schedule=info_dict.get(name, None)
	
	if work_schedule==None:
		print("Employee not found!")

	else:
		os.system("cls||clear")
		for key, value in work_schedule.items():
			print("{}: \n{}\n".format(key, value))

		print("-----------------------------------------------------------------")
		day=input("For which day do you want to change the employee's work schedule: \n1) Monday \n2) Tuesday \n3) Wednesday \n4) Thursday \n5) Friday \n6) Saturday\n").capitalize().strip()
		work_week={"1":"Monday", "2":"Tuesday", "3":"Wednesday", "4":"Thursday", "5":"Friday", "6":"Saturday"}
		if day in work_week:
			day=work_week.get(day)
			   
		old_work_schedule=work_schedule.get(day, None)

		if old_work_schedule==None:
			print("You entered the day of the week incorrectly!")
		
		else:
			new_work_schedule=input("Enter a new working time (hh:mm-hh:mm):\n").strip()
			if ":" not in new_work_schedule or "-" not in new_work_schedule or " " in new_work_schedule:
				print("The work time was entered incorrectly!")
			
			else:
				work_schedule[day]=new_work_schedule
				os.system("cls||clear")
				print("New work schedule on {} - {}. Old work schedule - {}.".format(day, new_work_schedule, old_work_schedule))

				info_dict[name]=work_schedule
				info_array=list(info_dict.values())

				save_csv(info_array, "timesheet.csv", ["Full name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

	back_to_menu()






def my_position():
	info_dict=csv_dictreader("workers_info.csv")

	worker_info=info_dict.get(fullname)
	for key, value in worker_info.items():
			print("{}:\n{}\n".format(key, value))

	back_to_menu()






def timesheet():
	info_dict=csv_dictreader("timesheet.csv")

	work_time=info_dict.get(fullname)
	for key, value in work_time.items():
			print("{}:\n{}\n".format(key, value))

	back_to_menu()






def my_addition():
	info_dict=csv_dictreader("additions.csv")

	month=input("For which month do you want to know your premium? \n 1) January \n 2) February \n 3) March \n 4) April \n 5) May \n 6) June \n 7) July \n 8) August \n 9) September \n10) October \n11) November \n12) December \n").capitalize().strip()
	calendar={"1":"January", "2":"February", "3":"March", "4":"April", "5":"May", "6":"June", "7":"July", "8":"August", "9":"September", "10":"October", "11":"November", "12":"December"}
	if calendar.get(month)!=None:
		month=calendar.get(month)

	addition=info_dict.get(fullname).get(month)
	if addition==None:
		print("You entered the wrong month!")

	else:
		os.system("cls||clear")
		print("Your premium for {} - {}".format(month, addition))

	back_to_menu()






def my_salary(n=1):
	info_dict=csv_dictreader("workers_info.csv")

	if n==1:
		person_info=info_dict.get(fullname)
		print("Your salary for one month - {}".format(person_info["Salary"]))

	elif n==12:
		person_info=info_dict.get(fullname)
		print("Your salary for one year - ${}".format(int(person_info["Salary"].replace("$",""))*12))

	back_to_menu()






def change_salary(up=True):
	info_array=csv_reader("workers_info.csv")
	info_dict=csv_dictreader("workers_info.csv")

	for i in info_array:
		print("\nFull name - {} \nSalary - {}".format(i["Full name"], i["Salary"]))

	print("----------------------------------------------")
	name=input("Which employee's salary do you want to change?\n").strip()

	person_info=info_dict.get(name, None)
	if person_info==None:
		os.system("cls||clear")
		print("Employee not found!")

	else:
		if up==True:
			try:
				r=input("Employee's salary supplement: $").strip()
				if r=="" or int(r)<0:
					os.system("cls||clear")
					print("Error!")
				
				else:
					s=person_info["Salary"].replace("$","")
					new_salary=int(s)+int(r)
					person_info["Salary"]="$"+str(new_salary)

					print("The salary is changed! The new salary of the employee is {}".format(person_info["Salary"]))
					save_csv(list(info_dict.values()), "workers_info.csv", ["Full name", "Post", "Date of employment", "Salary"])

			except:
				print("You have incorrectly entered an employee's salary allowance!")

		elif up==False:
			try:
				r=input("The employee's salary reduction will be: $").strip()
				if r=="" or int(r)<0:
					os.system("cls||clear")
					print("Error")
				
				else:
					s=person_info["Salary"].replace("$","")
					new_salary=int(s)-int(r)

					if s=="0":
						os.system("cls||clear")
						print("The employee don't receive a salary, you can't lower it!")
					
					elif new_salary<0:
						os.system("cls||clear")
						print("Too much salary reduction! An employee can't receive a negative salary!")

					else:
						person_info["Salary"]="$"+str(new_salary)

						print("The salary is changed! The new salary of the employee is {}".format(person_info["Salary"]))
						save_csv(list(info_dict.values()), "workers_info.csv", ["Full name", "Post", "Date of employment", "Salary"])

			except:
				print("The employee's salary reduction was incorrectly entered!")

	back_to_menu()






def salary_sum(avl=False): #avl - average salary level
	info_array=csv_reader("workers_info.csv")

	sum=0
	workers=0
	
	for i in info_array:
		if i["Post"]=="Director":
			continue
		else:
			sum+=int(i["Salary"].replace("$",""))
			workers+=1

	if avl==False:
		print("Salary of all employees for one month - ${}".format(sum))

	elif avl==True:
		print("Average salary level among employees - ${}, number of employees - {}.".format(int(sum/workers), workers))

	back_to_menu()






def biggest_salary():
	info_array=csv_reader("workers_info.csv")
	max_salary=0

	for i in info_array:
		if i["Post"]=="Director":
			continue

		elif max_salary<int(i["Salary"].replace("$","")):
			max_salary=int(i["Salary"].replace("$",""))

	for i in info_array:
		if i["Post"]=="Director":
			continue

		elif max_salary==int(i["Salary"].replace("$","")):
			print("\nSalary - {}, employee's name - {}".format(i["Salary"], i["Full name"]))

	back_to_menu()






def smallest_salary():
	info_array=csv_reader("workers_info.csv")
	min_salary=int(info_array[0]["Salary"].replace("$", ""))

	for i in info_array:
		if min_salary>int(i["Salary"].replace("$", "")):
			min_salary=int(i["Salary"].replace("$", ""))

	for i in info_array:
		if min_salary==int(i["Salary"].replace("$", "")):
			print("\nSalary - {}, employee's name - {}".format(i["Salary"], i["Full name"]))

	back_to_menu()






def list_of_additions():
	additions=csv_reader("additions.csv")

	counter=1
	for i in additions:
		for key, value in i.items():
			print(key, "-", value)
		print("")
	
	back_to_menu()






def add_addition():
	additions_dict=csv_dictreader("additions.csv")

	print("List:")
	counter=1
	for i in additions_dict:
		print("{}) {}".format(counter, i))
		counter+=1

	print("------------------------------------------------")
	name=input("Which employee do you want to give a premium to?\n").strip()
	worker_dict=additions_dict.get(name, None)
	if worker_dict==None:
		os.system("cls||clear")
		print("Employee not found!")

	else:
		os.system("cls||clear")
		for key, value in worker_dict.items():
			print("{} - {}".format(key, value))
		
		try:
			print("----------------")
			addition=int(input("Enter the bonus: \n$").strip())
			os.system("cls||clear")
			month=input("For which month do you want to give the premium: \n 1) January \n 2) February \n 3) March \n 4) April \n 5) May \n 6) June \n 7) July \n 8) August \n 9) September \n10) October \n11) November \n12) December \n").capitalize().strip()

			calendar={"1":"January", "2":"February", "3":"March", "4":"April", "5":"May", "6":"June", "7":"July", "8":"August", "9":"September", "10":"October", "11":"November", "12":"December"}
			if calendar.get(month)!=None:
				month=calendar.get(month)

			worker_dict[month]="$"+str(addition)
			print("The premium was successfully given!")

			additions_dict[name]=worker_dict
			additions_array=list(additions_dict.values())

			save_csv(additions_array, "additions.csv", ["Full name","January","February","March","April","May","June","July","August","September","October","November","December"])
		
		except:
			print("The premium was entered incorrectly!")

	back_to_menu()






def calculator():
	try:
		num1=float(input("...").strip())
		action=input("Select an action (+, -, *, /)\n").strip()

		if action in ("+", "-", "*", "/"):
			num2=float(input("...").strip())

			if action=="+":
				print("Answer: {}".format(num1+num2))

			elif action=="-":
				print("Answer: {}".format(num1-num2))

			elif action=="*":
				print("Answer: {}".format(num1*num2))

			try:
				if action=="/":
					print("Answer: {}".format(num1/num2))
			except:
				print("Division by zero!")
			
		else:
			print("Error!")

	except:
		print("You entered the number incorrectly!")

	back_to_menu()






def account_info():
	info_dict=csv_dictreader("workers_logins_passwords_names.csv")
	my_lp=info_dict.get(fullname)

	for key, value in my_lp.items():
		print("{} - {}".format(key, value))
	print("")

	back_to_menu()






def change_my_lp(l=True): #lp - login or password
	info_dict=csv_dictreader("workers_logins_passwords_names.csv")
	worker_lp=info_dict.get(fullname)

	if l==True:
		login=input("Enter a new login:\n")
		worker_lp["Login"]=login

		info_dict[fullname]=worker_lp
		save_csv(list(info_dict.values()), "workers_logins_passwords_names.csv", ["Account type", "Login", "Password", "Full name"])

		os.system("cls||clear")
		print("Your login is changed!")
	
	else:
		password=input("Enter a new password:\n")
		worker_lp["Password"]=password

		info_dict[fullname]=worker_lp
		save_csv(list(info_dict.values()), "workers_logins_passwords_names.csv", ["Account type", "Login", "Password", "Full name"])

		os.system("cls||clear")
		print("Your password is changed!")
	
	back_to_menu()