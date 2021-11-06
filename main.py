# Due Monday 11/08/2021
#create lists
#create random gen function to return a value from the lists
#"loop" the function/process
    #print gen/selected function
    #ask for an "ok" or to change
    #re-gen
#display result (reuse the print function)
import random

destinations = ["my couch", "Mexico", "downtown Milwaukee", "as close as possible", "anywhere but here", "up north", "get into bed"]
restaurants = ["Taco Hut", "Steak House", "Italian Goodness", "Real Chilli", "Salads'R'Us", "nothing but your own sadness"]
transport_options = ["a car ride", "walking", "calling an Uber", "taking an airplane", "stapping on the old Heelys", "hitchhiking", "biking", "not going anywhere"]
entertain_options = ["to the movies", "drinking", "go garting", "splunking", "people watching", "dancing", "bowling", "to be bored"]

# random generator - print(random.choice("The list goes here"))
# start with user input to "run" yes or no

# yes = true, no = fasle
    
def run_tip_planner(yes_no):
    if yes_no == "yes":
        return True
    if yes_no == "no":
        return print("Fine! Maybe another time...")

def generate_from_list(list_of_input): #output = random selection from the inputed list.
    output = random.choice(list_of_input)
    return output

def entire_list_of_options(i_1, i_2, i_3, i_4):
    print(f"\nHow about this for a fun day trip idea? \nDestination: {i_1}, To eat: {i_2}, Travling by: {i_3}, Then some fun: {i_4}\n")
    list_answer = (input("Should I re-Generate?:\nYes or No: ").lower())
    if list_answer == "no":
        return False
        #print("Complete!")
    if list_answer == "yes":
        return True
    
#run_y_n = run_tip_planner(str(input("Should we start the trip planner? Yes or No: ")).lower()) #run_y_n will name the answer to continue.

#let_go = run_tip_planner(str(input("Should we start the trip planner? Yes or No: ")).lower())

#entire_list_of_options(where, eat, how, fun)

# now I have to take the true output of the starter function to start the generation of the day trip using the list inputs from above.

where = generate_from_list(destinations)
eat = generate_from_list(restaurants)
how = generate_from_list(transport_options)
fun = generate_from_list(entertain_options)

lets_go = run_tip_planner(str(input("\nShould we start the day-trip planner?\nYes or No: ")).lower())

if lets_go == True:
    results = entire_list_of_options(where, eat, how, fun)
    while results == True:
        re_gen = input("\n\nWhat would you like to change?\nFor All, type 'a'\nFor the destination, type 'd'\nFor what to eat, type 'e'\nFor transportation method, type 't'\nFor entertainment, type 'f'\nEnter HERE:").lower()
        if re_gen == "a":
            where = generate_from_list(destinations)
            eat = generate_from_list(restaurants)
            how = generate_from_list(transport_options)
            fun = generate_from_list(entertain_options)
            results = entire_list_of_options(where, eat, how, fun)
        elif re_gen == "d":
            where = generate_from_list(destinations)
            results = entire_list_of_options(where, eat, how, fun)
        elif re_gen == "e":
            eat = generate_from_list(restaurants)
            results = entire_list_of_options(where, eat, how, fun)
        elif re_gen == "t":
            how = generate_from_list(transport_options)
            results = entire_list_of_options(where, eat, how, fun)
        elif re_gen == "f":
            fun = generate_from_list(entertain_options)
            results = entire_list_of_options(where, eat, how, fun)
    else:
        print(f"\n\nCompleted!\n\nYour generated day trip will consist of {how} to {where}, to eat {eat}, then going {fun} to conclude the night. \nHAVE FUN!\n\n")
