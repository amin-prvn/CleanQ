# CleanQ
 We all have to go to a clinic once in a while (hopefully, only for a routine checkup), and we all hate having to sit there waiting until it’s our turn. (not to mention now that we have a pandemic going on, waiting in a crowded place may be really dangerous!). So, once again we want to use technology to solve a problem! CleanQ (clearly a play on Clinic and a Clean Queue), aims to create a platform in which clinics can sign up to accept patients, and patients can make reservations on clinics.
## Installation

1. Create virtualenv.
```
python3 -m virtualenv venv
```
2. Active environment.
```
source venv/bin/activate 
```
3. Install requirements.
```
pip install -r requirements.txt
```
4. Make migrations
```
python manage.py makemigrations
```
5. Migrate model to database
```
python manage.py migrate  
```
6. Run development server
```
python manage.py runserver 
```

---
## TODO list
- [x] Standard Django admin panel, with access to all data
- [x] Verifying signed up clinics for admin
- [x] Sign up for clinic
- [x] Profile actions for clinic
- [ ] Login for clinic
- [x] Seeing a list of reservations (+filtering the past/upcoming reservations) for clinic
- [x] Signup/login/profile actions for patient
- [ ] Loginfor patient
- [x] Seeing a list of clinics + search for patient 
- [x] Seeing list of own reservations  (+filtering the past/upcoming reservations) for patient

---
Developed by Mohammad Amin Parvanian
