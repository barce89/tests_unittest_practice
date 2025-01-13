import unittest,requests
import unittest.mock
from src.api_client import get_url
from unittest.mock import patch


class ApiClientTest(unittest.TestCase):
    
    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self,mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value={ 
            'countryName': 'United States of America',  
            'cityName': 'Mountain View', 
            'regionName': 'California',
            'countryCode':'US'
            }
        result = get_url('8.8.8.8')
        self.assertEqual(result.get("country"),'United States of America')
        self.assertEqual(result.get("region"),'California')
        self.assertEqual(result.get("city"),'Mountain View')
        self.assertEqual(result.get("countryCode"),'US')

        mock_get.assert_called_once_with(f'https://freeipapi.com/api/json/8.8.8.8')



    #asi podemos hacer mock para poder simular la salida o el retorno de la aplicacion

    @patch('src.api_client.requests.get')
    def test_get_location_side_effect(self,mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavilable"),unittest.mock.Mock(
                status_code = 200,
                json = lambda:{
                    'countryName': 'United States of America',  
                    'cityName': 'Mountain View', 
                    'regionName': 'California',
                    'countryCode':'US'
                }
            )
        ]
        
        with self.assertRaises(requests.exceptions.RequestException):
            get_url('8.8.8.8')
        
        result = get_url('8.8.8.8')
        self.assertEqual(result.get("country"),'United States of America')
        self.assertEqual(result.get("region"),'California')
        self.assertEqual(result.get("city"),'Mountain View')
        self.assertEqual(result.get("countryCode"),'US')

        # mock_get.assert_called_once_with(f'https://freeipapi.com/api/json/8.8.8.8')


