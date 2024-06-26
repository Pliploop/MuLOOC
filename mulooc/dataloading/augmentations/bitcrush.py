
from . import PedalBoardAudiomentation
from pedalboard import Pedalboard, Bitcrush



class BitcrushAudiomentation(PedalBoardAudiomentation):
    
    def __init__(self, board=None, sample_rate = 22050, mode='per_example', p=0.5, p_mode=None, output_type=None, randomize_parameters = True, *args, **kwargs):
        try:
            board = Pedalboard([
                Bitcrush(**kwargs)
            ])
        except:
            board = Pedalboard([
                Bitcrush()
            ])
        
    
        
        super().__init__(board, mode, p, p_mode, sample_rate , output_type=output_type, randomize_parameters=randomize_parameters)
        self.set_kwargs(**kwargs)
        