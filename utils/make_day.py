import datetime
import sys
from pathlib import Path


def main():
    args = sys.argv[1:]
    day_number = (
        args[0]
        if len(args) > 0
        else datetime.date.today().strftime("%d").removeprefix("0")
    )

    file_content = """from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

content = open(0).read()
    """

    folder_path = Path(__file__).parent.parent / f"d{day_number}"
    if folder_path.exists():
        print("Folder already exists. Doing Nothing...")
        return
    folder_path.mkdir(parents=True, exist_ok=True)

    # create p1
    p1 = folder_path / "p1.py"
    p1.touch()
    p1.write_text(file_content)

    # create justfile
    justfile_content = """t1:
  uv run p1.py < t.in

r1:
  uv run p1.py < r.in

t2:
  uv run p2.py < t.in

r2:
  uv run p2.py < r.in
"""
    jstfile = folder_path / "justfile"
    jstfile.touch()
    jstfile.write_text(justfile_content)


if __name__ == "__main__":
    main()
