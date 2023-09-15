from datetime import timedelta

import stripe
from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user

from project import app, db, login_manager
from project.loginForm import LoginForm, user_confirmation
from project.bookingForms import BookingForm
from project.models.user import User, Receipt
from project.userForms import UserForm, validate_email

app.config['SECRET_KEY'] = '23bb8ccb2331455dc681eec4'
app.config[
    'STRIPE_PUBLIC_KEY'] = 'pk_test_51Nnk4hHFmbL2tNiZaiBGBtofoa4syCp6P3F1zLntka00KFJiXXUvXMzkVTEgxpbk8NNx0NKqsSiEru1wsyXKoth600lOW00m73'
app.config[
    'STRIPE_SECRET_KEY'] = 'sk_test_51Nnk4hHFmbL2tNiZo2CbNy518UyaGeKY6xEJepWn4BfUCp1eMfmYyzbzM7bRWHvKzXxrNTzCADpH8KlP2aGRIr2O005tmzhF1Z'
stripe.api_key = 'sk_test_51Nnk4hHFmbL2tNiZo2CbNy518UyaGeKY6xEJepWn4BfUCp1eMfmYyzbzM7bRWHvKzXxrNTzCADpH8KlP2aGRIr2O005tmzhF1Z'
login_manager.login_view = 'login'


surge = 1

@login_manager.user_loader
def load_user(user_id):
    from project import db
    return db.get_obj(id=user_id)


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login route"""
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = user_confirmation(email, password)
        if user:
            login_user(user)
            print(str(current_user))
            return redirect(url_for('dashboard'))
        else:
            print('failed')
            flash('Wrong email or password', category='danger')

    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dashboard():
    """dashboard route"""
    return render_template('dashboard.html')


@app.route('/stripe_payment/<uId>/<amount>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def stripe_payment(uId, amount):
    """bookings route"""
    amount = int(amount)
    qty = amount / (500 * surge)

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NnqAjHFmbL2tNiZhdxyclOP',
                    'quantity': int(qty),
                },
            ],
            mode='payment',
            success_url=url_for('dashboard', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('cancel', _external=True),
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@app.route('/bookings', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bookings():
    form = BookingForm()
    if form.validate_on_submit():
        # get the form and crete arecet ig=
        vehicle_image = request.files['vehicle_image']
        duration = ''
        if form.time_unit.data == 'hours':
            duration = str(timedelta(hours=form.duration.data)) + 'hour(s)'
        else:
            duration = str(timedelta(days=form.duration.data)) + 'day(s)'
        amt = amount(form.duration.data, form.time_unit.data)
        print("amount:", amt)
        receipt = Receipt(status="Active",
                          lot=form.lot.data,
                          space=form.space.data,
                          duration=duration,
                          start_time=form.start_time.data,
                          model=form.model.data,
                          plate_number=form.plate_number.data,
                          reservation_type=form.reservation_type.data,
                          amount=amt,
                          )
        current_user_uid = current_user.uId

        db.update_user_receipt(uId=current_user_uid, receipts=receipt)

        return redirect(url_for('stripe_payment', uId=current_user.uId, amount=amt))
    return render_template('bookings.html', form=form)


@app.route('/cancel', methods=['GET'], strict_slashes=False)
@login_required
def cancel():
    render_template('cancel.html')


@app.route('/welcome', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def landing_page():
    """landing page"""
    return render_template('landing_page.html')


@app.route('/payments', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def payments():
    """route to payment page"""
    return render_template('payment.html')


@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def profile():
    """route to profile page"""
    return render_template('profile.html')


@app.route('/sign_up', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """route to register page"""
    form = UserForm()
    if form.validate_on_submit():
        if validate_email(input_email=form.email.data):
            flash('User with email already exist')
            return redirect(url_for('register.html', form=form))
        print('great')

        file_v = request.files['vehicle_image']
        mimetype_v = file_v.mimetype
        print(file_v)
        vehicle_image = request.files['vehicle_image']

        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    vehicle_model=form.vehicle_model.data,
                    plate_number=form.plate_number.data,
                    vehicle_image=vehicle_image
                    )
        user.password = form.password.data
        print(form.email.data)
        db.insert(user)
        # profile_pic=file.read(),

        login_user(user)
        print(current_user)

        return redirect(url_for('dashboard'))

    return render_template('register.html', form=form)


@app.route('/sign_up', methods=['GET', 'POST'], strict_slashes=False)
def sign_out():
    """"""
    logout_user()
    return render_template('landing_page.html')


# flash('You are successfully logged in {}'
#       .format(user.first_name), category='primary')


def amount(duration, unit, surge=1):
    """"""
    if unit == "hours":
        return duration * 500 * surge
    else:
        return duration * 500 * 24 * surge
