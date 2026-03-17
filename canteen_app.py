from json import JSONDecodeError, load
from pathlib import Path
from tkinter import BOTH, END, LEFT, RIGHT, Button, Entry, Frame, Label, StringVar, Tk
from tkinter import messagebox as mb

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = None
    ImageTk = None

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    InstalledAppFlow = None


APP_TITLE = "GIET Canteen"
APP_BG = "#C75B12"
BUTTON_BG = "#FFF4E8"
GOOGLE_BG = "#4285F4"
VALID_USERS = {
    "GIET123": "cant",
    "ADMIN01": "admin123",
}
SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]


def resolve_path(filename: str) -> Path:
    return Path(__file__).resolve().parent / filename


def load_logo(parent: Tk) -> Label:
    logo_path = resolve_path("star.png")

    if Image is None or ImageTk is None or not logo_path.exists():
        return Label(
            parent,
            text="GIET",
            font=("Arial", 24, "bold"),
            bg=APP_BG,
            fg="white",
            width=8,
        )

    image = Image.open(logo_path)
    image = image.resize((95, 75))
    logo = ImageTk.PhotoImage(image)

    label = Label(parent, image=logo, bg=APP_BG)
    label.image = logo
    return label


def read_client_config() -> dict:
    config_path = resolve_path("client_secret.json")

    if not config_path.exists():
        raise FileNotFoundError(
            "Missing client_secret.json. Add an OAuth client file to use Google sign-in."
        )

    with config_path.open("r", encoding="utf-8") as file:
        try:
            return load(file)
        except JSONDecodeError as exc:
            raise ValueError("client_secret.json is not valid JSON.") from exc


def validate_google_oauth_config() -> None:
    config = read_client_config()

    if config.get("type") == "service_account":
        raise ValueError(
            "client_secret.json is a service-account key. Google sign-in needs an OAuth client ID file."
        )

    if not any(key in config for key in ("installed", "web")):
        raise ValueError(
            "client_secret.json must contain an 'installed' or 'web' OAuth client configuration."
        )


def get_google_login_status() -> tuple[bool, str]:
    if InstalledAppFlow is None:
        return False, "Install google-auth-oauthlib to enable Google sign-in."

    try:
        validate_google_oauth_config()
    except Exception as exc:
        return False, str(exc)

    return True, "Google sign-in is ready."


class CanteenApp:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.roll_var = StringVar()
        self.password_var = StringVar()
        self.google_login_ready, self.google_login_message = get_google_login_status()

        self.root.title(APP_TITLE)
        self.root.geometry("520x560")
        self.root.minsize(480, 520)
        self.root.configure(bg=APP_BG)

        self.build_ui()

    def build_ui(self) -> None:
        container = Frame(self.root, bg=APP_BG, padx=28, pady=20)
        container.pack(fill=BOTH, expand=True)

        logo_label = load_logo(container)
        logo_label.pack(pady=(5, 18))

        title = Label(
            container,
            text=APP_TITLE,
            font=("Arial", 24, "bold"),
            bg=APP_BG,
            fg="white",
        )
        title.pack()

        subtitle = Label(
            container,
            text="Log in to access orders, balance, and canteen services",
            font=("Arial", 11),
            bg=APP_BG,
            fg="#FFF1E8",
        )
        subtitle.pack(pady=(8, 25))

        self.add_labeled_entry(container, "Roll Number", self.roll_var)
        self.add_labeled_entry(container, "Password", self.password_var, show="*")

        login_btn = Button(
            container,
            text="Login",
            font=("Arial", 14, "bold"),
            bg=BUTTON_BG,
            fg=APP_BG,
            width=18,
            command=self.confirm_login,
            relief="flat",
            cursor="hand2",
        )
        login_btn.pack(pady=(18, 12))

        or_label = Label(
            container,
            text="---------- OR ----------",
            font=("Arial", 12, "bold"),
            bg=APP_BG,
            fg="white",
        )
        or_label.pack(pady=10)

        google_btn = Button(
            container,
            text="Sign in with Google" if self.google_login_ready else "Google Sign-in Unavailable",
            font=("Arial", 12, "bold"),
            bg=GOOGLE_BG,
            fg="white",
            width=22,
            command=self.google_login,
            relief="flat",
            cursor="hand2",
            state="normal" if self.google_login_ready else "disabled",
        )
        google_btn.pack(pady=8)

        google_status = Label(
            container,
            text=self.google_login_message,
            font=("Arial", 9),
            bg=APP_BG,
            fg="#FFF1E8",
            wraplength=400,
            justify="center",
        )
        google_status.pack(pady=(2, 10))

        hint = Label(
            container,
            text="Demo users: GIET123 / canteen or ADMIN01 / admin123",
            font=("Arial", 10),
            bg=APP_BG,
            fg="#FFF1E8",
        )
        hint.pack(pady=(20, 0))

    def add_labeled_entry(
        self, parent: Frame, label_text: str, variable: StringVar, show: str | None = None
    ) -> None:
        label = Label(
            parent,
            text=label_text,
            font=("Arial", 14),
            bg=APP_BG,
            fg="white",
            anchor="w",
        )
        label.pack(fill="x", pady=(12, 6))

        entry = Entry(parent, font=("Arial", 14), textvariable=variable, width=28, show=show)
        entry.pack(ipady=5)

    def confirm_login(self) -> None:
        roll = self.roll_var.get().strip().upper()
        password = self.password_var.get().strip()

        if not roll or not password:
            mb.showerror("Error", "Please enter both Roll Number and Password.")
            return

        if VALID_USERS.get(roll) == password:
            mb.showinfo("Login Successful", f"Welcome to {APP_TITLE}, {roll}.")
            self.password_var.set("")
            return

        mb.showerror("Login Failed", "Invalid Roll Number or Password.")
        self.password_var.set("")

    def google_login(self) -> None:
        if not self.google_login_ready:
            mb.showerror("Google Login Unavailable", self.google_login_message)
            return

        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(resolve_path("client_secret.json")),
                scopes=SCOPES,
            )
            flow.run_local_server(port=0)
            mb.showinfo("Google Login", "Google sign-in completed successfully.")
        except Exception as exc:
            mb.showerror("Google Login Failed", str(exc))


def main() -> None:
    root = Tk()
    app = CanteenApp(root)
    root.bind(
        "<Return>",
        lambda event: app.confirm_login(),
    )
    root.mainloop()


if __name__ == "__main__":
    main()
