#2021 429 csq
import unittest

def city_functions(City,Country,population=''):
	if population :
		
		out = City + ',' + Country + ' - population ' + population
	else:
		out = City + ',' + Country
	return out

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_cities = city_functions('Santiago','Chile')
		self.assertEqual(formatted_cities,'Santiago,Chile')
	def test_city_country_population(self):
		formatted_cities = city_functions('Santiago','Chile','12')
		self.assertEqual(formatted_cities,'Santiago,Chile - population 12')
unittest.main()
