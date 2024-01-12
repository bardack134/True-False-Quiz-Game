# Importamos todos los elementos del módulo data
import html
from data import *

# Importamos todos los elementos del módulo question_model
from question_model import *

from quiz_brain import *

# Creamos un nuevo objeto de la clase Question con los argumentos "cwvwcw" y "tyhj6ythty"
new_question=Question("cwvwcw", "tyhj6ythty")

# Creamos una lista vacía llamada question_bank
question_bank=[]

# Iteramos sobre cada diccionario en la lista question_data
for  diccionary in question_data:
    
    diccionary["question"]=html.unescape(diccionary["question"])
    # Creamos un nuevo objeto de la clase Question con los valores asociados a las claves "text" y "answer" en el diccionario actual
    new_question=Question(text=diccionary["question"], answer=diccionary["correct_answer"])
    # Añadimos el nuevo objeto Question a la lista question_bank
    question_bank.append(new_question)


# Imprimimos el texto de pregunta asociado al primer objeto de la lista question_bank
print(question_bank[0].answer)    

#recibe como parametro la lista de preguntas llamada "question_bank"
quiz=QuizBrain(question_list=question_bank)



while quiz.still_has_question():
    
    quiz.next_question()