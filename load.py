import os, pygame
import pygame.image, pygame.mixer

'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
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
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def load_images(dirName):

	allImages = dict()

	files = getListOfFiles(dirName)
	for path in files:
		if path.endswith('.png'):
			allImages[path] = pygame.image.load(path).convert_alpha()
	
	return allImages

def load_sounds(dirName):

	allSounds = dict()

	files = getListOfFiles(dirName)
	for path in files:
		if path.endswith('.wav'):
			allSounds[path] = pygame.mixer.Sound(path)
	
	return allSounds

def load_level(world, stage):
	filename = os.path.join('levels', world, stage, '.save')
	level = [ [ char for char in row ] for row in open(filename).read().splitlines() ]
	return level
