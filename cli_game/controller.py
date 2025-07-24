import argparse
from typing import Optional, Dict, Any
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

from .models import Host


class CommandParser:
    """Parse command strings using argparse."""
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='', exit_on_error=False)
        self.subparsers = self.parser.add_subparsers(dest='command')
        
        # Add whoami command
        self.subparsers.add_parser('whoami', help='print current username')
    
    def parse_command(self, command_str: str) -> Optional[Dict[str, Any]]:
        """Parse command string and return structured data."""
        if not command_str.strip():
            return None
            
        try:
            args = self.parser.parse_args(command_str.split())
            return vars(args)
        except (argparse.ArgumentError, SystemExit):
            return None


class GameLoop:
    """Main game controller and command loop."""
    
    def __init__(self):
        self.host = Host()
        self.parser = CommandParser()
        self.history = FileHistory('.game_history')
    
    def run(self) -> None:
        """Main game loop."""
        print("Welcome to CLI Game!")
        print("Type 'exit' or 'quit' to leave, 'whoami' to test.")
        
        while True:
            try:
                shell = self.host.get_shell()
                user_input = prompt(shell.get_prompt(), history=self.history)
                
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                
                self._execute_command(user_input)
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
    
    def _execute_command(self, command_str: str) -> None:
        """Execute a parsed command."""
        parsed = self.parser.parse_command(command_str)
        
        if parsed is None:
            print(f"Command not found: {command_str}")
            return
        
        command = parsed.get('command')
        
        if command == 'whoami':
            print("nobody")
        else:
            print(f"Command not implemented: {command}")