import pygame.locals
from pygame.locals import *
from random import randint

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

class Nave:
    def __init__(self, tam):
        
        self.tamanho = 30
        self.posX = int(tam[0] / 2)
        self.posY = int(tam[1] - self.tamanho/2 - 5)
        self.direcao = 0
        self.velocidade = 10
        self.rect = pygame.Rect(self.posX - int(self.tamanho/2),
                                self.posY - int(self.tamanho/2),
                                self.tamanho, self.tamanho)
        self.cor = (randint(0,255), randint(0,255), randint(0,255))
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)
    def update(self, tam):
        self.posX += self.direcao * self.velocidade
        
        if (self.posX - self.tamanho) < 0:
            self.posX = self.tamanho
        if (self.posX + self.tamanho) > (tam[0]-1):
            self.posX = tam[0] - 1 - self.tamanho

        self.rect.center = (self.posX, self.posY)
        
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right < 0:
            self.rect.right = 0
        self.cor = (randint(0,255), randint(0,255), randint(0,255))




class Meteoro:
    def __init__(self, tam):
        self.posX = randint(30, tam[0] - 30)
        self.posY = -100
        self.rect = pygame.Rect( self.posX - 15, self.posY - 15, 30, 30 )
        self.velocidade = 3
        self.cor = (randint(0,200), randint(0,200), randint(0,200))

    def desenhar(self, tela):
        pygame.draw.ellipse(tela, self.cor, self.rect)
    def update(self):
        self.posY += self.velocidade
        self.rect.center = (self.posX, self.posY)


def main():
    pygame.init()
    tamanhoTela = (800, 600)
    tela = pygame.display.set_mode(tamanhoTela)
    
    clock = pygame.time.Clock()
    
    jogador = Nave(tamanhoTela)
    inimigos = []
    
    tempo = 0
    
    rodando = True

    while rodando:
        clock.tick(60)
        tempo = (tempo + 1) % 2
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    jogador.direcao = 1
                if evento.key == K_LEFT:
                    jogador.direcao = -1
            if evento.type == KEYUP:
                if evento.key == K_RIGHT and jogador.direcao == 1:
                    jogador.direcao = 0
                if evento.key == K_LEFT and jogador.direcao == -1:
                    jogador.direcao = 0
        if tempo == 1:
            inimigos.append(Meteoro(tamanhoTela))
        jogador.update(tamanhoTela)
        for inimigo in inimigos:
            inimigo.update()
        tela.fill(BRANCO)
        for inimigo in inimigos:
            inimigo.desenhar(tela)

        jogador.desenhar(tela)
        pygame.display.flip()
    pygame.quit()


main()









