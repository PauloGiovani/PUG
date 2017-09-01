# -*- coding: cp1252 -*-
# Exemplo de sistema massa-mola simples (Lei de Hooke)
# Autor: Paulo Giovani

from visual import *
from visual.graph import *
import numpy as np

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
# Cria um plano
# ------------------------------------------------------
def cria_plano(posicao, largura, profundidade, altura, cor, opacidade = 1):
    """Cria um plano utilizando um objeto do tipo box."""
    
    # Cria o plano
    plano = box(pos = posicao, 
                length = profundidade, 
                height = altura, 
                width = largura,
                color = cor,
                opacity = opacidade)
    
    # Retorna o objeto
    return plano  

# ------------------------------------------------------
# Criação da cena
# ------------------------------------------------------

# Dimensões e cor de fundo da janela da aplicação
largura_janela = 600
altura_janela = 600
cor_janela = (0.069,0.343,1.000)

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
# Eixo 3D
# ------------------------------------------------------ 
                
# Insere um eixo 3D de referência
criaEixo_XYZ(-7, 1, 0.2, color.yellow)

# ------------------------------------------------------
# Piso
# ------------------------------------------------------                 

# Define as dimensões e cor do piso
posicao = vector(0, -1, 0)
largura_piso = 4
profundidade_piso = 8
altura_piso = 0.1
cor_piso = (0.9, 0.9, 0.9)

# Cria o piso
piso = cria_plano(posicao,
                  largura_piso, 
                  profundidade_piso, 
                  altura_piso, 
                  cor_piso)
                  
# ------------------------------------------------------
# Parede
# ------------------------------------------------------

posicao = vector(-3, 0.5, 0)
largura_parede = 0.2
altura_parede = 3
profundidade_parede = 3
cor_parede = color.white
opacidade_parede = 0.3
                       
# Cria a parede
parede = cria_plano(posicao, 
                    profundidade_parede, 
                    largura_parede, 
                    altura_parede,
                    cor_parede,
                    opacidade_parede)                     

# ------------------------------------------------------
# Cria o cubo (massa M1)
# ------------------------------------------------------ 

# Massa do cubo
m  = 25            

# Posição inicial e tamanho do deslocamento
x_inicial = 3.0
x_deslocamento = 0.5

# Velocidade inicial
v_inicial = 0

# Posição, tamanho e cor
posicao = vector(x_inicial, 0, 0)
tamanho = vector(1.2, 1.2, 1.2)
cor = color.red

# Cria o cubo
cubo = box(pos = posicao, 
           size = tamanho, 
           color = cor)

# Adiciona uma legenda para o cubo           
cubo.label = label(axis = cubo.axis, 
                   pos = cubo.pos, 
                   color = color.white, 
                   opacity = 0, 
                   box = 0,
                   text = 'M1')

# ------------------------------------------------------
# Cria a mola
# ------------------------------------------------------                 

# Constante da mola
k = 15

# Comprimento da mola
comprimento_mola = x_inicial - parede.pos.x

# Cria a mola 
mola = helix(pos = vector(parede.pos.x, 0, 0), 
             axis = vector(1, 0, 0), 
             length = comprimento_mola, 
             radius = 0.3, 
             coils = 10, 
             color = (0.9, 0.9, 0.9))            

# ------------------------------------------------------
# Cria a janela para exibir o gráfico da plotagem
# ------------------------------------------------------

# Define a janela de plotagem
graph = gdisplay(x = 0, 
                 y = 0, 
                 width = largura_janela, 
                 height = altura_janela, 
                 title = 'Plotagem: Posição (vermelho) e Velocidade (azul)',
                 xtitle = 'Tempo',
                 foreground = color.black,
                 background = color.white)

# Cria os gráficos para representar a posição e velocidade do cubo                 
posicao = gcurve(color = color.red)
velocidade = gcurve(color = color.blue)   
aceleracao = gcurve(color = color.green)           

# ------------------------------------------------------
# Simulação
# ------------------------------------------------------

# Parâmetros de tempo
t = 0
dt = 0.01

# Aguarda um click
scene.waitfor('click')

# Exibe a cena       
while True:
    
    # Taxa de animação
    rate(100)    
    
    # Calcula o deslocamento do cubo
    delta_x = (x_inicial - x_deslocamento)
    
    # Calcula a aceleração
    # Lei de Hooke      -> F = -kx
    # 2a. Lei de Newton -> F = ma
    # ma = -kx
    # a  = -kx / m
    # a = -(k / m) * delta_x
    a = -k / m * delta_x
    
    # Calcula a velocidade de deslocamento do cubo
    # v = v0 + at
    v_final = v_inicial + a * dt
    
    # Calcula a posição do cubo
    # x = x0 + vt
    x_final = x_inicial + v_final * dt
    
    # Movimenta o cubo e a sua legenda
    cubo.pos = (x_final, 0, 0)
    cubo.label.pos = cubo.pos
    
    # Atualiza o comprimento da mola
    mola.length = cubo.pos.x - parede.pos.x
    
    # Plota a posição e a velocidade
    posicao.plot(pos = (t, x_final))
    velocidade.plot(pos = (t, v_final))
    
    # Atualiza a posição e velocidade do cubo
    x_inicial = x_final
    v_inicial = v_final
    
    # Atualiza o tempo
    t = t + dt

    
