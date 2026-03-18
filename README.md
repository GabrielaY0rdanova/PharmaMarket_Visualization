# 📊 PharmaMarket_Visualization

## 🏷️ Project Badges

![Tableau](https://img.shields.io/badge/Tableau-Desktop-blue?logo=tableau&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-orange?logo=kaggle&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Overview

This project delivers an **interactive Tableau dashboard** built on top of the analytical outputs of the PharmaMarket EDA project.  
It visualises the structure, pricing patterns and market competition of the Bangladeshi pharmaceutical market across two dashboards connected via a Tableau Story.

The dashboard is built on top of the PostgreSQL database produced in [PharmaMarket_EDA](https://github.com/GabrielaY0rdanova/PharmaMarket_EDA), using a relationship-based master data source in Tableau Desktop.

## 📊 Dashboard Preview

### Market Structure Overview
![Dashboard Overview](docs/dashboard_overview.png)

### Pricing & Market Competition
![Dashboard Pricing](docs/dashboard_pricing.png)

🔗 **[View on Tableau Public](https://public.tableau.com/app/profile/gabriela.yordanova/viz/PharmaMarket_Visualization/PharmaMarketAnalysis)**

## 📊 Key Questions Answered

This dashboard is designed to answer the following analytical questions visually:

- Which therapeutic classes dominate the pharmaceutical market?
- Which manufacturers produce the most medicines?
- How are manufacturers distributed by portfolio size?
- What dosage forms are most commonly used?
- How are medicines distributed across price segments?
- How competitive are different generics based on brand count?
- How do unit prices vary across dosage forms?

## 🎯 What This Project Demonstrates

This project showcases an end-to-end data visualisation workflow including:

- Connecting **Tableau Desktop** to a **PostgreSQL** database using a relationship-based master data source
- Building a **multi-dashboard Tableau Story** with two interconnected analytical views
- Designing **KPI strips, bar charts, packed bubbles, treemaps, and box plots** in Tableau
- Applying **custom colour themes, container-based layouts and card styling** for a polished dashboard presentation
- Writing **LOD expressions and table calculations** for dynamic segmentation and percentage metrics
- Publishing a finished dashboard to **Tableau Public**

## 🔗 Related Projects

This project is the **fourth and final stage** of the PharmaMarket portfolio series:

👉 **[PharmaMarket_ETL](https://github.com/GabrielaY0rdanova/PharmaMarket_ETL)** — ETL pipeline from raw CSV files into a structured SQL Server database  
👉 **[PharmaMarket_Cleaning](https://github.com/GabrielaY0rdanova/PharmaMarket_Cleaning)** — Data cleaning and quality validation on the ETL output  
👉 **[PharmaMarket_EDA](https://github.com/GabrielaY0rdanova/PharmaMarket_EDA)** — Exploratory data analysis using modular SQL scripts in PostgreSQL

---

## 🗂️ Project Structure

```
PharmaMarket_Visualization/
│
├── docs/                              # Documentation and visuals
│   ├── Pharma_ERD.png                 # Entity Relationship Diagram
│   ├── dashboard_overview.png         # Dashboard 1 screenshot
│   └── dashboard_pricing.png          # Dashboard 2 screenshot
│
├── PharmaMarket_Visualization.twbx    # Packaged Tableau workbook (includes data extract)
├── calculated_fields.md               # All Tableau calculated fields with formulas and explanations
├── LICENSE.txt
└── README.md
```

---

## 🏗️ Data Source Architecture

The dashboard connects to the `PharmaMarketAnalytics_EDA` PostgreSQL database using a **relationship-based master data source** (`PharmaMarket_Master`) with `medicine` as the central table, related to:

| Related Table | Relationship |
|---|---|
| `generic` | medicine.generic_id → generic.generic_id |
| `drug_class` | generic.drug_class_id → drug_class.drug_class_id |
| `manufacturer` | medicine.manufacturer_id → manufacturer.manufacturer_id |
| `dosage_form` | medicine.dosage_form_id → dosage_form.dosage_form_id |
| `medicine_package_size` | medicine.brand_id → medicine_package_size.brand_id |
| `medicine_package_container` | medicine.brand_id → medicine_package_container.brand_id |

> ⚠️ **Why relationships instead of Custom SQL joins?**  
> Tableau's relationship model handles NULL foreign keys correctly via lazy joins, preventing KPI undercounting that occurred with Custom SQL joins. KPI fields are sourced from their respective dimension tables to ensure accurate counts.

---

## 📈 Dashboard Structure

### Dashboard 1 — Market Structure Overview

| Chart | Type | Description |
|---|---|---|
| KPI Strip | Text sheets | Medicines, Manufacturers, Generics, Drug Classes, Dosage Forms, Avg. Pack Price |
| Medicines by Drug Class | Horizontal bar | Top 10 drug classes by medicine count |
| Top 10 Manufacturers | Horizontal bar | Top 10 manufacturers by medicine count |
| Dosage Form Distribution | Packed bubbles | Distribution of medicines across dosage forms |
| Manufacturer Portfolio Size | Treemap | Manufacturers segmented by portfolio size (Small / Medium / Large) |

### Dashboard 2 — Pricing & Market Competition

| Chart | Type | Description |
|---|---|---|
| KPI Strip | Text sheets | Same KPIs as Dashboard 1 |
| Generic Market Competition | Vertical bar | Generics segmented by competition level |
| Price Segmentation | Vertical bar | Medicines segmented by pack price range |
| Unit Price Distribution | Box plot (log scale) | Unit price distribution across top 10 dosage forms |

---

## 🔄 Visualization Workflow

### Step 1 — Set up the PostgreSQL database

Ensure the `PharmaMarketAnalytics_EDA` database is running locally. Follow the setup instructions in [PharmaMarket_EDA](https://github.com/GabrielaY0rdanova/PharmaMarket_EDA).

### Step 2 — Connect Tableau to PostgreSQL

1. Open Tableau Desktop
2. Connect to **PostgreSQL**
3. Enter your server details and connect to `PharmaMarketAnalytics_EDA`
4. Set up the relationship-based master source with `medicine` as the central table

### Step 3 — Open the workbook

Open `PharmaMarket_Visualization.twbx` in Tableau Desktop.

### Step 4 — Explore the Story

Navigate between **Market Structure Overview** and **Pricing & Market Competition** using the story navigation tabs.

---

## 🔍 Key Insights

### Market Structure
- The dataset contains **21,708 medicines** produced by **240 manufacturers**, covering **1,711 generics** across **422 drug classes**
- **Tablet** is the dominant dosage form, representing the largest bubble in the dosage form distribution
- The majority of manufacturers have **small portfolios (1–10 medicines)**, indicating a highly fragmented producer landscape

### Pricing Patterns
- The vast majority of medicines (**78.89%**) fall into the **Medium price segment (100–500 BDT)**
- Only **4.79%** of medicines are classified as **Premium (> 1,000 BDT)**
- Unit prices vary significantly across dosage forms, as shown by the box plot distribution

### Generic Competition
- **34.07%** of generics operate in **Low Competition** markets (2–5 brands)
- **26.24%** are **Monopoly** generics with only one branded medicine
- Only **18.04%** of generics face **High Competition** (> 15 brands)

---

## ⚠️ Dataset Limitations

| Issue | Count | Decision |
|---|---|---|
| Medicines with no linked generic (NULL generic_id) | 214 | Documented — not fixable from source data |
| Medicines with no linked manufacturer (NULL manufacturer_id) | 147 | Documented — not fixable from source data |
| Unit-Priced container records with NULL unit price | 39 | Documented — accepted as-is |

---

## 🛠️ Technologies Used

- **Tableau Desktop** — dashboard design, data visualisation and story assembly
- **PostgreSQL** — database engine and live data source
- **SQL** — custom queries for Tableau data sources
- **Tableau Public** — dashboard publishing and sharing

---

## 📚 Data Source

The source data was obtained from the Kaggle dataset:

[Assorted Medicine Dataset of Bangladesh](https://www.kaggle.com/datasets/ahmedshahriarsakib/assorted-medicine-dataset-of-bangladesh)

This dataset is used for educational purposes and to demonstrate data visualisation workflows.

## 👩‍💻 About Me

Hi! I'm [Gabriela Yordanova](https://www.linkedin.com/in/gabriela-yordanova-837ba2124/).
Check out my full portfolio 🗂️ [here](https://gabrielay0rdanova.github.io/).

Having spent years working in pharmacy, I find this dataset genuinely interesting —
the patterns here reflect a real market I understand well. This project is the visual
payoff of the pipeline: clean data, meaningful analysis, and a dashboard that tells the story.

*This project is part of my portfolio showcasing data analytics and visualisation skills.*

## 🛡️ License

This project is licensed under the [MIT License](LICENSE.txt) and is available for educational and portfolio purposes.