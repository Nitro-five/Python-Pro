Usage
Start the Django server:

bash
Copy code
python manage.py runserver
Creating a short link:

Navigate to the /register/ page to create a new link.

Generate QR code for a shortened URL:

Visit the URL /qr/<short_url>/ to generate and view the QR code for any shortened URL.
View Click Analytics:

Visit the URL /analytics/ to view detailed statistics of your shortened URLs.
You will see a table with the number of clicks, unique clicks, clicks by device type, and clicks by country.
Admin Panel:

To manage users, links, and QR codes, visit the Django admin panel at /admin/.

Username: admin
Password: (use the password you set when creating the superuser)
Development