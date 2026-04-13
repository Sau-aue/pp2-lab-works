import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
black = (0, 0, 0)
screen.fill(black)
isDone = True
index = 0
sounds = ["sounds/Eminem Mockingbird.mp3", "sounds/2Pac All Eyez On Me.mp3",
          "sounds/The Neighbourhood Sweater Weather.mp3"]
isPaused = False
isPlayed = True
pygame.mixer.music.load(sounds[index])



while isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if isPaused:
                    pygame.mixer.music.unpause()
                    isPaused = False
                else:
                    pygame.mixer.music.play()

            
            elif event.key == pygame.K_s:
                pygame.mixer.music.pause()
                isPaused = True

            
            elif event.key == pygame.K_n:
                index = (index + 1) % len(sounds)
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play()
                isPaused = False

            
            elif event.key == pygame.K_b:
                index = (index - 1) % len(sounds)
                pygame.mixer.music.load(sounds[index])
                pygame.mixer.music.play()
                isPaused = False

           
            elif event.key == pygame.K_q:
                isDone = False

    pygame.display.flip()

pygame.quit()