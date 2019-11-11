"""Contains implementation of BlumMicaliGenerator class"""


class BlumMicaliGenerator:
    """Blum-Micali pseudo random bit sequence generator"""
    a: int
    p: int
    root: int
    x_prev: int

    def __init__(self, base: int, modulus: int, root: int):
        self.a = base
        self.p = modulus
        self.root = root
        self.x_prev = self.root
        pass

    def __del__(self):
        pass

    @staticmethod
    def _modular_pow(base, exponent, modulus):
        """
        Source: https://math.stackexchange.com/questions/195634/how-do-you-calculate-the-modulo-of-a-high-raised-number
        Modular Power (based on pseudo code).
        """
        result: int = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent >>= 1
            base = (base ** 2) % modulus
        return result

    def generate_random_number(self, bit_length: int) -> str:
        """
        Generates random sequence of bits

        :param bit_length: Number of bits to be generated
        :return: Random bit sequence
        """
        bin_number: str = ""
        j: int = 0
        while j < bit_length:
            x_i: int = BlumMicaliGenerator._modular_pow(self.a, self.x_prev, self.p)
            if x_i < (self.p - 1) / 2:
                bin_number += "1"
            else:
                bin_number += "0"
            self.x_prev = x_i
            j += 1
        return bin_number
