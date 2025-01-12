import tkinter as tk
import numpy as np
import pygame
from threading import Thread
from PIL import Image, ImageTk

def generate_random_audio(sample_rate=44100, duration=1):
    audio_data = np.random.uniform(-1, 1, int(sample_rate * duration)).astype(np.float32)
    return audio_data

def play_sound():
    sample_rate = 44100
    pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)
    while True:
        sound = generate_random_audio(sample_rate)
        sound = (sound * 32767).astype(np.int16)  # Приведение к 16-битному формату
        pygame.mixer.Sound(buffer=sound.tobytes()).play()
        pygame.time.delay(100)  # Пауза для возможности восприятия звука

def generate_random_video(width=640, height=480):
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

def display_video():
    video_window = tk.Toplevel()  # Создание нового окна
    video_window.title("Random Video")

    canvas = tk.Canvas(video_window, width=640, height=480)
    canvas.pack()

    def update_frame():
        frame = generate_random_video()

        # Преобразование массива в изображение PIL
        frame_image = Image.fromarray(frame)
        frame_image = ImageTk.PhotoImage(frame_image)

        canvas.create_image(0, 0, anchor=tk.NW, image=frame_image)
        canvas.image = frame_image  # Сохранение ссылки на изображение
        video_window.after(10, update_frame)  # Непрерывное обновление

    update_frame()

def start_audio_and_video():
    Thread(target=play_sound, daemon=True).start()  # Запуск звука в отдельном потоке
    display_video()  # Запуск отображения видео в новом окне

# Создание графического интерфейса
root = tk.Tk()
root.title("Procedural Audio and Video Generator")

start_button = tk.Button(root, text="Start", command=start_audio_and_video)
start_button.pack()

# Запустить основной цикл интерфейса
root.mainloop()
