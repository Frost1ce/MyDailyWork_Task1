def create_list():

	# Create a dictionary list to store the items of the To-Do List

	todo_list={}

	print("\n Create Your To-Do List (type 'done' to stop adding items)\n")

	item_number=1

	while True:

		item= input(f" Enter Task {item_number}: ")

		if item.lower()=="done":
			break

		todo_list[item_number]={"task":item,"completed":False}

		item_number+=1

	print("\n To-Do List Created Successfully\n")

	return todo_list

def update_list(todo_list):

	# Update the existing dictionary list for status such as Add/Remove/Mark item completed

	if not todo_list:
		print(" No Task available to Update")
		input("\n Press Enter to return to main menu")
		return todo_list

	while True:

		try:

			choice=int(input(
				"\n Update Menu:\n"
				"\n Press [1] = Mark Task as Completed"
				"\n Press [2] = Add New Task"
				"\n Press [3] = Remove Task"
				"\n Press [4] = Show Updated To-Do List"
				"\n Press [5] = Return to main menu\n"
				"\n Enter Your choice... : "
				))

		except ValueError:
			print(" Invalid Input! enter numbers values only.")
			continue

		if choice==1:

			try:
				task_number=int(input(" Enter Task number to mark as completed: "))
				if task_number in todo_list:
					todo_list[task_number]["completed"]=True
					print(" Task marked as Completed")
				else:
					print(" Task number not found.")
			except ValueError:
				print(" Enter a Valid Task number.")

		elif choice==2:

			new_task=input(" Enter new Task: ")

			if todo_list:
				new_number=max(todo_list.keys())+1
			else:
				new_number=1
			
			todo_list[new_number]={"task":new_task,"completed":False}
			print(" New task added")

		elif choice==3:

			try:
				task_number=int(input(" Enter Task number to remove: "))
				if task_number in todo_list:
					del todo_list[task_number]
					print(" Task Removed")
				else:
					print(" Task number not found.")
			except ValueError:
				print(" Enter a Valid Task number.")

		elif choice==4:

			print("\n Current To-Do List: ")

			print("\n Pending Tasks: ")
			for number,details in todo_list.items():
				if not details["completed"]:
					print(f"{number}.{details['task']}")

			print("\n Completed Tasks: ")
			for number,details in todo_list.items():
				if details["completed"]:
					print(f"{number}.{details['task']}")

		elif choice==5:
			return todo_list

		else:
			print(" Invalid choice!")

def delete_list(todo_list):

	# delete the existing dictionary list and give a warning of agree or not

	if not todo_list:
		print(" No existing To-Do List to delete")
		return {}

	confirm=input(" Are you sure you want to delete the entire list?\n(yes/no): ")

	if confirm.lower()=="yes":
		todo_list.clear()
		print("\n To-Do List deleted Successfully")

	else:
		print(" Deletion cancelled.")

	return todo_list

def view_list(todo_list):

	# Show dictionary list but seperate them with items completed and remaining

	if not todo_list:
		print(" No To-Do List available")
		input(" Press Enter to return to Main Menu...")
		return

	print("\n Pending Tasks:")

	for number, details in todo_list.items():
		if not details["completed"]:
			print(f"{number}. {details['task']}")

	print("\n Completed Tasks:")

	for number, details in todo_list.items():
		if details["completed"]:
			print(f"{number}. {details['task']}")

	input("\n Press Enter to return to main menu...")
	return

def main():

	print("\n Welcome To Command-Line Based To-Do List Application\n")

	todo_list={}

	while True:

		try:

			# Ask what action does the user want to perform 

			main_action=int(input(
				"\n Enter What do you want to do\n"
				"\n Press [1] = Create a new To-Do List"
				"\n Press [2] = Update Existing List"
				"\n Press [3] = Delete Existing List"
				"\n Press [4] = View Existing List"
				"\n Press [5] = Exit To-Do List Command-Line Based Application\n\n : "
				))

		except ValueError:
			print(" Invalid Input! Please enter numerical values only")
			continue

		# Call the create function when pressed 1

		if main_action==1:
			todo_list=create_list()

		# Call the update function when pressed 2

		elif main_action==2:
			todo_list=update_list(todo_list)

		# Call the delete function when pressed 3

		elif main_action==3:
			todo_list=delete_list(todo_list)

		# Call the view function when pressed 4

		elif main_action==4:
			view_list(todo_list)

		#Add the way to close the program when pressed 5

		elif main_action==5:
			print(" \nExiting the Command-Line Based To-Do List Application")
			break

if __name__=="__main__":
	main()