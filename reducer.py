#!/usr/bin/env python

import sys
import itertools

class Reducer:
    
    def __init__(self, stream):
        self.stream = stream
        
    def emit(self, key, value):
        sys.stdout.write("{}\t{}\n".format(key, value)) 

    def reduce(self):
        ##
        ## Esta función reduce los elementos que 
        ## tienen la misma clave
        ##
        for key, group in itertools.groupby(self, lambda x: x[0]):
            list_keys = []
            is_first_num = True
            for _, val in group:
                if is_first_num is True:
                    is_first_num = False
                    list_keys.append(val)
                else:
                    #if set([val]).intersection(list_keys):
                    #    pass
                    #else:
                    list_keys.append(val)
                #list_keys.sort()
                tuples = tuple(list_keys)
            
            self.emit(key=key, value=','.join(map(str, tuples)))
                
                
                
                        
                

    def __iter__(self):
        
        for line in self.stream:
            ##
            ## Lee el stream de datos y lo parte 
            ## en (clave, valor)
            ##
            key, val = line.split("\t") 
            val = int(val)
            ##
            ## retorna la tupla (clave, valor)
            ## como el siguiente elemento del ciclo for
            ##
            yield (key, val)


if __name__ == '__main__': 
  
    reducer = Reducer(sys.stdin)
    reducer.reduce()