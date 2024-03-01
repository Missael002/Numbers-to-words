# Numbers-to-words

Programa en Python que convierte números que representan horas y minutos en su equivalente en palabras en inglés. Funciona mediante una clase llamada ConversorNumerosPalabras, que contiene métodos para convertir la hora y los minutos por separado, así como un método para combinarlos en una representación completa de la hora en palabras en inglés. En resumen, su función principal es tomar una entrada en formato de hora:minutos, validarla y producir una 
salida que representa la hora en palabras en inglés.

Diccionario: En el constructor de la clase ConversorNumerosPalabras, se inicializa un diccionario numeros_a_palabras que mapea números enteros de 1 a 59 a sus correspondientes representaciones en palabras en inglés.

Método convertir_hora: Este método toma un número entero num que representa la hora y devuelve su representación en palabras. Maneja casos especiales para horas que son múltiplos de 12 (por ejemplo, 12 se convierte en "twelve").

Método convertir_minutos: Este método toma un número entero num que representa los minutos y devuelve su representación en palabras, manejando casos especiales para minutos como 0, 15, 30, y 45.

Método convertir_a_palabras: Este método toma dos argumentos, num1 y num2, que representan la hora y los minutos, y devuelve una cadena de texto que representa la hora en palabras según las reglas especificadas.

Se crea una instancia de ConversorNumerosPalabras, se solicita al usuario que ingrese una hora en formato HH:MM, y se llama al método convertir_a_palabras con los números extraídos de la entrada del usuario.





