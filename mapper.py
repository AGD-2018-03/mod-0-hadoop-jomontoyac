#! /usr/bin/env python

##
## Esta es la función que mapea la entrada a parejas (clave, valor)
##
import sys


##
## Se usa una clase iterable para implementar el mapper.
##

class Mapper:
    
    def __init__(self, stream):
        ## 
        ## almacena el flujo de entrada como una
        ## variable del objeto
        ##
        self.stream = stream
    
    def emit(self, key, value):
        ##
        ## escribe al flujo estándar de salida
        ##
        sys.stdout.write("{}\t{}\n".format(key, value))
        
        
    def status(self, message):
        ##
        ## imprime un reporte en el flujo de error
        ## no se debe usar el stdout, ya que en este 
        ## unicamente deben ir las parejas (key, value)
        ##
        sys.stderr.write('reporter:status:{}\n'.format(message))

        
    def counter(self, counter, amount=1, group="ApplicationCounter"):
        ## 
        ## imprime el valor del contador
        ##
        sys.stderr.write('reporter:counter:{},{},{}\n'.format(group, counter, amount))
        
    def map(self):
        import re
        word_counter = 0
        ##
        ## imprime un mensaje a la entrada
        ##
        self.status('Iniciando procesamiento ')
            
        for word in self:
            ##
            ## cuenta la cantidad de palabras procesadas
            ##
            word_counter += 1
            try:
                valor = int(word)
            except ValueError:
                list_letras = word.split(',')
                for letra in list_letras:
                    self.emit(key=letra, value= valor)
                

            ##
            ## por cada palabra del flujo de datos
            ## emite la pareja (word, 1)
            ##
            

        ##
        ## imprime un mensaje a la salida
        ##
        self.counter('num_words', amount=word_counter)
        self.status('Finalizadno procesamiento ')

 
            
            
    def __iter__(self):
        ##
        ## itera sobre cada linea de código recibida
        ## a través del flujo de entrada
        ##
        for line in self.stream:
            ##
            ## itera sobre cada palabra de la línea
            ## (en los ciclos for, retorna las palabras
            ## una a una)
            ##
            for word in line.split():
                ##
                ## retorna la palabra siguiente en el
                ## ciclo for
                ##
                yield word
    

if __name__ == "__main__": 
    ##
    ## inicializa el objeto con el flujo de entrada
    ##
    mapper = Mapper(sys.stdin)
    
    ##
    ## ejecuta el mapper
    ##
    mapper.map()