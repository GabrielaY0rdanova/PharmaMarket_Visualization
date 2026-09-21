# Tableau Calculated Fields

This file documents the calculated fields used in `PharmaMarket_Visualization.twbx`.

## Generic Competition

### Brands Per Generic

```tableau
{ FIXED [Generic Id] : COUNTD([Brand Id]) }
```

Counts distinct medicines for each generic represented in the medicine table.

### Competition Level

```tableau
IF [Brands Per Generic] = 1 THEN "1. Monopoly"
ELSEIF [Brands Per Generic] >= 2 AND [Brands Per Generic] <= 5 THEN "2. Low Competition"
ELSEIF [Brands Per Generic] >= 6 AND [Brands Per Generic] <= 15 THEN "3. Moderate Competition"
ELSE "4. High Competition"
END
```

| Segment | Distinct brands |
|---|---:|
| Monopoly | 1 |
| Low Competition | 2 to 5 |
| Moderate Competition | 6 to 15 |
| High Competition | More than 15 |

### Competition %

```tableau
COUNTD([Generic Id]) / TOTAL(COUNTD([Generic Id])) * 100
```

Calculates each segment's share of the 1,635 generics represented by at least one medicine. It does not use all 1,711 rows from the generic dimension.

## Manufacturer Portfolio

### Medicines Per Manufacturer

```tableau
{ FIXED [Manufacturer Id] : COUNTD([Brand Id]) }
```

Counts distinct medicines for each represented manufacturer.

### Portfolio Size

```tableau
IF [Medicines Per Manufacturer] >= 1 AND [Medicines Per Manufacturer] <= 10 THEN "1. Small (1-10)"
ELSEIF [Medicines Per Manufacturer] >= 11 AND [Medicines Per Manufacturer] <= 50 THEN "2. Medium (11-50)"
ELSE "3. Large (> 50)"
END
```

| Segment | Distinct medicines |
|---|---:|
| Small | 1 to 10 |
| Medium | 11 to 50 |
| Large | More than 50 |

### Portfolio Size %

```tableau
COUNTD([Manufacturer Id]) / TOTAL(COUNTD([Manufacturer Id])) * 100
```

Calculates each segment's share of the 215 manufacturers represented by at least one medicine. It does not use all 240 rows from the manufacturer dimension.

## Package Price

### Price Segment

```tableau
IF [Pack Price] < 100 THEN "1. Low (< 100)"
ELSEIF [Pack Price] <= 500 THEN "2. Medium (100-500)"
ELSEIF [Pack Price] <= 1000 THEN "3. High (500-1000)"
ELSE "4. Premium (> 1000)"
END
```

| Segment | Pack price in BDT |
|---|---:|
| Low | Below 100 |
| Medium | 100 to 500 |
| High | Above 500 to 1,000 |
| Premium | Above 1,000 |

The supplied package-size table has no null pack prices. If future data introduces nulls, the formula should add an explicit `Unknown` branch before the price comparisons.

### Price Segment %

```tableau
COUNT([Pack Price]) * 100.0 / TOTAL(COUNT([Pack Price]))
```

Calculates each segment's share of 14,349 package-size records. The measure counts package options, not unique medicines.

## Calculation Notes

- Numeric prefixes preserve the intended segment order. Tableau aliases hide the prefixes in chart labels.
- `FIXED` expressions keep brand and medicine counts at the intended entity grain.
- Percentage measures use `TOTAL()` across the displayed segment table.
- All prices use Bangladeshi Taka (BDT).
