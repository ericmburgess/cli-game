#!/usr/bin/env python3

import os
from cli_game.controller import CommandParser
from cli_game.models import Host

class GameServer:
    def __init__(self, cmd_pipe="/tmp/game_cmd", resp_pipe="/tmp/game_resp"):
        self.cmd_pipe = cmd_pipe
        self.resp_pipe = resp_pipe
        self.host = Host()
        self.parser = CommandParser()
    
    def start(self):
        if os.path.exists(self.cmd_pipe):
            os.unlink(self.cmd_pipe)
        if os.path.exists(self.resp_pipe):
            os.unlink(self.resp_pipe)
            
        os.mkfifo(self.cmd_pipe)
        os.mkfifo(self.resp_pipe)
        
        print("Game server started...")
        
        while True:
            with open(self.cmd_pipe, 'r') as f:
                command = f.read().strip()
            
            if command == "__shutdown__":
                response = "Server shutting down"
                with open(self.resp_pipe, 'w') as f:
                    f.write(response)
                break
            
            response = self._execute_command(command)
            
            with open(self.resp_pipe, 'w') as f:
                f.write(response)
        
        os.unlink(self.cmd_pipe)
        os.unlink(self.resp_pipe)
    
    def _execute_command(self, command_str: str) -> str:
        parsed = self.parser.parse_command(command_str)
        
        if parsed is None:
            return f"Command not found: {command_str}"
        
        command = parsed.get('command')
        
        if command == 'whoami':
            return "nobody"
        else:
            return f"Command not implemented: {command}"

if __name__ == "__main__":
    server = GameServer()
    server.start()