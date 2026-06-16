# FINAL-PROJECT

## Topic 6: Cafe Management System

---

# 1. Project Description

A Python application for managing a cafe system, built with OOP principles and a layered architecture.

Features: Menu management, Table management, Promotions, Invoice generation, Statistics, CSV export, and a full GUI (Tkinter).

**Topic 6 – Restaurant / Cafe Management System**

---

# 2. OOP Concepts Applied

## 2.1 Encapsulation
Private attributes with `@property` and validation in `MenuItem`, `Table`, `Promotion`, `Invoice`.

## 2.2 Inheritance
`Food`, `Drink`, `Combo` inherit from abstract base class `MenuItem`.

## 2.3 Polymorphism
Each subclass overrides `calculate_price()` with different logic:
- Food: base price
- Drink: base price + 5% service fee
- Combo: base price − 10% discount

## 2.4 Abstraction
`MenuItem(ABC)` defines `@abstractmethod calculate_price()` — all subclasses must implement it.

---

# 3. Technologies Used

| Component | Purpose |
|-----------|---------|
| Python 3 | Main language |
| Tkinter | GUI interface |
| JSON | Persistent storage |
| CSV | Statistics export |
| PrettyTable | CLI table display |
| Git / GitHub | Version control |

---

# 4. Project Structure

```text
FINAL-PROJECT/
├── data/
│   ├── menu.json
│   ├── tables.json
│   ├── promotions.json
│   └── invoices.json
├── models/
│   ├── menu_item.py      # Abstract base class
│   ├── food.py
│   ├── drink.py
│   ├── combo.py
│   ├── table.py
│   ├── promotion.py
│   └── invoice.py
├── services/
│   ├── menu_service.py
│   ├── table_service.py
│   ├── promotion_service.py
│   ├── invoice_service.py
│   └── file_service.py
├── views/
│   ├── gui_view.py       # Tkinter GUI
│   └── menu_view.py      # CLI view
├── main.py
├── requirements.txt
└── README.md
```

---

# 5. Features

## Menu Management
- Add / View / Search / Update / Delete items
- Sort by price (ascending / descending)
- Item types: Food, Drink, Combo

## Table Management
- Add / View tables
- Update table status: Available / Occupied

## Promotion Management
- Add / View / Delete promotions (0–100% discount)

## Invoice Management
- Create invoice linked to a table
- Add multiple items to an invoice
- Apply promotion code → auto-calculate total

## Statistics
- Total revenue
- Invoice count
- Most expensive item sold
- Revenue breakdown by item type (Food / Drink / Combo)
- Revenue breakdown by month
- Top 3 best-selling items
- Export invoices to CSV (`data/invoices_export.csv`)

---

# 6. How To Run

Install dependencies:

```bash
pip install prettytable
```

Run (GUI mode by default):

```bash
python main.py
```

To switch to CLI mode, choose option at startup (or edit `main.py`).

---

# 7. Git Workflow

```bash
git checkout -b <branch-name>
git add .
git commit -m "describe change"
git push --set-upstream origin <branch-name>
```

Then open a Pull Request on GitHub and merge into `main`.

---

# 8. Student Information

| Field | Info |
|-------|------|
| Student Name | Trần Lê Bảo Nghi |
| Student ID | 24S7040007 |
| Class | Tin2E |
| Course | Programming Methods |
| Instructor | Dr. Tran Van Long |
| Faculty | Faculty of Informatics, Hue University of Education |