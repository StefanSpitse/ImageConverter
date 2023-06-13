from PIL import Image
from pathlib import Path

import os


def setFormat(Min, Max):
    size = input("Het niewe formaat dat je wilt: ")
    size = size.split('x')
    if len(size) != 2:
        raise IncorrectFormat

    size[0] = int(size[0])
    size[1] = int(size[1])

    if size[0] > Max[0] or size[1] > Max[1]:
        raise FormatToBig

    if size[0] < Min[0] or size[1] < Min[1]:
        raise FormatToSmall

    sizes = tuple(size)
    return sizes


def setPath():
    pathIn = input("Path of the images: ")
    if not os.path.exists(pathIn):
        raise PathDoesNotExist

    pathOut = input("Path where the images are saved: ")
    if not os.path.exists(pathOut):
        raise PathDoesNotExist

    return pathIn, pathOut


def getImages(path):
    pathList = Path(path).glob("**/*.jpeg")
    path_list = []
    for path in pathList:
        path_list.append(path)
    images = []
    for path in range(len(path_list)):
        paths = path_list[path]
        image = str(paths).split("\\")
        print("Changing " + image[len(image) - 1])
        images.append(image[len(image) - 1])
    return images


def changeImages(images, size, path):
    for _x in range(len(images)):
        with Image.open(path[0] + "\\" + images[_x]) as im:
            im.resize(size).save(path[1] + "\\" + images[_x])


def main():
    Min = [1, 1]
    Max = [3000, 2000]
    try:
        size = setFormat(Min, Max)
        path = setPath()

        images = getImages(path[0])
        changeImages(images, size, path)

    except IncorrectFormat:
        print("Not a correct format!")
    except ValueError:
        print("Not a correct value!")
    except FormatToBig:
        print("Size can't be bigger then" + str(Max[0]) + "x" + str(Max[1]) + "!")
    except FormatToSmall:
        print("Size can't be smaller then " + str(Min[0]) + "x" + str(Min[1]) + "!")
    except PathDoesNotExist:
        print("Path does not exist!")
    except KeyboardInterrupt:
        exit(main())

    finally:
        main()


class IncorrectFormat(Exception):
    pass


class FormatToBig(Exception):
    pass


class FormatToSmall(Exception):
    pass


class PathDoesNotExist(Exception):
    pass


if __name__ == "__main__":
    main()
