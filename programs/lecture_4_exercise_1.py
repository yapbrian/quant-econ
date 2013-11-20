class ecdf:
    def __init__(self, initobs):
        self.observations = initobs

    def __call__(self, x_n):
        result = 0.0
        for obs in self.observations:
            if obs <= x_n:
                result += 1
        return result / len(self.observations)

