from cupom import desconto_valido

LIMITE = 26  # meu LIMITE = 20 + 6


def test_t1_percentual_igual_ao_limite_e_aceito():
    # preparar
    percentual = LIMITE
    # agir
    resultado = desconto_valido(percentual)
    # verificar
    assert resultado is True


def test_t2_percentual_acima_do_limite_e_rejeitado():
    # preparar
    percentual = LIMITE + 1
    # agir
    resultado = desconto_valido(percentual)
    # verificar
    assert resultado is False


def test_t3_percentual_zero_e_rejeitado():
    # preparar
    percentual = 0
    # agir
    resultado = desconto_valido(percentual)
    # verificar
    assert resultado is False


def test_t4_percentual_com_virgula_e_rejeitado():
    # preparar
    percentual = LIMITE - 0.5
    # agir
    resultado = desconto_valido(percentual)
    # verificar
    assert resultado is False
