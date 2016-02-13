import bottle
from bottle import route, run, response

import subprocess
import random

animals = [
    "apt",
    "bud-frogs",
    "bunny",
    "cock",
    "default",
    "dragon",
    "duck",
    "elephant",
    "gnu",
    "hellokitty",
    "kitty",
    "koala",
    "meow",
    "milk",
    "moofasa",
    "moose",
    "pony",
    "pony-smaller",
    "sheep",
    "stegosaurus",
    "turtle",
    "tux",
    "unipony-smaller"
]

def fortune_cow():
    animal = random.choice(animals)
    p1 = subprocess.Popen(["/usr/games/fortune", "-s", "-n", "50"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["/usr/games/cowsay", "-f", animal], stdin=p1.stdout, stdout=subprocess.PIPE)
    output = p2.communicate()[0]
    return output + animal


@route('/')
def index():
    output = fortune_cow()
    return "<html><head><meta name='viewport' content='width=device-width, initial-scale=1'></head><body><pre>%s</pre></body></html>" % (output)

if __name__ == "__main__":
    run(host='localhost', port=8080)

app = bottle.default_app()
