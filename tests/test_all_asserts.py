import unittest

SERVER = "server_b"
class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10,10) #este assert se ocupa de manera mas general
        self.assertEqual("Hola","Hola")

    def test_assert_true_or_false(self):#assert para verificar valores boolenaos
        self.assertTrue(True)
        # self.assertTrue(False)


    def test_assert_raises(self):#este assert captura las excepciones
        with self.assertRaises(ValueError):
            int('no soy un numero')

    def test_assert_in(self):
        self.assertIn(10,[2,4,5,10]) #validar que 10 este dentro de la lista
        self.assertNotIn(5,[2,4,67,10])# caso contrario, que 5 no  este en la lista

    def test_assert_dicts(self):
        user={"first_name":"Luis",
             "last_name":"Martinez"}
        self.assertDictEqual(
            {"first_name":"Luis",
             "last_name":"Martinez"},user
        )

        self.assertSetEqual(
            {1,2,3},{1,2,3}
        )

    
    @unittest.skip("Este decorador es para poderse saltar una prueba en dado caso se este trabajando en eso")
    def test_skip(self):
        self.assertEqual(10,10,'mensaje')



    #este decorador sirve para evaluar que la condicion sea verdadera, si la condicion es verdadera entra y se salta la prueba
    @unittest.skipIf(SERVER =="server_b",'saltado porque no estamos en el servidor')
    def test_skip_if(self):
        self.assertEqual(100,100)


    #este decorador es para esperar fallos y capturarlos
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,150)