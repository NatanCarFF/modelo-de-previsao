# Modelo de Previsão Simples

Este é um modelo de previsão simples criado com Python, Flask e scikit-learn.

## Como cheguei a essa etapa?

1. Criei um novo repositório no GitHub.
2. Implementei um modelo de previsão em Python.
3. Configurei um ponto de extremidade usando Flask para prever valores.
4. Escrevi um `readme.md` para documentar o processo.

## Configuração do Ponto de Extremidade

- **POST /predict:** Endpoint para receber os dados de entrada e retornar a previsão.

### Exemplo de Uso

```bash
curl -X POST -H "Content-Type: application/json" -d '{"input": 3}' http://localhost:5000/predict
