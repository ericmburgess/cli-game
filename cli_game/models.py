from pathlib import Path

from .constants import FS_DIR


class FileSystem:
    """Pure filesystem operations - no command logic."""

    def __init__(self, hostname: str) -> None:
        self.hostname = hostname
        self.root_path = Path(FS_DIR) / hostname
        self.root_path.mkdir(parents=True, exist_ok=True)

    def _resolve_path(self, path: str) -> Path:
        """Convert game path to real filesystem path."""
        # Remove leading slash if present (treat as relative to root)
        clean_path = path.lstrip("/")
        resolved = (self.root_path / clean_path).resolve()

        # Ensure path stays within host root
        if not resolved.is_relative_to(self.root_path.resolve()):
            raise ValueError(f"Path escapes host root: {path}")

        return resolved

    def list_directory(self, path: str) -> list[str]:
        """List contents of directory at path."""
        try:
            real_path = self._resolve_path(path)
            if not real_path.exists() or not real_path.is_dir():
                return []

            return [item.name for item in real_path.iterdir()]
        except ValueError:
            return []

    def file_exists(self, path: str) -> bool:
        """Check if file or directory exists."""
        try:
            real_path = self._resolve_path(path)
            return real_path.exists()
        except ValueError:
            return False

    def is_directory(self, path: str) -> bool:
        """Check if path is a directory."""
        try:
            real_path = self._resolve_path(path)
            return real_path.exists() and real_path.is_dir()
        except ValueError:
            return False


class Shell:
    """Shell environment state - cwd, env vars, prompt, history."""

    def __init__(self, hostname: str = "gamehost", username: str = "user"):
        self.hostname = hostname
        self.username = username
        self.cwd = "/home/user"
        self.command_history: list[str] = []

    def get_prompt(self) -> str:
        """Generate shell prompt string."""
        return f"{self.username}@{self.hostname}:{self.cwd}$ "

    def change_directory(self, path: str, filesystem: FileSystem) -> None:
        """Change current working directory."""
        pass

    def to_dict(self) -> dict:
        """Serialize shell state to dictionary."""
        return {
            "hostname": self.hostname,
            "username": self.username,
            "cwd": self.cwd,
            "command_history": self.command_history.copy(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Shell":
        """Deserialize shell from dictionary."""
        shell = cls(
            hostname=data.get("hostname", "gamehost"),
            username=data.get("username", "user"),
        )
        shell.cwd = data.get("cwd", "/home/user")
        shell.command_history = data.get("command_history", []).copy()
        return shell


class Host:
    """Complete machine state - filesystem + shell."""

    def __init__(self, hostname: str = "gamehost"):
        self.filesystem = FileSystem(hostname=hostname)
        self.shell = Shell(hostname=hostname)

    def get_filesystem(self) -> FileSystem:
        """Get filesystem instance."""
        return self.filesystem

    def get_shell(self) -> Shell:
        """Get shell instance."""
        return self.shell

    def to_dict(self) -> dict:
        """Serialize host state to dictionary."""
        return {"hostname": self.shell.hostname, "shell": self.shell.to_dict()}

    @classmethod
    def from_dict(cls, data: dict) -> "Host":
        """Deserialize host from dictionary."""
        hostname = data.get("hostname", "gamehost")
        host = cls(hostname=hostname)

        if "shell" in data:
            host.shell = Shell.from_dict(data["shell"])

        return host
