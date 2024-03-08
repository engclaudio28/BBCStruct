import matplotlib.pyplot as plt
from no import No as no

class PlotNos() :
        
    data = [ ]
    
    fig , ax = plt.subplots()
        
    for bag in range( len( no().CN ) ):

        data.append( no().CN[ bag ] )

    for i in range( len( data ) ) :
        
        plt.text( data[ i ][ 0 ] + 0.1 , data[ i ][ 1 ] + 0.1 , str( i + 1 ) )
        
        plt.plot( data[ i ][ 0 ] + 0.1 , data[ i ][ 1 ] + 0.1 , i + 1 )
    
    ax.set_facecolor('k')
    x,y = zip( * data )

    plt.scatter( x , y )
    

    ax.set_yticks( [ ] )
    ax.set_xticks( [ ] )

    plt.axis('off')

    plt.show()

plot_nodes = PlotNos()