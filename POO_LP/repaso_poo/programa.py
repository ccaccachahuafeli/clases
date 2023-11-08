from rich import print
from rich.markdown import Markdown
        # titulo
edad=16
respuesta="ES MAYOR DE EDAD" if edad>17 else "es menor de edad"
texto="""
      parrafo
      ```bash
      git commit -m "titulo" -m "cuerpo de commit"
      # comentario
      ```
      * lista
      *lista
      > informacion valiosa
      {}
""".format(respuesta)
mostrar_mark=Markdown(texto)
print(mostrar_mark)