from elemento import element as el

class Material:

    def __init__( self , mat = { } ) :
      self.mat = mat

    def concreto( self , n_elem ) :
      self.mat[ n_elem ] = 25000000

    def aco( self , n_elem ) :
      self.mat[ n_elem ] = 205000000

    def cprb190( self , n_elem ):
      self.mat[ n_elem ] = 195000000

    def generic( self , modulo_elasticidade , n_elem ):
      self.mat[ n_elem ] = modulo_elasticidade


material = Material()