from elemento import Elemento as el
from no import No as no
import numpy as np

class CarregDist( ) :

    def __init__( self , forca_eq_l = { } , forca_eq_g = { } ) :

        self.forca_eq_l = forca_eq_l
        self.forca_eq_g = forca_eq_g

    def carga_dist( self , n_elem , q ) :

        if el().ligacao[ n_elem ][ 0 ] == 'engaste' and el().ligacao[ n_elem ][ 1 ] == 'engaste' :

            MA = q * ( el().Le[ n_elem ] ) ** 2 / 12
            MB = - q * ( el().Le[ n_elem ] ) ** 2 / 12
            RA = ( ( q * ( el().Le[ n_elem ] ) ** 2 / 2 ) + MB + MA ) / el().Le[ n_elem ]
            RB = q * el().Le[ n_elem ] - RA
            self.forca_eq_l[ n_elem ] = np.array( [ [ 0 ] , [ RA ] , [ MA ] , [ 0 ] , [ RB ] , [ MB ] ] )

        if el().ligacao[ n_elem ][ 0 ] == 'rotula' and el().ligacao[ n_elem ][ 1 ] == 'rotula' :
            MA = 0
            MB = 0
            RA = q * el().Le[ n_elem ] / 2
            RB = q * el().Le[ n_elem ] / 2
            self.forca_eq_l[ n_elem ] = np.array( [ [ 0 ] , [ RA ] , [ MA ] , [ 0 ] , [ RB ] , [ MB ] ] )

        # rotação dos vetores de forças equivalentes

        self.forca_eq_g[ n_elem ] = el().RT[ n_elem ].dot( self.forca_eq_l[ n_elem ] )

        # Vetor de Espalhamento

        i = el().elem[ n_elem ][ 0 ]
        j = el().elem[ n_elem ][ 1 ]

        eT = [ 3 * i - 3 , 3 * i - 2 , 3 * i - 1 , 3 * j - 3 , 3 * j - 2 , 3 * j - 1 ]

        # preenchimento do vetor de forças equivalentes
        
        linha_aux2 = - 1

        for already in eT:
            linha_aux2 += 1
            no().forca_eq_tot[ already ][ 0 ] += self.forca_eq_g[ n_elem ][ linha_aux2 ][ 0 ]

q_load = CarregDist()