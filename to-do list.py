#Kiara
#To do list
#Add a task to the to-do list
#View the current to-do list
#Mark a task as completed
#Remove a task from the to-do list
#Exit the program


movie_list = ["cars", "Barbie", "Iron Man", "mean girls"]
a = input("what movie would you like to add?")
w = input("what movie did you watch?")
r = input("what movie would you like to remove?")


print("Movie watch list")
print("please choose an operator: (type in a number between 1-5) \n1.Add a task to the to-do list \n2.view the current to-do list \n3.Mark a task as completed \n4.remove a task from the to do list \n5.Quit the program")
option = int(input("option: "))




def to_do_list():
   if option == 1:
       movie_list.append(a)
       print(movie_list)
   elif option == 2:
       print(movie_list)
   elif option == 3:
       movie_list.insert(w,"X")
   elif option == 4:
       movie_list.pop(r)
   elif option == 5:
       quit()






#main
to_do_list()
