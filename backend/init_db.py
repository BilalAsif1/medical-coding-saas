import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

def init_database():
    try:
        conn = sqlite3.connect("codes.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS codes (
                entity TEXT PRIMARY KEY,
                icd10 TEXT,
                cpt TEXT,
                hcc TEXT
            )
        """)
        
        sample_data = [
            ("diabetes mellitus", "E11.9", "99213", "19"),
            ("essential hypertension", "I10", "99214", "85"),
            ("heart failure", "I50.9", "99215", "85")
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO codes (entity, icd10, cpt, hcc) VALUES (?, ?, ?, ?)",
            sample_data
        )
        
        conn.commit()
        logging.info("Database initialized with %d records", len(sample_data))
        
    except sqlite3.Error as e:
        logging.error("Database error: %s", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    init_database()
