#!/usr/bin/env python3

# Script that generates missing secrets.

from pathlib import Path
from secrets import token_hex

def init():
    input(
        "This script will ask user for missing secrets, and generate secure ones if not provided.\n"
        "Press Enter to continue."
    )

    secrets = Path(__file__).parent
    secrets.mkdir(exist_ok=True)

    with Section("Resend", secrets / "resend") as resend:
        resend.secret("token", "Resend token")

    with Section("Authelia", secrets / "authelia") as authelia:
        authelia.secret("reset_password_jwt_secret", "Reset password JWT secret", token_hex(128))
        authelia.secret("session_secret", "Session secret", token_hex(128))
        authelia.secret("storage_encryption_key", "Storage encryption key", token_hex(128))

    with Section("Postgres", secrets / "postgres") as postgres:
        postgres.secret("db", "Database name")
        postgres.secret("user", "User")
        postgres.secret("password", "Password")
    
    with Section("pgadmin", secrets / "pgadmin") as pgamin:
        pgamin.secret("password", "Password")

class Section:
    def __init__(self, name: str, path: Path) -> None:
        self.name = name
        self.path = path.resolve()
        self.to_save: dict[Path, str] = {}
        self.any_missing = False
        pass

    def __enter__(self):
        s = f" {self.name} "
        print(f"\n={s:=^20}=")
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if (exception_type == None):
            if (not self.any_missing):
                print("All secrets present")
                return
            self.path.mkdir(exist_ok=True)
            for (path, value) in self.to_save.items():
                path.write_text(value)

            s = " Saved "
            print(f"={s:=^20}=")

    def secret(self, name: str, display: str, default: str = None):
        path = self.path / name
        if (path.exists()):
            return
        else:
            self.any_missing = True
            self.to_save[path] = self.ask(display, default)

    def ask(self, name: str, default: str = None) -> str | None:
        question = f"{name}: "
        if (default != None): question = f"{name} (optional): "

        s = input(question).strip()
        if (s == ""):
            if (default == None):
                print("Required")
                return self.ask(name, default)
            else:
                return default
        return s

if __name__ == "__main__":
    init()
