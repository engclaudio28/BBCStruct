from matplotlib import pyplot as plt
from elemento import element as el
from no import node as nd
from apoio import apoio as ap

class PlotElements() :

    fig , ax = plt.subplots()

    for well in range( 1 , len( el.Le ) + 1 , 1 ) :
        
        plt.plot(  [ el.coord_elem[ well ][ 0 ]  , el.coord_elem[ well ][ 1 ] ] , [ el.coord_elem[ well ][ 2 ]  , el.coord_elem[ well ][ 3 ] ] )

    for wonder in range( 1 , len( el.Le ) + 1 , 1 ) :
        
        plt.text(   ( ( el.coord_elem[ wonder ][ 0 ] + el.coord_elem[ wonder ][ 1 ] ) / 2 ) + 0.1 ,
                    ( ( el.coord_elem[ wonder ][ 2 ] + el.coord_elem[ wonder ][ 3 ] ) / 2 ) + 0.2 ,
                    wonder ,
                    rotation = el.arct[ wonder ]  )

    for amazing in ap.apoio_i:
        
        if ap.apoio_i[ amazing ] == 'rolete':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] - 0.15 , 'g^' )
        
        if ap.apoio_i[ amazing ] == 'pino':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] - 0.15 , 'b^' )
        
        if ap.apoio_i[ amazing ] == 'engaste':
            plt.plot( nd.indice[ amazing ][ 0 ] , nd.indice[ amazing ][ 1 ] , 'rs' )
    
    ax.set_xticks( [ ] )
    ax.set_yticks( [ ] )
    ax.set_facecolor('k')
    plt.axis('off')

    

    plt.show()

plot_elements = PlotElements()

