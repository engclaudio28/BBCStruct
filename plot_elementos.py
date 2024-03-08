from matplotlib import pyplot as plt
from elemento import element as el
from no import node as nd
from apoio import apoio as ap

class PlotElements() :

    fig , ax = plt.subplots()

    for well in range( 1 , len( el.Le ) + 1 , 1 ) :
        
        if el.ligacao[ well ][ 0 ] == 'engaste' and el.ligacao[ well ][ 1 ] == 'engaste' :

            plt.plot(  [ el.coord_elem[ well ][ 0 ]  , el.coord_elem[ well ][ 1 ] ] , [ el.coord_elem[ well ][ 2 ]  , el.coord_elem[ well ][ 3 ] ] , linewidth = 0.5 , color = 'k' )
        
        if el.ligacao[ well ][ 0 ] == 'rotula' and el.ligacao[ well ][ 1 ] == 'rotula' :

                plt.plot( [ el.coord_elem[ well ][ 0 ] , el.coord_elem[ well ][ 1 ] ] , [ el.coord_elem[ well ][ 2 ] , el.coord_elem[ well ][ 3 ] ] , linewidth = 0.5 , color = 'blue'  )
                plt.plot( el.coord_elem[ well ][ 0 ] , el.coord_elem[ well ][ 2 ] , 'yo' , alpha = 0.6 )
                plt.plot( el.coord_elem[ well ][ 1 ] , el.coord_elem[ well ][ 3 ] , 'yo' , alpha = 0.6 )

    for wonder in range( 1 , len( el.Le ) + 1 , 1 ) :
        
        if el.ligacao[ wonder ][ 0 ] == 'engaste' and el.ligacao[ wonder ][ 1 ] == 'engaste' :
            plt.text(   ( ( el.coord_elem[ wonder ][ 0 ] + el.coord_elem[ wonder ][ 1 ] ) / 2 ) ,
                        ( ( el.coord_elem[ wonder ][ 2 ] + el.coord_elem[ wonder ][ 3 ] ) / 2 ) ,
                        wonder , fontsize = 2 ,
                        color = 'blue' )

        if el.ligacao[ wonder ][ 0 ] == 'rotula' and el.ligacao[ wonder ][ 1 ] == 'rotula' :
            plt.text(   ( ( el.coord_elem[ wonder ][ 0 ] + el.coord_elem[ wonder ][ 1 ] ) / 2 ) ,
                        ( ( el.coord_elem[ wonder ][ 2 ] + el.coord_elem[ wonder ][ 3 ] ) / 2 ) ,
                        wonder , fontsize = 2 ,
                        color = 'teal' )

    for amazing in ap.apoio_i:
        
        if ap.apoio_i[ amazing ] == 'rolete':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] , 'g^' )
        
        if ap.apoio_i[ amazing ] == 'pino':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] , 'b^' )
        
        if ap.apoio_i[ amazing ] == 'engaste':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] , 'rs' )
    
    ax.set_xticks( [ ] )
    ax.set_yticks( [ ] )
    ax.set_facecolor('dimgrey')
    plt.title(' SEMI-HARPA ' , color = 'k')
    plt.axis('off')

    

    plt.show()

plot_elements = PlotElements()