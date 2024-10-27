from pathlib import Path


def rename_clear_png(src, des):
    number = 1

    for file in Path(src).glob("*.png"):
        new_filename = f"{number:04}.png"
        file.rename(f"{Path(des)}/{new_filename}")

        print(new_filename)

        number += 1


def rename_haze_png(src, des, number):
    number1 = 1
    number2 = 0
    files = []

    for file in Path(src).glob("*.png"):
        files.append(file)

    for _, _ in enumerate(files):
        for i in range(number):
            new_filename = f"{number1:04}_{i + 1}.png"
            files[number2].rename(f"{Path(des)}/{new_filename}")
            print(new_filename)
            number2 += 1

        number1 += 1


def rename_clear_jpg(src, des):
    number = 1

    for file in Path(src).glob("*.jpg"):
        new_filename = f"{number:04}.png"
        file.rename(f"{Path(des)}/{new_filename}")

        print(new_filename)

        number += 1


def rename_haze_jpg(src, des, number):
    number1 = 1
    number2 = 0
    files = []

    for file in Path(src).glob("*.jpg"):
        files.append(file)

    for _, _ in enumerate(files):
        for i in range(number):
            new_filename = f"{number1:04}_{i + 1}.png"
            files[number2].rename(f"{Path(des)}/{new_filename}")
            print(new_filename)
            number2 += 1

        number1 += 1


def main():
    rename_clear_jpg(
        "C:/Users/mattc/Documents/GitHub/RESIDE-Standard/OTS/val/clear",
        "C:/Users/mattc/Documents/GitHub/RESIDE-Standard/OTS/val/clear_new",
    )
    rename_haze_jpg(
        "C:/Users/mattc/Documents/GitHub/RESIDE-Standard/OTS/val/haze",
        "C:/Users/mattc/Documents/GitHub/RESIDE-Standard/OTS/val/haze_new",
        35,
    )


if __name__ == "__main__":
    main()
