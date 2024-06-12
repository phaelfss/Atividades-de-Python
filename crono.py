import tkinter as tk

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro")
        
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False
        
        self.label = tk.Label(master, text="00:00:00", font=("Arial", 24))
        self.label.pack()
        
        self.start_button = tk.Button(master, text="Iniciar", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(master, text="Parar", command=self.stop_stopwatch)
        self.stop_button.pack(side=tk.LEFT)
        
        self.reset_button = tk.Button(master, text="Resetar", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.LEFT)
        
    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.update_time()
    
    def stop_stopwatch(self):
        self.running = False
    
    def reset_stopwatch(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.update_display()
    
    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1
            self.update_display()
            self.master.after(1000, self.update_time)
    
    def update_display(self):
        time_string = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        self.label.config(text=time_string)

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
