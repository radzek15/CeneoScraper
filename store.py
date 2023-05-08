from statistics import mean


class Store:
    def __init__(self):
        self.store = {}

    def add_product(self, p_id, name, opinions):
        self.store[p_id] = {"ID": p_id, "name": name, "opinions": opinions, 'stats': {}}

    def get_product(self, p_id):
        return self.store[p_id]

    def get_product_name(self, p_id):
        return self.store[p_id]["name"]

    def get_all_products(self):
        return [i for i in self.store.values()]

    def get_all_opinions(self):
        return [i['opinions'] for i in self.store.values()]

    def get_product_opinions(self, p_id):
        return self.store[p_id]["opinions"]

    def set_stats(self, p_id, stats):
        self.store[p_id]["stats"] = stats

    def get_stats(self, p_id):
        return self.store[p_id]["stats"]

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
                 'pros_number': [review['pros'] for review in reviews],
                 'cons_number': [review['cons'] for review in reviews],
                 'mean': round(sum(float(review['score'].split('/')[0].replace(',', '.')) for review in reviews) / len(reviews), 2)
                 }
        return stats
