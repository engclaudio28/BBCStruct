from no import No
import numpy as np


class Elemento( ) :

    def __init__( self , Re = { } , RT = { } , Le = { } , elem = { } , ligacao = { } , n_elem = 0 , coord_elem = { } , arct = { } ) :
        
        self.Re = Re
        self.RT = RT
        self.Le = Le
        self.elem = elem
        self.ligacao = ligacao
        self.n_elem = n_elem
        self.coord_elem = coord_elem
        self.arct = arct

    def elemento( self, indice_i , indice_j ) :
        
        self.n_elem += 1

        xi = No().indice[ indice_i ][ 0 ]
        yi = No().indice[ indice_i ][ 1 ]
        xf = No().indice[ indice_j ][ 0 ]
        yf = No().indice[ indice_j ][ 1 ]

        dx = xf - xi
        dy = yf - yi

        Li = ( dx ** 2 + dy ** 2 ) ** 0.5

        cx = dx / Li
        cy = dy / Li

        if dx == 0 :
            theta = 0
            
        if dx != 0 :
            theta = np.arctan( dy / dx ) * 180 / np.pi

        R = np.array(   [   [   cx , cy , 0 ,   0  , 0  , 0 ] , 
                            [ - cy , cx , 0 ,   0  , 0  , 0 ] , 
                            [ 0    , 0  , 1 ,   0  , 0  , 0 ] , 
                            [ 0    , 0  , 0 ,   cx , cy , 0 ] , 
                            [ 0    , 0  , 0 , - cy , cx , 0 ] ,
                            [ 0    , 0  , 0 ,   0  , 0  , 1 ] ] )

        self.Re[ self.n_elem ] = R
        self.RT[ self.n_elem ] = R.T
        self.Le[ self.n_elem ] = Li
        self.elem[ self.n_elem ] = [ indice_i , indice_j ]
        self.ligacao[ self.n_elem ] = [ 'engaste' , 'engaste' ]
        self.coord_elem[ self.n_elem ] = [ xi , xf , yi , yf ]
        self.arct[ self.n_elem ] = theta

element = Elemento()