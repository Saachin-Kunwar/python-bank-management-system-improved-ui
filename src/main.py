from bank import Bank
import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class BankApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.bank = Bank()

        self.current_user = None

        self.title("Professional Banking System")

        self.geometry("1400x800")

        self.resizable(False, False)

        self.configure(fg_color="#0f172a")

        self.show_login_screen()

    # ---------------- CLEAR WINDOW ----------------

    def clear_window(self):

        for widget in self.winfo_children():
            widget.destroy()

    # ---------------- LOGIN SCREEN ----------------

    def show_login_screen(self):

        self.clear_window()

        login_frame = ctk.CTkFrame(
            self,
            width=500,
            height=650,
            corner_radius=25,
            fg_color="#1e293b"
        )

        login_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        logo = ctk.CTkLabel(
            login_frame,
            text="🏦",
            font=("Arial", 70)
        )

        logo.pack(pady=(40, 10))

        title = ctk.CTkLabel(
            login_frame,
            text="Modern Banking System",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=10)

        subtitle = ctk.CTkLabel(
            login_frame,
            text="Secure Digital Banking",
            font=("Arial", 16),
            text_color="gray"
        )

        subtitle.pack(pady=(0, 30))

        self.username_entry = ctk.CTkEntry(
            login_frame,
            placeholder_text="Username",
            width=320,
            height=50,
            corner_radius=15
        )

        self.username_entry.pack(pady=15)

        self.pin_entry = ctk.CTkEntry(
            login_frame,
            placeholder_text="PIN",
            show="*",
            width=320,
            height=50,
            corner_radius=15
        )

        self.pin_entry.pack(pady=15)

        login_btn = ctk.CTkButton(
            login_frame,
            text="Login",
            width=320,
            height=50,
            corner_radius=15,
            font=("Arial", 18, "bold"),
            command=self.login
        )

        login_btn.pack(pady=15)

        create_btn = ctk.CTkButton(
            login_frame,
            text="Create Account",
            width=320,
            height=50,
            corner_radius=15,
            fg_color="#16a34a",
            hover_color="#15803d",
            font=("Arial", 18, "bold"),
            command=self.create_account
        )

        create_btn.pack(pady=15)

        reactivate_btn = ctk.CTkButton(
            login_frame,
            text="Reactivate Account",
            width=320,
            height=50,
            corner_radius=15,
            fg_color="orange",
            hover_color="#ea580c",
            font=("Arial", 18, "bold"),
            command=self.reactivate_account
        )

        reactivate_btn.pack(pady=15)

    # ---------------- LOGIN ----------------

    def login(self):

        name = self.username_entry.get()

        pin = self.pin_entry.get()

        success, result = self.bank.login(name, pin)

        if success:

            self.current_user = result

            self.show_dashboard()

        else:

            messagebox.showerror(
                "Error",
                result
            )

    # ---------------- CREATE ACCOUNT ----------------

    def create_account(self):

        name = self.username_entry.get()

        pin = self.pin_entry.get()

        if not name or not pin:

            messagebox.showerror(
                "Error",
                "Fill all fields"
            )

            return

        success, message = self.bank.create_account(
            name,
            pin
        )

        if success:

            messagebox.showinfo(
                "Success",
                message
            )

            self.username_entry.delete(0, "end")
            self.pin_entry.delete(0, "end")

        else:

            messagebox.showerror(
                "Error",
                message
            )

    # ---------------- REACTIVATE ACCOUNT ----------------

    def reactivate_account(self):

        name = self.username_entry.get()

        pin = self.pin_entry.get()

        if not name or not pin:

            messagebox.showerror(
                "Error",
                "Enter username and PIN"
            )

            return

        success, message = self.bank.reactivate_account(
            name,
            pin
        )

        if success:

            messagebox.showinfo(
                "Success",
                message
            )

        else:

            messagebox.showerror(
                "Error",
                message
            )

    # ---------------- DASHBOARD ----------------

    def show_dashboard(self):

        self.clear_window()

        # ---------------- SIDEBAR ----------------

        sidebar = ctk.CTkFrame(
            self,
            width=260,
            fg_color="#111827",
            corner_radius=0
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        logo = ctk.CTkLabel(
            sidebar,
            text="🏦 MyBank",
            font=("Arial", 30, "bold")
        )

        logo.pack(pady=40)

        menu_buttons = [

            ("💰 Deposit", self.deposit_money),
            ("💸 Withdraw", self.withdraw_money),
            ("📊 Balance", self.show_balance),
            ("📜 History", self.show_history),
            ("🔁 Transfer", self.transfer_money),
            ("⚠️ Deactivate", self.deactivate_account),
            ("🗑 Delete", self.delete_account),
            ("🚪 Logout", self.logout)

        ]

        for text, command in menu_buttons:

            btn = ctk.CTkButton(
                sidebar,
                text=text,
                width=220,
                height=50,
                corner_radius=12,
                anchor="w",
                font=("Arial", 18),
                fg_color="#1f2937",
                hover_color="#2563eb",
                command=command
            )

            btn.pack(pady=10)

        # ---------------- MAIN AREA ----------------

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="#0f172a"
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        welcome = ctk.CTkLabel(
            self.main_frame,
            text=f"Welcome Back, {self.current_user.name}",
            font=("Arial", 38, "bold")
        )

        welcome.pack(pady=20)

        # ---------------- ATM CARD ----------------

        card = ctk.CTkFrame(
            self.main_frame,
            width=500,
            height=250,
            corner_radius=25,
            fg_color="#2563eb"
        )

        card.pack(pady=30)

        card.pack_propagate(False)

        bank_name = ctk.CTkLabel(
            card,
            text="🏦 MyBank",
            font=("Arial", 28, "bold")
        )

        bank_name.pack(
            anchor="nw",
            padx=25,
            pady=20
        )

        chip = ctk.CTkLabel(
            card,
            text="💳",
            font=("Arial", 40)
        )

        chip.pack(
            anchor="w",
            padx=25
        )

        self.balance_label = ctk.CTkLabel(
            card,
            text=f"Balance: Rs. {self.current_user.balance}",
            font=("Arial", 30, "bold")
        )

        self.balance_label.pack(
            anchor="w",
            padx=25,
            pady=20
        )

        user_text = ctk.CTkLabel(
            card,
            text=self.current_user.name.upper(),
            font=("Arial", 22)
        )

        user_text.pack(
            anchor="sw",
            padx=25,
            pady=10
        )

        # ---------------- DASHBOARD BOXES ----------------

        stats_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        stats_frame.pack(pady=20)

        self.create_stat_box(
            stats_frame,
            "💰 Balance",
            f"Rs. {self.current_user.balance}",
            0
        )

        self.create_stat_box(
            stats_frame,
            "📜 Transactions",
            str(len(self.current_user.history)),
            1
        )

    # ---------------- STAT BOX ----------------

    def create_stat_box(
        self,
        parent,
        title,
        value,
        column
    ):

        box = ctk.CTkFrame(
            parent,
            width=250,
            height=140,
            corner_radius=20,
            fg_color="#1e293b"
        )

        box.grid(
            row=0,
            column=column,
            padx=20
        )

        box.grid_propagate(False)

        title_label = ctk.CTkLabel(
            box,
            text=title,
            font=("Arial", 22)
        )

        title_label.pack(pady=20)

        value_label = ctk.CTkLabel(
            box,
            text=value,
            font=("Arial", 28, "bold")
        )

        value_label.pack()

    # ---------------- SHOW BALANCE ----------------

    def show_balance(self):

        messagebox.showinfo(
            "Current Balance",
            f"Your balance is Rs. {self.current_user.balance}"
        )

        self.balance_label.configure(
            text=f"Balance: Rs. {self.current_user.balance}"
        )

    # ---------------- DEPOSIT ----------------

    def deposit_money(self):

        amount = ctk.CTkInputDialog(
            text="Enter amount",
            title="Deposit"
        ).get_input()

        if amount:

            self.current_user.deposit(
                float(amount)
            )

            self.bank.save_data()

            self.balance_label.configure(
                text=f"Balance: Rs. {self.current_user.balance}"
            )

            messagebox.showinfo(
                "Success",
                "Amount deposited successfully"
            )

    # ---------------- WITHDRAW ----------------

    def withdraw_money(self):

        amount = ctk.CTkInputDialog(
            text="Enter amount",
            title="Withdraw"
        ).get_input()

        if amount:

            self.current_user.withdraw(
                float(amount)
            )

            self.bank.save_data()

            self.balance_label.configure(
                text=f"Balance: Rs. {self.current_user.balance}"
            )

            messagebox.showinfo(
                "Success",
                "Amount withdrawn successfully"
            )

              # ---------------- HISTORY ----------------

    def show_history(self):

        history_window = ctk.CTkToplevel(self)

        history_window.title("Transaction History")

        history_window.geometry("700x500")

        history_window.configure(
            fg_color="#0f172a"
        )

        history_window.transient(self)

        history_window.grab_set()

        title = ctk.CTkLabel(
            history_window,
            text="📜 Transaction History",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=20)

        textbox = ctk.CTkTextbox(
            history_window,
            width=650,
            height=380,
            font=("Arial", 18)
        )

        textbox.pack(pady=10)

        if not self.current_user.history:

            textbox.insert(
                "end",
                "No transaction history available."
            )

        else:

            for item in self.current_user.history:

                textbox.insert(
                    "end",
                    f"• {item}\n\n"
                )

        textbox.configure(
            state="disabled"
        )

        history_window.lift()

        history_window.focus_force()
    # ---------------- TRANSFER MONEY ----------------

    def transfer_money(self):

        receiver = ctk.CTkInputDialog(
            text="Receiver Name",
            title="Transfer"
        ).get_input()

        amount = ctk.CTkInputDialog(
            text="Amount",
            title="Transfer"
        ).get_input()

        if receiver and amount:

            success, message = self.bank.transfer_money(
                self.current_user,
                receiver,
                float(amount)
            )

            self.bank.save_data()

            self.balance_label.configure(
                text=f"Balance: Rs. {self.current_user.balance}"
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    message
                )

            else:

                messagebox.showerror(
                    "Error",
                    message
                )

    # ---------------- DEACTIVATE ----------------

    def deactivate_account(self):

        confirm = messagebox.askyesno(
            "Confirm",
            "Deactivate account?"
        )

        if confirm:

            self.bank.deactivate_account(
                self.current_user
            )

            self.logout()

    # ---------------- DELETE ACCOUNT ----------------

    def delete_account(self):

        confirm = messagebox.askyesno(
            "Confirm",
            "Delete account permanently?"
        )

        if confirm:

            self.bank.delete_account(
                self.current_user
            )

            self.logout()

    # ---------------- LOGOUT ----------------

    def logout(self):

        self.current_user = None

        self.show_login_screen()


if __name__ == "__main__":

    app = BankApp()

    app.mainloop()