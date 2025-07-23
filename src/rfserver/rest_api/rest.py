from flask import Flask, jsonify, request
from rfserver.db.database import DetailDataBaseManager

# create a Flask app
app = Flask(__name__)

@app.route('/search/<float:min_power>/<float:max_power>/<float:min_frequency>/<float:max_frequency>',methods=['GET'])
def search(min_power,max_power,min_frequency,max_frequency):
    result = DetailDataBaseManager.search_power_frequency(min_power, max_power, min_frequency, max_frequency)
    return result

#@app.route('/search', methods=['POST'])
#def search():
#  query = request.get_json()
#  return query
#

if __name__ == '__main__':
    app.run(debug=True)
# testing :
# $ curl -X POST  http://127.0.0.1:5000/search -H 'Content-Type: application/json' -d '{"freq":"[34.55,5.55]","power":"[123.33,23.33]"}'