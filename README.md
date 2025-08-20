# 📖 Phonebook — Sorted List + Binary Search (Python)

A small Python module to manage a **phonebook** with fast search and ordered insert using **binary search** on a unique key *(name + address)*. Supports adding, deleting, searching, and loading/saving from files. :contentReference[oaicite:0]{index=0}

---

## ✨ Features
- **Add user** in sorted order (no full re-sort) via `searchInsert` position. :contentReference[oaicite:1]{index=1}  
- **Delete user** found by `searchUser` (binary search). :contentReference[oaicite:2]{index=2}  
- **Search by (name + address)** — concatenated key is unique. :contentReference[oaicite:3]{index=3}  
- **Load** from `input.txt` and **save** to `output.txt` (CSV-like lines). :contentReference[oaicite:4]{index=4}  
- Simple **menu UI** in `main.py` for demo/testing. :contentReference[oaicite:5]{index=5}

---

## 🧱 Data Model
- Phonebook stored as a **list of lists** (matrix) with `n × 3`:
  - column 0: **name**, column 1: **address**, column 2: **phone**.  
  - Kept **alphabetically sorted** by `name + address`. :contentReference[oaicite:6]{index=6}

---

## 📂 Project Structure

├─ functions.py # core operations (load/save/search/add/delete/print)

├─ main.py # menu-driven runner with test cases

├─ input.txt # sample input (seed data)

└─ output.txt # saved phonebook snapshot

---

## ⚙️ Core Algorithms

### Binary Search (searchUser)
Searches for a user by **concatenated `name+address`**; returns **index** or **-1** if not found. :contentReference[oaicite:8]{index=8}

### Ordered Insert (searchInsert + addUser)
Finds the **insertion position** (using a binary-search variant) to keep the list ordered, then calls Python’s `.insert(position, entry)`. :contentReference[oaicite:9]{index=9}

### Delete (deleteUser)
Calls `searchUser`; if found, removes the entry and returns success; otherwise returns `-1`. :contentReference[oaicite:10]{index=10}

---

## 📥 File I/O Format
Each line has **three fields** separated by `", "` (comma + space):  Name, Address, PhoneNumber

- `input.txt` is used to **load** initial data.  
- `output.txt` is written on **save**. :contentReference[oaicite:11]{index=11}


