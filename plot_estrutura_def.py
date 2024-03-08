from matplotlib import pyplot as plt
from elemento import element as el
from no import node as nd
from apoio import apoio as ap
import numpy as np
from matrizrigidez import Ug

Ug = np.reshape( Ug , ( len( nd.CN ) , 3 ) )

class PlotElementsDef( ) :

    def make( self , scale ) :

        fig , ax = plt.subplots( )

        for well in range( 1 , len( el.Le ) + 1 , 1 ) :

            #if el.ligacao[ well ][ 0 ] == 'engaste' and el.ligacao[ well ][ 1 ] == 'engaste' :

            #    plt.plot(  [ el.coord_elem[ well ][ 0 ]  , el.coord_elem[ well ][ 1 ] ] , [ el.coord_elem[ well ][ 2 ]  , el.coord_elem[ well ][ 3 ] ] , linewidth = 2.5 , color = 'k' )

            if el.ligacao[ well ][ 0 ] == 'rotula' and el.ligacao[ well ][ 1 ] == 'rotula' :

                plt.plot( [ el.coord_elem[ well ][ 0 ] + ( Ug[ el.elem[ well ][ 0 ] - 1 ][ 0 ] ) * scale , el.coord_elem[ well ][ 1 ] + ( Ug[ el.elem[ well ][ 1 ] - 1 ][ 0 ] ) * scale ] , [ el.coord_elem[ well ][ 2 ] + ( Ug[ el.elem[ well ][ 0 ] - 1 ][ 1 ] ) * scale , el.coord_elem[ well ][ 3 ] + ( Ug[ el.elem[ well ][ 1 ] - 1 ][ 1 ] ) * scale ] , linewidth = 0.5 , color = 'blue'  )
                plt.plot( el.coord_elem[ well ][ 0 ] + ( Ug[ el.elem[ well ][ 0 ] - 1 ][ 0 ] ) * scale , el.coord_elem[ well ][ 2 ] + ( Ug[ el.elem[ well ][ 0 ] - 1 ][ 1 ] ) * scale, 'yo' , alpha = 0.6 )
                plt.plot( el.coord_elem[ well ][ 1 ] + ( Ug[ el.elem[ well ][ 1 ] - 1 ][ 0 ] ) * scale , el.coord_elem[ well ][ 3 ] + ( Ug[ el.elem[ well ][ 1 ] - 1 ][ 1 ] ) * scale , 'yo' , alpha = 0.6 )

        for amazing in ap.apoio_i :

            if ap.apoio_i[ amazing ] == 'rolete':
                plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] - 0.15 , 'g^' )

            if ap.apoio_i[ amazing ] == 'pino':
                plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] - 0.15 , 'b^' )

            if ap.apoio_i[ amazing ] == 'engaste':
                plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] , 'rs' )

        for i in range( 1 , len( el.Le ) + 1 , 1 ) :
            plt.plot( [ el.coord_elem[ i ][ 0 ] + ( Ug[ el.elem[ i ][ 0 ] - 1 ][ 0 ] ) * scale , el.coord_elem[ i ][ 1 ] + ( Ug[ el.elem[ i ][ 1 ] - 1 ][ 0 ] ) * scale ] , [ el.coord_elem[ i ][ 2 ] + ( Ug[ el.elem[ i ][ 0 ] - 1 ][ 1 ] ) * scale , el.coord_elem[ i ][ 3 ] + ( Ug[ el.elem[ i ][ 1 ] - 1 ][ 1 ] ) * scale ] , linewidth = 2 , linestyle = 'dotted' , color = 'blue'  )

        ax.set_xticks( [ ] )
        ax.set_yticks( [ ] )
        ax.set_facecolor('k')
        plt.axis('off')

        plt.show( )

plot_elements_def = PlotElementsDef()