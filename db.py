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
timeshed TEXT,
lang TEXT DEFAULT 'ru'
)
"""
            )
            # self.custom()
            self.get_db()
            return

    def get_db(self) -> None:
        with self.conn:
            print(self.cur.execute("SELECT * FROM `users`").fetchall(),
                  self.cur.execute("SELECT * FROM `settings`").fetchall(),
                  sep="\n")
    
    def custom(self):
        with self.conn:
            self.cur.execute("DELETE FROM `users`")
            self.cur.execute("DELETE FROM `settings`")
    
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

    def add_tz(self, tz: str, user_id: int) -> None:
        with self.conn:
            try:
                self.cur.execute(
                    "INSERT INTO `settings` `timezone` VALUES (?) WHERE `user_id` = ?",
                    (tz, user_id,)
                )
            except Exception:
                self.cur.execute(
                    "UPDATE `settings` SET `timezone` = (?) WHERE `user_id` = ?",
                    (tz, user_id,)
                )
            return
    
    def add_time(self, time: str, user_id: int) -> None:
        with self.conn:
            try:
                self.cur.execute(
                    "INSERT INTO `settings` `timeshed` VALUES (?) WHERE `user_id` = ?",
                    (time, user_id,)
                )
            except Exception:
                self.cur.execute(
                    "UPDATE `settings` SET `timeshed` = (?) WHERE `user_id` = ?",
                    (time, user_id,)
                )
            return
    
    def set_lang(self, lang: str, user_id: int) -> None:
        with self.conn:
            self.cur.execute(
                "UPDATE `settings` SET `lang` = ? WHERE `user_id` = ?",
                (lang, user_id,)
            )
    def get_lang(self, user_id: int) -> str:
        with self.conn:
            return self.cur.execute("SELECT `lang` FROM `settings` WHERE `user_id` = ?", (user_id,)).fetchone()[0]
    
    def set_time(self, time: str, user_id: int) -> None:
        with self.conn:
            self.cur.execute(
                "UPDATE `settings` SET `timeshed` = ? WHERE `user_id` = ?",
                (time, user_id)
            )
    
    def get_time(self, user_id: int) -> str:
        with self.conn:
            return self.cur.execute("SELECT `timeshed` FROM `settings` WHERE `user_id` = ?", (user_id,)).fetchone()[0]