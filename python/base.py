"""Dooba doo."""import randomimport reimport numpy as np"""Def global vars."""class Stimulus:    def __init__(self,                 name="stimulus",                 proportion=0,                 refractory_length=0,                 refractory_period=False,                 response_rate=0,                 spontaneous_rate=0):        self.name = str(name)        self.proportion = proportion  # Proportion of total neurons        self.refractory_length = refractory_length  # Length of RP        self.refractory_period = bool(refractory_period)  # Is there a RP?        self.response_rate = response_rate  # Prob of neuron responding to stim        self.spontaneous_rate = spontaneous_rate  # Prob of firing randomlystimulus_dict = {    "audio" : Stimulus(name="audio",                       proportion=1,                       refractory_length=3,                       refractory_period=True,                       response_rate=1,                       spontaneous_rate=0)}print(stimulus_dict["audio"])if __name__ == '__main__':    print("Boop!\n")def assign_neurons(number, proportions):    """Return a list of strings, len = number, with distro. assigned based on provided proportions."""    neuron_list = list()    for i in range(number):        neuron_list.append(weighted_choice(proportions))    return neuron_listdef if_fire(neuron_type_list, neuron_fired_list, stimulus_type,            fire_rate_dict):    for neuron in range(len(neuron_type_list)):        if neuron_type_list[neuron].lower() == stimulus_type.lower():            if random.random() < fire_rate_dict[neuron_type_list[neuron]]:                neuron_fired_list[neuron] = True            else:                pass        else:            pass    return neuron_fired_listdef generate_neurons(number=300, time_steps=500):    """Create an empty array with n neurons, over t steps."""    neurons = np.zeros(shape=(number, time_steps))    return neuronsdef parse_input(input_string):    """Interpret input."""    return re.compile('\w+').findall(input_string.lower())    # Similar to str.split(), but only extracts words + numbersdef pulse_neurons(neurons_array, fired_neurons_list, time_point,                  refractory_time=5):    """Non-class version."""    for i in range(len(fired_neurons_list)):        if time_point < refractory_time and (neurons_array[i][0:time_point] == np.zeros(time_point)).all() and fired_neurons_list[i]:            neurons_array[i][time_point] = 1        elif time_point >= refractory_time and (neurons_array[time_point-refractory_time:time_point] == np.zeros(refractory_time)) and fired_neurons_list[i]:            neurons_array[i][time_point] = 1    return neurons_arraydef pulse_neurons_class(neurons_array, stimulus_class, time_point):    """Class version."""    try:        pass    except:        raise Exception("stimulus_class must be an instance of Stimulus.")def generate_response_types():    passdef weighted_choice(choices):    """Like random.choice, but each element can have a different chance of    being selected.    choices is a dictionary with single-number values.    Technically, they can have more than two items, the rest will just be    ignored.  The key is the thing being chosen, the value is    its weight.  The weights can be any numeric values, what matters is the    relative differences between them.    Adapted from: https://stackoverflow.com/questions/3679694/    a-weighted-version-of-random-choice    """    space = {}    current = 0    for choice in choices:        if choices[choice] > 0:            space[current] = choice            current += choices[choice]    rand = random.uniform(0, current)    for key in sorted(list(space.keys()) + [current]):        if rand < key:            return choice        choice = space[key]    return Nonedef main():    """The main function."""    neuron_count = 5    neuron_proportion = {        "audio"  : 0.8,        "visual" : 0.5,        "dead"   : 0,        "other"  : 0,    }    response_rate = {        "audio"  : 0.5,        "visual" : 0.3,        "random" : 0.5,    }    time_steps = 5    neurons = generate_neurons(number=neuron_count, time_steps=time_steps)    print("Response rates: {}".format(response_rate))    fired_neurons = [False] * neuron_count    neuron_types = assign_neurons(neuron_count, neuron_proportion)    print("Neuron types: {}".format(neuron_types), "\n")    fired_neurons = if_fire(neuron_types, fired_neurons, "audio", response_rate                            )    neurons = pulse_neurons(neurons, fired_neurons, 2)    print("First signal:")    for i in range(len(fired_neurons)):        print("Neuron {0} triggered: {1}".format(i + 1, fired_neurons[i]))    print()    print(neurons, "\n")    fired_neurons = [False] * neuron_count    fired_neurons = if_fire(neuron_types, fired_neurons, "audio", response_rate                            )    neurons = pulse_neurons(neurons, fired_neurons, 3)    print("Second signal:")    for i in range(len(fired_neurons)):        print("Neuron {0} triggered: {1}".format(i + 1, fired_neurons[i]))    print()    print(neurons, "\n")if __name__ == '__main__':    main()