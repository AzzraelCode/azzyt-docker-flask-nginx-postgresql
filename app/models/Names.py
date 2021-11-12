import string
import random

from db import conn

class Names(conn.Model):
    """

    """
    id = conn.Column(conn.Integer, primary_key=True)
    name = conn.Column(conn.String(80), unique=False, nullable=False)
    amount = conn.Column(conn.Integer(), unique=True, nullable=False)

    def fill_random(self):
        self.name = ''.join(random.choice(string.ascii_letters) for i in range(10))
        self.amount = random.randrange(1000, 9999)

    def save(self):
        conn.session.add(self)
        conn.session.commit()