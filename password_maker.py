# TODO: super secret and secure password maker for my best friend Ann
import hashlib

def secret_password_maker():
    questions = []
    m = hashlib.sha256()
    for question in questions:
        x = input(question+'\n').lower().strip()
        m.update(x.encode())
    return m.hexdigest()

if __name__ == '__main__':
    print(secret_password_maker())
