from flask import Flask, request

from raizen.services.open_weather import OpenWeatherService
from raizen.database.models import Account, Weather

app = Flask(__name__)

@app.route("/health", methods=['GET'])
def get_health():
    return {"msg": "ok"}

@app.route("/free/<city>", methods=['GET'], endpoint='get_weather_free')
def get_weather_free(city: str):
    service = OpenWeatherService()
    return service.get_weather(city)


@app.route("/account",methods = ['POST'])
def create_account():
    data = request.get_json()

    account = Account()

    id = account.create(data['nome'], data['email'])

    return id

@app.route("/account/user/<email>",methods = ['GET'])
def get_account(email):

    print(email)
    account = Account()

    return str(account.get_account(email))



@app.route("/weather/<city>/<account_id>", methods=['GET'], endpoint='get_weather_account')
def get_weather_account(city: str, account_id: str):
    forecast = OpenWeatherService()

    weather = Weather()
    weather.create(
        city,
        forecast.get_weather(city),
        account_id
    )

    return forecast.get_weather(city)

@app.route("/history/<account_id>",methods = ['GET'])
def get_history(account_id: str):
    weather = Weather()
    return str(weather.get_history(account_id))

if __name__ == "__main__":
    app.run(debug=True)