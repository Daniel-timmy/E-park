

# E-park

E-park is a web-based parking lot management system designed to streamline parking operations. This application provides a user-friendly interface for drivers to locate available parking spots and allows administrators to manage and monitor parking usage efficiently. It integrates secure payment processing and leverages vehicle detection for enhanced functionality.

## Features

- **Real-time Parking Spot Availability**: Users can view available parking spots in real-time.
- **Vehicle Detection**: Using YOLOv5, the system detects and counts vehicles in designated parking areas, enabling accurate availability tracking.
- **Secure Payments**: Integrated with Stripe to handle secure transactions for parking fees.
- **Admin Dashboard**: Admins can manage parking spots, view real-time usage, and generate reports on parking data.
- **User-friendly Interface**: Developed with a responsive front end using HTML, CSS, and JavaScript for easy access on any device.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **Vehicle Detection**: YOLOv5
- **Payment Processing**: Stripe API

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- MongoDB server (local or cloud)
- YOLOv5
- Stripe account and API keys

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/e-park.git
   cd e-park
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up Stripe API keys and MongoDB URI in environment variables:

   ```bash
   export STRIPE_PUBLIC_KEY="your-public-key"
   export STRIPE_SECRET_KEY="your-secret-key"
   export MONGODB_URI="your-mongodb-uri"
   ```

### MongoDB Setup

1. Set up a MongoDB database (e.g., using MongoDB Atlas or a local MongoDB instance).
2. Create collections for users, parking spots, and transactions.
3. Update any MongoDB configuration in the Flask app as needed.

### Running the Application

```bash
flask run
```

The application should now be accessible at `http://127.0.0.1:5000`.

## Usage

1. **User**: Sign up and log in to view available parking spots and make payments.
2. **Admin**: Log in to the admin dashboard to manage spots, view occupancy reports, and monitor revenue.

## Future Enhancements

- Add support for multiple parking lots
- Enhance vehicle detection accuracy with further machine learning models
- Implement a mobile app version
