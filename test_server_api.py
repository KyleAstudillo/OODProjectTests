#!/usr/bin/python

import requests
import unittest
import random

server_ip = 'localhost:5000'
server_url = 'http://{0}/api/coffee'.format(server_ip)
number_of_data = 1

class coffee:
	def __init__(self):
		self.name = name
		self.

class a(unittest.TestCase):
	
	def test_equal(self):
		self.assertEquals(0, 0)
	def test_GetAll(self):
		r = requests.get(server_url)
		data = r.json()
		number_of_data = len(data)
		self.assertGreater(len(data), 0)
	def test_get(self):
		random_int = random.randint(1, 5)
		r = requests.get('{0}/{1}'.format(server_url, random_int))
		data = r.json()
		self.assertNotIn("null", data["name"])
	def test_put(self):
		object_string =  let urlOptions  = '?id={0}&name={1}&imageLink1={2}&imageLink2={3}&userId={4}coffeeId=${5}'.format(22, 'test_coffee', 'null','null', 0, 0)
		r = requests.put('{0}{1}'.format(server_url, object_string), '')
		data = r.json()
	def test_update(self):
			print()
	def test_delete(self):
			print()
		
if __name__ == "__main__":
	unittest.main()
	