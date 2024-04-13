import unittest

def reverse_string(test_str):
  """ 
  Función que invierte una cadena de texto.
  Argumentos:
    test_str (str): Cadena de texto a invertir.
  Retorna:
    str: Cadena de texto invertida.
  """
  rev_str = test_str[::-1]
  return rev_str

class TestReverseString(unittest.TestCase):
  """ 
  Clase para pruebas unitarias de la función `reverse_string`.
  """
  def test_reverse_string_exito(self):
    """ 
    Prueba que la función invierte correctamente una cadena de texto.
    """
    texto_original = "Hola, mundo!"
    texto_invertido = reverse_string(texto_original)
    self.assertEqual(texto_invertido, "!odnum ,aloH")
  
  def test_reverse_string_vacio(self):
    """ 
    Prueba que la función maneja correctamente una cadena de texto vacía.
    """
    texto_original = ""
    texto_invertido = reverse_string(texto_original)
    self.assertEqual(texto_invertido, "")
  
  def test_reverse_string_espacios(self):
    """ 
    Prueba que la función invierte correctamente una cadena de texto con espacios.
    """
    texto_original = "Esta es una frase con espacios."
    texto_invertido = reverse_string(texto_original)
    self.assertEqual(texto_invertido, ".soicapse noc esarf anu se atsE")

if __name__ == "__main__":
  unittest.main()
