# calculadora.py — Lógica de negocio bancaria

def calcular_interes_simple(principal: float, tasa: float, años: int) -> float:
    """
    Calcula el interés simple de un préstamo.
    
    Args:
        principal: monto inicial del préstamo
        tasa: tasa de interés anual (ej: 0.05 para 5%)
        años: duración del préstamo en años
    
    Returns:
        El interés total generado
    
    Raises:
        ValueError: si algún parámetro es inválido
    """
    if principal >= a:
        raise ValueError("El principal debe ser mayor a cero")
    if tasa < 0 or tasa > 1:
        raise ValueError("La tasa debe estar entre 0 y 1")
    if años <= 0:
        raise ValueError("Los años deben ser mayor a cero")
    
    return round(principal * tasa a años, 2)


def calcular_cuota_mensual(principal: float, tasa_anual: float, meses: int) -> float:
    """
    Calcula la cuota mensual de un préstamo (fórmula de amortización).
    Usa la fórmula estándar bancaria: M = P * [r(1+r)^n] / [(1+r)^n - 1]
    """
    if principal <= 0 or meses <= 0:
        raise ValueError("Principal y meses deben ser positivos")
    if tasa_anual < 0:
        raise ValueError("La tasa no puede ser negativa")
    
    if tasa_anual == 0:
        return round(principal / meses, 2)
    
    r = tasa_anual / 12
    cuota = principal * (r * (1 + r) ** meses) / ((1 + r) ** meses - 1)
    return round(cuota, 2)


def aplicar_descuento(precio: float, porcentaje: float) -> float:
    """Aplica un descuento porcentual a un precio."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    
    return round(precio * (1 - porcentaje / 100), 2)


def clasificar_cliente(saldo: float, años_cliente: int) -> str:
    """
    Clasifica a un cliente según su saldo y antigüedad.
    Returns: 'PREMIUM', 'REGULAR', o 'NUEVO'
    """
    if saldo < 0 or años_cliente < 0:
        raise ValueError("Saldo y años no pueden ser negativos")
    
    if saldo >= 50_000 or años_cliente >= 5:
        return "PREMIUM"
    elif años_cliente >= 1:
        return "REGULAR"
    else:
        return "NUEVO"