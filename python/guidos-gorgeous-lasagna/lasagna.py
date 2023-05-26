"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

#time that it takes to bake a lasagna
EXPECTED_BAKE_TIME = 40
"""Constant of the time that it takes to bake a lasagna, 40min."""

#time that it takes to prepare each layer of a lasagna
PREPARATION_TIME = 2
"""Constant of the time that it takes to prepare a layer, 2min."""

#calculate time that it takes to prepare a lasagna of x layers
def preparation_time_in_minutes(num_of_layers=1):
    """Calculate the time that it takes to prepare a lasagna of x layers, taking into consideration the number of minutes taken to prepare one layer, through a multiplication of both numbers.
    :param num_of_layers: int the number of layers
    :return: int - preparation time
    """
    return PREPARATION_TIME * num_of_layers

#calculate time remaining to finish baking lasagna given x time
def bake_time_remaining(time_elapsed=0):
    """Calculate the time left to finish baking a lasagna, taking into account how much time already passed through a subtraction.
    :param time_elapsed: int time already passed while baking
    :return: int - time remaining to be baked
    """
    return EXPECTED_BAKE_TIME - time_elapsed

#calculate time elapsed since started to make lasagna
def elapsed_time_in_minutes(num_of_layers=1,time_elapsed_baking=0):
    """Calculate total time elapsed since starting the recipe of the lasagna, through adding the number of minutes it took to prepare the layers, and the time elapsed of baking so far.
    :param num_of_layers: int number of layers of the lasagna
    :param time_elapsed_baking: int number of minutes that the lasagna spent baking so far
    :result: int - time elapsed since preparation to the current moment
    """
    return preparation_time_in_minutes(num_of_layers) + time_elapsed_baking 