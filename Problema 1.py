def clasificar_compromiso(duracion_seg: int, num_clics: int) -> str:
    """
    Calcula el nivel de compromiso de una sesión según su duración (en segundos)
    y el número de clics realizados.
    """
    if duracion_seg > 180 and num_clics > 8:
        return "Alto"
    elif duracion_seg < 60 or num_clics < 3:
        return "Bajo"
    else:
        return "Medio"


def generar_informe_compromiso(sesiones: list[list]) -> None:
    """
    Imprime un informe con el ID del cliente y su clasificación final de compromiso.
    """
    print("=== INFORME DE NIVEL DE COMPROMISO POR SESIÓN ===")
    print(f"{'ID Cliente':<15} | {'Clasificación':<15}")
    print("-" * 33)

    for sesion in sesiones:
        id_cliente, duracion_seg, num_clics = sesion
        clasificacion = clasificar_compromiso(duracion_seg, num_clics)
        print(f"{str(id_cliente):<15} | {clasificacion:<15}")


def main() -> None:
    # Matriz inicial: [ID del Cliente, Duración en segundos, Número de clics]
    matriz_sesiones = [
        ["CLI-001", 240, 12],  # Alto (>180s y >8 clics)
        ["CLI-002", 45, 6],     # Bajo (<60s)
        ["CLI-003", 150, 2],    # Bajo (<3 clics)
        ["CLI-004", 120, 5],    # Medio
        ["CLI-005", 180, 9],    # Medio (duración no es > 180)
        ["CLI-006", 310, 10],   # Alto
    ]

    generar_informe_compromiso(matriz_sesiones)


if __name__ == "__main__":
    main()
