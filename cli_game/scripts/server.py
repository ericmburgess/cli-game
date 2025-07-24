#!/usr/bin/env python3

import os

from cli_game.controller import CommandParser
from cli_game.game_state import GameState


class GameServer:
    def __init__(self, cmd_pipe: str = "/tmp/game_cmd", resp_pipe: str = "/tmp/game_resp") -> None:
        self.cmd_pipe = cmd_pipe
        self.resp_pipe = resp_pipe
        self.game_state = GameState()
        self.parser = CommandParser()

        # Load existing game state or initialize default
        if not self.game_state.load():
            self.game_state.initialize_default()
            self.game_state.save()

    def start(self) -> None:
        if os.path.exists(self.cmd_pipe):
            os.unlink(self.cmd_pipe)
        if os.path.exists(self.resp_pipe):
            os.unlink(self.resp_pipe)

        os.mkfifo(self.cmd_pipe)
        os.mkfifo(self.resp_pipe)

        print("Game server started...")

        while True:
            with open(self.cmd_pipe) as f:
                command = f.read().strip()

            if command == "exit":
                response = "Server shutting down"
                with open(self.resp_pipe, "w") as f:
                    f.write(response)
                break

            response = self._execute_command(command)

            # Auto-save after every command
            self.game_state.save()

            with open(self.resp_pipe, "w") as f:
                f.write(response)

        os.unlink(self.cmd_pipe)
        os.unlink(self.resp_pipe)

    def _execute_command(self, command_str: str) -> str:
        parsed = self.parser.parse_command(command_str)

        if parsed is None:
            return f"Command not found: {command_str}"

        command = parsed.get("command")
        current_host = self.game_state.get_current_host()

        if not current_host:
            return "No active host found"

        # Add command to history
        current_host.shell.command_history.append(command_str)

        if command == "whoami":
            return current_host.shell.username
        else:
            return f"Command not implemented: {command}"


if __name__ == "__main__":
    server = GameServer()
    server.start()
