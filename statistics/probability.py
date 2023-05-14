import random
# I used this script to simulate the picking of examples that my main program does
# it generates a random example from a pool of 1000 every time the user generates a new response 
# (clicks the generate a new response button or submits the previous with an anwser)
# I've done this to calculate what the probability of someone getting repeating examples when doing my experiment is
# I've fixed the issue of getting the same example by implementing the "generate another example" button on my webpage
simulations = 1000000

# Number of examples the user generates during their session
# I've chosen 10 since I do not really expect people to do more than 10 examples per session
num_draws = 10

# number of examples that we chose from (in this case 1000)
examples = 1000

# Counter for number of simulations with at least one repeating number (repeating example)
not_unique = 0
for draws in range(196,200):
    num_draws = draws
    not_unique = 0
    for i in range(simulations):
        drawn_numbers = set()
        for j in range(num_draws):
            drawn_numbers.add(random.randint(1, examples))
    
        # Checks if all of the numbers that were generated are unique
        if len(drawn_numbers) == num_draws:
            not_unique += 1
    ratio =     not_unique/simulations
    print("number of draws",draws)
    print("times that all of the chosen numbers were unique:", not_unique, "out of", simulations)
    print("ratio",round(ratio,2))
