from turtle import color
from matplotlib import pyplot as plt
from elemento import element as el
from no import node as nd
from apoio import apoio as ap
from matrizrigidez import esforces_finally as ef
import numpy as np

class PlotResults() :

    number_estai = 0

    fig , ax = plt.subplots()
    
    for well in range( 1 , len( el.Le ) + 1 , 1 ) :
        
        if el.ligacao[ well ][ 0 ] == 'engaste' and el.ligacao[ well ][ 1 ] == 'engaste' :

            plt.plot(  [ el.coord_elem[ well ][ 0 ]  , el.coord_elem[ well ][ 1 ] ] , [ el.coord_elem[ well ][ 2 ]  , el.coord_elem[ well ][ 3 ] ] , linewidth = 2.5 , color = 'k' )
        
        if el.ligacao[ well ][ 0 ] == 'rotula' and el.ligacao[ well ][ 1 ] == 'rotula' :

            plt.plot(  [ el.coord_elem[ well ][ 0 ]  , el.coord_elem[ well ][ 1 ] ] , [ el.coord_elem[ well ][ 2 ]  , el.coord_elem[ well ][ 3 ] ] , linewidth = 0.5 , color = 'blue'  )
            plt.plot( el.coord_elem[ well ][ 0 ] , el.coord_elem[ well ][ 2 ] , 'yo' , alpha = 0.6 )
            plt.plot( el.coord_elem[ well ][ 1 ] , el.coord_elem[ well ][ 3 ] , 'yo' , alpha = 0.6 )
    
   
    for wonder in range( 1 , len( el.Le ) + 1 , 1 ) :

        if el.ligacao[ wonder ][ 0 ] == 'rotula' and el.ligacao[ wonder ][ 1 ] == 'rotula' :

            number_estai += 1

            if el.coord_elem[ wonder ][ 3 ] > el.coord_elem[ wonder ][ 2 ] :
        
                plt.text(   ( abs( el.coord_elem[ wonder ][ 1 ] + el.coord_elem[ wonder ][ 0 ] ) / 2 ) ,
                            ( abs( el.coord_elem[ wonder ][ 3 ] + el.coord_elem[ wonder ][ 2 ] ) / 2 ) ,
                            ef.f_final[ wonder ][ 3 ][ 0 ] , fontsize = 10 ,
                            color = 'red' )
            
            if el.coord_elem[ wonder ][ 3 ] < el.coord_elem[ wonder ][ 2 ] :
        
                plt.text(   ( abs( el.coord_elem[ wonder ][ 1 ] + el.coord_elem[ wonder ][ 0 ] ) / 2 ) ,
                            ( abs( el.coord_elem[ wonder ][ 3 ] + el.coord_elem[ wonder ][ 2 ] ) / 2 ) ,
                            ef.f_final[ wonder ][ 3 ][ 0 ] , fontsize = 10 ,
                            color = 'red'  )
    


    for amazing in ap.apoio_i:
        
        if ap.apoio_i[ amazing ] == 'rolete':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] - 2 , 'g^' )
        
        if ap.apoio_i[ amazing ] == 'pino':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] - 2 , 'b^' )
        
        if ap.apoio_i[ amazing ] == 'engaste':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] , 'rs'  )
    
    ax.set_xticks( [ ] )
    ax.set_yticks( [ ] )
    

    plt.axis('off')
    plt.title(' ANÁLISE LINEAR ' , color = 'blue')
    ax.set_facecolor("yellow")
    plt.show()

plot_results = PlotResults()

