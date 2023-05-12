from scraper import Scraper
from flask import Flask, render_template, request
from store import Store
import jsonpickle

app = Flask(__name__, template_folder="templates")

app_store = Store()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/extract', methods=['GET'])
def _product():
    product_id = request.args.get('product_id')
    if product_id is None:
        return render_template('extract.html')
    try:
        scrap = Scraper(product_id)
        app_store.add_product(product_id, scrap.get_product_name(), scrap.get_all_opinions())
        app_store.set_stats(product_id, Store.calculate_stats(scrap.get_all_opinions()))

        with open(file=f'./static/{product_id}.json', mode='w') as f:
            jsonpickle.set_encoder_options('json', indent=2)
            f.write(jsonpickle.encode(scrap.get_all_opinions()))

        return render_template('product.html', reviews=scrap.get_all_opinions(),
                               product_id=product_id, json=jsonpickle.encode(scrap.get_all_opinions()),
                               reviews_number=len(scrap.get_all_opinions()))
    except Exception as e:
        print("Error: ", e)
        return render_template('extract.html', error=str(e))


@app.route(rule='/product', methods=['GET'])
def opinion():
    return render_template('product.html', error="Wrong product ID!")


@app.route(rule='/details/<product_id>', methods=['GET'])
def details(product_id):
    reviews = app_store.get_product_opinions(product_id)
    return render_template('details.html', id=product_id, product_data=app_store.calculate_recommendations(reviews),
                           rating=app_store.calculate_ratings(reviews), product_name=app_store.get_product_name(product_id))


@app.route(rule='/all_products', methods=['GET'])
def product_list():
    return render_template('all_products.html', products=app_store.get_all_products())


if __name__ == '__main__':
    app.run(debug=True)
