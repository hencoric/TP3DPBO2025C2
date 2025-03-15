class Overclocking:
    def __init__(self, max_speed_ghz=0.0):
        self._max_speed_ghz = max_speed_ghz

    def set_max_speed_ghz(self, max_speed_ghz):
        self._max_speed_ghz = max_speed_ghz

    def get_max_speed_ghz(self):
        return self._max_speed_ghz