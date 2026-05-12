# test_calculadora.py — Suite de pruebas unitarias
import pytest
from calculadora import (
    calcular_interes_simple,
    calcular_cuota_mensual,
    aplicar_descuento,
    clasificar_cliente
)


# ─── PRUEBAS: calcular_interes_simple ─────────────────

class TestInteresSimple:

    def test_calculo_correcto(self):
        """1.000.000 al 5% por 3 años = 150.000 de interés"""
        resultado = calcular_interes_simple(1_000_000, 0.05, 3)
        assert resultado == 150_000.0

    def test_un_año(self):
        resultado = calcular_interes_simple(500_000, 0.10, 1)
        assert resultado == 50_000.0

    def test_principal_negativo_lanza_error(self):
        """Debe rechazar principal negativo"""
        with pytest.raises(ValueError, match="principal"):
            calcular_interes_simple(-100, 0.05, 1)

    def test_tasa_mayor_a_uno_lanza_error(self):
        with pytest.raises(ValueError, match="tasa"):
            calcular_interes_simple(1000, 1.5, 1)


# ─── PRUEBAS: calcular_cuota_mensual ──────────────────

class TestCuotaMensual:

    def test_prestamo_sin_interes(self):
        """Con tasa 0, la cuota es simplemente principal / meses"""
        resultado = calcular_cuota_mensual(1_200_000, 0, 12)
        assert resultado == 100_000.0

    def test_cuota_con_interes(self):
        """Préstamo de 1M al 12% anual a 12 meses → ~88.849"""
        resultado = calcular_cuota_mensual(1_000_000, 0.12, 12)
        assert 88_000 < resultado < 89_000  # rango esperado

    def test_meses_cero_lanza_error(self):
        with pytest.raises(ValueError):
            calcular_cuota_mensual(1000, 0.1, 0)


# ─── PRUEBAS: aplicar_descuento ───────────────────────

class TestDescuento:

    def test_descuento_20_por_ciento(self):
        resultado = aplicar_descuento(100_000, 20)
        assert resultado == 80_000.0

    def test_descuento_cero(self):
        """Con 0% de descuento, el precio no cambia"""
        resultado = aplicar_descuento(50_000, 0)
        assert resultado == 50_000.0

    def test_descuento_100_por_ciento(self):
        """Descuento total: precio final es 0"""
        resultado = aplicar_descuento(50_000, 100)
        assert resultado == 0.0

    def test_descuento_invalido_lanza_error(self):
        with pytest.raises(ValueError, match="porcentaje"):
            aplicar_descuento(1000, 150)  # 150% no es válido


# ─── PRUEBAS: clasificar_cliente ──────────────────────

class TestClasificarCliente:

    def test_cliente_premium_por_saldo(self):
        resultado = clasificar_cliente(50_000, 0)
        assert resultado == "PREMIUM"

    def test_cliente_premium_por_antiguedad(self):
        resultado = clasificar_cliente(100, 5)
        assert resultado == "PREMIUM"

    def test_cliente_regular(self):
        resultado = clasificar_cliente(1_000, 2)
        assert resultado == "REGULAR"

    def test_cliente_nuevo(self):
        resultado = clasificar_cliente(500, 0)
        assert resultado == "NUEVO"