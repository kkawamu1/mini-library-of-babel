import os
import random
import string

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    num_character = 3200
    num_character_for_title = 10
    num_character_in_one_line = 100
    random_sequence = ''.join(random.choices(string.ascii_lowercase + ' ,.', k=num_character))
    lines = []
    for i in range(0, num_character, num_character_in_one_line):
        lines.append(random_sequence[i:i+num_character_in_one_line] + '<br>')
    random_sequence = ''.join(lines)

    
    title = ''.join(random.choices(string.ascii_lowercase + ' ', k=num_character_for_title))
    
    return render_template('index.html', name=random_sequence, title=title)



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
