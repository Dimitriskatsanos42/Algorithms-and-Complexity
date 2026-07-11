# 🧮 Algorithms & Complexity

### Design, Analysis, and Implementation of Classic Algorithms in Python

![Python](https://img.shields.io/badge/Python-100%25-3776AB?logo=python&logoColor=white)
![Domain](https://img.shields.io/badge/Domain-Algorithms%20%26%20Complexity-blueviolet)
![Status](https://img.shields.io/badge/status-Academic%20Coursework-orange)

> Υλοποιήσεις κλασικών αλγοριθμικών προβλημάτων σε **Python**, στο πλαίσιο του μαθήματος **Αλγόριθμοι και Πολυπλοκότητα**. Κάθε project εστιάζει σε διαφορετική αλγοριθμική τεχνική — δυναμικός προγραμματισμός, αναζήτηση σε γράφους/πλέγμα, greedy strategies — με ανάλυση χρονικής και χωρικής πολυπλοκότητας.

---

## 📑 Table of Contents

| Section |
|---|
| [Overview](#-overview) |
| [Projects & Complexity Summary](#-projects--complexity-summary) |
| [Project Details](#-project-details) |
| [Algorithmic Techniques Covered](#-αλγοριθμικές-τεχνικές) |
| [Technologies](#️-technologies) |
| [Skills Developed](#-skills-developed) |
| [Execution](#️-execution) |
| [Repository Structure](#-repository-structure) |

---

## 🚀 Overview

| Field | Details |
|---|---|
| **Γλώσσα** | Python |
| **Μάθημα** | Αλγόριθμοι και Πολυπλοκότητα (Algorithms & Complexity) |
| **Εστίαση** | Ανάλυση πολυπλοκότητας (Big-O), σχεδιασμός αλγορίθμων, ορθότητα |
| **Παράδειγμα** | Dynamic Programming · Graph/Grid Traversal · Greedy Algorithms |
| **Στόχος** | Πρακτική εφαρμογή θεωρητικών αλγοριθμικών εννοιών σε πραγματικά προβλήματα |

---

## 📊 Projects & Complexity Summary

| # | Project | Πρόβλημα | Τεχνική | Time Complexity | Space Complexity |
|---|---|---|---|---|---|
| 1 | `MAXSUBARRAY` | Maximum Subarray Sum | Dynamic Programming (Kadane's Algorithm) | O(n) | O(1) |
| 2 | `Maze solver` | Εύρεση διαδρομής σε λαβύρινθο | Graph/Grid Traversal (BFS/DFS/Backtracking) | O(V + E) ≈ O(rows × cols) | O(rows × cols) |
| 3 | `Longest Common Subsequence` | LCS δύο ακολουθιών | Dynamic Programming | O(n × m) | O(n × m) |
| 4 | `Restaurant` | Διαχείριση Παραγγελιών Εστιατορίου (CRUD σε λίστες/πλειάδες) | Data Structures — Lists & Tuples Manipulation | O(n) ανά λειτουργία | O(n) |

> 📌 Οι πολυπλοκότητες του πίνακα αντιστοιχούν στη *standard* υλοποίηση κάθε αλγορίθμου. Αν κάποια από τις δικές σου υλοποιήσεις διαφέρει (π.χ. χρήση memoization vs. tabulation, ή διαφορετικό traversal strategy στο Maze solver), πες μου να διορθώσω τις τιμές.

---

## 📘 Project Details

### 1️⃣ MAXSUBARRAY — Maximum Subarray Problem

| Πεδίο | Λεπτομέρεια |
|---|---|
| **Πρόβλημα** | Εύρεση της συνεχόμενης υπακολουθίας ενός πίνακα με το μέγιστο άθροισμα |
| **Αλγόριθμος** | Kadane's Algorithm (Dynamic Programming, single-pass) |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) |
| **Είσοδος** | Πίνακας ακεραίων (θετικών/αρνητικών) |
| **Έξοδος** | Μέγιστο άθροισμα υπακολουθίας (και προαιρετικά τα όριά της) |

### 2️⃣ Maze Solver

| Πεδίο | Λεπτομέρεια |
|---|---|
| **Πρόβλημα** | Εύρεση διαδρομής από αρχικό σε τελικό κελί μέσα σε πλέγμα (maze) με εμπόδια |
| **Αλγόριθμος** | Αναζήτηση σε γράφημα/πλέγμα (BFS για συντομότερη διαδρομή ή DFS/backtracking) |
| **Time Complexity** | O(rows × cols) |
| **Space Complexity** | O(rows × cols) (visited grid + recursion/queue) |
| **Είσοδος** | 2D πλέγμα με ελεύθερα κελιά/εμπόδια, αρχική & τελική θέση |
| **Έξοδος** | Διαδρομή (ή "no solution" αν δεν υπάρχει) |

### 3️⃣ Longest Common Subsequence (LCS)

| Πεδίο | Λεπτομέρεια |
|---|---|
| **Πρόβλημα** | Εύρεση της μεγαλύτερης κοινής υπακολουθίας δύο ακολουθιών (strings) |
| **Αλγόριθμος** | Dynamic Programming με πίνακα `dp[i][j]` |
| **Time Complexity** | O(n × m) |
| **Space Complexity** | O(n × m) (ή O(min(n,m)) με βελτιστοποίηση χώρου) |
| **Είσοδος** | Δύο ακολουθίες/strings |
| **Έξοδος** | Μήκος LCS (και προαιρετικά η ίδια η υπακολουθία) |

### 4️⃣ Restaurant — Σύστημα Παραγγελιών Φοιτητικού Εστιατορίου

| Πεδίο | Λεπτομέρεια |
|---|---|
| **Πρόβλημα** | Πρόγραμμα διαχείρισης παραγγελιών φαγητού σε φοιτητικό εστιατόριο εντός campus, για χρήση από σερβιτόρο |
| **Δομές Δεδομένων** | `menu`: λίστα από πλειάδες (όνομα, περιγραφή, τιμή) · `order`: λίστα από πλειάδες (θέση προϊόντος στο menu, ποσότητα) |
| **Λειτουργίες Μενού** | 1. Έναρξη Παραγγελίας · 2. Εμφάνιση Παραγγελίας · 3. Αφαίρεση Προϊόντος · 4. Πληρωμή |
| **Πληρωμή** | Υποστήριξη πληρωμής με κάρτα ή μετρητά, με έλεγχο και υπολογισμό ρέστων στην περίπτωση μετρητών |
| **Time Complexity** | O(n) ανά λειτουργία (n = πλήθος γραμμών παραγγελίας) — αναζήτηση/αφαίρεση/υπολογισμός συνόλου με γραμμική διάσχιση της λίστας |
| **Space Complexity** | O(n) — αποθήκευση παραγγελίας ως λίστα πλειάδων |
| **Τεχνική** | Διαχείριση δομών δεδομένων (lists & tuples), CLI menu-driven interaction loop |

**Παράδειγμα ροής εκτέλεσης** (από την εκφώνηση):

```
Επιλογές:
==========
1. Έναρξη Παραγγελίας
2. Εμφάνιση Παραγγελίας
3. Αφαίρεση προϊόντος από την παραγγελία
4. Πληρωμή

Εισάγετε την επιλογή: 1
Επιλογή #0: Chicken Burger
...
Εισάγετε τον αριθμό προϊόντος από το μενού: 0
Εισάγετε ποσότητα: 2
Επιθυμείτε να εισάγετε άλλο (ν/ο): ν

Εισάγετε την επιλογή: 2
α/α  ΟΝΟΜΑ              ΤΜΧ   ΤΙΜΗ ΤΜΧ   ΑΞΙΑ
1.   Chicken Burger      2     4.2€        8.4€
2.   Σαλάτα ceasar's     1     6.9€        6.9€

Εισάγετε την επιλογή: 4
Παρακαλώ επιβεβαιώστε την αγορά (ν/ο): ν
Παρακαλούμε πληρώστε 8.40€
Σας ευχαριστούμε για την αγορά σας!
```

---

## 🧠 Αλγοριθμικές Τεχνικές

| Κατηγορία | Εφαρμογή σε αυτό το repo |
|---|---|
| **Dynamic Programming** | Maximum Subarray (Kadane), Longest Common Subsequence |
| **Grid/Graph Traversal** | Maze Solver |
| **Πολυπλοκότητα & Ανάλυση** | Big-O ανάλυση για κάθε υλοποίηση |
| **Βελτιστοποίηση** | Σύγκριση naive vs. βελτιστοποιημένων λύσεων (π.χ. brute-force O(n²) → Kadane O(n)) |
| **Δομές Δεδομένων & CRUD Λογική** | Restaurant — διαχείριση παραγγελιών με λίστες/πλειάδες, menu-driven interaction |

---

## 🛠️ Technologies

| Κατηγορία | Στοιχεία |
|---|---|
| Γλώσσα | Python 3.x |
| Δομές Δεδομένων | Arrays, 2D Grids/Matrices, Strings |
| Παράδειγμα | Dynamic Programming, Recursion, Iterative Traversal |

---

## 🎯 Skills Developed

| # | Δεξιότητα |
|---|---|
| 1 | Σχεδιασμός και ανάλυση αλγορίθμων (Big-O) |
| 2 | Dynamic Programming (memoization & tabulation) |
| 3 | Αναζήτηση σε γραφήματα/πλέγματα (BFS/DFS) |
| 4 | Βελτιστοποίηση χρονικής/χωρικής πολυπλοκότητας |
| 5 | Ανάλυση ορθότητας αλγορίθμων |
| 6 | Προγραμματισμός σε Python |

---

## ▶️ Execution

```bash
git clone https://github.com/Dimitriskatsanos42/Algorithms-and-Complexity.git
cd Algorithms-and-Complexity
```

| Project | Εντολή Εκτέλεσης |
|---|---|
| MAXSUBARRAY | `cd MAXSUBARRAY && python main.py` |
| Maze solver | `cd "Maze solver" && python main.py` |
| Longest Common Subsequence | `cd "Longest Common Subsequence" && python main.py` |
| Restaurant | `cd Restaurant && python main.py` |

> 📌 Προσάρμοσε το όνομα του entry-point αρχείου (`main.py`) ανάλογα με το πραγματικό όνομα αρχείου σε κάθε φάκελο.

---

## 📂 Repository Structure

```
Algorithms-and-Complexity/
├── MAXSUBARRAY/                     # Maximum Subarray (Kadane's Algorithm)
├── Maze solver/                     # Grid/Graph traversal — pathfinding
├── Longest Common Subsequence/      # LCS — Dynamic Programming
├── Restaurant/                      # Σύστημα παραγγελιών φοιτητικού εστιατορίου (lists & tuples)
└── README.md
```

---

## 👤 Author

**Δημήτρης Κατσάνος** — [@Dimitriskatsanos42](https://github.com/Dimitriskatsanos42)
University coursework — Algorithms & Complexity.
