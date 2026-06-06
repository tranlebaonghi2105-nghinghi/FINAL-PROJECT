# FINAL-PROJECT

## Topic 6: Cafe Management System

---

# 1. Project Description

This project is a Python console application developed for managing a cafe system.

The application allows users to manage menu items, tables, promotions, invoices, statistics, and persistent data storage through JSON files.

The system is implemented using Object-Oriented Programming (OOP) principles and follows a modular architecture with separate Models, Services, Views, and Data layers.

This project was developed to apply knowledge from Programming Methods, including:

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- File Handling
- JSON Storage
- Data Validation
- Modular Programming
- GitHub Version Control

Selected Topic:

**Topic 6 – Restaurant / Cafe Management System**

---

# 2. Project Objectives

The system aims to:

- Manage food, drink, and combo items
- Manage cafe table status
- Generate invoices
- Apply promotions and discounts
- Store data permanently using JSON
- Calculate business statistics
- Practice Object-Oriented Programming concepts
- Practice Git and GitHub workflow

---

# 3. OOP Concepts Applied

## 3.1 Encapsulation

Private attributes are used in classes such as:

- MenuItem
- Table
- Promotion
- Invoice

Properties are used to control access to data.

---

## 3.2 Inheritance

Classes:

- Food
- Drink
- Combo

inherit from:

- MenuItem

---

## 3.3 Polymorphism

Each menu item implements:

```python
calculate_price()
```

allowing different pricing behaviors.

---

## 3.4 Abstraction

Abstract class:

```python
MenuItem
```

defines:

```python
calculate_price()
```

which must be implemented by subclasses.

---

# 4. Technologies Used

| Component | Purpose |
|------------|------------|
| Python 3 | Main programming language |
| JSON | Persistent data storage |
| PrettyTable | Formatted table display |
| Git | Version control |
| GitHub | Source code hosting |
| CLI | User interaction |

---

# 5. Project Structure

```text
FINAL-PROJECT
│
├── data
│   ├── menu.json
│   ├── tables.json
│   ├── promotions.json
│   └── invoices.json
│
├── models
│   ├── menu_item.py
│   ├── food.py
│   ├── drink.py
│   ├── combo.py
│   ├── table.py
│   ├── promotion.py
│   └── invoice.py
│
├── services
│   ├── menu_service.py
│   ├── table_service.py
│   ├── promotion_service.py
│   ├── invoice_service.py
│   └── file_service.py
│
├── views
│   └── menu_view.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

# 6. Main Features

## 6.1 Menu Management

Supports:

- Add Menu Item
- View Menu
- Search Menu Item
- Update Menu Item
- Delete Menu Item
- Sort Ascending
- Sort Descending

Supported item types:

- Food
- Drink
- Combo

---

## 6.2 Table Management

Supports:

- Add Table
- View Tables
- Update Table Status

Table statuses:

- Available
- Occupied

---

## 6.3 Promotion Management

Supports:

- Add Promotion
- View Promotions
- Delete Promotion

Promotion discount percentage:

```text
0% - 100%
```

---

## 6.4 Invoice Management

Supports:

- Create Invoice
- Add Item To Invoice
- Apply Promotion To Invoice
- View Invoice

Invoice automatically calculates:

- Subtotal
- Discount
- Total

---

## 6.5 Statistics

Supports:

### Total Revenue

Calculates total revenue from all invoices.

### Number Of Invoices

Displays total number of invoices.

### Most Expensive Item

Displays the most expensive item sold.

---

## 6.6 JSON Storage

Automatically saves:

- Menu
- Tables
- Promotions
- Invoices

Data is restored automatically when the application starts.

---

# 7. Menu

```text
1. Add Menu Item
2. View Menu
3. Search Menu Item
4. Update Menu Item
5. Delete Menu Item
6. Sort Menu Ascending
7. Sort Menu Descending
8. Add Table
9. View Tables
10. Update Table Status
11. Add Promotion
12. View Promotions
13. Delete Promotion
14. Create Invoice
15. Add Item To Invoice
16. Apply Promotion To Invoice
17. View Invoices
18. Total Revenue
19. Number Of Invoices
20. Most Expensive Item
0. Exit
```

---

# 8. Persistent Storage

The application uses JSON files:

```text
menu.json
tables.json
promotions.json
invoices.json
```

Data is loaded when the application starts and saved when the application exits.

---

# 9. Statistics Examples

Example:

```text
Total Revenue: 270.00
```

```text
Number Of Invoices: 15
```

```text
Most Expensive Item:
ID: C01
Name: Family Combo
Price: 120.00
```

---

# 10. How To Run

Install dependency:

```bash
pip install prettytable
```

Run application:

```bash
python main.py
```

---

# 11. Git Workflow

Development process:

```bash
git checkout -b <branch>

git add .

git commit -m "message"

git push --set-upstream origin <branch>
```

GitHub:

```text
Create Pull Request
Merge Pull Request
```

Back to main:

```bash
git checkout main
git pull origin main
```

---

# 12. Self Assessment

| Criteria | Score |
|-----------|-----------|
| OOP Design | 1.0 |
| Menu Management | 1.0 |
| Table Management | 1.0 |
| Promotion Management | 1.0 |
| Invoice Management | 1.0 |
| PrettyTable Display | 1.0 |
| JSON Storage | 1.0 |
| Statistics | 1.0 |
| GitHub Workflow | 1.0 |
| Documentation | 1.0 |
| TOTAL | 10.0 / 10.0 |

---

# 13. Student Information

Student Name: Trầ Lê Bảo Nghi

Student ID: 24S7040007

Class: Tin2E

Course: Programming Methods

Instructor: Dr. Tran Van Long

Faculty of Informatics

Hue University of Education