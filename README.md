# Cash Management

A Personal Cash Management web app to provide users with a convenient and efficient way to manage their finances. This application helps individuals track their income, expenses, and transactions, allowing them to gain insights into their spending habits, save money, and maintain financial stability.

## 🚀 Features

- **User Authentication**
  - User registration with username, email, and password
  - Login with username or email
  - Secure logout functionality

- **Cash Management Dashboard**
  - View total income, expenses, and balance
  - Real-time financial summary
  - Transaction history

- **Transaction Management**
  - Add income/cash with source and description
  - Add expenses with description
  - Track all transactions with timestamps

- **Profile Management**
  - Update username, email, first name, and last name
  - View current profile information

---

## 🛠️ Technology Stack

- **Backend:** Django 5.x (Python)
- **Database:** SQLite3
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django Authentication System

---

## 📋 Project Structure

```
Cash-Management/
├── Rabbi_20_ManageCash/
│   ├── ManageCash/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── Rabbi_20_ManageCash/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Templates/
│   │   ├── add_cash.html
│   │   ├── add_expense.html
│   │   ├── base.html
│   │   ├── base,html
│   │   ├── dashboard.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── navbar.html
│   │   ├── profile.html
│   │   └── register.html
│   ├── db.sqlite3
│   └── manage.py
├── Env/
├── requirments.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```
bash
git clone <repository-url>
cd Cash-Management
```

### 2. Create Virtual Environment
```
bash
python -m venv Env
```

### 3. Activate Virtual Environment
```
bash
# Windows
Env\Scripts\activate

# Linux/Mac
source Env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirments.txt
```

### 5. Run Migrations
```
bash
cd Rabbi_20_ManageCash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server
```
bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and navigate to: **http://127.0.0.1:8000/**

---

## 🔗 URL Patterns

| URL | View | Description |
|-----|------|-------------|
| `/` | login_function | Login page |
| `/register/` | register_function | User registration |
| `/logout/` | logout_function | Logout |
| `/dashboard/` | dashboard_function | Cash Management Dashboard |
| `/add-cash/` | add_cash_function | Add Income form |
| `/add-expense/` | add_expense_function | Add Expense form |
| `/profile/` | profile_function | Profile management |

---

## 📊 Database Models

### CustomUserModel
Extends Django's AbstractUser for custom authentication.

### AddCashModel
- `user` - ForeignKey to CustomUserModel
- `source` - Income source (e.g., Salary, Freelance)
- `datetime` - Date of transaction
- `amount` - Income amount
- `description` - Optional description

### ExpenseModel
- `user` - ForeignKey to CustomUserModel
- `description` - Expense description
- `amount` - Expense amount
- `datetime` - Date of transaction

---

## 🎨 Templates

- **login.html** - User login with email/username support
- **register.html** - User registration form
- **dashboard.html** - Main dashboard with financial summary
- **add_cash.html** - Add income transaction form
- **add_expense.html** - Add expense transaction form
- **profile.html** - Profile management view
- **base.html** - Base template with footer

---

## 📱 Usage

1. Navigate to the login page
2. Click "Register" to create a new account
3. After registration, login with your credentials
4. Use the dashboard to view your financial summary
5. Add income using "Add Income" button
6. Add expenses using "Add Expense" button
7. Update your profile using the "Profile" link

---

## 🔒 Security Features

- CSRF protection
- Password validation
- User authentication required for protected routes
- Secure logout functionality

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Developer

**Md. Rabbi Islam**

- Portfolio: [rabbi.crsyndicate.info](https://rabbi.crsyndicate.info)
- Email: rabbiprimon00000@gmail.com
- LinkedIn: [/in/md-rabbi-islam-747770231/](https://linkedin.com/in/md-rabbi-islam-747770231/)
- Phone: +8801644358765
- LeetCode: [rabbiprimon](https://leetcode.com/u/rabbiprimon/)
- HackerRank: [rabbiprimon00000](https://www.hackerrank.com/profile/rabbiprimon00000)

---

Built with ❤️ using Django
