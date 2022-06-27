from flask import render_template, Blueprint


assignment3_1 = Blueprint('assignment3_1', __name__, static_folder='static',
                          static_url_path='/pages/assignment3_1',
                          template_folder='templates')


@assignment3_1.route('/assignment3_1')
def assignment3_1_func():
    actor_info = {'name': 'brad', 'second_name': 'piTT', 'living in': 'USA'}
    best_movies = ('Mr. & Mrs. Smith', 'Mr. & Mrs. Smith', 'Oceans Eleven', 'World War Z', 'helma & Louise',
                   'the curious Case of Benjamin Button', 'Deadpool', 'Deadpool')
    awards = (
        'academy Awards', 'prime-time Emmy Award', 'Golden Globe Awards', 'briTIsh Academy Film Awards',
        'academy Awards')
    return render_template('assignment3_1.html', actor_info=actor_info, best_movies=best_movies, awards=awards)

