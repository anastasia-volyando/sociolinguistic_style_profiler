import sqlite3

DB_NAME = "style_markers.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS markers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marker TEXT NOT NULL,
            category TEXT NOT NULL,
            weight INTEGER NOT NULL,
            description TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_sample_markers():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM markers")
    count = cursor.fetchone()[0]

    if count == 0:
        markers = [
            # Internet slang
            ("lol", "internet_slang", 3, "laughing out loud; common online laughter marker"),
            ("lmao", "internet_slang", 4, "stronger online laughter marker"),
            ("ngl", "internet_slang", 4, "not gonna lie; informal stance marker"),
            ("tbh", "internet_slang", 3, "to be honest; informal stance marker"),
            ("idk", "internet_slang", 3, "I don't know; informal abbreviation"),
            ("imo", "internet_slang", 2, "in my opinion; online opinion marker"),
            ("btw", "internet_slang", 2, "by the way; informal abbreviation"),
            ("fr", "internet_slang", 3, "for real; emphasis marker"),
            ("rn", "internet_slang", 2, "right now; informal abbreviation"),
            ("omg", "internet_slang", 3, "oh my god; emotional reaction marker"),

            # Casual speech
            ("bro", "casual_speech", 4, "informal address term"),
            ("dude", "casual_speech", 3, "casual address term"),
            ("guy", "casual_speech", 2, "informal reference term"),
            ("kinda", "casual_speech", 3, "informal form of kind of"),
            ("sorta", "casual_speech", 3, "informal form of sort of"),
            ("gonna", "casual_speech", 3, "informal form of going to"),
            ("wanna", "casual_speech", 3, "informal form of want to"),
            ("gotta", "casual_speech", 3, "informal form of got to"),
            ("yeah", "casual_speech", 2, "informal yes"),
            ("nah", "casual_speech", 3, "informal no"),

            # Gen Z / internet style
            ("lowkey", "gen_z_speech", 4, "informal understatement or stance marker"),
            ("highkey", "gen_z_speech", 4, "informal emphasis marker"),
            ("slay", "gen_z_speech", 4, "positive evaluation marker"),
            ("fire", "gen_z_speech", 4, "slang adjective meaning very good"),
            ("vibe", "gen_z_speech", 3, "informal aesthetic or feeling marker"),
            ("sus", "gen_z_speech", 4, "suspicious; internet slang"),
            ("cringe", "gen_z_speech", 3, "negative evaluation marker"),
            ("based", "gen_z_speech", 4, "approval marker in internet discourse"),
            ("mid", "gen_z_speech", 4, "negative/neutral evaluation meaning mediocre"),
            ("delulu", "gen_z_speech", 4, "slang for delusional"),

            # Formal register
            ("therefore", "formal_register", 4, "formal logical connector"),
            ("however", "formal_register", 3, "formal contrastive connector"),
            ("moreover", "formal_register", 4, "formal additive connector"),
            ("nevertheless", "formal_register", 4, "formal contrastive connector"),
            ("consequently", "formal_register", 4, "formal result connector"),
            ("furthermore", "formal_register", 4, "formal additive connector"),
            ("thus", "formal_register", 3, "formal conclusion marker"),
            ("hence", "formal_register", 3, "formal result marker"),
            ("whereas", "formal_register", 3, "formal contrast marker"),
            ("accordingly", "formal_register", 3, "formal result marker"),

            # Academic register
            ("argues", "academic_register", 3, "academic reporting verb"),
            ("suggests", "academic_register", 3, "academic reporting verb"),
            ("indicates", "academic_register", 3, "academic evidence marker"),
            ("demonstrates", "academic_register", 4, "academic evidence marker"),
            ("analysis", "academic_register", 3, "academic noun"),
            ("hypothesis", "academic_register", 4, "academic research term"),
            ("evidence", "academic_register", 3, "academic reasoning term"),
            ("methodology", "academic_register", 4, "academic research term"),
            ("framework", "academic_register", 3, "academic theoretical term"),
            ("phenomenon", "academic_register", 3, "academic descriptive term"),

            # Politeness
            ("please", "politeness", 2, "politeness marker"),
            ("thank you", "politeness", 3, "gratitude marker"),
            ("thanks", "politeness", 2, "informal gratitude marker"),
            ("would you mind", "politeness", 4, "indirect polite request"),
            ("could you", "politeness", 3, "polite request form"),
            ("I would appreciate", "politeness", 4, "formal politeness phrase"),
            ("sorry", "politeness", 2, "apology marker"),
            ("excuse me", "politeness", 3, "polite attention marker"),
            ("if possible", "politeness", 3, "softening phrase"),
            ("kindly", "politeness", 3, "formal politeness marker"),

            # Hedging
            ("maybe", "hedging", 3, "uncertainty marker"),
            ("perhaps", "hedging", 3, "formal uncertainty marker"),
            ("I think", "hedging", 3, "epistemic stance marker"),
            ("I guess", "hedging", 3, "informal uncertainty marker"),
            ("probably", "hedging", 2, "probability marker"),
            ("possibly", "hedging", 3, "uncertainty marker"),
            ("kind of", "hedging", 3, "softening expression"),
            ("sort of", "hedging", 3, "softening expression"),
            ("seems", "hedging", 2, "indirect claim marker"),
            ("apparently", "hedging", 2, "evidential uncertainty marker"),
        ]

        cursor.executemany("""
            INSERT INTO markers (marker, category, weight, description)
            VALUES (?, ?, ?, ?)
        """, markers)

    conn.commit()
    conn.close()


def get_markers():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT marker, category, weight, description FROM markers")
    rows = cursor.fetchall()

    conn.close()
    return rows