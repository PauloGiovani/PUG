# -*- coding: cp1252 -*-
# Bola pulando em queda-livre (força gravitacional uniforme sem resistência do ar)
# Autor: Paulo Giovani

from visual import *

# ------------------------------------------------------
# Cria um plano
# ------------------------------------------------------
def cria_plano(largura, profundidade, altura, cor):
    """Cria um plano utilizando um objeto do tipo box."""
    
    # Cria o plano
    plano = box(pos = (0, -1, 0), 
                length = profundidade, 
                height = altura, 
                width = largura,
                color = cor)
    
    # Retorna o objeto
    return plano


# ------------------------------------------------------
# Cria uma bola
# ------------------------------------------------------
def cria_bola(raio, massa, pressao, altura, velocidade):
    """Cria uma bola de futebol utilizando uma esfera."""

    # Textura da bola
    tex = materials.texture(data = materials.loadTGA('textura_bola.tga'),
                            mapping = 'spherical', 
                            interpolate = False)

    # Cria a bola
    bola = sphere(pos = vector(0, altura, 0), 
                  material = tex)

    # Define os atributos da bola
    bola.massa = massa
    bola.raio = raio
    bola.circunferencia = 2.0 * raio
    bola.pressao = pressao
    bola.velocidade = velocidade

    # Retorna o objeto
    return bola


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

# Define as dimensões e cor do piso
largura_piso = 10
profundidade_piso = 10
altura_piso = 0.01
cor_piso = (0.9, 0.9, 0.9)

# Cria o piso
piso = cria_plano(largura_piso, 
                  profundidade_piso, 
                  altura_piso, 
                  cor_piso)

# Define alguns atributos para a bola
raio_bola = 0.7
massa_bola = 0.45
pressao_bola = 1.1
altura_inicial = 4.0
velocidade_inicial = vector(0, -1, 0)

# Cria a bola
bola = cria_bola(raio_bola, 
                 massa_bola, 
                 pressao_bola,
                 altura_inicial,
                 velocidade_inicial)

# Define a área para salvar a imagem
area = (10, 4, largura_janela + 150, altura_janela + 110)
nome_imagem = 'Bola_Pulando_'

# ------------------------------------------------------
# Animação da cena
# ------------------------------------------------------

# Incremento de tempo
dt = 0.01

# Força da gravidade
forca_gravidade = 9.8

# Contador de snapshots
contador = 1

# Aguarda um click
scene.waitfor('click')

# Exibe a cena       
while True:
    
    # Taxa de animação
    rate(100)

    # Forças que atuam na bola
    # F = ma (segunda lei de Newton) 
    forca_bola = vector(0, -bola.massa * forca_gravidade, 0)
    aceleracao = forca_bola / bola.massa

    # Atualiza a velocidade da bola
    # v = v0 + at
    bola.velocidade += aceleracao * dt

    # Atualiza a posição da bola
    # s = s0 + vt - 0.5at^2
    bola.pos += bola.velocidade * dt -0.5 * aceleracao * dt**2

    # Adiciona uma rotação na bola
    bola.rotate(angle = -0.02/4, axis = vector(0, 0, 1), origin = bola.pos)

    # Verifica se a bola colidiu com o piso e altera a direção da velocidade
    if (bola.pos.y - bola.raio - 0.3) <= piso.pos.y:
        bola.velocidade.y = -bola.velocidade.y               
