from scraper import Scraper
from flask import Flask, render_template, request
from store import Store
import jsonpickle

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/extract', methods=['GET'])
def _product():
    p_id = request.args.get('product_id')
    if p_id is None:
        return render_template('extract.html')
    try:
        scrap = Scraper(p_id)
        Store().add_product(p_id, scrap.get_product_name(), scrap.get_all_opinions())
        Store().set_stats(p_id, Store.calculate_stats(scrap.get_all_opinions()))

        with open(file=f'./static/{p_id}.json', mode='w') as f:
            jsonpickle.set_encoder_options('json', indent=2)
            f.write(jsonpickle.encode(scrap.get_all_opinions()))

        return render_template('product.html', reviews=scrap.get_all_opinions(),
                               p_id=p_id, json=jsonpickle.encode(scrap.get_all_opinions()),
                               reviews_number=len(scrap.get_all_opinions()))
    except Exception as e:
        print("Error: ", e)
        return render_template('extract.html', error=str(e))

@app.route(rule='/product', methods=['GET'])
def opinion():
    return render_template('product.html', error="Wrong product ID!")

@app.route(rule='/all_products', methods=['GET'])
def product_list():
    return render_template('all_products.html', products=Store().get_all_products())

if __name__ == '__main__':
    app.run(debug=True)
