# Guild Canteen Inventory Management System

A command-line inventory management system for the **Guild Canteen at Uganda Christian University (UCU)**. It helps canteen staff track stock, record sales, monitor expiry dates and account for spoiled, damaged or lost goods, all from a simple text menu.

Developed by **Group 7** as a university project.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Using the System](#using-the-system)
- [Built-in Test Demo](#built-in-test-demo)
- [Project Design](#project-design)
- [Input Validation](#input-validation)
- [Known Limitations](#known-limitations)
- [Possible Improvements](#possible-improvements)
- [Team](#team)

---

## Features

- **Add products** with a unique code, name, price, quantity and expiry date
- **View inventory** with live status flags for expiry (`OK` / `EXPIRED`) and stock level (`OK` / `LOW STOCK`)
- **Add stock** to existing products
- **Sell products**, with automatic total calculation and stock deduction
- **Expiry checking**: lists expired products still in stock with the estimated financial loss
- **Loss recording** for spoiled, damaged or lost goods, including the reason and estimated loss
- **Low-stock alerts**: a product is flagged when its quantity falls to or below its threshold (default: 10)
- **Automated test demo** that walks through every major feature, useful for presentations

---

## Requirements

- **Python 3.7 or newer** (uses `date.fromisoformat` and f-strings)
- No third-party packages. The program uses only the Python standard library (`datetime`).

Check your Python version:

```bash
python --version
```

---

## Getting Started

1. **Save** the source file, for example as `guild_canteen.py`.
2. **Open a terminal** in the folder containing the file.
3. **Run** the program:

```bash
python guild_canteen.py
```

On some systems you may need to use `python3` instead of `python`.

---

## Using the System

When the program starts, the main menu is displayed:

```
==================================================
           GUILD CANTEEN - UCU
        INVENTORY MANAGEMENT SYSTEM
==================================================
1. Add product
2. View products
3. Add stock
4. Sell product
5. Check expired products
6. Record spoiled/damaged/lost goods
7. Run complete test demo
0. Exit
```

| Option | Description |
|--------|-------------|
| **1. Add product** | Enter a product code, name, selling price (UGX), quantity and expiry date (`YYYY-MM-DD` or `N/A`). |
| **2. View products** | Displays every product with its price, quantity, expiry date and status. |
| **3. Add stock** | Select a product by its list number and enter the quantity to add. |
| **4. Sell product** | Select a product and enter the quantity sold. Shows the total amount and remaining stock. |
| **5. Check expired products** | Lists expired items that still have stock and the estimated loss (`quantity × price`). |
| **6. Record loss** | Select a product, enter the quantity lost and a reason (Spoiled / Damaged / Lost). Stock is reduced automatically. |
| **7. Run complete test demo** | Loads sample data and runs 16 automated tests. **This clears the current product list.** |
| **0. Exit** | Closes the program. |

### Example: adding a product

```
Product code: GC001
Product name: Rolex
Selling price (UGX): 5000
Quantity: 20
Expiry date (YYYY-MM-DD or N/A): N/A

Product added successfully.
Product code: GC001
Product name: Rolex
```

### Example: recording a sale

```
Sale successful.
Product: Rolex
Quantity sold: 2
Total amount: UGX 10,000.00
Remaining stock: 18
```

---

## Built-in Test Demo

Menu option **7** runs a scripted demonstration using sample canteen products:

| Code | Product | Price (UGX) | Quantity | Expiry |
|------|---------|-------------|----------|--------|
| GC001 | Rolex | 5,000 | 20 | N/A |
| GC002 | Bottled Water | 1,000 | 50 | 2027-03-15 |
| GC003 | Samosa | 1,500 | 30 | 2026-09-20 |
| GC004 | Mango Juice | 3,000 | 15 | 2026-09-18 |
| GC005 | Expired Milk | 2,500 | 10 | 2026-01-10 |

The demo verifies the following:

- Adding and viewing products
- Adding stock
- Selling products and calculating totals
- Blocking sales above available stock
- Blocking zero and negative quantities
- Detecting expired products and blocking their sale
- Recording spoiled, damaged and lost goods
- Detecting duplicate product codes
- Final inventory check

> **Note:** Expiry checks compare against today's date. The demo's Samosa and Mango Juice expiry dates (September 2026) are now in the past, so they will be treated as expired. Update those dates to a future date to see them sold normally.

---

## Project Design

The program is built from two classes.

### `Product`

Represents a single item sold at the canteen.

| Attribute | Description |
|-----------|-------------|
| `product_code` | Unique identifier (e.g. `GC001`) |
| `name` | Product name |
| `price` | Selling price of one item (UGX) |
| `quantity` | Current stock level |
| `expiry` | Expiry date (`YYYY-MM-DD`) or `N/A` |
| `low_stock_threshold` | Stock level at or below which the product is flagged low (default `10`) |

| Method | Purpose |
|--------|---------|
| `sell(amount)` | Validates and processes a sale, reducing stock |
| `add_stock(amount)` | Increases stock by a positive amount |
| `is_low_stock()` | Returns `True` if quantity is at or below the threshold |
| `is_expired()` | Returns `True` if the expiry date has passed |
| `show()` | Prints the product's details and status |

### `Shop`

Manages the full inventory (a list of `Product` objects) and the user interface.

| Method | Purpose |
|--------|---------|
| `add_product()` | Interactive product creation with validation |
| `add_demo_product()` | Adds a product without prompts (used by the demo) |
| `view_products()` | Lists all products |
| `select_product()` | Lets the user pick a product by number |
| `add_stock()` / `sell_product()` | Menu handlers for restocking and selling |
| `expired_products()` | Reports expired stock and estimated loss |
| `record_loss()` | Records spoiled, damaged or lost goods |
| `test_demo()` | Runs the automated demonstration |
| `run()` | Displays the main menu and handles user choices |

---

## Input Validation

The system protects data integrity with these checks:

- Product code and name cannot be empty
- Product codes must be unique (case-insensitive)
- Price must be greater than zero
- Quantity cannot be negative when adding a product
- Expiry dates must be in `YYYY-MM-DD` format or `N/A`
- Sales, restocks and loss records must use quantities greater than zero
- Sales and loss records cannot exceed available stock
- Expired products cannot be sold
- Non-numeric input is caught and the user is asked to try again

---

## Known Limitations

- **No data persistence**: all data is held in memory and is lost when the program exits. Products must be re-entered each session.
- **No sales history**: individual transactions and loss records are not logged, only the resulting stock levels.
- **Single user, no authentication**: anyone running the program has full access.
- **Fixed low-stock threshold** of 10 for products added through the menu.

---

## Possible Improvements

- Save and load inventory from a file (CSV, JSON) or a database (e.g. SQLite)
- Keep a transaction log and generate daily or weekly sales and loss reports
- Allow editing and deleting products
- Support selling multiple items in a single transaction (a cart or receipt)
- Add user accounts with roles (e.g. manager vs. cashier)
- Let staff set a custom low-stock threshold per product
- Add unit tests and a graphical or web interface

---

## Team

**Group 7**, Uganda Christian University

| # | Name | Registration No. |
|---|------|------------------|
| 1 | Ajak Deng Garang | M25B38/031 |
| 2 | Bulima Eekiel | M25B38/028 |
| 3 | Aponi Allan Daniel | M25B38/029 |
| 4 | Ayoo Alice | S25B38/026 |
| 5 | Agenorwot Cynthia Jillian | S25B38/034 |
| 6 | Ayebazibwe Travis | S24B38/007 |