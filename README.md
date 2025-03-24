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

### Store-Klasse
- Verwaltung einer Produktliste
- Methoden:
  - add_product()
  - remove_product()
  - get_total_quantity()
  - get_all_products()
  - order() zur Bestellverarbeitung
- Lagerprüfung und Gesamtsummenberechnung

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
├── store.py
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
Bitte wählen Sie eine Option:
1. Alle Produkte im Store anzeigen
2. Gesamtmenge im Store anzeigen
3. Bestellung durchführen
4. Beenden
...
Bestellung erfolgreich! Zusammenfassung:
Produkt                        Stückpreis   Menge     Zwischensumme
MacBook Air M2                    1450 €        1       1450 €
--------------------------------------------------------------
Gesamt                                              1450 €
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

### Store Class
- Manages a list of products
- Methods:
  - add_product()
  - remove_product()
  - get_total_quantity()
  - get_all_products()
  - order() to process orders
- Stock check and total price calculation

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
├── store.py
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
Please choose an option:
1. List of all products in the store
2. Show total amount in store
3. Make an order
4. Quit
...
Order successful! Summary:
Product                        Unit Price   Quantity     Subtotal
MacBook Air M2                    1450 €        1       1450 €
--------------------------------------------------------------
Total                                              1450 €
```

---

## Ideas for Future Development
- GUI enhancement
