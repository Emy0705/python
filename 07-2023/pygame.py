import pygame

# Variaveis
TELA_LARGURA = 1280
TELA_ALTURA = 720

pygame.init()

# Criando a tela
display = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Jogo Pong")

fps = pygame.time.Clock()

jogando = True

# Personagem 1 - Jogador
personagem_1 = pygame.image.load("assets/player1.png")
personagem_1_rect = personagem_1.get_rect(left=20)
velocidade_1 = 5
placar_1 = 0


# Personagem 2
personagem_2 = pygame.image.load("assets/player2.png")
personagem_2_rect = personagem_2.get_rect(right=TELA_LARGURA - 20)
velocidade_2 = 5
placar_2 = 0

# Bolinha
bolinha = pygame.image.load("assets/ball.png")
bolinha_rect = bolinha.get_rect()
bolinha_rect.x = TELA_LARGURA / 2
bolinha_rect.y = TELA_ALTURA / 2

dir_x = 4
dir_y = 4

# Carregando uma fonte para o placar
fonte = pygame.font.Font(None, 50)
fonte_vencedor = pygame.font.Font(None, 150)

#Carrega imagem de bg
bg = pygame.image.load("assets/bg.png")

# Sons
som_bolinha = pygame.mixer.Sound("assets/pong.wav")
musica = pygame.mixer.Sound("assets/music.ogg")

musica.play(-1)
musica.set_volume(1)

# Imagem de menu
menu = pygame.image.load("assets/menu.png")
menu_rect = menu.get_rect()

# Cena
cena = "inicio"
vencedor = ""

while jogando:

    # Carrega os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False # Encerra o Jogo

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                velocidade_1 = -5
            elif event.key == pygame.K_s:
                velocidade_1 = 5

            if event.key == pygame.K_UP:
                velocidade_2 = -5
            elif event.key == pygame.K_DOWN:
                velocidade_2 = 5

            if event.key == pygame.K_RETURN:
                placar_1 = 0
                placar_2 = 0
                cena = "jogando"

            if event.key == pygame.K_q:
                jogando = False

    # Configura Cenas
    if cena == "inicio":
        display.fill((0, 0, 0))
        display.blit(menu, menu_rect)

    elif cena == "jogando":

        # Movimentação do personagem 1
        if personagem_1_rect.y > 0 and personagem_1_rect.y < TELA_ALTURA - 160:
            personagem_1_rect.y += velocidade_1
        elif (personagem_1_rect.y <= 0 and velocidade_1 > 0) \
                or (personagem_1_rect.y >= TELA_ALTURA - 160
                    and velocidade_1 < 0):
            personagem_1_rect.y += velocidade_1

        # Movimentação do personagem 2
        if personagem_2_rect.y > 0 and personagem_2_rect.y < TELA_ALTURA - 160:
            personagem_2_rect.y += velocidade_2
        elif (personagem_2_rect.y <= 0 and velocidade_2 > 0) \
                or (personagem_2_rect.y >= TELA_ALTURA - 160
                    and velocidade_2 < 0):
            personagem_2_rect.y += velocidade_2

        # Movimentação da Bolinha
        if bolinha_rect.y <= 0 or bolinha_rect.y >= TELA_ALTURA:
            dir_y = dir_y * -1
            som_bolinha.play()

        # Verifica colição com o personagem 1
        if personagem_1_rect.colliderect(bolinha_rect):
            dir_x = dir_x * -1
            som_bolinha.play()

        # Verifica colição com o personagem 2
        if personagem_2_rect.colliderect(bolinha_rect):
            dir_x = dir_x * -1
            som_bolinha.play()

        # Verifica se a bolinha saiu da tela
        if bolinha_rect.x <= 0:
            bolinha_rect.x = TELA_LARGURA / 2
            bolinha_rect.y = TELA_ALTURA / 2
            placar_2 += 1
            if placar_2 >= 3:
                vencedor = "Jogador 2"
                cena = "FIM"
        elif bolinha_rect.x >= TELA_LARGURA:
            bolinha_rect.x = TELA_LARGURA / 2
            bolinha_rect.y = TELA_ALTURA / 2
            placar_1 += 1
            if placar_1 >= 3:
                vencedor = "Jogador 1"
                cena = "FIM"

        bolinha_rect.y += dir_y
        bolinha_rect.x += dir_x

        # Desenhar a tela
        display.fill((0, 0, 0))
        display.blit(bg, (0, 0))

        # Desenhar os personagens
        display.blit(personagem_1, personagem_1_rect)
        display.blit(personagem_2, personagem_2_rect)

        # Desenha Bolinha
        display.blit(bolinha, bolinha_rect)

        # Desenha o placar
        texto_placar_1 = fonte.render(str(placar_1), True, (255, 255, 255))
        texto_placar_2 = fonte.render(str(placar_2), True, (255, 255, 255))

        display.blit(texto_placar_1, (TELA_LARGURA / 2 - 50, 10))
        display.blit(texto_placar_2, (TELA_LARGURA / 2 + 50, 10))

    elif cena == "FIM":
        display.fill((0, 0, 0))
        display.blit(bg, (0, 0))

        texto = fonte_vencedor.render("O Vencedor é " + vencedor, True, (255, 255, 255))

        display.blit(texto, (40, TELA_ALTURA / 2 - 100 ))

    fps.tick(60)
    pygame.display.flip()