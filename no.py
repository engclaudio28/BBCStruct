
class No() :

    def __init__( self , CN = [ ] , restricao = [ ] , indice = { } , forca_nodal = [ ] , forca_eq_tot = [ ] ,
                forca_tot = [ ] , n_no = 0 ) :

        self.CN = CN
        self.restricao = restricao
        self.indice = indice
        self.forca_nodal = forca_nodal
        self.forca_eq_tot = forca_eq_tot
        self.forca_tot = forca_tot
        self.n_no = n_no

    def no( self , x , y ) :
        
        self.n_no += 1

        self.CN.append( [ x , y ] )
        self.indice[ self.n_no ] = [ x , y ]
        
        for restriction in range( 3 ) :
            self.restricao.append( 1 )
        for equivalente in range( 3 ) :
            self.forca_eq_tot.append( [ 0 ] )
        for nodal in range( 3 ) :
            self.forca_nodal.append( [ 0 ] )
        for force in range( 3 ) :
            self.forca_tot.append( [ 0 ] )


node = No()