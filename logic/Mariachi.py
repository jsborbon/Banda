from logic.Instrument import *
from logic.Fiddle import *
from logic.Guitar import *
from logic.Guitarron import *
from logic.Trompet import *
from logic.Vihuela import *


class Mariachi:

    instrumento = Instrument()
    listInstrument = [
        Fiddle(),
        Guitar(),
        Guitarron(),
        Trompet(),
        Vihuela()
    ]

    def assignInstrument(self, numInstrumento):
        """Asigna un instrumento al mariachi"""
        self.instrumento = self.listInstrument[numInstrumento]
        return self.instrumento.NAME

    def tuneInstrument(self):
        """afina el instrumento del mariachi"""
        return self.instrumento.tune()

    def playInstrument(self):
        """El mariachi toca"""
        return self.instrumento.play()
