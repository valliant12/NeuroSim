import base_class_version

import random

import matplotlib.pyplot as plt
import numpy as np
import pprint

class Spike:
    def __init__(self):
        pass

    def assign_parameters(self, **parameters):
        """
        Assign an arbitrary number of parameters.
        _______________________________________________________________________

        Possible parameters:

        rate: Spike rate (Hz)
        train_length: Duration of a single train (sec)
        mode: The behaviour of the fire rate
             - "constant"
             - "burst"
             - "random"

            constant:
                 - The average rate of of fire does not change
            bursty:
                 - Spikes occur in rapid bursts, separated by regions of
                 reduced activity
                 - Need to supply a tuple containing two scalars - "burst_parameters":
                     - Average number of spikes per burst
                     - Average length of rest (interspike duration) (sec)
            noisy:
                 - Train is full of noise, not "real" spikes
        repeats: The number of trains in the interval
        """
        for i in parameters:
            setattr(self, i.lower(), parameters[i])

        print(self.__repr__())

    def gen_spike_train(self):
        try:
            # Assign the number of times to repeat the train
            self.repeats = 1 if not self.repeats else self.repeats

            spikes = np.zeros(shape=(self.repeats, self.train_length))
            print(spikes, self.repeats, np.shape(spikes))

        except ValueError:
            print(f"Number of repeats is {self.repeats}. Should be int > 0.\n"
                   "Unable to generate spike train.")
            return None

        except TypeError:
            print(f"Number of repeats is {self.repeats}. Should be int > 0.\n"
                   "Unable to generate spike train.")
            return None

        if self.mode.lower() == "constant":
            spike_count_array = np.random.poisson(self.rate * self.train_length, (1, self.repeats))[0]

            spikes = []

            print(spike_count_array, "cat")

            # Create a nested list containing the times of each spike

            for i in range(0, self.repeats):
                spike_times = sorted([random.random() * self.train_length for\
                    j in range(spike_count_array[i])])
                spikes += [spike_times]

            pprint.pprint(spikes)

            return spikes

        if self.mode.lower() == "burst":
            try:
                # Are burst parameters defined?
                spikes_per_burst = self.burst_parameters[0]
                interspike_duration = self.burst_parameters[1]

            except AttributeError:
                spikes_per_burst = 1
                interspike_duration = 0.1
                print(f"No burst parameters defined, assuming ",
                       "{spikes_per_burst} spikes per burst and interspike",
                       "duration of {interspike_duration}.")

            burst_freq = self.rate / spikes_per_burst

            for i in range(0, self.repeats):
                burst_count = np.random.poisson(burst_freq * self.train_length)
                burst_list = []

                for j in range(burst_count):
                    spike_count_array = np.random.poisson(spikes_per_burst)

                    if spike_count_array > 0:
                        burst_list[j] =

                print(burst_count)




audio_parameters = {
        "identity": "audio",
        "rate": 10,
        "train_length": 5,
        "mode": "BUrsT",
        #"burst_parameters": (3, 1),
        "repeats": 2
}

burst = Spike()
burst.assign_parameters(**audio_parameters)
burst.spikes = burst.gen_spike_train()


