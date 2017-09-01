# -*- coding: cp1252 -*-
# Exemplo de sistema massa-mola vertical simples (Lei de Hooke)
# Autor: Paulo Giovani

from visual import *

# ------------------------------------------------------
# Cria um objeto para representar os eixos X, Y e Z
# ------------------------------------------------------
def criaEixo_XYZ(deslocamento, distancia, opacidade = 0.2, corTexto = color.black):
    """Cria um objeto para representar os eixos X, Y e Z."""
    
    X = arrow(pos = vector(deslocamento, 0, 0), opacity = opacidade, axis = distancia * vector(1, 0, 0), color = color.red)
    wx = label(text = "X", pos = vector(deslocamento + 1.1, 0, 0), color = corTexto, opacity = opacidade, box = 0)
    
    Y = arrow(pos = vector(deslocamento, 0, 0), opacity = opacidade, axis = distancia * vector(0, 1, 0), color = color.blue)
    wy = label(text = "Y", pos = vector(deslocamento, 1.1, 0), color = corTexto, opacity = opacidade, box = 0)
    
    Z = arrow(pos = vector(deslocamento, 0, 0), opacity = opacidade, axis = distancia * vector(0, 0, 1), color = color.green)
    wz = label(text = "Z", pos = vector(deslocamento, 0, 1.1), color = corTexto, opacity = opacidade, box = 0)
    
    base = sphere(pos = vector(deslocamento, 0, 0), radius = 0.1 * distancia)

# ------------------------------------------------------
# Criação da cena
# ------------------------------------------------------

# Dimensões e cor de fundo da janela da aplicação
largura_janela = 800 #1200 
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

#scene.lights = [vector(0, 0, -1)] 
#scene.ambient = 0.01
                
# ------------------------------------------------------
# Eixo 3D
# ------------------------------------------------------ 
                
# Insere um eixo 3D de referência
criaEixo_XYZ(-4, 1, 0.2, color.yellow)

# ------------------------------------------------------
# Criação dos objetos - 1
# ------------------------------------------------------

# Comprimento inicial da mola 
L1_0 = 0 

# Teto onde a mola está fixada
teto1 = box(pos = vector(0, 4, 0),
            size = vector(2, 0.1, 2),
            color = (0.9, 0.9, 0.9))

# Cubo oscilante          
cubo1 = box(pos = vector(0, -L1_0, 0),
            size = vector(1.2, 1.2, 1.2),
            color = color.red) 
            
# Massa e momento inicial do cubo                  
cubo1.m = 4
cubo1.p = cubo1.m * vector(0, 0, 0)
            
# Adiciona uma legenda para o cubo           
cubo1.label = label(axis = cubo1.axis, 
                    pos = cubo1.pos, 
                    color = color.white, 
                    opacity = 0, 
                    box = 0,
                    text = '%3s\n%s kg' %('M1', cubo1.m),
                    twosided = False)

# Mola que liga o cubo ao teto           
mola1 = helix(pos = teto1.pos, 
              axis = cubo1.pos - teto1.pos,              
              radius = 0.3, 
              coils = 10,
              color = (0.9, 0.9, 0.9))
              
# Constante da mola
k1 = 15 
              
# ------------------------------------------------------
# Criação dos objetos - 2
# ------------------------------------------------------

# Comprimento inicial da mola 
L2_0 = 0 

# Teto onde a mola está fixada
teto2 = box(pos = vector(3, 4, 0),
            size = vector(2, 0.1, 2),
            color = (0.9, 0.9, 0.9))

# Cubo oscilante          
cubo2 = box(pos = vector(3, -L2_0, 0),
            size = vector(1.2, 1.2, 1.2),
            color = color.orange)
            
# Massa e momento inicial do cubo                  
cubo2.m = 5
cubo2.p = cubo1.m * vector(0, 0, 0)

# Adiciona uma legenda para o cubo           
cubo2.label = label(axis = cubo2.axis, 
                    pos = cubo2.pos, 
                    color = color.white, 
                    opacity = 0, 
                    box = 0,
                    text = '%3s\n%s kg' %('M2', cubo2.m),
                    twosided = False)

# Mola que liga o cubo ao teto           
mola2 = helix(pos = teto2.pos, 
              axis = cubo2.pos - teto2.pos,              
              radius = 0.3, 
              coils = 10,
              color = (0.9, 0.9, 0.9))   

# Constante da mola
k2 = 15              

# ------------------------------------------------------
# Define as propriedades gerais
# ------------------------------------------------------ 

# Acelaração da gravidade
g = vector(0, -9.8, 0)

# Tempo inicial e passo de tempo
t = 0
dt = 0.01

# Aguarda um click para iniciar a simulação
scene.waitfor('click')

# ------------------------------------------------------
# Executa a simulação
# ------------------------------------------------------
while True:

    # Taxa de animação
    rate(100)
    
    # Atualiza o comprimento das molas
    L1 = cubo1.pos - teto1.pos
    L2 = cubo2.pos - teto2.pos
      
    # Forças aplicadas nas molas
    Fs1 = -k1 * (mag(L1) - L1_0) * norm(L1)
    Fs2 = -k2 * (mag(L2) - L2_0) * norm(L2)

    # Calcula a força total
    F1 = Fs1 + cubo1.m * g
    F2 = Fs2 + cubo2.m * g
    
    # Atualiza o momento dos cubos
    cubo1.p += F1 * dt
    cubo2.p += F2 * dt
    
    # Atualiza a posição dos cubos e de suas legendas
    cubo1.pos += cubo1.p * dt / cubo1.m
    cubo1.label.pos = cubo1.pos
    cubo2.pos += cubo2.p * dt / cubo2.m
    cubo2.label.pos = cubo2.pos
    
    # Atualiza o comprimento das molas
    mola1.axis = cubo1.pos - teto1.pos
    mola2.axis = cubo2.pos - teto2.pos
    
    # Atualiza o tempo
    t = t + dt