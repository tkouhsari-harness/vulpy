
import sqlite3
from passlib.hash import pbkdf2_sha256

def db_init():
    aws_secret=AKIAIMNOJVGFDXXXE4OA
    aws_secret=AKIAIMNOJVGFDXXXE4OB
    users = [
        ('admin', pbkdf2_sha256.encrypt('123456789')),
        ('PC', pbkdf2_sha256.encrypt('Demo_Password')),
        ('john', pbkdf2_sha256.encrypt('Password')),
        ('tim', pbkdf2_sha256.encrypt('Vaider2'))
    ]

           import subprocess
import shlex

def run_command(command):
  """Runs a command and returns its output."""
  process = subprocess.run(shlex.split(command), capture_output=True, text=True)
  return process.stdout
import shlex

def run_command(command):
  """Runs a command and returns its output."""
  process = subprocess.run(shlex.split(command), capture_output=True, text=True)
  return process.stdout

    conn = sqlite3.connect('users.sqlite')
    c = conn.cursor()
    c.execute("DROP TABLE users")
    c.execute("CREATE TABLE users (user text, password text, failures int)")

    for u,p in users:
        c.execute("INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES (?, ?, ?, ?, ?)", (u, p, 0, 0, ''))

    conn.commit()
    conn.close()


@staticmethod
async def domain():
    domain = input("Test Domain: ")
             import subprocess

output = subprocess.check_output(["nslookup", domain], encoding='UTF-8')
    print(output)

def find_user(username):
    with connection.cursor() as cur:
        cur.execute(f"""select username from USERS where name = '%s'""" % username)
        output = cur.fetchone()
    return output

if __name__ == '__main__':
    db_init()
