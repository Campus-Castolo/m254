## Login-Funktion

### Ziel
Mein Ziel war es, aus bereitgestellten Registrationsinformationen eine funktionierende Login-Funktion zu erstellen. Ich arbeite bei diesem Projekt das erste Mal mit Python, was für mich eine große Herausforderung, aber auch eine Chance darstellt, um Python zu lernen. Es war auch ein sehr professionell organisiertes Projekt, und daher war ein weiteres Ziel, so viele Learnings wie möglich daraus zu ziehen.

### Python Learning
Da ich mit Python, wie gesagt, noch nicht vertraut war, wollte ich zuerst ein wenig in das Thema reinkommen. Dafür habe ich meine ersten kleinen Python-Codes geschrieben und ausprobiert. Dies war mein erstes Script, welches prüft, ob eine Zahl gerade oder ungerade ist:

```python
def ist_gerade(n):
    return n % 2 == 0

zahl = int(input("Bitte geben Sie eine Zahl ein: "))
if ist_gerade(zahl):
    print(f"{zahl} ist gerade.")
else:
    print(f"{zahl} ist ungerade.")
```

Solche kleinen Codes habe ich ein paar geschrieben, einfach um mich im Thema Python wohler zu fühlen. Danach fühlte ich mich bereit, an die Login-Funktion zu treten.

### Login-Funktion
Bei der Login-Funktion gab es mehrere Schwierigkeiten. Einerseits war es schwer, sich im Code zurechtzufinden, vor allem mit meinen wenigen Python-Kenntnissen. Zum anderen war mein Wissen trotzdem noch relativ gering und ich musste mir vieles zusammengoogeln.

Hier ist die Schritt-für-Schritt-Erklärung des Login-Codes:

```python
@auth.route('/login', methods=['POST'])
def login():
```
- **@auth.route('/login', methods=['POST'])**: Das ist ein Dekorator in Flask, der eine neue Route (URL) definiert. Diese Route `/login` akzeptiert nur POST-Anfragen. POST-Anfragen werden normalerweise für das Senden von Daten, wie Benutzeranmeldedaten, verwendet.
- **def login():**: Hier definieren wir eine Funktion namens `login`, die ausgeführt wird, wenn jemand die `/login`-Route aufruft.

```python
    username_or_email = request.form.get('username_or_email')
    password = request.form.get('password')
```
- **username_or_email = request.form.get('username_or_email')**: Diese Zeile holt sich die Eingabe des Benutzers aus dem Formularfeld `username_or_email`. Das Formularfeld wird in einer POST-Anfrage gesendet.
- **password = request.form.get('password')**: Diese Zeile holt sich die Eingabe des Benutzers aus dem Formularfeld `password`.

```python
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
```
- **hashed_password = hashlib.sha256(password.encode()).hexdigest()**: Diese Zeile hasht das eingegebene Passwort mit dem SHA-256-Algorithmus. Hashing ist eine Technik, um Passwörter sicher zu speichern. Anstatt das Passwort im Klartext zu speichern, speichern wir den Hashwert, der schwer zu erraten ist.

```python
    connection = create_connection()
```
- **connection = create_connection()**: Diese Zeile ruft die Funktion `create_connection()` auf, die eine Verbindung zur Datenbank herstellt. Wenn die Verbindung erfolgreich ist, wird sie in der Variable `connection` gespeichert.

```python
    if connection:
```
- **if connection:**: Diese Zeile überprüft, ob die Verbindung zur Datenbank erfolgreich war. Wenn `connection` nicht `None` ist, fahren wir fort.

```python
        cursor = connection.cursor(dictionary=True)
```
- **cursor = connection.cursor(dictionary=True)**: Diese Zeile erstellt einen Cursor, der zum Ausführen von SQL-Befehlen in der Datenbank verwendet wird. Der Parameter `dictionary=True` bedeutet, dass die Ergebnisse als Wörterbuch (Dictionary) zurückgegeben werden, was den Zugriff auf die Daten erleichtert.

```python
        try:
            cursor.execute("SELECT * FROM users WHERE (username = %s OR email = %s) AND password = %s",
                           (username_or_email, username_or_email, hashed_password))
            user = cursor.fetchone()
```
- **try:**: Diese Zeile beginnt einen `try`-Block, der Fehlerbehandlung ermöglicht. Wenn ein Fehler auftritt, können wir ihn im `except`-Block behandeln.
- **cursor.execute("SELECT * FROM users WHERE (username = %s OR email = %s) AND password = %s", (username_or_email, username_or_email, hashed_password))**: Diese Zeile führt eine SQL-Abfrage aus, um zu überprüfen, ob ein Benutzer mit dem eingegebenen Benutzernamen (oder E-Mail) und Passwort in der Datenbank existiert.
- **user = cursor.fetchone()**: Diese Zeile holt das erste Ergebnis der Abfrage. Wenn kein Benutzer gefunden wird, ist `user` `None`.

```python
            if user:
                return jsonify({'message': 'Login successful!', 'status': 'text-success'}), 200
            else:
                return jsonify({'message': 'Invalid username/email or password!', 'status': 'text-danger'}), 401
```
- **if user:**: Diese Zeile überprüft, ob `user` nicht `None` ist, was bedeutet, dass ein Benutzer gefunden wurde.
- **return jsonify({'message': 'Login successful!', 'status': 'text-success'}), 200**: Wenn ein Benutzer gefunden wurde, senden wir eine Erfolgsmeldung zurück und setzen den HTTP-Statuscode auf 200 (OK).
- **else:**: Wenn kein Benutzer gefunden wurde, fahren wir mit dem `else`-Block fort.
- **return jsonify({'message': 'Invalid username/email or password!', 'status': 'text-danger'}), 401**: Wenn kein Benutzer gefunden wurde, senden wir eine Fehlermeldung zurück und setzen den HTTP-Statuscode auf 401 (Unauthorized).

```python
        except Error as e:
            return jsonify({'message': f"Error: {str(e)}", 'status': 'text-danger'}), 500
        finally:
            cursor.close()
            connection.close()
```
- **except Error as e:**: Wenn ein Fehler auftritt, fangen wir ihn hier ab. `e` enthält die Fehlerdetails.
- **return jsonify({'message': f"Error: {str(e)}", 'status': 'text-danger'}), 500**: Wir senden eine Fehlermeldung zurück und setzen den HTTP-Statuscode auf 500 (Internal Server Error).
- **finally:**: Dieser Block wird immer ausgeführt, unabhängig davon, ob ein Fehler aufgetreten ist oder nicht.
- **cursor.close()**: Schließt den Cursor.
- **connection.close()**: Schließt die Datenbankverbindung.

```python
    else:
        return jsonify({'message': 'Database connection failed!', 'status': 'text-danger'}), 500
```
- **else:**: Wenn die Datenbankverbindung fehlgeschlagen ist (d.h., `connection` ist `None`), führen wir diesen Block aus.
- **return jsonify({'message': 'Database connection failed!', 'status': 'text-danger'}), 500**: Wir senden eine Fehlermeldung zurück und setzen den HTTP-Statuscode auf 500 (Internal Server Error).

Der Code ist nicht ganz kompatibel mit der Umgebung, jedoch hatte ich keine Zeit mehr, ihn anzupassen. Der Code wäre jedoch an sich funktional und läuft. Ich bin sehr stolz auf den Code und wie schnell ich Python gelernt habe.

### Projekt Learnings
Ich habe in diesem Projekt unabhängig vom Fachwissen sehr viel über Projektmanagement gelernt. Die angesetzten Weeklys waren fixe Termine in der Freizeit, welche das Commitment unter Beweis stellten. Auch die ganze Rollenteilung und Arbeitsaufteilung war sehr professionell gestaltet und ich denke, davon kann ich viel lernen. Es gab auch eine Verfügbarkeitsliste, in der jeder eintrug, wann und über welchen Kanal man verfügbar ist, was eine große Hilfe war.

### Fazit
Ich habe in diesem Projekt extrem viel gelernt. Von Projektmanagement über Python zu den dazugehörigen Geschäftsprozessen. Auch die Arbeit im Team lernte ich durch die Weeklys nochmals besser kennen und ich sehe jetzt, wie wichtig der regelmäßige Austausch ist. Das Projekt war für mich ein voller Erfolg und ich bin stolz auf das, was ich in dieser kurzen Zeit erreicht habe.
