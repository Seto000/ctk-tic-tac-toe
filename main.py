import customtkinter
import random


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.minsize(width=600, height=600)
        self.maxsize(width=600, height=600)
        self.buttons = []
        self.avail_buttons = []
        self.player_turn = True
        self.computer_after = None
        self.player_score = 0
        self.computer_score = 0
        self.player_score_label = customtkinter.CTkLabel(master=self, text=f"Player: {self.player_score}",
                                                         fg_color="gray20", font=("System", 16), corner_radius=8)
        self.player_score_label.place(relx=0.24, y=20, anchor="center")
        self.computer_score_label = customtkinter.CTkLabel(master=self, text=f"Computer: {self.computer_score}",
                                                           fg_color="gray20", font=("System", 16), corner_radius=8)
        self.computer_score_label.place(relx=0.75, y=20, anchor="center")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=8, fg_color="gray20")
        self.my_frame.pack(expand=True)
        self.game_label = customtkinter.CTkLabel(master=self, text="Tic-Tac-Toe", fg_color="gray20", corner_radius=8,
                                                 font=("System", 24), height=50)
        self.game_label.pack(pady=(0, 30))
        self.reset_button = customtkinter.CTkButton(master=self, text="Reset", command=self.reset_game,
                                                    fg_color="gray20", corner_radius=8, font=("System", 24), height=30)
        self.reset_button.pack(pady=(0, 15))
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for column in range(3):
                button = customtkinter.CTkButton(self.my_frame, text=" ", font=("System", 24), height=120, width=120)
                button.configure(command=lambda btn=button: self.button_clicked(btn))
                button.grid(row=row, column=column, padx=5, pady=5)
                self.buttons.append(button)
                self.avail_buttons.append(button)

    def button_clicked(self, btn):
        if not self.is_game_over():
            self.enable_buttons()
            if self.player_turn:
                btn.configure(text="X")
                self.player_turn = False
                self.disable_buttons()
                self.avail_buttons.remove(btn)
                self.computer_after = self.after(1000, self.computer_turn)
            else:
                btn.configure(text="O", state="disabled")
                self.avail_buttons.remove(btn)
                self.player_turn = True

    def computer_turn(self):
        if not self.is_game_over():
            selected_button = random.choice(self.avail_buttons)
            self.button_clicked(selected_button)
            self.is_game_over()

    def disable_buttons(self):
        for button in self.buttons:
            button.configure(state="disabled")

    def enable_buttons(self):
        for button in self.avail_buttons:
            button.configure(state="normal")

    def is_game_over(self):
        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(self.buttons[i].cget("text") == "X" for i in condition):
                self.game_label.configure(text="Player Won!")
                self.player_score += 1
                self.player_score_label.configure(text=f"Player: {self.player_score}")
                return True
            elif all(self.buttons[i].cget("text") == "O" for i in condition):
                self.game_label.configure(text="Computer Won!")
                self.disable_buttons()
                self.computer_score += 1
                self.computer_score_label.configure(text=f"Computer: {self.computer_score}")
                return True
        if not self.avail_buttons:
            self.game_label.configure(text="It's a tie!")
            return True
        return False

    def reset_game(self):
        for button in self.buttons:
            button.configure(text=" ", state="normal")
        self.avail_buttons = list(self.buttons)
        self.player_turn = True
        self.game_label.configure(text="Tic-Tac-Toe")
        self.after_cancel(self.computer_after)


app = App()
app.mainloop()
