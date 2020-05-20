from logic.Instrument import Instrument as i


class Fiddle(i):
    NAME = "Fiddle"

    def tune(self):
        super().tune()
        return self.NAME + " is tuned"

    def play(self):
        super().play()
        return self.NAME + " is Playing now"
