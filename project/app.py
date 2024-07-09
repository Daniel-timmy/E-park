from datetime import timedelta, datetime
from apscheduler.schedulers.background import BackgroundScheduler
import stripe
from flask import render_template, request, redirect, flash, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from project import app, db, login_manager
# from project.AdminForm import AdminForm, admin_confirmation, AForm, validate_admin_email
from project.loginForm import LoginForm, user_confirmation
from project.bookingForms import BookingForm, dayHourChoices
# from project.models.active_receipts import ActiveReceipt
# from project.models.admin import Admin
from project.models.parking_lot import Lot
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

scheduler = BackgroundScheduler(daemon=True)


# def receipt_lot_status_update():
#     """"""


@login_manager.user_loader
def load_user(user_id):
    from project import db
    return db.get_obj(id=user_id)


# @app.route('/admin_login', methods=['GET', 'POST'], strict_slashes=False)
# def admin_login():
#     """Admin Login route"""
#     form = AdminForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         password = form.password.data
#         admin_code = form.admin_code.data
#
#         admin = admin_confirmation(email, password, admin_code)
#         if admin:
#             login_user(admin)
#             print(str(current_user))
#             return redirect(url_for('admin_dashboard'))
#         else:
#             print('failed')
#             flash('Wrong email or password', category='danger')
#
#     return render_template('admin.html', form=form)
#
#
# @app.route('/admin_sign_up', methods=['GET', 'POST'], strict_slashes=False)
# def admin_register():
#     """route to register page"""
#     form = AForm()
#     if form.validate_on_submit():
#         if validate_admin_email(input_email=form.email.data):
#             flash('User with email already exist')
#             return redirect(url_for('register.html', form=form))
#         print('great')
#
#         user = Admin(first_name=form.first_name.data,
#                      last_name=form.last_name.data,
#                      email=form.email.data,
#                      admin_code=form.admin_code.data
#
#                      )
#         user.password = form.password.data
#         print(form.email.data)
#         db.insert(user)
#         login_user(user)
#         print(current_user)
#
#         return redirect(url_for('admin_dashboard'))
#
#     return render_template('register_admin.html', form=form)
#
#
# @app.route('/admin_dashboard', methods=['GET', 'POST'], strict_slashes=False)
# def admin_dashboard():
#     paymentReceipts = []
#     receipts = ActiveReceipt.objects()
#     for receipt in receipts:
#         paymentReceipts.append(receipt)
#         paymentReceipts.reverse()
#     return render_template('payment.html', mReceipts=paymentReceipts)
#

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
    current_rate = 500
    empty_spaces = db.get_empty_space_count()
    # lot = Lot.objects(space__status='empty').count()
    car_status = ''
    mReceipts = []
    image = []

    pSpace = []
    # for individual_lot in lot:
    #     for individual_space in individual_lot.space:
    #         if individual_space.status == 'empty':
    #             pSpace.append(individual_space.space)
    receipts = current_user.receipts
    #
    # b = app.extensions['mongoengine'][1]
    # fs = b.connection.gridfs
    #
    #     # Replace 'vehicle_image' with the actual field name in your model
    # vehicle_image = fs.get(current_user.vehicle_image.grid_id)
    #
    # image_data = vehicle_image.read()
    # image = base64.b64encode(image_data).decode('utf-8')

    for receipt in receipts:#improve
        if receipt.status == 'Active':
            if receipt.plate_number == current_user.plate_number:
                car_status = 'Parked'
                break
            else:
                car_status = 'Not parked'

    for receipt in receipts:
        if receipt.status == 'Active':
            mReceipts.append(receipt)

    return render_template('dashboard.html', current_rate=current_rate, available_space=empty_spaces,
                           current_user=current_user, car_status=car_status, mReceipts=mReceipts, mimetype='jpg')


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


def get_available_spaces(lot_name, day):
    space_dict = {}
    if lot_name is None:
        return None
    space_list = []
    lot = db.get_lot(name=lot_name)[0]
    for space in lot.space:
        if day not in space.reserved_day_slot:
            space_list.append[space.space_name]
    space_dict['space_available'] = space_list
    return space_dict


@app.route('/bookings', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bookings():
    days = dayHourChoices('days')
    form = BookingForm()
    if form.validate_on_submit():

        duration = form.duration.data

        vehicle_image = request.files['vehicle_image']
        original_datetime = datetime.now()
        delta = timedelta(days=days.index(form.start_day.data))
        sTime = original_datetime + delta

        amt = amount(form.duration.data)
        receipt = Receipt(status="Active",
                          lot=form.lot.data,
                          space=form.space.data,
                          duration=duration,
                          start_time=sTime,
                          model=form.model.data,
                          plate_number=form.plate_number.data,
                          reservation_type=form.reservation_type.data,
                          amount=amt,
                          )
        uLot = Lot.objects.get(lot_name=form.lot.data)
        for space in uLot.space:
            if space.space == form.space.data:
                if form.reservation_type.data == 'On spot':
                    space.status = "occupied"
                else:
                    space.status = "reserved"
                space.time_left = duration
                uLot.save()

        db.update_user_receipt(uId=current_user.uId, receipts=receipt)

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
    paymentReceipts = []
    receipts = current_user.receipts
    for receipt in receipts:
        paymentReceipts.append(receipt)
        paymentReceipts.reverse()
    return render_template('payment.html', mReceipts=paymentReceipts)


@app.route('/cancel_order/<string:uid>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def cancel_order(uid):
    """"""

    mReceipts = []
    receipts = current_user.receipts
    for receipt in receipts:
        if receipt.uId == uid:
            receipt.status = "Canceled"
            current_user.save()
            uLot = Lot.objects.get(lot_name=receipt.lot)
            for space in uLot.space:
                if space.space_name == receipt.space:
                    space.time_left = 0
                    space.status = 'empty'
                    uLot.save()
                    break
    return render_template('dashboard.html')


@app.route('/profile', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def profile():
    """route to profile page"""
    return render_template('profile.html', current_user=current_user)


@app.route('/sign_up', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """route to register page"""
    form = UserForm()
    if form.validate_on_submit():
        if validate_email(input_email=form.email.data):
            flash('User with email already exist')
            return redirect(url_for('register.html', form=form))
        print('great')

        profile_pic = request.files['profile_pic']
        mimetype_v = profile_pic.mimetype
        vehicle_image = request.files['vehicle_image']

        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    vehicle_model=form.vehicle_model.data,
                    plate_number=form.plate_number.data,
                    vehicle_image=vehicle_image,
                    profile_pic=profile_pic
                    )
        user.password = form.password.data
        print(form.email.data)
        db.insert(user)
        # profile_pic=file.read(),

        login_user(user)
        print(current_user)

        return redirect(url_for('dashboard'))

    return render_template('register.html', form=form)


@app.route('/sign_out', methods=['GET', 'POST'], strict_slashes=False)
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
    

@app.route('/api/<string:lot_name>/<string:day>', methods=['GET'])
def get_data(lot_name, day):
    # ldict, lot_json = get_lot_and_spaces()
    response_dict = get_available_spaces(lot_name=lot_name, day=day)
    return jsonify(response_dict)

if __name__ == '__main__':
    app.run(debug=True)