# -*- coding: cp1252 -*-
# Exemplo que simula uma partida de ping-pong
# Atenção: Esse exemplo roda em VPython 7!
# Autor: Paulo Giovani

from random import *
from vpython import *

# ------------------------------------------------------
# Criação da cena
# ------------------------------------------------------

# Dimensões e cor de fundo da janela da aplicação
largura_janela = 940
altura_janela = 680
cor_janela = vector(0.069, 0.343, 1.000)

# Define a cena
scene.title = 'Aprendendo Física com VPython'
scene.x = 0
scene.y = 0
scene.autoscale = True
scene.width = largura_janela
scene.height = altura_janela
scene.center = vector(0, 0, 0)
scene.background = cor_janela

# ------------------------------------------------------
# Criação da mesa
# ------------------------------------------------------                
                
# Desenha a mesa
table_top = box(pos = vector(0, 0, 0), 
                length = 27.4, 
                height = 0.2, 
                width = 15.2, 
                color = color.green)
                
# Linhas brancas da mesa
center_line = box(pos = vector(0, 0.1, 0), 
                  length = 27.4, 
                  height = 0.01, 
                  width = 0.5, 
                  color = color.white)

right_line = box(pos = vector(13.45, 0.1, 0), 
                 length = 0.5, 
                 height = 0.01, 
                 width = 15.2, 
                 color = color.white) 

left_line = box(pos = vector(-13.45, 0.1, 0), 
                length = 0.5, 
                height = 0.01, 
                width = 15.2, 
                color = color.white) 

border_line1 = box(pos = vector(0, 0.1, 7.35), 
                   length = 27.4, 
                   height = 0.01, 
                   width = 0.5, 
                   color = color.white)

border_line2 = box(pos = vector(0, 0.1, -7.35), 
                   length = 27.4, 
                   height = 0.01, 
                   width = 0.5, 
                   color = color.white)                   
                
# Pés da mesa - lado direito
table_leg1 = box(pos = vector(11.4, -3.8, -7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue)
                 
table_leg2 = box(pos = vector(11.4, -3.8, 7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue)

table_leg3 = box(pos = vector(4.4, -3.8, -7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue)
                 
table_leg4 = box(pos = vector(4.4, -3.8, 7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue)                   

# Pés da mesa - lado esquerdo
table_leg5 = box(pos = vector(-11.4, -3.8, -7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue)  

table_leg6 = box(pos = vector(-11.4, -3.8, 7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue) 

table_leg7 = box(pos = vector(-4.4, -3.8, -7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue)  

table_leg8 = box(pos = vector(-4.4, -3.8, 7.3), 
                 length = 0.5, 
                 height = 7.6, 
                 width = 0.5, 
                 color = color.blue) 

# Laterais do pé da mesa - direita                 
table_lateral1 = box(pos = vector(8.0, -2.5, 7.3), 
                     length = 7, 
                     height = 0.5, 
                     width = 0.5, 
                     color = color.blue)   

table_lateral2 = box(pos = vector(8.0, -2.5, -7.3), 
                     length = 7, 
                     height = 0.5, 
                     width = 0.5, 
                     color = color.blue)

# Laterais do pé da mesa - esquerda                 
table_lateral3 = box(pos = vector(-8.0, -2.5, 7.3), 
                     length = 7, 
                     height = 0.5, 
                     width = 0.5, 
                     color = color.blue)   

table_lateral4 = box(pos = vector(-8.0, -2.5, -7.3), 
                     length = 7, 
                     height = 0.5, 
                     width = 0.5, 
                     color = color.blue)                     

# ------------------------------------------------------
# Criação da bola
# ------------------------------------------------------ 

ball = sphere(pos = vector(13, 3, 0), 
              radius = 0.25, 
              color = color.white) 
              
# ------------------------------------------------------
# Criação da raquete direita
# ------------------------------------------------------               

# Cabo da raquete                                  
handle1 = box(pos = vector(0, -1, 0), 
              length = 2, 
              height = 1, 
              width = 0.1, 
              color = vector(0.72,0.42,0))                 
                  
# Raquete                  
paddle1 = cylinder(pos = vector(0, 0, 0),
                   size = vector(.1, 1.5, 10),
                   axis = vector(0, 0, 1),
                   color = vector(0.72,0.42,0))                   

# Une os objetos e cria a raquete direita
racket_face_right = compound([handle1, paddle1])
racket_face_right.axis = vector(0, 0, 1) 
racket_face_right.pos = vector(14, 3, 0)
racket_face_right.rotate(angle = 3.14/4, axis = vector(-1, 0, 0)) 

# ------------------------------------------------------
# Criação da raquete esquerda
# ------------------------------------------------------

# Cabo da raquete                                  
handle2 = box(pos = vector(0, -1, 0), 
              length = 2, 
              height = 1, 
              width = 0.1, 
              color = vector(0.72,0.42,0))                 
                  
# Raquete                  
paddle2 = cylinder(pos = vector(0, 0, 0),
                   size = vector(.1, 1.5, 10),
                   axis = vector(0, 0, 1),
                   color = vector(0.72,0.42,0)) 

# Une os objetos e cria a raquete esquerda
racket_face_left = compound([handle2, paddle2])
racket_face_left.axis = vector(0, 0, -1) 
racket_face_left.pos = vector(-14, 3, 0) 
racket_face_left.rotate(angle = 3.14/4, axis = vector(1, 0, 0))                

# ------------------------------------------------------
# Criação da rede
# ------------------------------------------------------              

# Rede
net = box(pos = vector(0, 0.8, 0), 
          length = 0.1, 
          height = 1.7,
          width = 15.2, 
          color = color.white,
          opacity = 0.5)

# Laterais da rede
net_lateral1 = box(pos = vector(0, 0.7, 7.6), 
                   length = 0.2, 
                   height = 2.0, 
                   width = 0.2, 
                   color = color.black) 

net_lateral2 = box(pos = vector(0, 0.7, -7.6), 
                   length = 0.2, 
                   height = 2.0, 
                   width = 0.2, 
                   color = color.black)                   

# ------------------------------------------------------
# Criação do piso
# ------------------------------------------------------ 

floor = box(pos = vector(0, -7.6, 0), 
                  length = 42, 
                  height = 0.3, 
                  width = 30, 
                  color = vector(0.7, 0.7, 0.7))                  

# ------------------------------------------------------
# Configuração dos atributos
# ------------------------------------------------------ 

# Velocidade das raquetes
racket_face_right.velocity = vector(-0.2, 0, 0)
racket_face_left.velocity = vector(0.2, 0, 0)

# Velocidade inicial da bola
ball.velocity = vector(-12, -1, 0)

# Limites para os números aleatórios
min_num = -2.0
max_num = 2.0

# Passo de tempo
dt = 0.01

# Aguarda um click
scene.waitfor("click")

# ------------------------------------------------------
# Simulação
# ------------------------------------------------------                 
      
while True:
    
    rate(75)
    
    # Atualiza a posição da bola
    ball.pos = ball.pos + ball.velocity * dt
    
    # Checa o quique da bola
    if ball.pos.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8 * dt
        
    # Verifica a colisão da bola com a raquete direita
    if ball.pos.x <= racket_face_right.pos.x:
        ball.velocity.x = ball.velocity.x + racket_face_right.velocity.x
        
    # Verifica a colisão da bola com a raquete direita
    if ball.pos.x > racket_face_right.pos.x:                         
        ball.velocity.x = -ball.velocity.x 
        ball.velocity.z = uniform(min_num, max_num)
        
    # Verifica a colisão da bola com a raquete esquerda
    if ball.pos.x >= racket_face_left.pos.x:
        ball.velocity.x = ball.velocity.x + racket_face_left.velocity.x
        
    # Verifica a colisão da bola com a raquete esquerda
    if ball.pos.x < racket_face_left.pos.x:                         
        ball.velocity.x = ball.velocity.x 
        ball.velocity.z = uniform(min_num, max_num)
        
    # Interrompe a movimentação das raquetes
    if ball.pos.x > 40 or ball.pos.x < -40:
        racket_face_right.velocity = vector(0, 0, 0)
        racket_face_left.velocity = vector(0, 0, 0)
        
    # Verifica a colisão da bola com rede 
    if (ball.pos.x < net.pos.x) and (ball.pos.y < net.pos.y):
        ball.velocity.x = abs(ball.velocity.x)         
    
    # Movimenta a raquete direita sozinho
    racket_face_right.pos.z = ball.pos.z
    racket_face_right.pos.y = ball.pos.y
    
    # Movimenta a raquete esquerda sozinho
    racket_face_left.pos.z = ball.pos.z
    racket_face_left.pos.y = ball.pos.y
     
            
    
    