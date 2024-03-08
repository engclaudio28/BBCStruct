import numpy as np


class Geometria( ) :

    def __init__( self, secao = { } ) :
        self.secao = secao

    def generic( self , Area , Inercia , n_elem ) :
        self.secao[ n_elem ] = [ Area , Inercia ]

    def ret( self , base , altura , n_elem ) :
        Area = base * altura
        Inercia = base * altura ** 3 / 12
        self.secao[ n_elem ] = [ Area , Inercia ]

    
    #def circ( self , Area , n_elem ) :
    #    d = ( 4 * Area / np.pi ) ** 0.5
    #    Inercia = np.pi * d ** 4 / 64
    #    self.secao[ n_elem ] = [ Area , Inercia ]


    def circ( self , diametro_d , n_elem ) :
        Area = np.pi * diametro_d ** 2 / 4
        Inercia = np.pi * diametro_d ** 4 / 64
        self.secao[ n_elem ] = [ Area , Inercia ]
    

section = Geometria()