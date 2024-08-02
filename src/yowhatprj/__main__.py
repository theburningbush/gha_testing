from .whatwhat import what  # Relative 
from yowhatprj.yoyoyo.yo import say_yo as s # Absolute
import httpx

def main() -> None:
    print(what.say_what())
    print(s())
