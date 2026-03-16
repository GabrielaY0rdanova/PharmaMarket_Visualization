# 🧮 Calculated Fields — PharmaMarket_Visualization

This file documents all calculated fields created in Tableau Desktop for the PharmaMarket Analysis dashboard.
Calculated fields are grouped by type: **LOD Expressions**, **Segmentation Fields**, and **Percentage Fields**.

---

## 🔒 LOD Expressions

LOD (Level of Detail) expressions compute aggregations at a fixed granularity, independent of the view's dimension level.

### Brands Per Generic

**Used in:** Generic Market Competition chart (via Competition Level)

```
{FIXED [Generic Id] : COUNTD([Brand Id])}
```

Counts the number of distinct branded medicines per generic, fixed at the generic level.
This ensures the brand count is not affected by other dimensions in the view.

---

### Medicines Per Manufacturer

**Used in:** Manufacturer Portfolio Size chart (via Portfolio Size)

```
{FIXED [Manufacturer Id] : COUNTD([Brand Id])}
```

Counts the number of distinct medicines produced by each manufacturer, fixed at the manufacturer level.
Used as the base measure for portfolio size segmentation.

---

## 🗂️ Segmentation Fields

Segmentation fields use IF/ELSEIF logic to assign each record to a meaningful category for analysis.

### Competition Level

**Used in:** Generic Market Competition chart

```
IF [Brands Per Generic] = 1 
    THEN "1. Monopoly"
ELSEIF [Brands Per Generic] >= 2 AND [Brands Per Generic] <= 5
    THEN "2. Low Competition"
ELSEIF [Brands Per Generic] >= 6 AND [Brands Per Generic] <= 15
    THEN "3. Moderate Competition"
ELSE 
    "4. High Competition"
END
```

Segments generics into four competition levels based on the number of branded medicines available.
The numeric prefix ensures correct sort order in the chart.

| Segment | Brand Count |
|---|---|
| Monopoly | 1 brand |
| Low Competition | 2–5 brands |
| Moderate Competition | 6–15 brands |
| High Competition | > 15 brands |

---

### Portfolio Size

**Used in:** Manufacturer Portfolio Size treemap

```
IF [Medicines Per Manufacturer] >= 1 AND [Medicines Per Manufacturer] <= 10
    THEN "1. Small (1-10)"
ELSEIF [Medicines Per Manufacturer] >= 11 AND [Medicines Per Manufacturer] <= 50
    THEN "2. Medium (11-50)"
ELSE
    "3. Large (> 50)"
END
```

Segments manufacturers into three portfolio size categories based on their total medicine count.
The numeric prefix ensures correct sort order in the treemap.

| Segment | Medicine Count |
|---|---|
| Small | 1–10 medicines |
| Medium | 11–50 medicines |
| Large | > 50 medicines |

---

### Price Segment

**Used in:** Price Segmentation chart

```
IF [Pack Price] < 100 THEN '1. Low (< 100)'
ELSEIF [Pack Price] <= 500 THEN '2. Medium (100-500)'
ELSEIF [Pack Price] <= 1000 THEN '3. High (500-1000)'
ELSE '4. Premium (> 1000)'
END
```

Segments medicines into four price tiers based on pack price in Bangladeshi Taka (BDT).
The numeric prefix ensures correct sort order in the chart.

| Segment | Pack Price (BDT) |
|---|---|
| Low | < 100 |
| Medium | 100–500 |
| High | 500–1,000 |
| Premium | > 1,000 |

---

## 📐 Percentage Fields

Percentage fields calculate each segment's share of the total using Tableau's `TOTAL()` table calculation.

### Competition %

**Used in:** Generic Market Competition chart labels

```
COUNTD([Generic Id]) / TOTAL(COUNTD([Generic Id])) * 100
```

Calculates each competition level's percentage share of total generics.
Displayed as a label above each bar in the Generic Market Competition chart.

---

### Portfolio Size %

**Used in:** Manufacturer Portfolio Size treemap labels

```
COUNTD([Manufacturer Id]) / TOTAL(COUNTD([Manufacturer Id])) * 100
```

Calculates each portfolio size segment's percentage share of total manufacturers.
Displayed as a label inside each rectangle in the treemap.

---

### Price Segment %

**Used in:** Price Segmentation chart labels

```
COUNT([Pack Price]) * 100.0 / TOTAL(COUNT([Pack Price]))
```

Calculates each price segment's percentage share of total medicine package records.
Displayed as a label above each bar in the Price Segmentation chart.

---

## 📝 Notes

- All segmentation fields use a numeric prefix (e.g. `1.`, `2.`, `3.`) to control sort order in Tableau charts without requiring a manual sort. Aliases were applied in the dashboard to display shorter labels (e.g. `Low` instead of `2. Low Competition`) for improved readability within chart labels and axis space.
- LOD expressions use `FIXED` to ensure counts are computed at the correct grain regardless of filters or view dimensions.
- Percentage fields use `TOTAL()` which is a table calculation — scope is set to the entire table in each chart.
- All prices are in **Bangladeshi Taka (BDT)**.