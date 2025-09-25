"""
Motor matemático para MathMaster
Contiene las funciones principales para cálculos y generación de ejercicios
"""

import random
import math
from typing import List, Dict, Tuple, Any
from fractions import Fraction
import sympy as sp

class MathEngine:
    """Clase principal para operaciones matemáticas y generación de ejercicios"""
    
    def __init__(self):
        self.topics = {
            'conjuntos_numericos': ConjuntosNumericos(),
            'numeros_primos': NumerosPrimos(),
            'fraccionarios': Fraccionarios(),
            'potenciacion_radicacion': PotenciacionRadicacion()
        }
    
    def generate_exercise(self, topic: str, difficulty: int = 1) -> Dict[str, Any]:
        """Genera un ejercicio para el tema especificado"""
        if topic in self.topics:
            return self.topics[topic].generate_exercise(difficulty)
        else:
            raise ValueError(f"Tema '{topic}' no encontrado")
    
    def check_answer(self, topic: str, exercise_id: str, user_answer: Any) -> Dict[str, Any]:
        """Verifica la respuesta del usuario"""
        if topic in self.topics:
            return self.topics[topic].check_answer(exercise_id, user_answer)
        else:
            raise ValueError(f"Tema '{topic}' no encontrado")

class ConjuntosNumericos:
    """Clase para ejercicios de conjuntos numéricos"""
    
    def __init__(self):
        self.exercises = {}
    
    def generate_exercise(self, difficulty: int = 1) -> Dict[str, Any]:
        """Genera ejercicios sobre conjuntos numéricos"""
        exercise_types = [
            'clasificar_numero',
            'propiedades_operaciones',
            'teorema_fundamental_aritmetica'
        ]
        
        exercise_type = random.choice(exercise_types)
        exercise_id = f"cn_{random.randint(1000, 9999)}"
        
        if exercise_type == 'clasificar_numero':
            return self._generate_clasificar_numero(exercise_id, difficulty)
        elif exercise_type == 'propiedades_operaciones':
            return self._generate_propiedades_operaciones(exercise_id, difficulty)
        else:
            return self._generate_teorema_fundamental(exercise_id, difficulty)
    
    def _generate_clasificar_numero(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de clasificación de números"""
        numbers = []
        if difficulty == 1:
            numbers = [5, -3, 0, 2.5, -1.7, 3/4]
        elif difficulty == 2:
            numbers = [math.sqrt(2), math.pi, -5/3, 0.333, 7, -2]
        else:
            numbers = [math.e, math.sqrt(8), -7/11, 0.142857, 13, -math.sqrt(5)]
        
        selected_number = random.choice(numbers)
        
        exercise = {
            'id': exercise_id,
            'type': 'clasificar_numero',
            'question': f'Clasifica el número {selected_number} según los conjuntos numéricos (N, Z, Q, I, R)',
            'number': selected_number,
            'options': ['Natural', 'Entero', 'Racional', 'Irracional', 'Real'],
            'difficulty': difficulty
        }
        
        # Determinar respuesta correcta
        correct_answer = self._classify_number(selected_number)
        exercise['correct_answer'] = correct_answer
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _classify_number(self, number) -> List[str]:
        """Clasifica un número en los conjuntos numéricos"""
        classifications = []
        
        # Todos los números son reales (en este contexto)
        classifications.append('Real')
        
        if isinstance(number, int) and number >= 0:
            classifications.append('Natural')
        
        if isinstance(number, int):
            classifications.append('Entero')
        
        # Verificar si es racional
        try:
            if isinstance(number, (int, float)):
                frac = Fraction(number).limit_denominator()
                if abs(float(frac) - number) < 1e-10:
                    classifications.append('Racional')
                else:
                    classifications.append('Irracional')
        except:
            classifications.append('Irracional')
        
        return classifications
    
    def _generate_propiedades_operaciones(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio sobre propiedades de operaciones"""
        properties = [
            'conmutativa_suma',
            'conmutativa_multiplicacion',
            'asociativa_suma',
            'asociativa_multiplicacion',
            'distributiva',
            'elemento_neutro',
            'elemento_inverso'
        ]
        
        prop = random.choice(properties)
        a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        
        exercise = {
            'id': exercise_id,
            'type': 'propiedades_operaciones',
            'property': prop,
            'difficulty': difficulty
        }
        
        if prop == 'conmutativa_suma':
            exercise['question'] = f'¿Es verdad que {a} + {b} = {b} + {a}? Justifica usando la propiedad conmutativa.'
            exercise['correct_answer'] = True
            exercise['explanation'] = f'Sí, por la propiedad conmutativa: {a} + {b} = {a + b} = {b + a} = {b} + {a}'
        
        elif prop == 'distributiva':
            exercise['question'] = f'Aplica la propiedad distributiva: {a}({b} + {c}) = ?'
            exercise['correct_answer'] = a * b + a * c
            exercise['explanation'] = f'{a}({b} + {c}) = {a}×{b} + {a}×{c} = {a*b} + {a*c} = {a*b + a*c}'
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_teorema_fundamental(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio sobre teorema fundamental de la aritmética"""
        if difficulty == 1:
            number = random.randint(12, 50)
        elif difficulty == 2:
            number = random.randint(51, 200)
        else:
            number = random.randint(201, 500)
        
        exercise = {
            'id': exercise_id,
            'type': 'teorema_fundamental',
            'question': f'Encuentra la factorización prima de {number}',
            'number': number,
            'difficulty': difficulty
        }
        
        # Calcular factorización prima
        factors = self._prime_factorization(number)
        exercise['correct_answer'] = factors
        exercise['explanation'] = f'La factorización prima de {number} es: {" × ".join(map(str, factors))}'
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _prime_factorization(self, n: int) -> List[int]:
        """Encuentra la factorización prima de un número"""
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    def check_answer(self, exercise_id: str, user_answer: Any) -> Dict[str, Any]:
        """Verifica la respuesta del usuario"""
        if exercise_id not in self.exercises:
            return {'error': 'Ejercicio no encontrado'}
        
        exercise = self.exercises[exercise_id]
        correct = exercise['correct_answer']
        
        is_correct = False
        feedback = ""
        
        if exercise['type'] == 'clasificar_numero':
            # Comparar listas de clasificaciones
            if isinstance(user_answer, list) and isinstance(correct, list):
                is_correct = set(user_answer) == set(correct)
                if is_correct:
                    feedback = "¡Correcto! Has clasificado el número correctamente."
                else:
                    feedback = f"Incorrecto. La clasificación correcta es: {', '.join(correct)}"
        
        elif exercise['type'] == 'propiedades_operaciones':
            if isinstance(correct, bool):
                is_correct = user_answer == correct
            else:
                is_correct = abs(float(user_answer) - float(correct)) < 1e-6
            
            feedback = exercise.get('explanation', '')
        
        elif exercise['type'] == 'teorema_fundamental':
            if isinstance(user_answer, list) and isinstance(correct, list):
                is_correct = sorted(user_answer) == sorted(correct)
                if is_correct:
                    feedback = "¡Excelente! La factorización prima es correcta."
                else:
                    feedback = f"Incorrecto. {exercise['explanation']}"
        
        return {
            'correct': is_correct,
            'feedback': feedback,
            'explanation': exercise.get('explanation', ''),
            'user_answer': user_answer,
            'correct_answer': correct
        }

class NumerosPrimos:
    """Clase para ejercicios de números primos, MCM y MCD"""
    
    def __init__(self):
        self.exercises = {}
    
    def generate_exercise(self, difficulty: int = 1) -> Dict[str, Any]:
        """Genera ejercicios sobre números primos"""
        exercise_types = [
            'identificar_primo',
            'calcular_mcd',
            'calcular_mcm',
            'criterios_divisibilidad'
        ]
        
        exercise_type = random.choice(exercise_types)
        exercise_id = f"np_{random.randint(1000, 9999)}"
        
        if exercise_type == 'identificar_primo':
            return self._generate_identificar_primo(exercise_id, difficulty)
        elif exercise_type == 'calcular_mcd':
            return self._generate_calcular_mcd(exercise_id, difficulty)
        elif exercise_type == 'calcular_mcm':
            return self._generate_calcular_mcm(exercise_id, difficulty)
        else:
            return self._generate_criterios_divisibilidad(exercise_id, difficulty)
    
    def _generate_identificar_primo(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de identificación de números primos"""
        if difficulty == 1:
            number = random.randint(2, 30)
        elif difficulty == 2:
            number = random.randint(31, 100)
        else:
            number = random.randint(101, 300)
        
        exercise = {
            'id': exercise_id,
            'type': 'identificar_primo',
            'question': f'¿Es {number} un número primo? Justifica tu respuesta.',
            'number': number,
            'difficulty': difficulty
        }
        
        is_prime = self._is_prime(number)
        exercise['correct_answer'] = is_prime
        
        if is_prime:
            exercise['explanation'] = f'{number} es primo porque solo es divisible por 1 y por sí mismo.'
        else:
            factors = self._find_factors(number)
            exercise['explanation'] = f'{number} no es primo. Sus factores son: {factors}'
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_calcular_mcd(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de cálculo de MCD"""
        if difficulty == 1:
            a, b = random.randint(6, 30), random.randint(6, 30)
        elif difficulty == 2:
            a, b = random.randint(20, 100), random.randint(20, 100)
        else:
            a, b, c = random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)
            exercise = {
                'id': exercise_id,
                'type': 'calcular_mcd',
                'question': f'Calcula el MCD de {a}, {b} y {c}',
                'numbers': [a, b, c],
                'difficulty': difficulty
            }
            mcd = math.gcd(math.gcd(a, b), c)
            exercise['correct_answer'] = mcd
            exercise['explanation'] = f'MCD({a}, {b}, {c}) = {mcd}'
            self.exercises[exercise_id] = exercise
            return exercise
        
        exercise = {
            'id': exercise_id,
            'type': 'calcular_mcd',
            'question': f'Calcula el MCD de {a} y {b}',
            'numbers': [a, b],
            'difficulty': difficulty
        }
        
        mcd = math.gcd(a, b)
        exercise['correct_answer'] = mcd
        exercise['explanation'] = f'MCD({a}, {b}) = {mcd}'
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_calcular_mcm(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de cálculo de MCM"""
        if difficulty == 1:
            a, b = random.randint(3, 15), random.randint(3, 15)
        elif difficulty == 2:
            a, b = random.randint(10, 50), random.randint(10, 50)
        else:
            a, b, c = random.randint(20, 100), random.randint(20, 100), random.randint(20, 100)
            exercise = {
                'id': exercise_id,
                'type': 'calcular_mcm',
                'question': f'Calcula el MCM de {a}, {b} y {c}',
                'numbers': [a, b, c],
                'difficulty': difficulty
            }
            mcm = abs(a * b * c) // math.gcd(math.gcd(a, b), c)
            exercise['correct_answer'] = mcm
            exercise['explanation'] = f'MCM({a}, {b}, {c}) = {mcm}'
            self.exercises[exercise_id] = exercise
            return exercise
        
        exercise = {
            'id': exercise_id,
            'type': 'calcular_mcm',
            'question': f'Calcula el MCM de {a} y {b}',
            'numbers': [a, b],
            'difficulty': difficulty
        }
        
        mcm = abs(a * b) // math.gcd(a, b)
        exercise['correct_answer'] = mcm
        exercise['explanation'] = f'MCM({a}, {b}) = {mcm}'
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_criterios_divisibilidad(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio sobre criterios de divisibilidad"""
        divisors = [2, 3, 4, 5, 6, 8, 9, 10, 11]
        divisor = random.choice(divisors)
        
        if difficulty == 1:
            number = random.randint(100, 999)
        elif difficulty == 2:
            number = random.randint(1000, 9999)
        else:
            number = random.randint(10000, 99999)
        
        exercise = {
            'id': exercise_id,
            'type': 'criterios_divisibilidad',
            'question': f'¿Es {number} divisible por {divisor}? Aplica el criterio de divisibilidad correspondiente.',
            'number': number,
            'divisor': divisor,
            'difficulty': difficulty
        }
        
        is_divisible = number % divisor == 0
        exercise['correct_answer'] = is_divisible
        exercise['explanation'] = self._get_divisibility_explanation(number, divisor, is_divisible)
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _is_prime(self, n: int) -> bool:
        """Verifica si un número es primo"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def _find_factors(self, n: int) -> List[int]:
        """Encuentra todos los factores de un número"""
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    def _get_divisibility_explanation(self, number: int, divisor: int, is_divisible: bool) -> str:
        """Genera explicación para criterios de divisibilidad"""
        explanations = {
            2: f"Un número es divisible por 2 si termina en cifra par. {number} {'sí' if is_divisible else 'no'} cumple este criterio.",
            3: f"Un número es divisible por 3 si la suma de sus cifras es divisible por 3. Suma de cifras de {number}: {sum(int(d) for d in str(number))}",
            5: f"Un número es divisible por 5 si termina en 0 o 5. {number} {'sí' if is_divisible else 'no'} cumple este criterio.",
            10: f"Un número es divisible por 10 si termina en 0. {number} {'sí' if is_divisible else 'no'} cumple este criterio."
        }
        
        return explanations.get(divisor, f"{number} {'es' if is_divisible else 'no es'} divisible por {divisor}")
    
    def check_answer(self, exercise_id: str, user_answer: Any) -> Dict[str, Any]:
        """Verifica la respuesta del usuario"""
        if exercise_id not in self.exercises:
            return {'error': 'Ejercicio no encontrado'}
        
        exercise = self.exercises[exercise_id]
        correct = exercise['correct_answer']
        
        is_correct = False
        feedback = ""
        
        if exercise['type'] in ['identificar_primo', 'criterios_divisibilidad']:
            is_correct = bool(user_answer) == bool(correct)
        else:  # calcular_mcd, calcular_mcm
            try:
                is_correct = int(user_answer) == int(correct)
            except (ValueError, TypeError):
                is_correct = False
        
        if is_correct:
            feedback = "¡Correcto! " + exercise.get('explanation', '')
        else:
            feedback = "Incorrecto. " + exercise.get('explanation', '')
        
        return {
            'correct': is_correct,
            'feedback': feedback,
            'explanation': exercise.get('explanation', ''),
            'user_answer': user_answer,
            'correct_answer': correct
        }

class Fraccionarios:
    """Clase para ejercicios de números fraccionarios"""
    
    def __init__(self):
        self.exercises = {}
    
    def generate_exercise(self, difficulty: int = 1) -> Dict[str, Any]:
        """Genera ejercicios sobre fracciones"""
        exercise_types = [
            'suma_fracciones',
            'resta_fracciones',
            'multiplicacion_fracciones',
            'division_fracciones',
            'simplificar_fraccion',
            'comparar_fracciones'
        ]
        
        exercise_type = random.choice(exercise_types)
        exercise_id = f"fr_{random.randint(1000, 9999)}"
        
        if exercise_type == 'suma_fracciones':
            return self._generate_suma_fracciones(exercise_id, difficulty)
        elif exercise_type == 'resta_fracciones':
            return self._generate_resta_fracciones(exercise_id, difficulty)
        elif exercise_type == 'multiplicacion_fracciones':
            return self._generate_multiplicacion_fracciones(exercise_id, difficulty)
        elif exercise_type == 'division_fracciones':
            return self._generate_division_fracciones(exercise_id, difficulty)
        elif exercise_type == 'simplificar_fraccion':
            return self._generate_simplificar_fraccion(exercise_id, difficulty)
        else:
            return self._generate_comparar_fracciones(exercise_id, difficulty)
    
    def _generate_suma_fracciones(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de suma de fracciones"""
        if difficulty == 1:
            # Mismo denominador
            den = random.randint(2, 10)
            num1 = random.randint(1, den-1)
            num2 = random.randint(1, den-1)
            frac1 = Fraction(num1, den)
            frac2 = Fraction(num2, den)
        else:
            # Diferentes denominadores
            num1, den1 = random.randint(1, 10), random.randint(2, 12)
            num2, den2 = random.randint(1, 10), random.randint(2, 12)
            frac1 = Fraction(num1, den1)
            frac2 = Fraction(num2, den2)
        
        result = frac1 + frac2
        
        exercise = {
            'id': exercise_id,
            'type': 'suma_fracciones',
            'question': f'Calcula: {frac1} + {frac2}',
            'fractions': [frac1, frac2],
            'difficulty': difficulty,
            'correct_answer': result,
            'explanation': f'{frac1} + {frac2} = {result}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_resta_fracciones(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de resta de fracciones"""
        if difficulty == 1:
            den = random.randint(2, 10)
            num1 = random.randint(2, den)
            num2 = random.randint(1, num1-1)
            frac1 = Fraction(num1, den)
            frac2 = Fraction(num2, den)
        else:
            num1, den1 = random.randint(2, 15), random.randint(2, 12)
            num2, den2 = random.randint(1, 10), random.randint(2, 12)
            frac1 = Fraction(num1, den1)
            frac2 = Fraction(num2, den2)
        
        result = frac1 - frac2
        
        exercise = {
            'id': exercise_id,
            'type': 'resta_fracciones',
            'question': f'Calcula: {frac1} - {frac2}',
            'fractions': [frac1, frac2],
            'difficulty': difficulty,
            'correct_answer': result,
            'explanation': f'{frac1} - {frac2} = {result}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_multiplicacion_fracciones(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de multiplicación de fracciones"""
        num1, den1 = random.randint(1, 8), random.randint(2, 10)
        num2, den2 = random.randint(1, 8), random.randint(2, 10)
        
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        result = frac1 * frac2
        
        exercise = {
            'id': exercise_id,
            'type': 'multiplicacion_fracciones',
            'question': f'Calcula: {frac1} × {frac2}',
            'fractions': [frac1, frac2],
            'difficulty': difficulty,
            'correct_answer': result,
            'explanation': f'{frac1} × {frac2} = {result}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_division_fracciones(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de división de fracciones"""
        num1, den1 = random.randint(1, 10), random.randint(2, 12)
        num2, den2 = random.randint(1, 10), random.randint(2, 12)
        
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        result = frac1 / frac2
        
        exercise = {
            'id': exercise_id,
            'type': 'division_fracciones',
            'question': f'Calcula: {frac1} ÷ {frac2}',
            'fractions': [frac1, frac2],
            'difficulty': difficulty,
            'correct_answer': result,
            'explanation': f'{frac1} ÷ {frac2} = {frac1} × {Fraction(den2, num2)} = {result}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_simplificar_fraccion(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de simplificación de fracciones"""
        if difficulty == 1:
            # Fracciones fáciles de simplificar
            base_num = random.randint(2, 6)
            base_den = random.randint(2, 6)
            multiplier = random.randint(2, 5)
            num = base_num * multiplier
            den = base_den * multiplier
        else:
            # Fracciones más complejas
            num = random.randint(12, 60)
            den = random.randint(12, 60)
        
        original = Fraction(num, den)
        simplified = original  # Fraction se simplifica automáticamente
        
        exercise = {
            'id': exercise_id,
            'type': 'simplificar_fraccion',
            'question': f'Simplifica la fracción: {num}/{den}',
            'original_fraction': f"{num}/{den}",
            'difficulty': difficulty,
            'correct_answer': simplified,
            'explanation': f'{num}/{den} = {simplified}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_comparar_fracciones(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de comparación de fracciones"""
        num1, den1 = random.randint(1, 10), random.randint(2, 12)
        num2, den2 = random.randint(1, 10), random.randint(2, 12)
        
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        
        if frac1 > frac2:
            comparison = ">"
        elif frac1 < frac2:
            comparison = "<"
        else:
            comparison = "="
        
        exercise = {
            'id': exercise_id,
            'type': 'comparar_fracciones',
            'question': f'Compara las fracciones: {frac1} ___ {frac2} (usa >, < o =)',
            'fractions': [frac1, frac2],
            'difficulty': difficulty,
            'correct_answer': comparison,
            'explanation': f'{frac1} {comparison} {frac2}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def check_answer(self, exercise_id: str, user_answer: Any) -> Dict[str, Any]:
        """Verifica la respuesta del usuario"""
        if exercise_id not in self.exercises:
            return {'error': 'Ejercicio no encontrado'}
        
        exercise = self.exercises[exercise_id]
        correct = exercise['correct_answer']
        
        is_correct = False
        feedback = ""
        
        if exercise['type'] == 'comparar_fracciones':
            is_correct = str(user_answer).strip() == str(correct)
        else:
            try:
                if isinstance(user_answer, str) and '/' in user_answer:
                    parts = user_answer.split('/')
                    user_fraction = Fraction(int(parts[0]), int(parts[1]))
                else:
                    user_fraction = Fraction(user_answer)
                
                is_correct = user_fraction == correct
            except (ValueError, TypeError, ZeroDivisionError):
                is_correct = False
        
        if is_correct:
            feedback = "¡Correcto! " + exercise.get('explanation', '')
        else:
            feedback = "Incorrecto. " + exercise.get('explanation', '')
        
        return {
            'correct': is_correct,
            'feedback': feedback,
            'explanation': exercise.get('explanation', ''),
            'user_answer': user_answer,
            'correct_answer': str(correct)
        }

class PotenciacionRadicacion:
    """Clase para ejercicios de potenciación y radicación"""
    
    def __init__(self):
        self.exercises = {}
    
    def generate_exercise(self, difficulty: int = 1) -> Dict[str, Any]:
        """Genera ejercicios sobre potenciación y radicación"""
        exercise_types = [
            'calcular_potencia',
            'leyes_exponentes',
            'calcular_raiz',
            'simplificar_radicales',
            'operaciones_radicales'
        ]
        
        exercise_type = random.choice(exercise_types)
        exercise_id = f"pr_{random.randint(1000, 9999)}"
        
        if exercise_type == 'calcular_potencia':
            return self._generate_calcular_potencia(exercise_id, difficulty)
        elif exercise_type == 'leyes_exponentes':
            return self._generate_leyes_exponentes(exercise_id, difficulty)
        elif exercise_type == 'calcular_raiz':
            return self._generate_calcular_raiz(exercise_id, difficulty)
        elif exercise_type == 'simplificar_radicales':
            return self._generate_simplificar_radicales(exercise_id, difficulty)
        else:
            return self._generate_operaciones_radicales(exercise_id, difficulty)
    
    def _generate_calcular_potencia(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de cálculo de potencias"""
        if difficulty == 1:
            base = random.randint(2, 10)
            exp = random.randint(2, 4)
        elif difficulty == 2:
            base = random.randint(2, 15)
            exp = random.randint(2, 6)
        else:
            base = random.randint(2, 20)
            exp = random.randint(3, 8)
        
        result = base ** exp
        
        exercise = {
            'id': exercise_id,
            'type': 'calcular_potencia',
            'question': f'Calcula: {base}^{exp}',
            'base': base,
            'exponent': exp,
            'difficulty': difficulty,
            'correct_answer': result,
            'explanation': f'{base}^{exp} = {result}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_leyes_exponentes(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio sobre leyes de exponentes"""
        laws = ['product', 'quotient', 'power', 'negative']
        law = random.choice(laws)
        
        base = random.randint(2, 8)
        exp1 = random.randint(2, 6)
        exp2 = random.randint(2, 6)
        
        exercise = {
            'id': exercise_id,
            'type': 'leyes_exponentes',
            'law': law,
            'difficulty': difficulty
        }
        
        if law == 'product':
            exercise['question'] = f'Simplifica: {base}^{exp1} × {base}^{exp2}'
            exercise['correct_answer'] = f'{base}^{exp1 + exp2}'
            exercise['explanation'] = f'{base}^{exp1} × {base}^{exp2} = {base}^{exp1}+{exp2} = {base}^{exp1 + exp2}'
        
        elif law == 'quotient':
            if exp1 <= exp2:
                exp1, exp2 = exp2, exp1  # Asegurar que exp1 > exp2
            exercise['question'] = f'Simplifica: {base}^{exp1} ÷ {base}^{exp2}'
            exercise['correct_answer'] = f'{base}^{exp1 - exp2}'
            exercise['explanation'] = f'{base}^{exp1} ÷ {base}^{exp2} = {base}^{exp1}-{exp2} = {base}^{exp1 - exp2}'
        
        elif law == 'power':
            exercise['question'] = f'Simplifica: ({base}^{exp1})^{exp2}'
            exercise['correct_answer'] = f'{base}^{exp1 * exp2}'
            exercise['explanation'] = f'({base}^{exp1})^{exp2} = {base}^{exp1}×{exp2} = {base}^{exp1 * exp2}'
        
        else:  # negative
            exercise['question'] = f'Simplifica: {base}^(-{exp1})'
            exercise['correct_answer'] = f'1/{base}^{exp1}'
            exercise['explanation'] = f'{base}^(-{exp1}) = 1/{base}^{exp1}'
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_calcular_raiz(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de cálculo de raíces"""
        if difficulty == 1:
            # Raíces cuadradas perfectas
            perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
            number = random.choice(perfect_squares)
            index = 2
        elif difficulty == 2:
            # Raíces cúbicas perfectas
            perfect_cubes = [8, 27, 64, 125, 216]
            number = random.choice(perfect_cubes)
            index = 3
        else:
            # Raíces más complejas
            bases = [2, 3, 4, 5, 6]
            base = random.choice(bases)
            index = random.randint(2, 4)
            number = base ** index
        
        result = number ** (1/index)
        
        if index == 2:
            question = f'Calcula: √{number}'
        elif index == 3:
            question = f'Calcula: ∛{number}'
        else:
            question = f'Calcula: {number}^(1/{index})'
        
        exercise = {
            'id': exercise_id,
            'type': 'calcular_raiz',
            'question': question,
            'number': number,
            'index': index,
            'difficulty': difficulty,
            'correct_answer': int(result) if result.is_integer() else result,
            'explanation': f'La raíz {index}-ésima de {number} es {int(result) if result.is_integer() else result}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_simplificar_radicales(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de simplificación de radicales"""
        if difficulty == 1:
            # Radicales simples
            factors = [2, 3, 5]
            factor = random.choice(factors)
            perfect_square = random.choice([4, 9, 16, 25])
            number = factor * perfect_square
        else:
            # Radicales más complejos
            number = random.randint(12, 200)
        
        # Simplificar el radical
        simplified = self._simplify_radical(number)
        
        exercise = {
            'id': exercise_id,
            'type': 'simplificar_radicales',
            'question': f'Simplifica: √{number}',
            'number': number,
            'difficulty': difficulty,
            'correct_answer': simplified,
            'explanation': f'√{number} = {simplified}'
        }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _generate_operaciones_radicales(self, exercise_id: str, difficulty: int) -> Dict[str, Any]:
        """Genera ejercicio de operaciones con radicales"""
        operations = ['suma', 'multiplicacion']
        operation = random.choice(operations)
        
        if operation == 'suma':
            # Radicales semejantes
            factor = random.randint(2, 8)
            coef1 = random.randint(2, 6)
            coef2 = random.randint(2, 6)
            
            exercise = {
                'id': exercise_id,
                'type': 'operaciones_radicales',
                'question': f'Calcula: {coef1}√{factor} + {coef2}√{factor}',
                'operation': 'suma',
                'difficulty': difficulty,
                'correct_answer': f'{coef1 + coef2}√{factor}',
                'explanation': f'{coef1}√{factor} + {coef2}√{factor} = ({coef1} + {coef2})√{factor} = {coef1 + coef2}√{factor}'
            }
        
        else:  # multiplicacion
            num1 = random.randint(2, 12)
            num2 = random.randint(2, 12)
            
            exercise = {
                'id': exercise_id,
                'type': 'operaciones_radicales',
                'question': f'Calcula: √{num1} × √{num2}',
                'operation': 'multiplicacion',
                'difficulty': difficulty,
                'correct_answer': f'√{num1 * num2}',
                'explanation': f'√{num1} × √{num2} = √({num1} × {num2}) = √{num1 * num2}'
            }
        
        self.exercises[exercise_id] = exercise
        return exercise
    
    def _simplify_radical(self, n: int) -> str:
        """Simplifica un radical"""
        if n <= 0:
            return "0"
        
        perfect_square_factor = 1
        remaining = n
        
        i = 2
        while i * i <= remaining:
            while remaining % (i * i) == 0:
                perfect_square_factor *= i
                remaining //= (i * i)
            i += 1
        
        if perfect_square_factor == 1:
            return f"√{n}"
        elif remaining == 1:
            return str(perfect_square_factor)
        else:
            return f"{perfect_square_factor}√{remaining}"
    
    def check_answer(self, exercise_id: str, user_answer: Any) -> Dict[str, Any]:
        """Verifica la respuesta del usuario"""
        if exercise_id not in self.exercises:
            return {'error': 'Ejercicio no encontrado'}
        
        exercise = self.exercises[exercise_id]
        correct = exercise['correct_answer']
        
        is_correct = False
        feedback = ""
        
        try:
            if exercise['type'] in ['leyes_exponentes', 'simplificar_radicales', 'operaciones_radicales']:
                # Comparación de strings para expresiones algebraicas
                is_correct = str(user_answer).replace(' ', '') == str(correct).replace(' ', '')
            else:
                # Comparación numérica
                is_correct = abs(float(user_answer) - float(correct)) < 1e-6
        except (ValueError, TypeError):
            is_correct = False
        
        if is_correct:
            feedback = "¡Correcto! " + exercise.get('explanation', '')
        else:
            feedback = "Incorrecto. " + exercise.get('explanation', '')
        
        return {
            'correct': is_correct,
            'feedback': feedback,
            'explanation': exercise.get('explanation', ''),
            'user_answer': user_answer,
            'correct_answer': correct
        }

# Función principal para testing
if __name__ == "__main__":
    engine = MathEngine()
    
    # Generar ejercicios de prueba
    print("=== EJERCICIOS DE PRUEBA ===\n")
    
    topics = ['conjuntos_numericos', 'numeros_primos', 'fraccionarios', 'potenciacion_radicacion']
    
    for topic in topics:
        print(f"--- {topic.upper().replace('_', ' ')} ---")
        exercise = engine.generate_exercise(topic, difficulty=1)
        print(f"Pregunta: {exercise['question']}")
        print(f"Respuesta: {exercise['correct_answer']}")
        print(f"Explicación: {exercise.get('explanation', 'N/A')}")
        print()
