import random

def monty_hall_simulation(num_simulations):
    switch_wins = 0
    stay_wins = 0
    list_carindex=[]
    list_initialchoice=[]
    list_switchchoice=[]

    for _ in range(num_simulations):

        doors = ["goat"] * 3
        car_index = random.randint(0, 2)
        doors[car_index] = "car"

        list_carindex.append(car_index)


        initial_choice = random.randint(0, 2)

        list_initialchoice.append(initial_choice)


        monty_choices = [i for i in range(3) if i != initial_choice and doors[i] == "goat"]
        monty_choice = random.choice(monty_choices)


        stay_strategy = doors[initial_choice]


        switch_strategy = doors[3 - initial_choice - monty_choice]
        switch_optn=3 - initial_choice - monty_choice
        list_switchchoice.append(switch_optn)


        if stay_strategy == "car":
            stay_wins += 1
        if switch_strategy == "car":
            switch_wins += 1

    return stay_wins, switch_wins,list_carindex,list_initialchoice,list_switchchoice


num_simulations = 10
stay_wins, switch_wins,car_index,initial_choice,switch_choice = monty_hall_simulation(num_simulations)
print(f"Stay strategy wins: {stay_wins} out of {num_simulations} games")
print(f"Switch strategy wins: {switch_wins} out of {num_simulations} games")
list_evaluation_notswitch=[]
list_evaluation_switch=[]

