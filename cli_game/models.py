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