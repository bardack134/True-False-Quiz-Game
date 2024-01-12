# Importamos todos los elementos del módulo data
from data import *

class Game():
    
    def __init__(self, text, answer):
        self.text=text
        
        self.answer=answer
        
    def question(self):
        """Metodo que crea la lista de preguntas"""
       
        # Creamos una lista vacía llamada question_bank
        question_bank=[]

        # Iteramos sobre cada diccionario en la lista question_data
        for  diccionary in question_data:
            # Imprimimos el diccionario actual
            print(diccionary)
            # Imprimimos el valor asociado a la clave "text" en el diccionario actual
            print(diccionary["text"])
            # Imprimimos el valor asociado a la clave "answer" en el diccionario actual
            print(diccionary["answer"])
            # Imprimimos una línea en blanco
            print()
            
            # Creamos un nuevo objeto de la clase Question con los valores asociados a las claves "text" y "answer" en el diccionario actual
            
            
            
            # Añadimos el nuevo objeto Question a la lista question_bank
            question_bank.append(new_question)
            
        # Imprimimos el primer objeto de la lista question_bank
        print(question_bank[0])    


        # Imprimimos el texto de pregunta asociado al primer objeto de la lista question_bank
        print(question_bank[0].answer)    

        #recibe como parametro la lista de preguntas llamada "question_bank"
        quiz_brain=QuizBrain(question_list=question_bank)
        
