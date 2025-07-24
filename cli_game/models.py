from typing import List


class FileSystem:
    """Pure filesystem operations - no command logic."""
    
    def __init__(self):
        pass
    
    def list_directory(self, path: str) -> List[str]:
        """List contents of directory at path."""
        return []
    
    def file_exists(self, path: str) -> bool:
        """Check if file or directory exists."""
        return False
    
    def is_directory(self, path: str) -> bool:
        """Check if path is a directory."""
        return False
    
    def to_dict(self) -> dict:
        """Serialize filesystem state to dictionary."""
        return {}
    
    @classmethod
    def from_dict(cls, data: dict) -> 'FileSystem':
        """Deserialize filesystem from dictionary."""
        filesystem = cls()
        return filesystem


class Shell:
    """Shell environment state - cwd, env vars, prompt, history."""
    
    def __init__(self, hostname: str = "gamehost", username: str = "user"):
        self.hostname = hostname
        self.username = username
        self.cwd = "/home/user"
        self.command_history: List[str] = []
    
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
            "command_history": self.command_history.copy()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Shell':
        """Deserialize shell from dictionary."""
        shell = cls(
            hostname=data.get("hostname", "gamehost"),
            username=data.get("username", "user")
        )
        shell.cwd = data.get("cwd", "/home/user")
        shell.command_history = data.get("command_history", []).copy()
        return shell


class Host:
    """Complete machine state - filesystem + shell."""
    
    def __init__(self, hostname: str = "gamehost"):
        self.filesystem = FileSystem()
        self.shell = Shell(hostname=hostname)
    
    def get_filesystem(self) -> FileSystem:
        """Get filesystem instance."""
        return self.filesystem
    
    def get_shell(self) -> Shell:
        """Get shell instance."""
        return self.shell
    
    def to_dict(self) -> dict:
        """Serialize host state to dictionary."""
        return {
            "hostname": self.shell.hostname,
            "filesystem": self.filesystem.to_dict(),
            "shell": self.shell.to_dict()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Host':
        """Deserialize host from dictionary."""
        hostname = data.get("hostname", "gamehost")
        host = cls(hostname=hostname)
        
        if "filesystem" in data:
            host.filesystem = FileSystem.from_dict(data["filesystem"])
        
        if "shell" in data:
            host.shell = Shell.from_dict(data["shell"])
        
        return host