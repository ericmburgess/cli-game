import json
from pathlib import Path

from cli_game.constants import DATA_DIR

from .models import Host


class GameState:
    """Manages complete game state with multiple hosts and persistence."""

    def __init__(self, save_dir: str = DATA_DIR):
        self.save_dir = Path(save_dir).expanduser()
        self.save_file = self.save_dir / "save.json"
        self.hosts: dict[str, Host] = {}
        self.current_host: str | None = None
        
        # Ensure save directory exists
        self.save_dir.mkdir(parents=True, exist_ok=True)
    
    def add_host(self, hostname: str, host: Host) -> None:
        """Add a host to the game state."""
        self.hosts[hostname] = host
        if self.current_host is None:
            self.current_host = hostname
    
    def get_host(self, hostname: str) -> Host | None:
        """Get a host by hostname."""
        return self.hosts.get(hostname)

    def get_current_host(self) -> Host | None:
        """Get the currently active host."""
        if self.current_host:
            return self.hosts.get(self.current_host)
        return None
    
    def set_current_host(self, hostname: str) -> bool:
        """Set the current active host."""
        if hostname in self.hosts:
            self.current_host = hostname
            return True
        return False
    
    def list_hosts(self) -> list[str]:
        """Get list of all host names."""
        return list(self.hosts.keys())
    
    def to_dict(self) -> dict:
        """Serialize complete game state to dictionary."""
        return {
            "current_host": self.current_host,
            "hosts": {
                hostname: host.to_dict() 
                for hostname, host in self.hosts.items()
            }
        }
    
    def from_dict(self, data: dict) -> None:
        """Load game state from dictionary."""
        self.current_host = data.get("current_host")
        self.hosts = {}
        
        hosts_data = data.get("hosts", {})
        for hostname, host_data in hosts_data.items():
            self.hosts[hostname] = Host.from_dict(host_data)
    
    def save(self) -> bool:
        """Save game state to disk."""
        try:
            with open(self.save_file, 'w') as f:
                json.dump(self.to_dict(), f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving game state: {e}")
            return False
    
    def load(self) -> bool:
        """Load game state from disk."""
        if not self.save_file.exists():
            return False
            
        try:
            with open(self.save_file) as f:
                data = json.load(f)
            self.from_dict(data)
            return True
        except Exception as e:
            print(f"Error loading game state: {e}")
            return False
    
    def initialize_default(self) -> None:
        """Initialize with default host if no save file exists."""
        if not self.hosts:
            default_host = Host("gamehost")
            self.add_host("gamehost", default_host)