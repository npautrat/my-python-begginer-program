# 📚 Lexical Book Analyzer (PDF & CSV)

A graphical desktop application built with **Python (Tkinter)** to extract text from books or documents in **PDF** (or **CSV**) format, automatically rate their vocabulary richness on a **5-star scale**, and run **15 lexical and statistical analyses**.

> **Note:** The application's user interface is in **French**. In the reference section below, all button labels are kept in French to match the interface, accompanied by their English explanations.

---

## ✨ Features

* **Multi-format import**:
  * **PDF files**: extracts text page by page in a background thread (with a progress bar so the UI stays responsive on long novels).
  * **CSV files**: directly loads a previously extracted word list.
* **CSV export**: saves extracted and cleaned words for fast reuse.
* **5-star rating system (1 to 5 ★)**: overall lexical evaluation computed from 5 vocabulary complexity criteria.
* **15 built-in analysis tools**: word frequencies, formal and rare vocabulary counts, lexical richness, word lengths, pangram detection, and palindrome search.

---

## 🛠️ Prerequisites

* **Python 3.8 or higher**
* **Tkinter** (included by default on Windows and macOS; must be installed via your package manager on Linux)
* **pdfplumber** (PDF text extraction library)

---

## 🚀 Installation & Launch

### 1. Clone or download the project

Navigate to the folder containing `note_livre.py`:

```bash
cd "path/to/note livre"
```

### 2. Check Tkinter (Linux users only)

On Windows and macOS, Tkinter comes pre-installed with Python. On Linux, install it if needed:

* **Arch Linux / Manjaro**:
  ```bash
  sudo pacman -S tk
  ```
* **Ubuntu / Debian / Mint**:
  ```bash
  sudo apt install python3-tk
  ```
* **Fedora**:
  ```bash
  sudo dnf install python3-tkinter
  ```

### 3. Create a virtual environment and install dependencies

Using a local virtual environment (`.venv`) avoids conflicts with system-managed Python packages:

* **Linux / macOS**:
  ```bash
  python3 -m venv .venv
  .venv/bin/python -m pip install pdfplumber
  ```

* **Windows (PowerShell or Command Prompt)**:
  ```powershell
  python -m venv .venv
  .venv\Scripts\python -m pip install pdfplumber
  ```

### 4. Run the application

* **Linux / macOS**:
  ```bash
  .venv/bin/python note_livre.py
  ```

* **Windows**:
  ```powershell
  .venv\Scripts\python note_livre.py
  ```

---

## 📖 Usage Guide

1. At the top right of the window, click **📂 Importer un PDF** to select a PDF book, or **📄 Importer un CSV** to load a previously extracted word list.
2. Wait while the words are extracted (the progress bar indicates loading progress).
3. Once loaded, the **star rating** and **quick summary** appear at the top, and a complete report is printed in the results console on the right (click **Effacer** at any time to clear the output console).
4. Before running specific analyses, you can adjust the input parameters in the left panel:
   * **Top N fréquents**: sets how many top words are displayed in the frequency ranking (button **7**).
   * **Longueur exacte (n°9)**: sets the exact character count to search for (button **9**).
   * **Min. palindrome (n°15)**: sets the minimum character length for detected palindromes (button **15**).
   * **Mot précis (n°6)**: text field to look up the exact occurrence count of a specific word (button **6**).
5. Click any analysis button (**0** to **15**) in the left panel to display its result on the right.
6. Click **💾 Exporter en CSV** at the top right to save the extracted word list for future reuse.

---

## ⭐ Star Rating Calculation

The global score (**1 to 5 stars**) awards 1 point for each of the following criteria:

| Criterion | Requirement for 1 ★ |
| :--- | :--- |
| **Lexical diversity** | Lexical richness ≥ 15% or ≥ 5,000 unique words |
| **Formal vocabulary** | ≥ 10 formal words found or proportion ≥ 0.1% |
| **Rare vocabulary** | ≥ 5 rare words found or proportion ≥ 0.05% |
| **Word length** | Average word length ≥ 4.5 characters |
| **Pangram** | All 26 letters of the alphabet (`A` to `Z`) used in a text of at least 50 words |

---

## 📊 Buttons Reference

Below are all the buttons available in the interface (in French) along with their explanations in English:

### Action & Utility Buttons

| Button (French UI) | Explanation |
| :--- | :--- |
| **📂 Importer un PDF** | Opens the file explorer to select a PDF document and automatically extract all its words page by page. |
| **📄 Importer un CSV** | Loads a CSV file containing a list of words already extracted during a previous session. |
| **💾 Exporter en CSV** | Saves all words extracted from the book into a reusable CSV file. |
| **Effacer** | Clears the entire results display area on the right. |

### Analysis Buttons (Left Panel)

| Button (French UI) | Explanation |
| :--- | :--- |
| **📊 Tout afficher (Bilan complet 1-15)** | Displays the star rating along with a complete summary of all the document's main statistics at once. |
| **1. Nombre total de mots** | Counts and displays the total number of words extracted from the entire document. |
| **2. Nombre de mots soutenus** | Counts how many times words belonging to the formal register appear in the text. |
| **3. Proportion de mots soutenus (%)** | Calculates the percentage of formal words relative to the total word count. |
| **4. Nombre de mots rares** | Counts how many times rare or literary words appear in the text. |
| **5. Proportion de mots rares (%)** | Calculates the percentage of rare words relative to the total word count. |
| **6. Fréquence d'un mot / aperçu** | Displays the occurrence count of the word entered in the "Mot précis" field (or a preview of the first 30 dictionary entries if the field is empty). |
| **7. Top N mots les plus fréquents** | Ranks and displays the top *N* most frequently used words in the book (based on the value set in "Top N fréquents"). |
| **8. Nombre de mots distincts** | Shows the number of different words (unique vocabulary, excluding duplicates) used in the work. |
| **9. Mots de longueur demandée** | Counts the number of words that have the exact character length specified in "Longueur exacte". |
| **10. Longueur moyenne des mots** | Calculates the average number of characters per word across the entire text. |
| **11. Nombre de mots longs (≥ 7)** | Counts all words made up of 7 or more characters. |
| **12. Nombre de mots courts (≤ 4)** | Counts all words made up of 4 or fewer characters. |
| **13. Richesse lexicale (%)** | Calculates the vocabulary variety rate using the formula `(unique words / total words) × 100`. |
| **14. Test Pangramme (A-Z)** | Checks whether every letter of the alphabet from A to Z appears at least once in the text. |
| **15. Liste des palindromes** | Finds and displays all unique palindromes (words that read the same backward and forward) that are at least as long as the value set in "Min. palindrome". |

---

## 📁 Project Structure

```text
note livre/
├── note_livre.py   # Complete source code (PDF/CSV extraction, analyzer class, and Tkinter UI)
├── README.md       # Project documentation
└── .venv/          # Python virtual environment (created during setup)
```
