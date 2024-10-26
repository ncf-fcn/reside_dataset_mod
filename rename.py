from pathlib import Path

directory = Path("C:/Users/mattc/Documents/RESIDE-Standard/SOTS/outdoor/test/clear")
directory_new = Path(
    "C:/Users/mattc/Documents/RESIDE-Standard/SOTS/outdoor/test/clear_new"
)
number = 1

for file in directory.glob("*.png"):
    new_filename = f"{number:04}.png"
    file.rename(f"{directory_new}/{new_filename}")
    print(new_filename)
    number += 1
