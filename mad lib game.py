import tkinter as tk
from tkinter import messagebox
import pygame
import os

# Set the working directory to where your script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# Function to play a sound
def play_sound():
   try:
      pygame.mixer.music.load("click.wav")
      pygame.mixer.music.play()
   except pygame.error:
      print("Sound file not found. Continuing without sound.")

# Function to create and display a Mad Libs story
def generate_madlib():
   play_sound()  # Play sound effect on button click
    
   # Collect inputs from the user
   celebrity = celebrity_entry.get()
   color = color_entry.get()
   animal = animal_entry.get()
   clothing = clothing_entry.get()
   food = food_entry.get()
   place = place_entry.get()
   verb_ing = verb_ing_entry.get()

   # Create the story
   story = (f"One day, {celebrity} decided to wear a {color} {clothing} and take their pet {animal} to {place}. "
      f"While there, they had an unexpected encounter and ended up {verb_ing} with a tasty {food}. "
      f"It turned out to be an unforgettable adventure, filled with excitement and {verb_ing}!")

   # Display the story in a message box
   messagebox.showinfo("Your Mad Libs Story", story)

# Function to clear all inputs
def clear_inputs():
   celebrity_entry.delete(0, tk.END)
   color_entry.delete(0, tk.END)
   animal_entry.delete(0, tk.END)
   clothing_entry.delete(0, tk.END)
   food_entry.delete(0, tk.END)
   place_entry.delete(0, tk.END)
   verb_ing_entry.delete(0, tk.END)

# Set up the main Tkinter window
root = tk.Tk()
root.title("Mad Libs Game")

# Create input labels and entry widgets
tk.Label(root, text="Celebrity:").grid(row=0, column=0, padx=10, pady=5)
celebrity_entry = tk.Entry(root)
celebrity_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Color:").grid(row=1, column=0, padx=10, pady=5)
color_entry = tk.Entry(root)
color_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Animal:").grid(row=2, column=0, padx=10, pady=5)
animal_entry = tk.Entry(root)
animal_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Clothing:").grid(row=3, column=0, padx=10, pady=5)
clothing_entry = tk.Entry(root)
clothing_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Food:").grid(row=4, column=0, padx=10, pady=5)
food_entry = tk.Entry(root)
food_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Place:").grid(row=5, column=0, padx=10, pady=5)
place_entry = tk.Entry(root)
place_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Verb (ending in -ing):").grid(row=6, column=0, padx=10, pady=5)
verb_ing_entry = tk.Entry(root)
verb_ing_entry.grid(row=6, column=1, padx=10, pady=5)

# Create buttons to generate the story and clear inputs
generate_button = tk.Button(root, text="Generate Mad Libs", command=generate_madlib)
generate_button.grid(row=7, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_inputs)
clear_button.grid(row=8, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()