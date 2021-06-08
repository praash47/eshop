from django.contrib.auth.models import User
from .models import User

from .kmeans import KMeansClustering
from .preferencebased import PreferenceRecommendation

class Recommendation:
    """
    Recommends products based on:
        - k means clustering: for similar behaviour and finding similar
        users among the users who have rated.
        - Preference based Recommendation: Such that, on the basis of
        number of views of a particular subcategory and wishlists added
        by the user.

    Public Function
    ---------------
    recommend(): returns the recommended products i.e. list of recommended
    product objects. Recommends by kmeans if the kmeans clustering is able
    to create 4 or more product recommendations on the basis of other user.
    - If not able to create, simply applies preference based recommendation.  
    """
    def __init__(self, username, wishlist=None):
        """
        Parameters:
        -----------
        username: username to create recommendation for.
        wishlist: default: None, if wishlist available, then
        send it for preference based recommendation.
        """
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
        kmeans = KMeansClustering(self.user)
        if (kmeans.is_products_available()):
            self.recommended_products = \
                kmeans.recommended_products
        else:
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
