from no import node as nd
from geometria import section as st
from material import material as mt
from elemento import element as el
import numpy as np
from carregdist import CarregDist as cd


Kglobal = np.zeros( ( 3 * len( nd.CN ) , 3 * len( nd.CN ) ) )


class MatrizRigidez() :

      def __init__( self , kl = { } ) :

            self.kl = kl

      def rigidez( self , n_elem ) :

            A = st.secao[ n_elem ][ 0 ]
            I = st.secao[ n_elem ][ 1 ]
            E = mt.mat[ n_elem ]
            L = el.Le[ n_elem ]

            if el.ligacao[ n_elem ][ 0 ] == 'engaste' and el.ligacao[ n_elem ][ 1 ] == 'engaste' :

                        self.kl[ n_elem ] = np.array( [ [ E * A / L   , 0                     , 0                    , - E * A / L          , 0                     , 0                    ] ,
                                                        [ 0           , 12 * E * I / L ** 3   , 6 * E * I / L ** 2   , 0                    , - 12 * E * I / L ** 3 , 6 * E * I / L ** 2   ] ,
                                                        [ 0           , 6 * E * I / L ** 2    , 4 * E * I / L        , 0                    , - 6 * E * I / L ** 2  , 2 * E * I / L        ] ,
                                                        [ - E * A / L , 0                     , 0                    , E * A / L            , 0                     , 0                    ] ,
                                                        [ 0           , - 12 * E * I / L ** 3 , - 6 * E * I / L ** 2 , 0                    , 12 * E * I / L ** 3   , - 6 * E * I / L ** 2 ] ,
                                                        [ 0           , 6 * E * I / L ** 2    , 2 * E * I / L        , 0                    , - 6 * E * I / L ** 2  , 4 * E * I / L        ] ] )

            if el.ligacao[ n_elem ][ 0 ] == 'rotula' and el.ligacao[ n_elem ][ 1 ] == 'rotula' :
                        
                        self.kl[ n_elem ] = np.array( [ [ E * A / L   , 0 , 0 , - E * A / L , 0 , 0 ] ,
                                                        [ 0           , 0 , 0 , 0           , 0 , 0 ] ,
                                                        [ 0           , 0 , 0 , 0           , 0 , 0 ] ,
                                                        [ - E * A / L , 0 , 0 , E * A / L   , 0 , 0 ] ,
                                                        [ 0           , 0 , 0 , 0           , 0 , 0 ] ,
                                                        [ 0           , 0 , 0 , 0           , 0 , 0 ] ] )

            # Matriz de rigidez elementar rotacionada
            
            kg = el.RT[ n_elem ].dot( self.kl[ n_elem ].dot( el.Re[ n_elem ] ) )

            # Vetor de Espalhamento

            i = el.elem[ n_elem ][ 0 ]
            j = el.elem[ n_elem ][ 1 ]
            
            eT = [ 3 * i - 3 , 3 * i - 2 , 3 * i - 1 , 3 * j - 3 , 3 * j - 2 , 3 * j - 1 ]

            # Matriz de rigidez global

            linha_aux = - 1

            for linha in eT:
                  linha_aux += 1
                  coluna_aux = - 1
                  for coluna in eT:
                        coluna_aux += 1
                        Kglobal[ linha ][ coluna ] += kg[ linha_aux ][ coluna_aux ]


for i in range( 1 , len( el.Le ) + 1 , 1 ) :
      MatrizRigidez().rigidez( i )


class CargaNodTot() :

      for what in range( 3 * len( nd.CN ) ) :
            nd.forca_tot[ what ][ 0 ] = nd.forca_nodal[ what ][ 0 ] - nd.forca_eq_tot[ what ][ 0 ]

      nd.forca_tot = np.array( nd.forca_tot )

CargaNodTot()


class ZeroUm():

      for ready in range( 3 * len( nd.CN ) ) :
            if nd.restricao[ ready ] == 0 :
                  nd.forca_tot[ ready ][ 0 ] = 0.0

      for suftiness in range( 3 * len( nd.CN ) ) :
            if nd.restricao[ suftiness ] == 0 :
                  for colum in range( 3 * len( nd.CN ) ) :
                        Kglobal[ suftiness ][   colum   ] = 0.0
                        Kglobal[ suftiness ][ suftiness ] = 1.0


ZeroUm()


from numpy import linalg

Kg_inv = np.linalg.inv( Kglobal )
Ug = Kg_inv.dot( nd.forca_tot )

#for i in range( 1 , 3 * 66 , 3 ):
#      print( Ug[ i ][ 0 ] )


class Deslocamentos() :
     
      def __init__( self , ul = { } ) :

            self.ul = ul

      def deslocamento_elemento( self , n_elem ) :

            ug = np.zeros( ( 6 , 1 ) )

            i = el.elem[ n_elem ][ 0 ]
            j = el.elem[ n_elem ][ 1 ]

            eT = [ 3 * i - 3 , 3 * i - 2 , 3 * i - 1 , 3 * j - 3 , 3 * j - 2 , 3 * j - 1 ]

            linha_aux3 = - 1

            for male in eT:
                  linha_aux3 += 1
                  ug[ linha_aux3 ] = Ug[ male ]
        
            self.ul[ n_elem ] = el.Re[ n_elem ].dot( ug )


for i in range( 1 , len( el.Le ) + 1 , 1 ) :
      Deslocamentos().deslocamento_elemento( i )




import pandas as pd

class EsforcoFinal( ) :

      def __init__( self , f_final = { } , n_elem = 0 ) :

            self.f_final = f_final
            self.n_elem = n_elem

      def esforco_final( self ) :

            self.n_elem += 1
            self.f_final[ self.n_elem ] = MatrizRigidez().kl[ self.n_elem ].dot( Deslocamentos().ul[ self.n_elem ] )

            for i in range( 6 ) :
                  self.f_final[ self.n_elem ][ i ][ 0 ] = round( self.f_final[ self.n_elem ][ i ][ 0 ] , 4 )

            if self.n_elem in cd().forca_eq_l.keys() :
                  for happy in range( 6 ) :
                        self.f_final[ self.n_elem ][ happy ][ 0 ] += round( cd().forca_eq_l[ self.n_elem ][ happy ][ 0 ] , 4 )

            resultado = pd.DataFrame( {   'N' : [ self.f_final[ self.n_elem ][ 0 ][ 0 ] , self.f_final[ self.n_elem ][ 3 ][ 0 ] ] ,
                                          'V':[ self.f_final[ self.n_elem ][ 1 ][ 0 ] , self.f_final[ self.n_elem ][ 4 ][ 0 ] ] ,
                                          'M': [ self.f_final[ self.n_elem ][ 2 ][ 0 ] , self.f_final[ self.n_elem ][ 5 ][ 0 ] ] } ,
                                          index = [ 'inicio' , 'fim' ] )

esforces_finally = EsforcoFinal()


class Results():

     def make( self ):
            for i in range( 1 , len( el.Le ) + 1 , 1 ) :
                  esforces_finally.esforco_final()

result = Results()