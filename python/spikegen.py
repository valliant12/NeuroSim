class Spike:
    def __init__(self, **parameters):
        self.__dict__.update(parameters)

    def assign_parameters(self, **parameters):
        """
        Assign an arbitrary number of parameters.
        _______________________________________________________________________

        Possible parameters:

        rate: Spike rate (Hz)
        train_length: Duration of a single train (sec)
        mode:
             - "constant"
             - "bursty"
             - "random"

            constant:
                 - The average rate of of fire does not change
            bursty:
                 - Spikes occur in rapid bursts, separated by regions of
                 reduced activity
                 - Need to supply a tuple containing two scalars - "burst":
                     - Average number of spikes per burst
                     - Average length of rest (interspike duration) (sec)
            random:
                 - Train is full of noise, not "real" spikes
        repeats: The number of trains in the interval
        """
        for i in parameters:
            setattr(self,i,parameters[i])

        print(self.__dict__.items())

audio_parameters = {
        "rate": 5,
        "train_length": 10,
        "mode": "bursty",
        "burst": (3,1)
}

burst = Spike(rate = 0.5)
burst.assign_parameters(**audio_parameters)


