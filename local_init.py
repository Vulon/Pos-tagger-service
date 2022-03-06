import os, sys
import venv

if __name__ == '__main__':
    if 'data' not in os.listdir():
        os.mkdir('data')
    if 'env' not in os.listdir():
        venv.create('env')

    path = os.path.join(os.getcwd(), 'env/Scripts/Activate')
    print(path)

    os.system(f"start cmd /c {path}")
    os.system(f"start cmd /k pip install -r requirements.txt")
