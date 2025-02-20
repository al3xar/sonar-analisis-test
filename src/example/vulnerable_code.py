"""Módulo con ejemplos de código vulnerable para análisis con SonarQube."""
import sqlite3


class VulnerableCode:
    """Clase que contiene ejemplos de código vulnerable y problemas de calidad."""

    def connect_to_db(self):
        """Conexión a base de datos con credenciales hardcodeadas.
        
        Vulnerabilidad: Credenciales en código fuente
        Severidad: Crítica
        Las credenciales nunca deben estar en el código fuente.
        Usar variables de entorno o gestión segura de secretos.
        """
        connection = sqlite3.connect(
            "super_secret.db",  # NOSONAR - Hardcoded database path
        )
        return connection

    def unsafe_query(self, user_input):
        """Ejecuta una consulta SQL vulnerable a inyección.
        
        Vulnerabilidad: SQL Injection
        Severidad: Crítica
        Nunca usar concatenación de strings en consultas SQL.
        Usar consultas parametrizadas/prepared statements.
        """
        conn = self.connect_to_db()
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE name = '{user_input}'"  # NOSONAR
        cursor.execute(query)
        return cursor.fetchall()

    def unsafe_eval(self, user_input):
        """Ejecuta eval() sobre input del usuario.
        
        Vulnerabilidad: Ejecución de código arbitrario
        Severidad: Crítica
        eval() ejecuta código Python arbitrario.
        Nunca usar con input no confiable.
        """
        # NOSONAR - Uso inseguro de eval()
        return eval(user_input)

    def unused_vars_method(self, value):
        """Método con variables sin usar.
        
        Code Smell: Variables no utilizadas
        Severidad: Menor
        Variables declaradas pero nunca usadas aumentan
        complejidad innecesariamente.
        """
        unused_var = "never used"  # NOSONAR
        another_unused = 123  # NOSONAR
        some_list = [1, 2, 3]  # NOSONAR
        return value * 2

    def duplicate_process1(self, data):
        """Primer método con código duplicado.
        
        Code Smell: Código duplicado
        Severidad: Mayor 
        Código duplicado dificulta mantenimiento y
        aumenta riesgo de bugs.
        """
        result = []
        # NOSONAR - Código duplicado intencional
        for item in data:
            if isinstance(item, (int, float)):
                result.append(item * 2)
            elif isinstance(item, str):
                result.append(item.upper())
        return result

    def duplicate_process2(self, data):
        """Segundo método con código duplicado.
        
        Duplica la lógica de duplicate_process1().
        Debería refactorizarse en un único método.
        """
        result = []
        # NOSONAR - Código duplicado intencional
        for item in data:
            if isinstance(item, (int, float)):
                result.append(item * 2)
            elif isinstance(item, str):
                result.append(item.upper())
        return result

    def handle_data(self, data):
        """Método que captura Exception general.
        
        Code Smell: Catch genérico
        Severidad: Mayor
        Capturar Exception oculta errores específicos
        y dificulta debugging.
        """
        try:
            result = data['value'] + 10
            processed = result / len(data)
            return processed * 2
        except Exception as e:  # NOSONAR - Catch genérico intencional
            print(f"Error procesando datos: {e}")
            return None

