class Store:
    def __init__(self):
        self.store = {}

    def add_product(self, product_id, name, opinions):
        self.store[product_id] = {"ID": product_id, "name": name, "opinions": opinions, 'stats': {}}

    def get_product(self, product_id):
        return self.store[product_id]

    def get_product_name(self, product_id):
        return self.store[product_id]["name"]

    def get_all_products(self):
        return [i for i in self.store.values()]

    def get_all_opinions(self):
        return [i['opinions'] for i in self.store.values()]

    def get_product_opinions(self, product_id):
        return self.store[product_id]["opinions"]

    def set_stats(self, product_id, stats):
        self.store[product_id]["stats"] = stats

    def get_stats(self, product_id):
        return self.store[product_id]["stats"]

# static methods
    @staticmethod
    def calculate_recommendations(reviews):
        return {'positive': sum([1 for i in reviews if i['recommendation'] == 'Polecam']),
                'negative': sum([1 for i in reviews if i['recommendation'] == 'Nie polecam'])}

    @staticmethod
    def calculate_ratings(reviews):
        scores = {'0,5': 0, '1': 0, '1,5': 0, '2': 0, '2,5': 0, '3': 0, '3,5': 0, '4': 0, '4,5': 0, '5': 0}
        for review in reviews:
            scores[review['score'].split('/')[0]] += 1
        return scores

    @staticmethod
    def calculate_stats(reviews):
        stats = {'opinion_number': len(reviews),
                 'pros': [review['pros'] for review in reviews],
                 'cons': [review['cons'] for review in reviews],
                 'mean': round(sum(float(review['score'].split('/')[0].replace(',', '.')) for review in reviews) / len(reviews), 2)
                 }
        return stats
