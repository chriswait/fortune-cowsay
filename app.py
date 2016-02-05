import bottle
from bottle import route, run, response

import subprocess
import random

animals = ["apt", "beavis.zen", "bong", "bud-frogs", "bunny", "calvin", "cheese", "cock", "cower", "daemon", "default", "dragon", "dragon-and-cow", "duck", "elephant", "elephant-in-snake", "eyes", "flaming-sheep", "ghostbusters", "gnu", "hellokitty", "kiss", "kitty", "koala", "kosh", "luke-koala", "mech-and-cow", "meow", "milk", "moofasa", "moose", "mutilated", "pony", "pony-smaller", "ren", "sheep", "skeleton", "snowman", "sodomized-sheep", "stegosaurus", "stimpy", "suse", "three-eyes", "turkey", "turtle", "tux", "unipony", "unipony-smaller", "vader", "vader-koala", "www"]

def fortune_cow():
    animal = random.choice(animals)
    p1 = subprocess.Popen(["/usr/games/fortune"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["/usr/games/cowsay", "-s", "-f", animal], stdin=p1.stdout, stdout=subprocess.PIPE)
    output = p2.communicate()[0]
    return output


@route('/')
def index():
    output = fortune_cow()
    return "<pre>%s</pre>" % (output)

if __name__ == "__main__":
    run(host='localhost', port=8080)

app = bottle.default_app()
