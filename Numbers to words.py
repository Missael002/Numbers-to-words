class ConversorNumerosPalabras:
    def __init__(self):
        # Diccionario de números a palabras en inglés
        self.numeros_a_palabras = {
            1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
            20: "twenty", 21: "twenty-one", 22: "twenty-two", 23: "twenty-three",
            24: "twenty-four", 25: "twenty-five", 26: "twenty-six", 27: "twenty-seven",
            28: "twenty-eight", 29: "twenty-nine", 31: "thirty-one", 32: "thirty-two",
            33: "thirty-three", 34: "thirty-four", 35: "thirty-five", 36: "thirty-six",
            37: "thirty-seven", 38: "thirty-eight", 39: "thirty-nine", 40: "forty",
            41: "forty-one", 42: "forty-two", 43: "forty-three", 44: "forty-four",
            46: "forty-six", 47: "forty-seven", 48: "forty-eight", 49: "forty-nine",
            50: "fifty", 51: "fifty-one", 52: "fifty-two", 53: "fifty-three",
            54: "fifty-four", 55: "fifty-five", 56: "fifty-six", 57: "fifty-seven",
            58: "fifty-eight", 59: "fifty-nine"
        }


    def convertir_hora(self, num):
        #Convertir las hora a palabras
        try:
            if num == 0:
                return "twelve"
            elif num <= 12:
                return self.numeros_a_palabras.get(num, "Number not found")
            else:
                return self.numeros_a_palabras.get(num % 12, "Number not found")
        except Exception as e:
            print(f"Error en convertir_hora: {e}")
            return "Error de conversión"

    def convertir_minutos(self, num):
        #Convertir los minutos a palabras
        try:
            if num == 30:
                return "half past"
            elif num == 15:
                return "quarter past"
            elif num == 45:
                return "quarter to"
            elif num < 30 and num > 1:
                return self.numeros_a_palabras.get(num, "Number not found") + " minutes past"
            elif num == 1:
                return self.numeros_a_palabras.get(num, "Number not found") + " minute past"
            else:
                return self.numeros_a_palabras.get(60 - num, "Number not found") + " minutes to"
        except Exception as e:
            print(f"Error en convertir_minutos: {e}")
            return "Error de conversión"


    def convertir_a_palabras(self, num1, num2):
        #Convierte la hora y los minutos en formato de palabras
        if num1 > 24:
         return "Invalid format"
        if num2 >= 60:
         return "Invalid format"
        
        hora = self.convertir_hora(num1)
        minutos = self.convertir_minutos(num2)
        if num2 > 30 and num2 < 59:
            siguiente_hora = self.convertir_hora((num1 % 12) + 1)
            return f"{minutos} {siguiente_hora}"
        if num2 == 59:
            siguiente_hora = self.convertir_hora((num1 % 12) + 1)
            return f"one minute to {siguiente_hora}"
        if num2 == 00:
            return f"{hora} o’ clock" 
        else:
            return f"{minutos} {hora}"


conversor = ConversorNumerosPalabras()
entrada = input("Enter the numbers separated by ':' (for example, 11:10): ")
numeros = entrada.split(':')


if len(numeros) == 2:
    try:
        num1 = int(numeros[0])
        num2 = int(numeros[1])

        resultado = conversor.convertir_a_palabras(num1, num2)
        print(resultado)
    except ValueError:
        print("Invalid input format. Please make sure to enter integers separated by ':' (for example, 11:10).")
else:
    print("Invalid input format")
