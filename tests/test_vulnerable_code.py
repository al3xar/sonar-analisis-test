import pytest
from unittest.mock import Mock, patch
from src.example.vulnerable_code import VulnerableCode

@pytest.fixture
def vulnerable_code():
    """
    Fixture que proporciona una instancia de VulnerableCode con la conexión DB mockeada
    """
    with patch('src.example.vulnerable_code.sqlite3') as mock_sqlite:
        # Configurar el mock de la conexión
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_sqlite.connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('result1',), ('result2',)]
        
        code = VulnerableCode()
        code.db_connection = mock_conn
        code.cursor = mock_cursor

        yield code

class TestVulnerableCode:
    """Tests para la clase VulnerableCode que contiene código intencionalmente vulnerable"""
    
    def test_connect_to_db_creates_connection(self, vulnerable_code):
        """
        Prueba que connect_to_db establece una conexión a la base de datos
        """
        result = vulnerable_code.connect_to_db()
        assert result == vulnerable_code.db_connection
        assert vulnerable_code.db_connection is not None
        assert vulnerable_code.cursor is not None

    def test_unsafe_query_normal_input(self, vulnerable_code):
        """
        Prueba unsafe_query con input normal
        """
        result = vulnerable_code.unsafe_query("test_user")
        assert result == [('result1',), ('result2',)]
        vulnerable_code.cursor.execute.assert_called_once()

    def test_unsafe_query_sql_injection(self, vulnerable_code):
        """
        Prueba unsafe_query con un intento de SQL injection
        """
        malicious_input = "admin' OR '1'='1"
        result = vulnerable_code.unsafe_query(malicious_input)
        assert result == [('result1',), ('result2',)]
        
    def test_unsafe_eval_normal_case(self, vulnerable_code):
        """
        Prueba unsafe_eval con una expresión matemática válida
        """
        result = vulnerable_code.unsafe_eval("2 + 2")
        assert result == 4

    def test_unsafe_eval_malicious_input(self, vulnerable_code):
        """
        Prueba unsafe_eval con input malicioso
        Este test verifica que se lance NameError al intentar acceder a módulos no importados
        """
        with pytest.raises(NameError):
            vulnerable_code.unsafe_eval("os.system('echo hacked')")

    def test_unused_vars_method(self, vulnerable_code):
        """
        Prueba el método que contiene variables sin usar
        """
        result = vulnerable_code.unused_vars_method(10)
        assert result == 20

    def test_duplicate_process1(self, vulnerable_code):
        """
        Prueba el primer método con código duplicado
        """
        result = vulnerable_code.duplicate_process1([1, 2, 3, 4, 5])
        assert result == [2, 4, 6, 8, 10]

    def test_duplicate_process2(self, vulnerable_code):
        """
        Prueba el segundo método con código duplicado
        """
        result = vulnerable_code.duplicate_process2([1, 2, 3, 4, 5])
        assert result == [2, 4, 6, 8, 10]

    def test_handle_data_success(self, vulnerable_code):
        """
        Prueba handle_data con un caso exitoso
        """
        result = vulnerable_code.handle_data([1, 2, 3])
        assert result == None

    def test_handle_data_catches_exception(self, vulnerable_code):
        """
        Prueba que handle_data atrapa todas las excepciones
        """
        result = vulnerable_code.handle_data(None)
        assert result is None

