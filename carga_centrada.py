from no import No
import numpy as np

class ForcaNodal( ) :

    def forca_nod( self , node_id , fx , fy  , Mz ) :

        No().forca_nodal[ 3 * ( node_id - 1 ) + 0 ][ 0 ] += fx
        No().forca_nodal[ 3 * ( node_id - 1 ) + 1 ][ 0 ] += fy
        No().forca_nodal[ 3 * ( node_id - 1 ) + 2 ][ 0 ] += Mz


point_load = ForcaNodal()