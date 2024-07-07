import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.conn.cursor()

    def start(self):
        with self.conn:
            self.cur.execute(
                """
CREATE TABLE IF NOT EXISTS `users`(
user_id INTEGER PRIMARY KEY UNIQUE NOT NULL
)
"""
            )
            self.cur.execute(
                """
CREATE TABLE IF NOT EXISTS `settings`(
user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
timezone TEXT,
timeshed TEXT
)
"""
            )
            self.get_db()
            return

    def get_db(self) -> None:
        with self.conn:
            print(self.cur.execute("SELECT * FROM `users`").fetchall(),
                  self.cur.execute("SELECT * FROM `settings`").fetchall(),
                  sep="\n")
    
    def custom(self):
        with self.conn:
            pass
    
    def get_users(self):
        with self.conn:
            return self.cur.execute("SELECT `user_id` FROM `users`").fetchall()

    def user_exists(self, user_id: int):
        with self.conn:
            result = self.cur.execute(
                "SELECT * FROM `users` WHERE `user_id` = ?",
                (user_id,)).fetchmany(1)
            return bool(len(result))
    
    def add_user(self, user_id: int) -> None:
        with self.conn:
            self.cur.execute(
                "INSERT INTO `users` (user_id) VALUES (?)",
                (user_id,))
            self.cur.execute(
                "INSERT INTO `settings` (user_id) VALUES (?)",
                (user_id,))

    def add_tz(self, tz: str, user_id: int):
        with self.conn:
            try:
                self.cur.execute(
                    "INSERT INTO `settings` `timezone` VALUES (?) WHERE `user_id` = ?",
                    (tz, user_id,)
                )
            except:
                self.cur.execute(
                    "UPDATE `settings` SET `timezone` = (?) WHERE `user_id` = ?",
                    (tz, user_id,)
                )
            return