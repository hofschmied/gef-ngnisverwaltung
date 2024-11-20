import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
    conn = sqlite3.connect('gefaengnis.db')
    cursor = conn.cursor()
    cursor.execute("SELECT GID, Namen FROM Gefaengnis")
    gefaengnisse = cursor.fetchall()
    conn.close()
    return [(name, gid) for name, gid in gefaengnisse]

@anvil.server.callable
def get_gefaengnis_details(gefaengnis_id):
    conn = sqlite3.connect('gefaengnis.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Verwaltung.Direktor, Verwaltung.Anzahl_freie_Zellen
        FROM Verwaltung
        JOIN Gefaengnis ON Gefaengnis.VID = Verwaltung.VID
        WHERE Gefaengnis.GID = Verwaltung.VID
    """, (gefaengnis_id))
    details = cursor.fetchone()
    conn.close()
