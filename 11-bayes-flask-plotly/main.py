import random
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
dice = [4, 6, 8, 12, 20]
priors = None
die = None
roll = None


@app.route('/', methods=['GET'])
def home():
    return render_template('bayes.html')


@app.route('/pick', methods=['POST'])
def pick():
    global die
    global priors
    die = random.choice(dice)
    priors = {die: 0.20 for die in dice}
    print('die:', die)
    return "1"


@app.route('/roll', methods=['POST'])
def roll():
    global roll
    global priors
    roll = random.randint(1, die)
    priors = update(roll, priors)
    print('roll:', roll, 'priors:', priors)
    return jsonify(priors)


def likelihood(roll, sides):
    return 0 if roll > sides else 1 / sides


def update(roll, priors):
    posterior = {}
    normalization = sum([likelihood(roll, die) * priors[die] for die in dice])
    for die, probability in priors.items():
        like = likelihood(roll, die)
        prior = probability
        posterior[die] = (like * prior) / normalization
    return posterior


app.run(host='0.0.0.0', port=3333, debug=True)
