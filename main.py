import os
from dotenv import load_dotenv
from pathlib import Path

from simple_machine import SimpleMachine

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

sm = SimpleMachine(program = [
901, 320, 901, 321,
520, 221, 716, 812,
521, 220, 321, 604,
520, 221, 320, 604,
520, 902, 000, 000
])

sm.run()