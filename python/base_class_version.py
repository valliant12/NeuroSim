"""Dooba doo."""

import random

import numpy as np
import pandas as pd


"""
Def global vars.

"""


class Stimulus:

    def __init__(self,
                 name="stimulus",
                 proportion=0,
                 refractory_length=0,
                 response_rate=0,
                 spontaneous_rate=0):
        self.name = str(name)
        self.proportion = proportion  # Proportion of total neurons
        self.refractory_length = refractory_length  # Length of RP
        self.response_rate = response_rate  # Prob of neuron responding to stim
        self.spontaneous_rate = spontaneous_rate  # Prob of firing randomly

    def __repr__(self):
        return """Stimulus(name={0}, proportion={1}, refractory_length={2},
                  response_rate={3}, spontaneous_rate={4})
               """.format(self.name,
                          self.proportion,
                          self.refractory_length,
                          self.response_rate,
                          self.spontaneous_rate)


stimulus_dict = {
    "audio": Stimulus(name="audio",
                      proportion=1,
                      refractory_length=3,
                      response_rate=1,
                      spontaneous_rate=0),

    "olfactory": Stimulus(name="olfactory",
                          proportion=1,
                          refractory_length=1,
                          response_rate=1,
                          spontaneous_rate=0),
}

if __name__ == '__main__':
    print("Boop!\n")


def assign_neurons(number=10, stimuli=None, overlap_chance=0.5):
    """Generate list of neuron types.

    overlap_chance refers to the probability of a neuron ATTEMPTING to generate
    a new type as well, not the proportion of neurons that are multi-sensing.
    Eg, if an "audio" neuron has a 50% chance, it will pick a "new type" 50%
    of the time. If that "new type" is audio, it will not change.
    """
    neuron_list = list()

    # Construct dict of stimuli proportions

    stimulus_proportions = {}

    try:
        for stimulus in stimuli:
            stimulus_proportions[stimulus] = stimuli[stimulus].proportion

        print("Stimulus ratios: ", stimulus_proportions, "\n")

    except:
        raise ValueError("Unable to find proportion method in stimulus: {}".format(stimulus))

    for neuron in range(number):
        neuron_list.append((weighted_choice(stimulus_proportions),))

    # Overlap neurons
    for i in range(len(neuron_list)):
        if random.random() < overlap_chance:
            new_neuron = weighted_choice(stimulus_proportions)
            print("Attempting to add stim: {0} to {1}".format
                  (new_neuron, neuron_list[i]))
            if new_neuron not in neuron_list[i]:
                neuron_list[i] += (new_neuron,)
    print()

    return neuron_list


def if_fire(neuron_type_list, neuron_fired_list, stimulus_type,
            fire_rate_dict):
    for neuron in range(len(neuron_type_list)):
        if neuron_type_list[neuron].lower() == stimulus_type.lower():
            if random.random() < fire_rate_dict[neuron_type_list[neuron]]:
                neuron_fired_list[neuron] = True

    return neuron_fired_list


def generate_neurons(number=300, time_steps=500):
    """Create an empty array with n neurons, over t steps."""
    neurons = np.zeros(shape=(number, time_steps))
    return neurons


def print_neurons():
    pass


def pulse_neurons(neurons_array, fired_neurons_list, time_point,
                  refractory_time=5):
    """Non-class version."""
    for i in range(len(fired_neurons_list)):
        if time_point < refractory_time and (neurons_array[i][0:time_point] == np.zeros(time_point)).all() and fired_neurons_list[i]:
            neurons_array[i][time_point] = 1
        elif time_point >= refractory_time and (neurons_array[time_point-refractory_time:time_point] == np.zeros(refractory_time)) and fired_neurons_list[i]:
            neurons_array[i][time_point] = 1
    return neurons_array


def pulse_neurons_class(neurons_array, stimulus_class, time_point):
    """Class version."""
    try:
        pass
    except:
        raise Exception("stimulus_class must be an instance of Stimulus.")


def weighted_choice(choices):
    """Like random.choice, but each element can have a different chance of
    being selected.

    choices is a dictionary with single-number values.
    Technically, they can have more than two items, the rest will just be
    ignored.  The key is the thing being chosen, the value is
    its weight.  The weights can be any numeric values, what matters is the
    relative differences between them.

    Adapted from: https://stackoverflow.com/questions/3679694/
    a-weighted-version-of-random-choice
    """
    space = {}
    current = 0

    for choice in choices:
        if choices[choice] > 0:
            space[current] = choice
            current += choices[choice]

    rand = random.uniform(0, current)

    for key in sorted(list(space.keys()) + [current]):
        if rand < key:
            return choice
        choice = space[key]

    return None


def main():
    """The main function."""
    neuron_count = 10

    time_steps = 5

    neurons = generate_neurons(number=neuron_count, time_steps=time_steps)

    fired_neurons = [False] * neuron_count
    neuron_types = assign_neurons(neuron_count, stimulus_dict)

    print(neuron_types, "\n")


if __name__ == '__main__':
    main()
