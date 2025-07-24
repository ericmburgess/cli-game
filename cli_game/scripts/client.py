#!/usr/bin/env python3

import sys


def main() -> None:
    cmd_pipe = "/tmp/game_cmd"
    resp_pipe = "/tmp/game_resp"
    
    if len(sys.argv) < 2:
        print("Usage: python client.py <command>")
        sys.exit(1)
    
    command = " ".join(sys.argv[1:])
    
    with open(cmd_pipe, 'w') as f:
        f.write(command)
    
    with open(resp_pipe) as f:
        response = f.read()
    
    print(response)

if __name__ == "__main__":
    main()