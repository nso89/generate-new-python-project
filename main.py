from pathlib import Path
import shutil


MAIN_PY = Path.home().joinpath("Projects\\main.py")


def verify(parameter: str, name: str) -> None:
    """
    Verify if parameter is blank, if so, raise ValueError.
    """
    if not parameter or parameter.isspace():
        raise ValueError(f"{name} cannot be blank!")
    if parameter.startswith(" ") or parameter.endswith(" "):
        raise ValueError(f"{name} cannot begin or end with an empty space!")


def main():

    try:

        project_name = input("Project Name: ").strip().lower().replace(" ","-")
        verify(parameter = project_name, name = "Project Name")

        project_folder = Path().home().joinpath("Projects").joinpath(project_name)

        print(f"Generating: {project_name}")
        project_folder.mkdir(parents = False, exist_ok = False)

        print(f"Copying main.py to {project_folder}")
        shutil.copy(src = MAIN_PY, dst = project_folder)
    
    except (FileExistsError, FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
