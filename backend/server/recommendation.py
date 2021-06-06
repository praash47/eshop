from django.contrib.auth.models import User
from .models import User

from .kmeans import KMeansClustering
from .preferencebased import PreferenceRecommendation

class Recommendation:
    def __init__(self, username, wishlist=None):
        self.user = User.objects.get(username=username)
        self.user_wishlist = wishlist
        self.recommended_products = []
    
    def recommend(self):
        """
        Recommends product based on product
        recommnedation availability through kmeans if
        kmeans products are available and views & 
        wishlist based recommenation.

        Parameters
        ----------
        None

        Returns
        -------
        list of product objects
            recommended_products
        """
        # kmeans = KMeansClustering(self.user)
        # if (kmeans.is_products_available()):
        #     self.recommended_products = \
        #         kmeans.recommended_products
        # else:
        preferencebased = \
            PreferenceRecommendation( \
                self.user,
                self.user_wishlist
            )
        preferencebased.recommend_products()
        self.recommended_products = \
            preferencebased \
                .recommended_products

        return self.recommended_products
