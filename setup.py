from cx_Freeze import setup, Executable
import os

ASSETS_DIR = os.path.abspath("./backend/assets")

executables = [Executable("main.py")]

files = {
    "include_files": [(ASSETS_DIR, "assets")],
    "packages": ["pygame"]
}

setup(
    name="WitchSeason",
    version="1.0",
    description="Witch Season app",
    options={"build_exe": files},
    executables=executables
)