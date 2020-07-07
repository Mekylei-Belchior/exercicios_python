"""
 Faça um programa em Python que abra o áudio de um arquivo MP3.

"""
from pygame import mixer

mixer.init()
mixer.music.load('scream_killers.mp3')
mixer.music.play()
