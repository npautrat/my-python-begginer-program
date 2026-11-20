#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import threading
import os
import re
import csv
import copy
import pdfplumber

# ==========================================
# 1. LISTES DE RÉFÉRENCE
# ==========================================
mots_soutenus_liste = [
  "abactinal", "abactor", "abderien", "abirritation", "ablastique",
  "abomasal", "aboulomanie", "abrachie", "abrenonciation", "abscissaire",
  "absolutivité", "absquatulation", "abulique", "acalephide", "acanthocephale",
  "acantholyse", "acapnie", "acaricide", "acathisie", "accablementiel",
  "accipitrin", "accrescence", "acerbité", "acervule", "acetabulum",
  "achilléen", "achlorhydrie", "achromatopsie", "acineticité", "aclinal",
  "acméisme", "acmonie", "acoelomate", "acolouthie", "aconitine",
  "acouphénique", "acratique", "acromégalie", "acroparesthésie", "acrostiche",
  "actantiel", "actinique", "actinotropisme", "acutance", "adamiques",
  "adaptativité", "additivité", "adelfité", "adénomégalie", "adénopathie",
  "adiaphorie", "adiastasie", "adjonctif", "adjuvantiel", "adnexiel",
  "adynamique", "aérolithe", "aéromancie", "aérophagie", "aérothermie",
  "aesthésiologie", "afférent", "affidavit", "affixation", "affouillement",
  "agalactie", "agénésie", "agglomérat", "aglycone", "agnosie",
  "agraphisme", "agroforesterie", "aguerrissement", "ailurophobie", "ajointement",
  "alacrimie", "alangui", "albedo", "alexie", "algolagnie",
  "algophobie", "alliciant", "allocentrisme", "allomorphie", "allopathique",
  "allostasie", "alluvialité", "almucantarat", "alogie", "altérabilité",
  "alvéolite", "amaurotiques", "amblyacousie", "ambrosiaque", "ameublementiel",
  "amphicèle", "amphidrome", "amphimixie", "amphisbène", "amyotrophie",
  "anabaptisme", "anacoluthique", "anagénèse", "anallagmatique", "anamorphose",
  "anankastique", "anastatique", "anatropisme", "anémométrie", "anergy",
  "angiogenèse", "angiospasme", "anhydrose", "aniconisme", "anisocorie",
  "ankylostomiase", "annalistique", "annexionnisme", "anomalistique",
  "anorexigène", "anorthite", "anoxémie", "anthéridie",
  "anthobiologie", "anthraciteux", "anthropométrique", "anthropopathie",
  "anthropotechnique", "antipéristaltique", "antipodisme",
  "antiscorbutique", "antonomastique", "aoristique",
  "apagogie", "apanagier", "aperceptif", "aphakie",
  "aphélie", "aphonique", "aplanétique", "apnéique",
  "apocatastatique", "apocrisiaire", "apolytique",
  "apomixie", "apophysaire", "aporétique",
  "aposiopétique", "apragmatisme", "apsychie",
  "aquilin", "arborescence", "archaisant",
  "archéose", "archimandritat", "architrave",
  "areligieux", "argyrisme", "arithmomancie",
  "armillaire", "arrhythmicité", "arsouille",
  "asémantique", "asomatognosie", "asphyxique",
  "assibilation", "astéréognosie", "astragalien",
  "astrobiologie", "astrolabe", "asynergie",
  "ataractique", "athymie", "atmidométrie",
  "atomistique", "atrophogène", "aubinisme",
  "audiométrique", "auteurisme", "autocatalepsie",
  "autogénétique", "autolyse", "autonymie",
  "autoscopique", "autotélisme",
  "axiomatique", "axoplasmique",
  "bactériolyse", "balbutial",
  "barycentrique", "bathymétrique",
  "belligénèse", "benthique",
  "bibliopathie", "bibliotaphe",
  "bifurcationnel", "biogénétique",
  "biomagnification", "bioturbation",
  "blastoderme", "blastogenèse",
  "brachygnathe", "brachymorphie",
  "bromhidrose", "bruxomanie",
  "buissonnementiel",
  "cacochymie", "cadastration",
  "calciphile", "callipyge",
  "calyptogame", "cantharide",
  "capillaroscopie", "capsulite",
  "catadioptre", "cataplexie",
  "catarrhal", "catéchétique",
  "catégorème", "catoptrique",
  "caudiforme", "céphalométrie",
  "cérébropathie", "chaînonner",
  "cheirognomonie", "chéliforme",
  "chiasmatique", "chirothésie",
  "chlorose", "cholinergique",
  "chrestomathique", "chromatolyse",
  "chronotropisme", "chthonien",
  "ciliopathie", "cinétose",
  "circonvolutionnel", "cladistique",
  "climactérique", "clinamen",
  "clivage", "coalescent",
  "coenesthésique", "cognitivité",
  "collapsologie", "colinéarité",
  "commensurabilité", "compartimentation",
  "complétude", "conatif",
  "conchoïdal", "concrétionnaire",
  "confluentiel", "conglobation",
  "conjoncturel", "connexité",
  "consécutivité", "consubstantialité",
  "contaminationnel", "contondant",
  "copulationnel", "corallien",
  "coriace", "corporéité",
  "corticotrope", "cosmothétique",
  "crénelage", "cristallogenèse",
  "cryptobiose", "cryptogamique",
  "cryptorchidie", "cténophore",
  "cumulatif", "cyanose",
  "cybernétique", "cyclogenèse",
  "cytolyse", "dactyloscopie",
  "déambiguïsation", "décentration",
  "décidual", "décoalescence",
  "défloration", "déictique",
  "délimitationnel", "déliquescent",
  "démimondain", "démographie",
  "démotique", "déontique",
  "déperfusion", "dépréciativité",
  "désagrégationnel", "désinence",
  "désobjectivation", "détergence",
  "diagraphie", "diathèse",
  "dichotomisation", "didascalie",
  "différentiabilité", "diglossie",
  "dilatance", "dimorphisme",
  "diplobionte", "disjonctif",
  "dispositivité", "dissimilitude",
  "dissociationnel", "dithyrambique",
  "diuréthique", "docimologie",
  "dogmatisme", "dolichocéphalie",
  "dorsiventral", "dravidien",
  "dromotropisme", "dualité",
  "dysgénésie", "dyslexie",
  "dyspraxie",
  "Majesté", "Vassaux", "Députés", "circulaire", "sceau", "Cour plénière",
  "magnificence", "Prince", "sujets", "puissance", "Monarque", "sévérité",
  "flatteur", "adulateur", "sotte flatterie", "Monseigneur", "Alléguant",
  "déguiser", "odorat", "sincère", "plaire", "Normand",
  "magnanimité", "déférence", "prérogative", "suzerain", "vassalité",
  "opprobre", "courroux", "clémence", "fastueux", "auguste",
  "péremptoire", "inflexible", "condescendance", "flagornerie",
  "servilité", "outrecuidance", "préséance", "éloquence",
  "impertinence", "circonspection", "dissimulation",
  "vindicatif", "commisération", "docilité",
  "prévenance", "indulgence", "autorité",
  "pompe", "ostentation", "apparat",
  "prééminence", "dignité", "honneur",
  "soumission", "obédience", "révérence"
]

mots_rares_liste = [
    "aboulie", "acatalepsie", "achéménide", "acinésie", "acroamatique",
    "adynaton", "aestival", "aethuse", "agogie", "albédo",
    "alcali", "alcyonien", "alef", "anaclase", "anacoluthe",
    "anadiplose", "anagnorisis", "anathème", "anfractuosité", "antépénultième",
    "antinomie", "aplomb", "apodictique", "aposiopèse", "apotropaïque",
    "arcanes", "arcane", "argutie", "armillaire", "ascèse",
    "atopie", "atrophie", "atonie", "aulcérique", "autochrone",
    "avulsé", "béotien", "boustrophédon", "cacochyme", "cacographie",
    "caliginosité", "capiteux", "carcan", "catachrèse", "catharsis",
    "cénobite", "chamarré", "chiral", "cicatrisation", "coercitif",
    "colubrine", "conchyliologue", "condignité", "contumélie", "coruscant",
    "crépusculaire", "déférent", "déictique", "démographe", "dénégation",
    "déréliction", "désinence", "désuet", "diaphane", "diatribe",
    "dichotomie", "différend", "dilatoire", "diluvien", "discernement",
    "disparate", "dispendieux", "dithyrambique", "dogmatique", "dolosif",
    "dysphorie", "ébrouement", "énigmatique", "épigone", "épirote",
    "épistolaire", "évocateur", "exégèse", "expédient", "faramineux",
    "fastidieux", "féerique", "féru", "flavescent", "florilège",
    "foliacé", "forclusion", "galimatias", "glauque", "gouailleur",
    "grommeler", "hâbleur", "hapax", "héraldique", "histrion",
    "holistique", "hubris", "iconoclaste", "idéogramme", "ignominieux",
    "illicite", "immanquable", "immuable", "impassible", "impétrant",
    "imprécation", "incunable", "inéluctable", "inénarrable", "inexorable",
    "infrangible", "ingénu", "inique", "insidieux", "insigne",
    "interlope", "interstice", "intransigeant", "introspection", "inviolé",
    "irrémissible", "itératif", "laconique", "lapidaire", "lénifiant",
    "léthargique", "lexicographe", "libation", "litanie", "logorrhée",
    "macabre", "marmoréen", "matutinal", "mendélien", "miasme",
    "miséricorde", "mnémonique", "mondegraphe", "monolithe", "nitescence",
    "nocivité", "nugatif", "obnubilé", "obséquieux", "occulte",
    "oligarchie", "ombrageux", "opiniâtre", "opprobre", "orbe",
    "orphelin", "orthogonal", "ostensible", "oxymore", "palliatif",
    "pandémonium", "panégyrique", "pérégrination", "pérennité", "pépiement",
    "phalanstère", "pharisaïque", "phénoménologie", "phlegmatique", "plénitude",
    "pléthore", "pochade", "polymathe", "posthume", "pragmatique",
    "prégnant", "prolixe", "prolusion", "prosaïque", "protasis",
    "puéril", "quintessence", "rémanence", "rhapsodie", "sagacité",
    "sérendipité", "sibyllin", "sommeiller", "solécisme", "somptuaire",
    "stène", "stupeur", "subodorer", "supplantation", "sybarite",
    "sylphide", "taciturne", "tanagras", "térébrant", "truculent",
    "ubiquité", "vaticinateur", "virtuose", "vitupérer", "volubile",
    "zélateur", "zénith"
]

pangramme_liste = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

csv.field_size_limit(10**9)


# ==========================================
# 2. CLASSE ANALYSEUR (SANS LE 16)
# ==========================================
class Analyseur:
    def __init__(self, nom, mots):
        self.nom = nom
        self.pdf = mots
        self.compteur = 0
        # Ensembles en minuscules pour une recherche rapide O(1)
        self._soutenus_set = {m.lower() for m in mots_soutenus_liste}
        self._rares_set = {m.lower() for m in mots_rares_liste}

    def nbr_mots(self):
        return len(self.pdf)

    def mots_soutenus(self):
        self.compteur = 0
        for mot in self.pdf:
            if mot.lower() in self._soutenus_set:
                self.compteur += 1
        return self.compteur

    def prop_mots_soutenus(self):
        if self.nbr_mots() == 0:
            return 0.0
        return round(self.mots_soutenus() / self.nbr_mots() * 100, 3)

    def mots_rares(self):
        self.compteur = 0
        for mot in self.pdf:
            if mot.lower() in self._rares_set:
                self.compteur += 1
        return self.compteur

    def prop_mots_rares(self):
        if self.nbr_mots() == 0:
            return 0.0
        return round(self.mots_rares() / self.nbr_mots() * 100, 3)

    def frequence_mots(self):
        frequence_mots_dico = {}
        for mot in self.pdf:
            if mot in frequence_mots_dico:
                frequence_mots_dico[mot] += 1
            else:
                frequence_mots_dico[mot] = 1
        return frequence_mots_dico

    def frequence_mots_top(self, top=20):
        a = self.frequence_mots()
        toppdf = sorted(a.items(), key=lambda x: x[1], reverse=True)[:top]
        return toppdf

    def longueur_mots(self, longueur=7):
        return sum(1 for mot in self.pdf if len(mot) == longueur)

    def longueur_mots_moy(self):
        if self.nbr_mots() == 0:
            return 0.0
        return round(sum(len(mot) for mot in self.pdf) / self.nbr_mots(), 2)

    def longs_mots(self):
        return sum(1 for mot in self.pdf if len(mot) >= 7)

    def courts_mots(self):
        return sum(1 for mot in self.pdf if len(mot) <= 4)

    def richesse_lexical(self):
        if self.nbr_mots() == 0:
            return 0.0
        a = len(self.frequence_mots()) / self.nbr_mots()
        return round(a * 100, 2)

    def pangrammes(self):
        copie_pangramme = copy.deepcopy(pangramme_liste)
        for mot in self.pdf:
            for lettre in mot:
                a = lettre.upper()
                if a in copie_pangramme:
                    copie_pangramme.remove(a)
            if not copie_pangramme:
                return True
        return len(copie_pangramme) == 0

    def palindromes(self, supp=4):
        palindrome_set = set()
        for mot in self.pdf:
            a = mot.lower()
            if a == a[::-1] and len(a) >= supp:
                palindrome_set.add(a)
        return sorted(palindrome_set, key=lambda x: (-len(x), x))

    def calculer_etoiles(self):
        """Calcule une note sur 5 étoiles selon la richesse et la complexité du texte."""
        if self.nbr_mots() == 0:
            return 0, []

        etoiles = 0
        details = []

        # Critère 1 : Diversité lexicale
        if self.richesse_lexical() >= 15.0 or len(self.frequence_mots()) >= 5000:
            etoiles += 1
            details.append("★ Diversité lexicale élevée")
        else:
            details.append("☆ Diversité lexicale modérée")

        # Critère 2 : Présence de mots soutenus
        if self.mots_soutenus() >= 10 or self.prop_mots_soutenus() >= 0.1:
            etoiles += 1
            details.append("★ Vocabulaire soutenu présent")
        else:
            details.append("☆ Peu de mots soutenus")

        # Critère 3 : Présence de mots rares
        if self.mots_rares() >= 5 or self.prop_mots_rares() >= 0.05:
            etoiles += 1
            details.append("★ Vocabulaire rare présent")
        else:
            details.append("☆ Peu de mots rares")

        # Critère 4 : Longueur moyenne des mots
        if self.longueur_mots_moy() >= 4.5:
            etoiles += 1
            details.append("★ Mots longs en moyenne (≥ 4.5 lettres)")
        else:
            details.append("☆ Mots courts en moyenne (< 4.5 lettres)")

        # Critère 5 : Pangramme complet
        if self.pangrammes() and self.nbr_mots() >= 50:
            etoiles += 1
            details.append("★ Alphabet complet utilisé (Pangramme)")
        else:
            details.append("☆ Alphabet incomplet")

        etoiles = max(1, min(5, etoiles))
        return etoiles, details


# ==========================================
# 3. APPLICATION TKINTER
# ==========================================
class ApplicationAnalysePDF:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyseur Lexical de PDF & CSV")
        self.root.geometry("1020x740")
        self.root.minsize(900, 650)
        self.root.configure(bg="#F3F4F6")

        self.analyseur = None
        self.mots = []
        self.nom_fichier = "Aucun fichier chargé"

        self._configurer_styles()
        self._construire_interface()

    def _configurer_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#F3F4F6")
        style.configure("Card.TFrame", background="#FFFFFF", relief="solid", borderwidth=1)
        style.configure("TLabel", background="#F3F4F6", foreground="#1F2937", font=("Segoe UI", 10))
        style.configure("Card.TLabel", background="#FFFFFF", foreground="#1F2937", font=("Segoe UI", 10))
        style.configure("Title.TLabel", background="#F3F4F6", foreground="#111827", font=("Segoe UI", 16, "bold"))
        style.configure("Stars.TLabel", background="#FFFFFF", foreground="#F59E0B", font=("Segoe UI", 24, "bold"))
        style.configure("Action.TButton", font=("Segoe UI", 10, "bold"), padding=6)
        style.configure("Menu.TButton", font=("Segoe UI", 9), padding=5, anchor="w")

    def _construire_interface(self):
        # --- En-tête : Import / Export ---
        header_frame = ttk.Frame(self.root, padding=(15, 12))
        header_frame.pack(fill="x")

        ttk.Label(header_frame, text="📚 Analyseur Lexical de Documents", style="Title.TLabel").pack(side="left")

        btn_frame = ttk.Frame(header_frame)
        btn_frame.pack(side="right")

        self.btn_import_pdf = ttk.Button(
            btn_frame, text="📂 Importer un PDF", style="Action.TButton", command=self.importer_pdf
        )
        self.btn_import_pdf.pack(side="left", padx=4)

        self.btn_import_csv = ttk.Button(
            btn_frame, text="📄 Importer un CSV", style="Action.TButton", command=self.importer_csv
        )
        self.btn_import_csv.pack(side="left", padx=4)

        self.btn_export_csv = ttk.Button(
            btn_frame, text="💾 Exporter en CSV", style="Action.TButton", command=self.exporter_csv, state="disabled"
        )
        self.btn_export_csv.pack(side="left", padx=4)

        # --- Barre de statut & Progression ---
        status_frame = ttk.Frame(self.root, padding=(15, 0, 15, 8))
        status_frame.pack(fill="x")

        self.lbl_fichier = ttk.Label(status_frame, text="Fichier actuel : Aucun", font=("Segoe UI", 10, "italic"))
        self.lbl_fichier.pack(side="left")

        self.progress = ttk.Progressbar(status_frame, mode="indeterminate", length=220)
        self.progress.pack(side="right")

        # --- Carte Étoiles & Résumé Global ---
        top_cards = ttk.Frame(self.root, padding=(15, 4))
        top_cards.pack(fill="x")

        # Carte Étoiles
        star_card = ttk.Frame(top_cards, style="Card.TFrame", padding=12)
        star_card.pack(side="left", fill="both", expand=True, padx=(0, 8))

        ttk.Label(star_card, text="Évaluation du document (Nombre d'étoiles)", style="Card.TLabel", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.lbl_etoiles = ttk.Label(star_card, text="☆☆☆☆☆  (0 / 5)", style="Stars.TLabel")
        self.lbl_etoiles.pack(anchor="w", pady=(2, 4))
        self.lbl_etoiles_details = ttk.Label(
            star_card, text="Importez un fichier PDF ou CSV pour calculer la note.", style="Card.TLabel", foreground="#4B5563"
        )
        self.lbl_etoiles_details.pack(anchor="w")

        # Carte Indicateurs Rapides
        summary_card = ttk.Frame(top_cards, style="Card.TFrame", padding=12)
        summary_card.pack(side="right", fill="both", expand=True, padx=(8, 0))

        ttk.Label(summary_card, text="Aperçu rapide", style="Card.TLabel", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.lbl_resume = ttk.Label(
            summary_card,
            text="Total mots : -\nMots distincts : -\nRichesse lexicale : -\nLongueur moyenne : -",
            style="Card.TLabel",
            justify="left"
        )
        self.lbl_resume.pack(anchor="w", pady=(4, 0))

        # --- Corps principal : Boutons d'analyse (1 à 15) à gauche + Résultats à droite ---
        main_frame = ttk.Frame(self.root, padding=(15, 10))
        main_frame.pack(fill="both", expand=True)

        # Panneau gauche : Commandes (1 à 15, sans 16)
        left_panel = ttk.Frame(main_frame, style="Card.TFrame", padding=10, width=320)
        left_panel.pack(side="left", fill="y", padx=(0, 10))
        left_panel.pack_propagate(False)

        ttk.Label(left_panel, text="Analyses disponibles (1 à 15)", style="Card.TLabel", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 6))

        # Paramètres configurables
        param_frame = ttk.Frame(left_panel, style="Card.TFrame", padding=6)
        param_frame.pack(fill="x", pady=(0, 8))

        row1 = ttk.Frame(param_frame)
        row1.pack(fill="x", pady=2)
        ttk.Label(row1, text="Top N fréquents :", style="Card.TLabel").pack(side="left")
        self.var_top = tk.IntVar(value=20)
        ttk.Spinbox(row1, from_=1, to=200, textvariable=self.var_top, width=6).pack(side="right")

        row2 = ttk.Frame(param_frame)
        row2.pack(fill="x", pady=2)
        ttk.Label(row2, text="Longueur exacte (n°9) :", style="Card.TLabel").pack(side="left")
        self.var_longueur = tk.IntVar(value=7)
        ttk.Spinbox(row2, from_=1, to=30, textvariable=self.var_longueur, width=6).pack(side="right")

        row3 = ttk.Frame(param_frame)
        row3.pack(fill="x", pady=2)
        ttk.Label(row3, text="Min. palindrome (n°15) :", style="Card.TLabel").pack(side="left")
        self.var_palindrome = tk.IntVar(value=4)
        ttk.Spinbox(row3, from_=2, to=20, textvariable=self.var_palindrome, width=6).pack(side="right")

        row4 = ttk.Frame(param_frame)
        row4.pack(fill="x", pady=2)
        ttk.Label(row4, text="Mot précis (n°6) :", style="Card.TLabel").pack(side="left")
        self.var_mot_recherche = tk.StringVar(value="")
        ttk.Entry(row4, textvariable=self.var_mot_recherche, width=12).pack(side="right")

        # Liste scrollable des boutons 1 à 15
        canvas_btn = tk.Canvas(left_panel, bg="#FFFFFF", highlightthickness=0)
        scrollbar_btn = ttk.Scrollbar(left_panel, orient="vertical", command=canvas_btn.yview)
        btn_list_frame = ttk.Frame(canvas_btn, style="Card.TFrame")

        btn_list_frame.bind(
            "<Configure>",
            lambda e: canvas_btn.configure(scrollregion=canvas_btn.bbox("all"))
        )
        canvas_btn.create_window((0, 0), window=btn_list_frame, anchor="nw", width=280)
        canvas_btn.configure(yscrollcommand=scrollbar_btn.set)

        canvas_btn.pack(side="left", fill="both", expand=True)
        scrollbar_btn.pack(side="right", fill="y")

        analyses = [
            (0, "📊 Tout afficher (Bilan complet 1-15)"),
            (1, "1. Nombre total de mots"),
            (2, "2. Nombre de mots soutenus"),
            (3, "3. Proportion de mots soutenus (%)"),
            (4, "4. Nombre de mots rares"),
            (5, "5. Proportion de mots rares (%)"),
            (6, "6. Fréquence d'un mot / aperçu"),
            (7, "7. Top N mots les plus fréquents"),
            (8, "8. Nombre de mots distincts"),
            (9, "9. Mots de longueur demandée"),
            (10, "10. Longueur moyenne des mots"),
            (11, "11. Nombre de mots longs (≥ 7)"),
            (12, "12. Nombre de mots courts (≤ 4)"),
            (13, "13. Richesse lexicale (%)"),
            (14, "14. Test Pangramme (A-Z)"),
            (15, "15. Liste des palindromes"),
        ]

        for code_id, libelle in analyses:
            ttk.Button(
                btn_list_frame,
                text=libelle,
                style="Menu.TButton",
                command=lambda c=code_id: self.executer_analyse(c)
            ).pack(fill="x", pady=2)

        # Panneau droit : Zone de résultats
        right_panel = ttk.Frame(main_frame, style="Card.TFrame", padding=10)
        right_panel.pack(side="right", fill="both", expand=True)

        res_header = ttk.Frame(right_panel, style="Card.TFrame")
        res_header.pack(fill="x", pady=(0, 6))

        ttk.Label(res_header, text="Résultats de l'analyse", style="Card.TLabel", font=("Segoe UI", 10, "bold")).pack(side="left")
        ttk.Button(res_header, text="Effacer", command=self.effacer_console).pack(side="right")

        self.txt_resultat = ScrolledText(
            right_panel, wrap="word", font=("Consolas", 10), bg="#FAFAFA", fg="#111827", relief="flat", padx=8, pady=8
        )
        self.txt_resultat.pack(fill="both", expand=True)
        self.ecrire_resultat("Bienvenue ! Cliquez sur « Importer un PDF » ou « Importer un CSV » pour commencer.\n")

    # ==========================================
    # GESTION DES FICHIERS (PDF & CSV)
    # ==========================================
    def importer_pdf(self):
        chemin = filedialog.askopenfilename(
            title="Sélectionner un fichier PDF",
            filetypes=[("Fichiers PDF", "*.pdf"), ("Tous les fichiers", "*.*")]
        )
        if not chemin:
            return

        self._definir_chargement(True, f"Extraction du PDF : {os.path.basename(chemin)}...")
        threading.Thread(target=self._tache_extraction_pdf, args=(chemin,), daemon=True).start()

    def _tache_extraction_pdf(self, chemin):
        try:
            pages_textes = []
            with pdfplumber.open(chemin) as pdf:
                total_pages = len(pdf.pages)
                for i, page in enumerate(pdf.pages):
                    if i % 10 == 0:
                        self.root.after(
                            0,
                            lambda p=i, t=total_pages: self.lbl_fichier.config(
                                text=f"Lecture de {os.path.basename(chemin)} : page {p + 1}/{t}..."
                            )
                        )
                    page_texte = page.extract_text()
                    if page_texte:
                        pages_textes.append(page_texte)

            texte = " ".join(pages_textes)
            texte = texte.replace("\n", " ")
            texte = re.sub(r"[^\wÀ-ÿ'-]", " ", texte)
            mots_extraits = [m for m in texte.split() if m not in ("-", "'")]

            self.root.after(0, lambda: self._finaliser_chargement(os.path.basename(chemin), mots_extraits))
        except Exception as exc:
            self.root.after(0, lambda: self._erreur_chargement(str(exc)))

    def importer_csv(self):
        chemin = filedialog.askopenfilename(
            title="Sélectionner un fichier CSV",
            filetypes=[("Fichiers CSV", "*.csv"), ("Tous les fichiers", "*.*")]
        )
        if not chemin:
            return

        try:
            with open(chemin, newline="", encoding="utf-8") as csvfile:
                lecteur = csv.reader(csvfile)
                liste_donnees = next(lecteur)

            texte = " ".join(liste_donnees)
            mots_extraits = re.findall(r"\['([^']+)'\]", texte)
            if not mots_extraits:
                # Repli si le CSV contient simplement des mots séparés
                mots_extraits = [m.strip() for m in liste_donnees if m.strip()]

            self._finaliser_chargement(os.path.basename(chemin), mots_extraits)
        except Exception as exc:
            messagebox.showerror("Erreur CSV", f"Impossible de lire le fichier CSV :\n{exc}")

    def exporter_csv(self):
        if not self.mots:
            return

        nom_defaut = os.path.splitext(self.nom_fichier)[0] + ".csv"
        chemin = filedialog.asksaveasfilename(
            title="Enregistrer les mots au format CSV",
            initialfile=nom_defaut,
            defaultextension=".csv",
            filetypes=[("Fichiers CSV", "*.csv")]
        )
        if not chemin:
            return

        try:
            mots_formates = [f"['{mot}']" for mot in self.mots]
            with open(chemin, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f, delimiter=" ")
                writer.writerow(mots_formates)
            messagebox.showinfo("Export réussi", f"Fichier CSV enregistré avec succès :\n{chemin}")
        except Exception as exc:
            messagebox.showerror("Erreur d'export", f"Erreur lors de l'enregistrement :\n{exc}")

    def _definir_chargement(self, actif, message=""):
        if actif:
            self.btn_import_pdf.config(state="disabled")
            self.btn_import_csv.config(state="disabled")
            self.progress.start(10)
            self.lbl_fichier.config(text=message)
        else:
            self.btn_import_pdf.config(state="normal")
            self.btn_import_csv.config(state="normal")
            self.progress.stop()

    def _erreur_chargement(self, erreur):
        self._definir_chargement(False)
        self.lbl_fichier.config(text="Erreur lors du chargement.")
        messagebox.showerror("Erreur", f"Une erreur est survenue :\n{erreur}")

    def _finaliser_chargement(self, nom, mots_extraits):
        self._definir_chargement(False)
        if not mots_extraits:
            messagebox.showwarning("Document vide", "Aucun mot n'a pu être extrait de ce fichier.")
            return

        self.nom_fichier = nom
        self.mots = mots_extraits
        self.analyseur = Analyseur(nom, self.mots)
        self.btn_export_csv.config(state="normal")
        self.lbl_fichier.config(text=f"Fichier chargé : {nom} ({len(self.mots):,} mots)".replace(",", " "))

        self._mettre_a_jour_tableau_de_bord()
        self.executer_analyse(0)

    def _mettre_a_jour_tableau_de_bord(self):
        # Mise à jour des étoiles
        nb_etoiles, details = self.analyseur.calculer_etoiles()
        etoiles_visuelles = "★" * nb_etoiles + "☆" * (5 - nb_etoiles)
        self.lbl_etoiles.config(text=f"{etoiles_visuelles}  ({nb_etoiles} / 5)")
        self.lbl_etoiles_details.config(text="  |  ".join(details[:3]) + "\n" + "  |  ".join(details[3:]))

        # Mise à jour de l'aperçu rapide
        total = self.analyseur.nbr_mots()
        distincts = len(self.analyseur.frequence_mots())
        richesse = self.analyseur.richesse_lexical()
        moyenne = self.analyseur.longueur_mots_moy()
        self.lbl_resume.config(
            text=(
                f"Total mots : {total:,}\n"
                f"Mots distincts : {distincts:,}\n"
                f"Richesse lexicale : {richesse} %\n"
                f"Longueur moyenne : {moyenne} caractères"
            ).replace(",", " ")
        )

    # ==========================================
    # EXÉCUTION DES ANALYSES (1 À 15)
    # ==========================================
    def ecrire_resultat(self, texte):
        self.txt_resultat.insert("end", texte + "\n")
        self.txt_resultat.see("end")

    def effacer_console(self):
        self.txt_resultat.delete("1.0", "end")

    def executer_analyse(self, c):
        if self.analyseur is None:
            messagebox.showinfo("Information", "Veuillez d'abord importer un fichier PDF ou CSV.")
            return

        self.ecrire_resultat("=" * 60)

        if c == 0:
            nb_etoiles, _ = self.analyseur.calculer_etoiles()
            etoiles_str = "★" * nb_etoiles + "☆" * (5 - nb_etoiles)
            self.ecrire_resultat(f"BILAN COMPLET : {self.nom_fichier}")
            self.ecrire_resultat(f"Note globale : {etoiles_str} ({nb_etoiles}/5 étoiles)\n")
            self.ecrire_resultat(f"1. Nombre total de mots          : {self.analyseur.nbr_mots()}")
            self.ecrire_resultat(f"2. Nombre de mots soutenus       : {self.analyseur.mots_soutenus()}")
            self.ecrire_resultat(f"3. Proportion de mots soutenus   : {self.analyseur.prop_mots_soutenus()} %")
            self.ecrire_resultat(f"4. Nombre de mots rares          : {self.analyseur.mots_rares()}")
            self.ecrire_resultat(f"5. Proportion de mots rares      : {self.analyseur.prop_mots_rares()} %")
            self.ecrire_resultat(f"8. Nombre de mots distincts      : {len(self.analyseur.frequence_mots())}")
            self.ecrire_resultat(f"10. Longueur moyenne des mots    : {self.analyseur.longueur_mots_moy()} caractères")
            self.ecrire_resultat(f"11. Nombre de mots longs (≥ 7)   : {self.analyseur.longs_mots()}")
            self.ecrire_resultat(f"12. Nombre de mots courts (≤ 4)  : {self.analyseur.courts_mots()}")
            self.ecrire_resultat(f"13. Richesse lexicale            : {self.analyseur.richesse_lexical()} %")
            self.ecrire_resultat(f"14. Pangramme complet (A-Z)      : {'Oui' if self.analyseur.pangrammes() else 'Non'}")

        elif c == 1:
            self.ecrire_resultat(f"[1] Nombre total de mots : {self.analyseur.nbr_mots()}")

        elif c == 2:
            self.ecrire_resultat(f"[2] Nombre de mots soutenus : {self.analyseur.mots_soutenus()}")

        elif c == 3:
            self.ecrire_resultat(f"[3] Proportion de mots soutenus : {self.analyseur.prop_mots_soutenus()} %")

        elif c == 4:
            self.ecrire_resultat(f"[4] Nombre de mots rares : {self.analyseur.mots_rares()}")

        elif c == 5:
            self.ecrire_resultat(f"[5] Proportion de mots rares : {self.analyseur.prop_mots_rares()} %")

        elif c == 6:
            dico = self.analyseur.frequence_mots()
            mot_cible = self.var_mot_recherche.get().strip()
            if mot_cible:
                occ = dico.get(mot_cible, 0)
                occ_min = sum(v for k, v in dico.items() if k.lower() == mot_cible.lower())
                self.ecrire_resultat(
                    f"[6] Fréquence de « {mot_cible} » : {occ} (exact) | {occ_min} (insensible à la casse)"
                )
            else:
                extrait = list(dico.items())[:30]
                self.ecrire_resultat("[6] Aperçu du dictionnaire des fréquences (30 premiers) :")
                for mot, freq in extrait:
                    self.ecrire_resultat(f"    - {mot} : {freq}")

        elif c == 7:
            top_n = self.var_top.get()
            top_liste = self.analyseur.frequence_mots_top(top_n)
            self.ecrire_resultat(f"[7] Top {top_n} des mots les plus fréquents :")
            for rang, (mot, freq) in enumerate(top_liste, start=1):
                self.ecrire_resultat(f"    {rang:>2}. {mot} ({freq} occurrences)")

        elif c == 8:
            self.ecrire_resultat(f"[8] Nombre de mots distincts : {len(self.analyseur.frequence_mots())}")

        elif c == 9:
            longueur = self.var_longueur.get()
            self.ecrire_resultat(
                f"[9] Nombre de mots de {longueur} caractères : {self.analyseur.longueur_mots(longueur)}"
            )

        elif c == 10:
            self.ecrire_resultat(f"[10] Longueur moyenne des mots : {self.analyseur.longueur_mots_moy()} caractères")

        elif c == 11:
            self.ecrire_resultat(f"[11] Nombre de mots longs (≥ 7 caractères) : {self.analyseur.longs_mots()}")

        elif c == 12:
            self.ecrire_resultat(f"[12] Nombre de mots courts (≤ 4 caractères) : {self.analyseur.courts_mots()}")

        elif c == 13:
            self.ecrire_resultat(f"[13] Richesse lexicale : {self.analyseur.richesse_lexical()} %")

        elif c == 14:
            est_pangramme = self.analyseur.pangrammes()
            self.ecrire_resultat(
                f"[14] Pangramme (toutes les lettres de A à Z présentes) : {'Oui ✅' if est_pangramme else 'Non ❌'}"
            )

        elif c == 15:
            min_len = self.var_palindrome.get()
            liste_pal = self.analyseur.palindromes(min_len)
            self.ecrire_resultat(f"[15] Palindromes uniques (≥ {min_len} lettres) — {len(liste_pal)} trouvé(s) :")
            if liste_pal:
                self.ecrire_resultat("    " + ", ".join(liste_pal))
            else:
                self.ecrire_resultat("    Aucun palindrome trouvé pour cette longueur.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationAnalysePDF(root)
    root.mainloop()