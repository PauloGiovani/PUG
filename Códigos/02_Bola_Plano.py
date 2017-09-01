# -*- coding: cp1252 -*-
# Bola sobre um plano
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
def cria_bola(raio, massa, pressao):
    """Cria uma bola de futebol utilizando uma esfera."""

    # Textura da bola
    tex = materials.texture(data = materials.loadTGA('textura_bola.tga'),
                            mapping = 'spherical', 
                            interpolate = False)

    # Cria a bola
    bola = sphere(pos = vector(0, 0, 0), 
                  material = tex)

    # Define os atributos da bola
    bola.massa = massa
    bola.circunferencia = 2.0 * raio
    bola.pressao = pressao

    # Retorna o objeto
    return bola


# ------------------------------------------------------
# Criação da cena
# ------------------------------------------------------

# Dimensões e cor de fundo da janela da aplicação
largura_janela = 640
altura_janela = 480
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

# Cria a bola
bola = cria_bola(raio_bola, 
                 massa_bola, 
                 pressao_bola)

# Define a área para salvar a imagem
area = (10, 4, largura_janela + 150, altura_janela + 110)
nome_imagem = 'teste_bola.png'

# Exibe a cena       
while True:
    
    # Taxa de animação
    rate(1)
