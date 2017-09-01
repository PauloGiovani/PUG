# Exemplo que exibe duas bolas (com e sem textura)
# Autor: Paulo Giovani

from visual import *

# Cria uma esfera vermelha
sphere(pos = vector(-1.1, 0, 0), 
       color = color.red)

# Cria uma esfera utilizando uma textura
tex = materials.texture(data = materials.loadTGA('textura_bola.tga'),
                        mapping = 'spherical', 
                        interpolate = False)

sphere(pos = vector(1.1, 0, 0), 
       material = tex)

# Exibe a cena       
while True:
    rate(1)
