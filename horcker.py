#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	A script to help trac progress in Prof. Grant Horner of The Master's Seminary's ten-list Bible-reading system
	
	Using Doxygen-formatted Pythonic docstrings.
"""

import csv

# Immutable tuple of Bible book names, for both OT and NT; assuming the Christian (romanised) Vulgate canonical structure, as this is what Horner's Ten Lists presupposes:
books = (
	"Genesis",
	"Exodus",
	"Leviticus",
	"Numbers",
	"Deuteronomy",
	"Joshua",
	"Judges",
	"Ruth",
	"I Samuel",
	"II Samuel",
	"I Kings",
	"II Kings",
	"I Chronicles",
	"II Chronicles",
	"Ezra",
	"Nehemiah",
	"Estha",
	"Job",
	"Psalms",
	"Proverbs",
	"Ecclesiastes",
	"Song of Songs",
	"Isaiah",
	"Jeremiah",
	"Lamentations",
	"Ezekiel",
	"Daniel",
	"Hosea",
	"Joel",
	"Amos",
	"Obediah",
	"Jonah",
	"Micah",
	"Naham",
	"Habakkuk",
	"Zephaniah",
	"Haggai",
	"Zechariah",
	"Malachi",
	"Matthew",
	"Mark",
	"Luke",
	"John",
	"Acts",
	"Romans",
	"I Corinthians",
	"II Corinthians",
	"Galatians",
	"Ephesians",
	"Philippians",
	"Colossians",
	"I thessalonians",
 	"II Thessalonians",
	"I Timothy",
	"II Timothy",
	"Titus",
	"Philemon",
	"Hebrews",
	"James",
	"I Peter",
	"II Peter",
	"I John",
	"II John",
	"III John",
	"Jude",
	"Revelation"
)

# Romanised structure of canonical OT & NT book chapter totals:
numChaps = (50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4, 28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22)

# Lists data:
lists = {
	"One" : [numChaps[39], numChaps[40], numChaps[41], numChaps[42]],# canonical Gospels -- synoptics (Mat., Mark, Luk) and John.
	"Two" : [numChaps[0], numChaps[1], numChaps [2], numChaps [3], numChaps[4]],# Torah/Pentateuch (Gen, Exod, Lev, Num, Deut).
	"Three" : [numChaps[44], numChaps[45], numChaps[46], numChaps[47], numChaps[48], numChaps[49], numChaps[50], numChaps[57]],# Paul/Luke? (Rom, I Cor, II Cor, Gal, Eph, Phil, Col, Heb).
	"Four" : [numChaps[51], numChaps[52], numChaps[53], numChaps[54], numChaps[55], numChaps[56], numChaps[58], numChaps[59], numChaps[60], numChaps[61], numChaps[62], numChaps[63], numChaps[64], numChaps[65]],# Basically the rest of the NT.
	"Five" : [numChaps[17], numChaps[20], numChaps [21]],# Wisdom literature/poetry (with Psalms and Proverbs excepted as these are their own lists as indidivudal books).
	"Six" : [numChaps[18]],# Psalms
	"Seven" : [numChaps[19]],# Proverbs
	"Eight" : [numChaps[5], numChaps[6], numChaps[7], numChaps[8], numChaps[9], numChaps[10], numChaps[11], numChaps[12], numChaps[13], numChaps[14], numChaps[15], numChaps[16]],# Former prophets/earlier Israelite history.
	"Nine" : [numChaps[22], numChaps[23], numChaps[24], numChaps[25], numChaps[26], numChaps[27], numChaps[28], numChaps[29], numChaps[30], numChaps[31], numChaps[32], numChaps[33], numChaps[34], numChaps[35], numChaps[36], numChaps[37], numChaps[38]],# Latter prophets (major and minor)
	"Ten" : [numChaps[43]]# Acts.
}

def getBookName (indx):
	"""
		Returns the name of the book being indexed according to the Vulgate canonical structure, rather than the in-code raw list index provided.
		
		@param indx: the canonically-structured index.
		@type: int
		
		@returns: The name of the requested book.
		@rtype: str
	"""
	
	while True:
		try:
			return books[indx - 1]
			break
		except IndexError:
			print ("Error: entry is out of range of book list. Please enter a number between 1 - 66.")
			Continue

def getBookIndx (name):
	"""
		Returns the index of the Bible book being nominally queried according to the Vulgate canonical structure, rather than the raw list index provided.
		
		@param name: the name of the requested book (provided that data entry is valid).
		@type: str
		
		@returns: The index of the requested book.
		@rtype: int
	"""
	
	bookIndx = 1# Canonical index, not computational/Pythonic!
	for i in books:
		if bookIndx == len(books):
			print ("Error: book not found. Please make sure you typed the name correctly or that it is a valid English-rendered cononical book name (Apocryphal literature not used).")
		elif not books.__contains__ (name):
			bookIndx+= 1

	if books.__contains__ (name):
		return bookIndx

def main ():
	print(getBookName (40))
	print(int(getBookIndx ("Mark")))

if __name__ == "__main__":
	main ()
