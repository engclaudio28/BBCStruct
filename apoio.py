from no import node

# identificacao dos graus de liberdade

class Apoio():

    def __init__( self , apoio_i = { } ):
        self.apoio_i = apoio_i
    
    def rolete( self , node_id ) :

        x = node.indice[ node_id ][ 0 ]
        y = node.indice[ node_id ][ 1 ]

        for i in range( len( node.CN ) ) :
            for j in range( 1 ) :
                if node.CN[ i ][ j ] == x and node.CN[ i ][ j + 1 ] == y : 
                    node.restricao[ 3 * i + 1 ] = 0
        
        self.apoio_i[ node_id ] = 'rolete'

    def pino( self , node_id ) :

        x = node.indice[ node_id ][ 0 ]
        y = node.indice[ node_id ][ 1 ]

        for i in range( len( node.CN ) ) :
            for j in range( 1 ) :
                if node.CN[ i ][ j ] == x and node.CN[ i ][ j + 1 ] == y : 
                    node.restricao[ 3 * i ] = 0
                    node.restricao[ 3 * i + 1 ] = 0
        
        self.apoio_i[ node_id ] = 'pino'
            
    def engaste( self , node_id ) :

        x = node.indice[ node_id ][ 0 ]
        y = node.indice[ node_id ][ 1 ]

        for i in range( len( node.CN ) ) :
            for j in range( 1 ) :
                if node.CN[ i ][ j ] == x and node.CN[ i ][ j + 1 ] == y : 
                    node.restricao[ 3 * i ] = 0
                    node.restricao[ 3 * i + 1 ] = 0
                    node.restricao[ 3 * i + 2 ] = 0

        self.apoio_i[ node_id ] = 'engaste'

apoio = Apoio()