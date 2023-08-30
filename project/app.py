from flask import Flask, render_template

from project.loginForm import LoginForm
from project.bookingForms import BookingForm
from project.userForms import UserForm

# __import__(LoginForm)
app = Flask(__name__)

app.config['SECRET_KEY'] = '23bb8ccb2331455dc681eec4'


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login route"""
    form = LoginForm()
    # if form.validate_on_submit():

    return render_template('login.html', form=form)


# @login_required
@app.route('/dashboard', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def dashboard():
    """dashboard route"""
    return render_template('dashboard.html')


@app.route('/booking', methods=['GET', 'POST'], strict_slashes=False)
def bookings():
    """bookings route"""
    form = BookingForm()
    return render_template('bookings.html', form=form)


@app.route('/welcome', methods=['GET', 'POST'], strict_slashes=False)
def landing_page():
    """landing page"""
    return render_template('landing_page.html')


@app.route('/payments', methods=['GET', 'POST'], strict_slashes=False)
def payments():
    """route to payment page"""
    return render_template('payment.html')


@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
def profile():
    """route to profile page"""
    return render_template('profile.html')


@app.route('/sign_up', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """route to register page"""
    form = UserForm()
    # if form.validate_on_submit():
    return render_template('register.html', form=form)
