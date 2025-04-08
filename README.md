# Best Buy - Konsolenbasierte Einkaufsanwendung

## Projektziel
Eine Konsolenanwendung zur Verwaltung eines kleinen Stores mit Produkten, Bestellfunktionen und Benutzeroberfläche. Ziel war es, eine robuste und benutzerfreundliche Lösung zur Simulation von Einkaufsvorgängen zu entwickeln.

---

## Features

### Product-Klasse
- Attribute: Name, Preis, Menge
- Getter/Setter mit Validierung
- buy()-Methode reduziert Lagerbestand
- Automatische Deaktivierung bei Menge = 0
- Formatierte Ausgabe über show()
- Unterstützt drei Promotion-Typen:
  - Prozentualer Rabatt (z. B. 30 %)
  - Zweites Produkt zum halben Preis
  - "3 für 2"-Aktion
- Promotions werden korrekt bei Bestellungen berücksichtigt
- Promotions können pro Produkt gesetzt und gewechselt werden
  Spezielle Produkttypen:
  - NonStockedProduct: Kann auch bei einem Bestand von 0 bestellt werden, da sie nicht lagerbestandsgeführt werden
  - LimitedProduct: Kann nur in begrenzter Menge pro Bestellung bestellt werden (z.B. Shipping: maximal 1 pro Bestellung, obwohl 5 im Bestand)

### Store-Klasse
- Verwaltung einer Produktliste
- Methoden:
  - add_product()
  - remove_product()
  - get_total_quantity()
  - get_all_products()
  - order() zur Bestellverarbeitung
- Lagerprüfung und Gesamtsummenberechnung
- Berücksichtigung von Produkttypen bei der Bestellung (z.B. NonStockedProduct, LimitedProduct)
- Berücksichtigt Promotions bei der Preisberechnung pro Produkt

### main.py Benutzeroberfläche
#### Menüoptionen:
1. Alle Produkte anzeigen  
2. Gesamtmenge anzeigen  
3. Bestellung durchführen  
4. Programm beenden

- Produktauswahl per Index
- Mengeneingabe mit Prüfung
- Mehrfachauswahl pro Bestellung
- Bestellzusammenfassung am Ende
- "q" zum Abbrechen an jeder Stelle
- Rückkehr ins Hauptmenü nach jeder Aktion
- Formatierte Quittung für Bestellungen
- Zeigt vorhandene Promotions bei jedem Produkt
- Berechnet Rabatte dynamisch je nach Aktionstyp

---

## Fehlerbehandlung und Validierung
- Typ- und Bereichsprüfungen für alle Eingaben
- Schutz vor Bestellungen über Lagerbestand
- Behandlung leerer oder ungültiger Eingaben
- Abfangen von KeyboardInterrupt (CTRL+C)
- Kein Hängenbleiben bei leeren Lagerbeständen

---

## Erweiterungen über die Anforderungen hinaus
- Anzeige von Produkten mit Bestand = 0 (inaktiv)
- Korrekte Bestandsführung auch bei mehrfachen Bestellvorgängen
- Detaillierte Quittung mit Subtotals und Gesamtsumme
- Verbesserte Nutzerführung bei allen Eingaben

---

## Projektstruktur
```
Best_Buy/
├── main.py
├── products.py
├── promotions.py
├── store.py
├── test_product.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Ausführen des Programms
```
python main.py
```

---

## Beispielausgabe (gekürzt)
```
Bestellung erfolgreich! Zusammenfassung:
Produkt                        Stückpreis   Menge     Zwischensumme
MacBook Air M2 (Second one half price)      1450 €        2       2175 €
Bose Earbuds (3 für 2 Aktion)                250 €        3        500 €
Windows License (30% off!)                  200 €        1        140 €
--------------------------------------------------------------
Gesamt                                               2815 €
```

---

## Ideen für die zukünftige Entwicklung
- GUI-Erweiterung

---

## English Version

### Project Goal
A console-based shopping application to manage a small store with products, ordering functionality, and a user-friendly interface.

---

## Features

### Product Class
- Attributes: name, price, quantity
- Getters/setters with validation
- buy() method to reduce stock
- Automatic deactivation when quantity = 0
- Formatted output via show()
- Supports three promotion types:
  - Percentage discount (e.g. 30%)
  - Second item at half price
  - "3 for 2" deal
- Promotions are correctly applied when placing orders
- Promotions can be assigned per product and changed
 - NonStockedProduct: Can be ordered even with a quantity of 0, as they are not stock-tracked
  - LimitedProduct: Can only be ordered in limited quantities per order (e.g., Shipping: maximum 1 per order, although 5 in stock)

### Store Class
- Manages a list of products
- Methods:
  - add_product()
  - remove_product()
  - get_total_quantity()
  - get_all_products()
  - order() to process orders
- Stock check and total price calculation
- Applies product-specific promotions when calculating totals

### main.py Interface
#### Menu Options:
1. List all products  
2. Show total quantity  
3. Place an order  
4. Quit program

- Product selection by index
- Quantity input with validation
- Multiple items per order
- Summary at the end
- Use "q" to cancel anytime
- Returns to main menu after each action
- Formatted receipt after each order
- Displays promotions next to products
- Calculates discounts live based on promotion type

---

## Error Handling and Validation
- Type and range checks for all inputs
- Prevents orders exceeding stock
- Handles invalid or empty inputs
- KeyboardInterrupt (CTRL+C) is handled gracefully
- No infinite loops with out-of-stock products

---

## Enhancements Beyond the Requirements
- Visibility for out-of-stock products (marked inactive)
- Accurate stock management even with multiple selections
- Structured receipt with subtotals and total
- Improved user guidance at all stages

---

## Project Structure
```
Best_Buy/
├── main.py
├── products.py
├── promotions.py
├── store.py
├── test_product.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run
```
python main.py
```

---

## Sample Output (shortened)
```
Order successful! Summary:
Product                        Unit Price   Quantity     Subtotal
MacBook Air M2 (Second one half price)      1450 €        2       2175 €
Bose Earbuds (3 for 2 deal)                 250 €         3        500 €
Windows License (30% off!)                  200 €         1        140 €
--------------------------------------------------------------
Total                                               2815 €
```

---

## Ideas for Future Development
- GUI enhancement
