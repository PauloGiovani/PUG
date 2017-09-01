# -*- coding: cp1252 -*-
# Autor: Paulo Giovani

from visual import *

# ------------------------------------------------------
# Revolução da Terra e Marte ao redor do Sol
# Revolução da Lua ao Redor da Terra
# Site com definições astrofísicas: http://astro.if.ufrgs.br/
# ------------------------------------------------------

# ------------------------------------------------------
# Criação da cena
# ------------------------------------------------------

# Dimensões e cor de fundo da janela da aplicação
largura_janela = 1200 
altura_janela = 600
cor_janela = (0.069, 0.343, 1.000) 

# Define a cena
scene = display(title = 'Aprendendo Física com VPython',
                x = 0,
                y = 0,
                autoscale = True,
                width = largura_janela,
                height = altura_janela,
                center = (0, 0, 0),
                background = cor_janela)

# ------------------------------------------------------
# Criação dos objetos
# ------------------------------------------------------ 

# Escala para as distâncias equatoriais e o raio do Sol
escala = 10.0              
        
# Textura do Sol
tex = materials.texture(data = materials.loadTGA('textura_sol.tga'),
                        mapping = 'spherical', 
                        interpolate = False)
        
# Cria o Sol
Sol = sphere(color = vector(1, 1, 0),
             pos = vector(0, 0, 0),
             radius = 109.0 / escala, 
             material = tex,
             shininess = 10)

# Cria a Terra
Terra = sphere(pos = vector(149.6 / escala, 0, 0),
               radius = 1.0, 
               shininess = 10, 
               material = materials.earth,              
               make_trail = True)

# Textura da Lua
tex = materials.texture(data = materials.loadTGA('textura_lua.tga'),
                        mapping = 'spherical', 
                        interpolate = False)               
               
# Cria a Lua
Lua = sphere(color = vector(0.384, 0.384, 0.384),
             pos = vector(12, 0, 0),
             radius = 0.27241, 
             shininess = 10, 
             material = tex)              

# Textura de Marte
tex = materials.texture(data = materials.loadTGA('textura_marte.tga'),
                        mapping = 'spherical', 
                        interpolate = False) 
               
# Cria Marte
Marte = sphere(pos = vector(227.9 / escala, 0, 0),
               radius = 0.53, 
               shininess = 10, 
               material = tex,
               make_trail = True)   

# ------------------------------------------------------
# Ângulos de revolução e rotação dos astros
# ------------------------------------------------------

# Período de rotação do Sol
periodoSol = 157.08

# Período sideral da Terra = 365.256
omegaTerra = 2 * 3.14159 / 365.256
periodoTerra = 6.266

# Período sideral de Marte = 686.980
omegaMarte = 2 * 3.14159 / 686.980
periodoMarte = 6.4463

# Período sideral da Lua = 27.3
omegaLua = 2 * 3.14159 / 27.3
anguloLua = 0
periodoLua = 169.65

# Aguarda um click
scene.waitfor('click')

# ------------------------------------------------------
# Executa a simulação
# ------------------------------------------------------
while True:

    # Taxa de animação
    rate(30)
    
    # Rotação do Sol
    Sol.rotate(angle = periodoSol, 
               axis = vector(0, 1, 0), 
               origin = Sol.pos)
  
    # Revolução da Terra
    Terra.rotate(angle = omegaTerra, 
                 axis = vector(0, 1, 0), 
                 origin = vector(0, 0, 0))
                 
    # Rotação da Terra
    Terra.rotate(angle = periodoTerra, 
                 axis = vector(0, 1, 0), 
                 origin = Terra.pos)
                 
    # Revolução de Marte
    Marte.rotate(angle = omegaMarte, 
                 axis = vector(0, 1, 0), 
                 origin = vector(0, 0, 0))
                 
    # Rotação de Marte
    Marte.rotate(angle = periodoMarte, 
                 axis = vector(0, 1, 0), 
                 origin = Marte.pos)

    # Atualiza o ângulo de revolução da Lua
    anguloLua += omegaLua

    # Atualiza a posição e realiza a revolução da Lua
    Lua.pos = Terra.pos + vector(2, 0, 0)
    Lua.rotate(angle = anguloLua, 
               axis = vector(0, 1, 0), 
               origin = Terra.pos)
               
    # Rotação da Lua
    Lua.rotate(angle = periodoLua, 
               axis = vector(0, 1, 0), 
               origin = Lua.pos)
               