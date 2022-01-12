from exercises.main import calculadora


def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculadora,"multiplicacion", lambda x:4)
    c = calculadora
    assert c.multiplicacion(2,2)== 4
    
