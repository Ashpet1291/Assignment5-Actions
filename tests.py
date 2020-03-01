import unittest
import task


class TestCase (unittest.TestCase) :

  def test1(self) :
    expected = "success"
    self.assertEqual(expected, task.firstrun())
    
    def test2(self) :
      expected = "failure"
      self.assertNotEqual(expected, task.firstrun())
      
if _name_ == '_main_':
  unittest.main
