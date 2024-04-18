import os
import fnmatch
import glob


def get_base_dir() -> str:
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_all_paths() -> list[str]:
    out = []

    # Get the parent directory of the script
    parent_dir = get_base_dir()

    # List to store the paths
    file_paths = []

    # Walk through the parent directory
    for dirpath, dirs, files in os.walk(parent_dir):
        for filename in files:
            # If the file is a .py or .rs file
            if fnmatch.fnmatch(filename, "*.py") or fnmatch.fnmatch(filename, "*.rs"):
                # Append the path to the list
                file_paths.append(os.path.join(dirpath, filename))

    # Print the paths
    for path in file_paths:
        out.append(path)

    # Clean up path list.
    # We don't want __init__.py or anything in the venv
    out = [
        path
        for path in out
        if "__init__.py" not in path and ".venv" not in path and "appendix" not in path
    ]
    # We also don't want anything in the target folder
    out = [path for path in out if "target" not in path]

    return out


def write_to_tex_file(path: str) -> None:
    # file path will be filename.tex
    if ".py" not in path:
        file_path = path.replace(".rs", ".tex")
    else:
        file_path = path.replace(".py", ".tex")

    # Remove workspaces/yr3_panspermia_project/ from the path
    file_path = file_path.replace(get_base_dir(), "")

    os.makedirs(os.path.dirname(f"appendix/{file_path}"), exist_ok=True)
    with open(f"appendix/{file_path}", "w") as f:
        f.write("\\begin{lstlisting}\n")

        with open(path, "r") as file:
            f.write(file.read())

        f.write("\\end{lstlisting}")


def delete_all_tex_files() -> None:
    for tex_file in glob.glob(get_base_dir() + "/**/*.tex", recursive=True):
        os.remove(tex_file)


def make_appendix_tex_code(paths: list[str]) -> None:
    base_dir = get_base_dir()

    # remove base_dir from path
    paths = [path.replace(base_dir, "") for path in paths]

    # remove initial slash from path
    paths = [path[1:] for path in paths]

    with open(f"{base_dir}/appendix/appendix.tex", "w") as f:
        # Write in subsection headings and then import in each file
        # Python is a subsection of the appendix.
        # Each python file is a subsubsection of the Python subsection
        # The name of the subsubsection is the path of the file
        f.write("\\subsection{Python}\n")
        for path in paths:
            if ".py" in path:
                f.write(f"\\subsubsection{{{path}}}\n")
                path = path.replace(".py", ".tex")
                f.write(f"\\input{{appendix/{path}}}\n")

        # Rust is a subsection of the appendix.
        # Each rust file is a subsubsection of the Rust subsection
        # The name of the subsubsection is the path of the file
        f.write("\\subsection{Rust}\n")
        for path in paths:
            if ".rs" in path:
                f.write(f"\\subsubsection{{{path}}}\n")
                path = path.replace(".rs", ".tex")
                f.write(f"\\input{{appendix/{path}}}\n")


def main() -> None:
    paths = get_all_paths()
    for path in paths:
        write_to_tex_file(path)
    make_appendix_tex_code(paths)
    # delete_all_tex_files()


if __name__ == "__main__":
    main()
