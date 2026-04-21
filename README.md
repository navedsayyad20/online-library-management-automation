# 📚 Online Library Management Automation (Playwright + Pytest)

## 🔹 Project Overview

This project automates an online library system using Playwright with Python and Pytest.

The Demo Web Shop site is used as a simulation where:

* Products → Books
* Cart → Borrowed books
* Wishlist → Saved books

---

## 🔹 Features Covered

* ✅ User Registration
* ⏭️ Login (Skipped - unstable on demo site)
* ✅ Book Search
* ✅ Borrow Book (Add to Cart)
* ✅ Return Book (Remove from Cart)
* ⏭️ Wishlist (Skipped - inconsistent behavior on site)

---

## 🔹 Tech Stack

* Python
* Playwright
* Pytest

---

## 🔹 Project Structure

```
Library_Automation/
│
├── pages/
│   ├── base_page.py
│   ├── register_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── cart_page.py
│   └── wishlist_page.py
│
├── tests/
│   ├── test_register.py
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_cart.py
│   └── test_wishlist.py
│
├── utils/
│   └── random_data.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## 🔹 How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Install Playwright browsers:

```
playwright install
```

3. Run tests:

```
pytest -v
```

---

## 🔹 Test Results

* Passed: 4
* Skipped: 2
* Failed: 0

---

## 🔹 Known Issues / Skipped Tests

* **Login Test** → Skipped due to unstable authentication behavior on demo website
* **Wishlist Test** → Skipped due to inconsistent element availability

These were skipped intentionally to maintain test stability and avoid flaky results.

---

## 🔹 Key Learnings

* Handling dynamic elements in UI automation
* Managing flaky tests
* Using Page Object Model (POM)
* Writing stable and maintainable test cases

---

## 🔹 Author

Naved Sayyad

