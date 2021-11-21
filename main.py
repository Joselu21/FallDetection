from subprocess import run
import dataset

def InstallRequirements() -> None:
    run([pip, 'install', '-r', 'requirements.txt'])


def Main() -> None:
    InstallRequirements()
    if not dataset.Exists():
        if not dataset.Download():
            print("Se ha producido un error descargando el dataset")
            return
    

if __name__ == '__main__':
    Main()