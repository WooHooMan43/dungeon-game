from __future__ import annotations

import pygame
import os

# Credit to Varun of thispointer.com
def get_files(dirName: str) -> list:
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + get_files(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def load_images(dirName: str) -> dict:
    # Load each image within a folder and every subfolder.
    allImages = dict()
    # Get the files
    files = get_files(dirName)
    for path in files:
        # Weed out all but the pngs and load.
        if path.endswith(".png"):
            allImages[path] = pygame.image.load(path).convert_alpha()

    return allImages


def load_sounds(dirName: str) -> dict:
    # Load each image within a folder and every subfolder.
    allSounds = dict()
    # Get the files
    files = get_files(dirName)
    for path in files:
        # Weed out all but the pngs and load.
        if path.endswith(".wav"):
            allSounds[path] = pygame.mixer.Sound(path)

    return allSounds


def load_level(world: int, stage: int) -> list[list[str]]:
    # Non-functional and likely to be removed.
    filename = os.path.join("levels", world, stage, ".save")
    level = [[char for char in row] for row in open(filename).read().splitlines()]
    return level
