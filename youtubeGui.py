import json
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# File to store video data
FILE_NAME = "youtube.txt"

def load_videos():
#Loads videos from the JSON file
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError):
        return []

def save_videos(videos):
#Saves videos to the JSON file
    with open(FILE_NAME, "w") as file:
        json.dump(videos, file)

def refresh_video_list():
#Refreshes the video list display
    video_listbox.delete(0, tk.END)
    for indx, video in enumerate(videos, start=1):
        video_listbox.insert(tk.END, f"{indx}. {video['name']} - {video['time']}")

def add_video():
#Adds a new video to the list
    name = simpledialog.askstring("Add Video", "Enter video name:")
    if not name:
        return
    time = simpledialog.askstring("Add Video", "Enter video duration:")
    if not time:
        return
    videos.append({"name": name, "time": time})
    save_videos(videos)

def update_video():
#Updates an existing video
    selected_index = video_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Update Video", "Please select a video to update!")
        return
    
    index = selected_index[0]
    name = simpledialog.askstring("Update Video", "Enter new video name:", initialvalue=videos[index]['name'])
    if not name:
        return
    time = simpledialog.askstring("Update Video", "Enter new duration:", initialvalue=videos[index]['time'])
    if not time:
        return

    videos[index] = {"name": name, "time": time}
    save_videos(videos)

def delete_video():
#Deletes a selected video
    selected_index = video_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Delete Video", "Please select a video to delete!")
        return

    index = selected_index[0]
    confirm = messagebox.askyesno("Delete Video", f"Are you sure you want to delete '{videos[index]['name']}'?")
    if confirm:
        del videos[index]
        save_videos(videos)

def show_videos():
#Displays the list of videos when the button is clicked."""
    refresh_video_list()

# Load videos initially
videos = load_videos()

# Tkinter GUI Setup
root = tk.Tk()
root.title("YouTube Manager")
root.geometry("500x400")
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="YouTube Video Manager", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Listbox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=5)

video_listbox = tk.Listbox(frame, width=50, height=10, font=("Arial", 12))
video_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

video_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=video_listbox.yview)

# Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Video", command=add_video, font=("Arial", 12), width=12, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Video", command=update_video, font=("Arial", 12), width=12, bg="#FFC107")
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Video", command=delete_video, font=("Arial", 12), width=12, bg="#F44336", fg="white")
delete_button.grid(row=0, column=2, padx=5)

# New "Show Videos" button
show_button = tk.Button(root, text="Show Videos", command=show_videos, font=("Arial", 12), bg="#2196F3", fg="white", width=12)
show_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12, "bold"), bg="#333", fg="white", width=10)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
