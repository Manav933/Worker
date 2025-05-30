# Worker Production Management System

A Django-based web application for managing worker production records in a textile or similar industry. The system allows tracking daily production meters for workers across different machines, calculating totals, and generating summaries.

## Features

- Track daily production meters for each worker
- Support for up to 192 machines
- 15-day production cycle tracking
- Automatic calculation of totals and averages
- Worker-wise and machine-wise summaries
- Monthly statistics and reports
- Responsive web interface

## Requirements

- Python 3.8 or higher
- Django 5.0 or higher
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd worker-management
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## Usage

1. Log in to the admin interface at http://127.0.0.1:8000/admin/ using your superuser credentials
2. Navigate to http://127.0.0.1:8000/ to access the main application
3. Use the navigation menu to:
   - View and add production records
   - View worker summaries
   - View machine summaries
   - Generate reports

## Data Structure

Each production record contains:
- Worker name
- Machine number (1-192)
- Date
- Daily meter readings (15 days)
- Rate per meter
- Auto-calculated fields:
  - Total meters
  - Total rate (earnings)
  - Average meters per day

## Security

- Login required for all operations
- CSRF protection enabled
- Form validation and sanitization
- Unique constraints to prevent duplicate entries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 