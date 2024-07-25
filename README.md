# Student Enrollment Application

This Django web application streamlines student enrollment with an AJAX-powered registration form and supports exporting student data to CSV and PDF formats. It includes an admin dashboard for efficient management of student records. To get started, clone the repository from GitHub and navigate to the project directory. It is recommended to create and activate a virtual environment for the project, then install the required packages, which include Django and ReportLab. After setting up the environment, create the database and apply migrations. Create a superuser to access the admin interface, then run the development server.

The registration form can be accessed at `http://127.0.0.1:8000/enrollment/register/`, where users can submit the form to register a student and receive immediate feedback. Student data can be exported by visiting `http://127.0.0.1:8000/enrollment/export/csv/` for CSV or `http://127.0.0.1:8000/enrollment/export/pdf/` for PDF. The admin interface is available at `http://127.0.0.1:8000/admin/`, allowing superusers to manage student records.

If registered entries are not appearing in the admin dashboard, ensure the AJAX submission is functioning correctly and data is being saved to the database. You can verify entries using Django’s shell and confirm that the `Student` model is registered in the admin interface.
