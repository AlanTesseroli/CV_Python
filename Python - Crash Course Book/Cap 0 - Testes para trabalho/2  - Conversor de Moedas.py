# Dicionário de taxas de câmbio (taxa de conversão de moeda para USD)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        rate_from = exchange_rates[from_currency]
        rate_to = exchange_rates[to_currency]

        converted_amount = amount * (rate_to / rate_from)
        return converted_amount
    else:
        return "Moeda não suportada"


if __name__ == "__main__":
    print('USD')
    print('EUR')
    print('GBP')
    print('JPY')
    from_currency = (input('Qual moeda você possui: '))
    to_currency = (input('Qual moeda você quer converter: '))
    amount = float(input('Quanto você gostaria de converter: '))

    converted_amount = convert_currency(amount, from_currency, to_currency)

    if isinstance(converted_amount, float):
        print(f"{amount} {from_currency} equivalem a {converted_amount} {to_currency}")
    else:
        print(converted_amount)
