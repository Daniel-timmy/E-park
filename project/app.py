import base64
from datetime import timedelta, datetime
import stripe
from flask import render_template, request, redirect, flash, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from project import app, db, login_manager, scheduler
# from project.AdminForm import AdminForm, admin_confirmation, AForm, validate_admin_email
from project.loginForm import LoginForm, user_confirmation
from project.bookingForms import BookingForm, dayHourChoices
# from project.models.active_receipts import ActiveReceipt
# from project.models.admin import Admin
from project.models.parking_lot import Lot
from project.models.user import User, Receipt
from project.userForms import UserForm, validate_email
from IPython.display import Image

app.config['SECRET_KEY'] = '23bb8ccb2331455dc681eec4'
app.config[
    'STRIPE_PUBLIC_KEY'] = 'pk_test_51Nnk4hHFmbL2tNiZaiBGBtofoa4syCp6P3F1zLntka00KFJiXXUvXMzkVTEgxpbk8NNx0NKqsSiEru1wsyXKoth600lOW00m73'
app.config[
    'STRIPE_SECRET_KEY'] = 'sk_test_51Nnk4hHFmbL2tNiZo2CbNy518UyaGeKY6xEJepWn4BfUCp1eMfmYyzbzM7bRWHvKzXxrNTzCADpH8KlP2aGRIr2O005tmzhF1Z'
stripe.api_key = 'sk_test_51Nnk4hHFmbL2tNiZo2CbNy518UyaGeKY6xEJepWn4BfUCp1eMfmYyzbzM7bRWHvKzXxrNTzCADpH8KlP2aGRIr2O005tmzhF1Z'
login_manager.login_view = 'login'
surge = 1

space_name_list = ['1', '2', '3', '4', '5', '6', '7', '8','9'
                   '10', '11', '12', '13', '14', '15', '16',
                   '17', '18', '19', '20', '21', '22', '23', '24',
                   '25', '26', '27', '28', '29', '30', '31', '32',
                   '33', '34', '35', '36', '37', '38', '39', '40',
                   '41', '42', '43', '44', '45', '46', '47', '48',
                   '49', '50', '51', '52', '53', '54', '55', '56',
                   '57', '58', '59', '60', '61', '62', '63', '64',
                   '65', '66', '67', '68', '69', '70', '71', '72',
                   '73', '74', '75', '76', '77', '78', '79', '80'
                   ]

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

@app.route('/api/get_date_for_timer')
def get_date():
    """
    An api endpoint that returns the end date for an active booking
    """
    receipts = current_user.receipts
    for receipt in receipts:
        if receipt.status == 'Active':
            delta = timedelta(days=receipt.duration)
            sTime = receipt.start_time + delta
            formatted_sTime = sTime.strftime("%b %d, %Y %H:%M:%S")
            return jsonify({'date': formatted_sTime, 'plate_number': receipt.plate_number})
    return jsonify({'date': 'Inactive', 'plate_number': 'Inactive'})

@app.route('/dashboard', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dashboard():
    """dashboard route"""
    current_rate = 500
    empty_spaces = db.get_empty_space_count()
    car_status = 'Not Parked'
    mReceipts = []
   
    receipts = current_user.receipts
    profile_pic = base64.b64encode(current_user.profile_pic.read()).decode('utf-8')
    vehicle_image = base64.b64encode(current_user.vehicle_image.read()).decode('utf-8')
    for receipt in receipts:
        if receipt.status == 'Active':
            mReceipts.append(receipt)
            if receipt.plate_number == current_user.plate_number:
                car_status = 'Parked'
    mReceipts.reverse()
            
    return render_template('dashboard.html', current_rate=current_rate, available_space=empty_spaces, 
                           vehicle_image=vehicle_image, profile_pic=profile_pic,
                           current_user=current_user, car_status=car_status,
                             mReceipts=mReceipts, mimetype='jpeg', enumerate=enumerate)


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

def amount(duration, surge=1):
    """
    Calculates the amount to be charged
    """
   
    return duration * 500 * 24 * surge

@app.route('/bookings', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bookings():
    days = dayHourChoices('days')
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    month = datetime.now().month
    day = datetime.now().day
   
    form = BookingForm()
    if form.validate_on_submit():
        duration = int(form.duration.data)
        end_day = day + duration
        if end_day > months[month]:
            end_day = end_day - months[month]

        vehicle_image = request.files['vehicle_image']
        original_datetime = datetime.now()
        delta = timedelta(days=days.index(form.start_day.data))
        sTime = original_datetime + delta

        amt =  duration * 500 * 24 * surge
            
        receipt = Receipt(status= 'Active' if form.reservation_type.data == 'On spot' else 'Inactive',
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
            if space.space_name == form.space.data:
                idx = days.index(form.start_day.data)
                i = duration-(7-idx)
                if form.reservation_type.data == 'On spot':
                    space.status = "occupied"
                    space.reserved_day_slot[receipt.uId] = [form.start_day.data, end_day, current_user.email]
                    if idx + duration <= 7:
                        space.days_filled.extend(days[idx:idx + duration])
                    else:
                        space.days_filled.extend(days[idx:] + days[:i])
                else:
                    receipt.status = 'Reserved'
                    space.reserved_day_slot[receipt.uId] = [form.start_day.data, end_day, current_user.email]
                    if idx + duration <= 7:
                        space.days_filled.extend(days[idx:idx + duration])
                    else:
                        space.days_filled.extend(days[idx:] + days[:i])
                space.time_left = duration
                space.duration = duration
                space.start_time = sTime
                space.email = current_user.email
                uLot.save()
                break
        # problem with the receipt
        current_user.receipts.append(receipt)
        current_user.save()

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


def get_available_spaces(lot_name, day, duration, sp):
    if lot_name is None or lot_name == ' ' or type(lot_name) != str:
        print(f'Type of lot_name: {type(lot_name)}')
        return None, {'status': f'Incorrect lot name: {lot_name}'}
    
    if day is None or day not in ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]:
        print(f'Type of day: {type(day)}')
        return None, {'status': f'Incorrect day:{day}'}
    
    if duration is None or duration < 1 or duration > 7:
        print(f'Type of duration: {type(duration)}')
        return None, {'status': 'Incorrect duration'}
    
    if sp is None or type(sp) != str or sp not in space_name_list:
        return None, {'status': 'Incorect space name'}
    
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    idx = days.index(day)
    day_set = set()
  
    if idx + duration <= 7:
        day_set.update(days[idx:idx + duration])
    else:
        day_set.update(days[idx:])
        day_set.update(days[:duration-(7-idx)])

    space_dict = {}

    lot = db.get_lot(name=lot_name)[0]
    
    for space in lot.space:
        ln = len(day_set - set(space.days_filled))
        if space.space_name == sp:
            if ln == duration:
                space_dict[f'Space{sp}'] = [list(day_set - set(space.days_filled)),ln]
                
                break
            else:
                space_dict[f'Space{sp}'] = [list(day_set - set(space.days_filled)), ln]
        else:
            space_dict[str(ln)] = space_dict.get(str(ln), []) + [space.space_name]
    
    # print(f'Space dict: {space_dict}')
    space_dict['status'] = 'success'
    return space_dict, {'status': 'success'}

@app.route('/api/<string:lot_name>/<string:space>/<string:day>/<int:duration>', methods=['GET'])
def get_data(lot_name, space, day, duration):
    response_dict, status_dict = get_available_spaces(lot_name=lot_name, day=day, duration=duration, sp=space)
    if response_dict is None:
        # print(f'Error: {status_dict}')
        return jsonify({'message': 'Invalid input', 'status': 'failed'})
    print(f'Response dict: {response_dict}')
    return jsonify(response_dict)
    

def update_lot_receipt_status():
    """
    Works with the scheduler to update the status of the receipt and
    the space in the lot
    """
    from bookingForms import today
    lots = Lot.objects()
    todays_date = datetime.now().day

    for lot in lots:
        for space in lot.space:
            completed = {}
            delete_idx = []
            starting = {}
            for idx in space.reserved_day_slot:
                if space.reserved_day_slot[idx][1] == todays_date:
                    completed[idx] = space.reserved_day_slot[idx]
                    delete_idx.append(idx)
                    space.time_left -= 1
                if space.reserved_day_slot[idx][0] == today:
                    starting[idx] = space.reserved_day_slot[idx]
                if space.reserved_day_slot[idx][1] < todays_date:# get index
                    space.time_left -= 1
                    space.days_filled.remove(today)

            if completed:
                for idx in completed:
                    space.status = 'empty'
                    lot.save()
                    for user in User.objects().filter(email=space.reserved_day_slot[idx][2]).only('receipts'):
                        for receipt in user.receipts:
                            if receipt.uId == idx and receipt.space == space.space_name:
                                receipt.status = 'expired'
                                del space.reserved_day_slot[idx]
                                space.days_filled.remove(today)
                                user.save()
                                break
            if starting:
                for idx in starting:
                    space.status = 'occupied'
                    lot.save()
                    for user in User.objects().filter(email=space.reserved_day_slot[idx][2]).only('receipts'):
                        for receipt in user.receipts:
                            if receipt.uId == idx and receipt.space == space.space_name:
                                receipt.status = 'Active'
                                user.save()
                                break

if __name__ == '__main__':
    scheduler.add_job(id='receipt_lot_status_update', func=update_lot_receipt_status, trigger='interval',)
    scheduler.start()
    app.run(debug=True, threaded=True)