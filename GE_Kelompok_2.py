# Author	:	Rizkiyana Prima Putra
#				Muhammad Iqbal Tawakal
#				Raditya Budi Handoko
#				Nikho Toga Bungaran S
# Date		: 	15 April 2017
# Desc		: 	Implements Grammatical Evolultion
#				for predicting average of gold price


# LIBRARY
from random import randint
import random
import numpy as np
import math as mt
import xlrd



def toDecimal(binarys):
	total = 0
	for x in range(len(binarys)):
		total += (2**x)*list(reversed(binarys))[x]
	return total

# FUNGSI UNTUK MEMBACA FILE
def loadData(filename, sheetNum, colNum, data):
	workbook = xlrd.open_workbook(filename)
	sheet = workbook.sheet_by_index(sheetNum)
	data = [val.value for val in sheet.col(colNum)]
	data = data[1:]

# FUNGSI MEMBANGKITKAN POPULASI SEBANYAK nPop KROMOSOM sebanyak nGen GEN
def generatePopulation(population, nPop, nGen, nBit):
	for x in range(nPop):
		population.update({"Chromosome-%d" % (x+1) : [random.randint(0,1) for x in range(nBit*nGen)]})
	return population

# FUNGSI UNTUK KONVERSI KROMOSOM BINER KE KROMOSOM INTEGER
def populationConvert(population, nBit):
	for key in population.keys():
		newGen = []
		chrom = [population[key][i:i+nBit] for i in range(0, len(population[key]), nBit)]
		print(len(chrom))
		for val in chrom:
			newGen.append(toDecimal(val))
		population[key] = newGen
	return population

# FUNGSI UNTUK MENG-OUTPUT-KAN SETIAP KROMOSOM PADA POPULASI
def showPopulation(population):
	for key in population.keys():
		print (key + " : " + str(population[key]))



# KAMUS DATA
data_train = []
population = {}
nBit = 8
nGen = 10
nPop = 100

productionRules = {
	'expr' : [['expr', 'op', 'expr'], ['(', 'expr', 'op', 'expr', ')'], ['pre_op', 'expr'], 'var'],
	'op' : ['-', '+', '/', '*'],
	'pre_op' : ['sin', 'cos', 'tan', 'log'],
	'var' : 'x'
}


# MAIN PROGRAM
# loadData("DataHistorisANTAM.xlsx", 0, 11, data_train)

population = generatePopulation(population, nPop, nGen, nBit)
population = populationConvert(population, nBit)
showPopulation(population)



# TEST CODE