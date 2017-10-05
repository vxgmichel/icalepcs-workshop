from facadedevice import combined_attribute, Facade

class Average(Facade):

    @combined_attribute(
        dtype=float,
        property_name='AttributesToAverage')
    def average(self, *args):
        return sum(args) / len(args)

