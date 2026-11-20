# 📚 Lexical Book Analyzer (PDF & CSV)

A graphical desktop application built with **Python (Tkinter)** to extract text from books or documents in **PDF** (or **CSV**) format, automatically rate their vocabulary richness on a **5-star scale**, and run **15 lexical and statistical analyses**.

> **Note:** The application's user interface is in **French**. In the sections below, all button labels and their corresponding explanations are kept in French to match the interface directly.

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

1. At the top right of the window, import a document using one of the two import buttons:
   * **📂 Importer un PDF** : *ouvre l'explorateur de fichiers pour sélectionner un document PDF et en extraire automatiquement tous les mots page par page.*
   * **📄 Importer un CSV** : *permet de charger directement un fichier CSV contenant une liste de mots déjà extraits lors d'une session précédente.*
2. Wait while the words are extracted (the progress bar indicates loading progress).
3. Once loaded, the **star rating** and **quick summary** appear at the top, and a complete report is printed in the results area on the right:
   * **Effacer** : *vide intégralement la console des résultats affichés à droite.*
4. Before running specific analyses, you can customize the input parameters on the left panel:
   * **Top N fréquents** : *permet de choisir le nombre de mots à afficher dans le classement des mots les plus utilisés (utilisé par le bouton 7).*
   * **Longueur exacte (n°9)** : *définit le nombre précis de lettres recherché pour le comptage du bouton 9.*
   * **Min. palindrome (n°15)** : *fixe la longueur minimale (en nombre de lettres) des palindromes à afficher avec le bouton 15.*
   * **Mot précis (n°6)** : *champ de saisie permettant d'entrer un mot précis dont on souhaite connaître le nombre d'apparitions via le bouton 6.*
5. Click any analysis button (**0** to **15**) in the left panel to display its output (see the French descriptions below).
6. To save the extracted word list for future use, click the export button at the top right:
   * **💾 Exporter en CSV** : *enregistre l'ensemble des mots extraits du livre dans un fichier CSV réutilisable.*

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

## 📊 Analysis Buttons Reference (French UI)

Below are the exact buttons available in the left panel along with their explanations in French:

| Bouton | Explication |
| :--- | :--- |
| **📊 Tout afficher (Bilan complet 1-15)** | *Affiche d'un seul coup la note en étoiles ainsi que le résumé complet de toutes les statistiques principales du document.* |
| **1. Nombre total de mots** | *Compte et affiche le nombre total de mots extraits dans l'ensemble du document.* |
| **2. Nombre de mots soutenus** | *Compte combien de fois des mots appartenant au registre soutenu apparaissent dans le texte.* |
| **3. Proportion de mots soutenus (%)** | *Calcule le pourcentage que représentent les mots soutenus par rapport au nombre total de mots.* |
| **4. Nombre de mots rares** | *Compte combien de fois des mots rares ou littéraires apparaissent dans le texte.* |
| **5. Proportion de mots rares (%)** | *Calcule le pourcentage que représentent les mots rares par rapport au nombre total de mots.* |
| **6. Fréquence d'un mot / aperçu** | *Affiche le nombre d'occurrences du mot saisi dans le champ « Mot précis » (ou un aperçu des 30 premiers mots du dictionnaire si le champ est vide).* |
| **7. Top N mots les plus fréquents** | *Classe et affiche les N mots les plus utilisés dans le livre (selon la valeur réglée dans « Top N fréquents »).* |
| **8. Nombre de mots distincts** | *Indique le nombre de mots différents (vocabulaire unique, sans les répétitions) utilisés dans l'œuvre.* |
| **9. Mots de longueur demandée** | *Compte le nombre de mots possédant exactement le nombre de lettres défini dans « Longueur exacte ».* |
| **10. Longueur moyenne des mots** | *Calcule le nombre moyen de caractères par mot sur l'ensemble du texte.* |
| **11. Nombre de mots longs (≥ 7)** | *Compte tous les mots composés de 7 caractères ou plus.* |
| **12. Nombre de mots courts (≤ 4)** | *Compte tous les mots composés de 4 caractères ou moins.* |
| **13. Richesse lexicale (%)** | *Calcule le taux de variété du vocabulaire selon la formule `(mots distincts / total des mots) × 100`.* |
| **14. Test Pangramme (A-Z)** | *Vérifie si toutes les lettres de l'alphabet de A à Z sont présentes au moins une fois dans le texte.* |
| **15. Liste des palindromes** | *Recherche et affiche tous les palindromes uniques (mots qui se lisent dans les deux sens) ayant au moins la taille définie dans « Min. palindrome ».* |

---

## 📁 Project Structure

```text
note livre/
├── note_livre.py   # Complete source code (PDF/CSV extraction, analyzer class, and Tkinter UI)
├── README.md       # Project documentation
└── .venv/          # Python virtual environment (created during setup)
```
