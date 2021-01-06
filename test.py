import unittest
from index import date_solution


#Testing
class SolutionTest(unittest.TestCase):
	def test_date_soluton(self):
		d1 = {"2020-01-01": 4, "2020-01-02": 4, "2020-01-03": 6, "2020-01-04": 8, "2020-01-05": 2, "2020-01-06": -6, "2020-01-07": 2, "2020-01-08": -2}
		expected_result = {'Mon':-6, 'Tue':2,'Wed':2,'Thu':4,'Fri':6,'Sat':8,'Sun':2}

		result  = date_solution(d1)
		self.assertEqual(result, expected_result)
		
	def test_date_soluton_case2(self):
			d2 =  {"2020-01-01": 6, "2020-01-04":12, "2020-01-05":14, "2020-01-06":2, "2020-01-07":4}
			expected_result = {'Mon':2, 'Tue':4,'Wed':6,'Thu':8,'Fri':10,'Sat':12,'Sun':14}

			result  = date_solution(d2)
			self.assertEqual(result, expected_result )

if __name__ == "__main__":
	unittest.main()