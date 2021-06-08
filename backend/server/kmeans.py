import random

from .models import User, Rating, Cluster, Product

global UPDATE_STEP;
UPDATE_STEP = 6

class KMeansClustering:
    """
    This class computes kmeans clustering and is able to show products within user cluster
    with similar product preferences.

    Public Functions
    ----------------
    is_products_available(): Returns true if products are available through
    kmeans, also assigns the recommended products if available. Only returns if 
    true if there are 4 or more products available to recommend.

    update_clusters(): Updates the kmeans cluster depending upon the update
    step. 

    Public Attributes
    -----------------
    recommended_products: the recommended product objects are set over
    this variable by the kmeans clustering.

    is_new_user: to specify if clusters are being created for a new or
    old user. Is already false by default. 
    """
    def __init__(self, user):
        """
        Parameters
        ----------
        user: user object to find kmeans clustering for.
        """
        self.user = user
        self.rated_product_ids = set()
        self.recommended_products = []
        self.is_new_user = False

    def is_products_available(self):
        """
        Checks if products recommendation trying to
        get recommended products

        Parameters
        ----------
        None

        Returns
        -------
        boolean
            True or False
        """
        self.get_recommended_products()
        if (len(self.recommended_products) >= 4):
            return True
        return False

    def get_recommended_products(self):
        """
        Sets recommended products by kmeans clustering
        IF AVAILABLE

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        self.get_rated_products()
        
        user_cluster_name = self.get_user_cluster()

        other_users_rated_products_ids = \
            self.get_other_users_rated_products( \
                user_cluster_name
        )

        # If more than 4 products, just get first four
        to_recommend_products = Product.objects.filter( \
            id__in=other_users_rated_products_ids
        )
        if len(to_recommend_products) > 4:
            to_recommend_products = to_recommend_products[:4]
            random.shuffle(to_recommend_products)

        # get a product list including the previous IDs
        self.recommended_products = to_recommend_products      
    
    def get_rated_products(self):
        """
        Sets rated products by user  

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        rated_products = Rating.objects.filter(user=self.user) \
            .prefetch_related('product')
        self.rated_product_ids = set(map(lambda rating: rating.product.id, \
             rated_products))

    def get_user_cluster(self):
        """
        Gets user's first cluster; 
            - if user is new, include him/her in the clusters
            by updating clusters  

        Parameters
        ----------
        None

        Returns
        -------
        cluster.name
            cluster_name
        """
        user_cluster_name = ''
        try:
            user_cluster_name = User.objects.get( \
                username=self.user.username,
            ).cluster_set.first().name
        except:
            self.is_new_user = True
            self.update_clusters()
            user_cluster_name = User.objects.get( \
                username=self.user.username,
            ).cluster_set.first().name
        return user_cluster_name

    def get_other_users_rated_products(\
        self, user_cluster_name):
        """
        Gets other user's rated products "IDs";

        Parameters
        ----------
        user_cluster_name
            the cluster used to get the ids. 

        Returns
        -------
        set
            set of the ids.
        """
        other_users_clusters = \
            Cluster.objects.get(name=user_cluster_name).users \
                .exclude(username=self.user.username).all()
        other_members_user_objects = set(map( \
            lambda user: user, other_users_clusters
        ))

        # get ratings by those users, excluding product rated by the request user
        other_users_ratings = \
            Rating.objects.filter(user__in=other_members_user_objects) \
                .exclude(product__id__in=self.rated_product_ids)
        other_users_rated_product_ids = set(map(
            lambda rating: rating.product.id, other_users_ratings
        ))

        return other_users_rated_product_ids

    def update_clusters(self):
        """
        Updates Clusters by Kmeans clustering if eligible to update

        Parameters
        ----------
        None 

        Returns
        -------
        Nothing
        """
        num_ratings = Rating.objects.count()
        
        if self.eligible_to_update(num_ratings):
            ratings_matrix, num_users, all_user_names = \
                self.construct_ratings_matrix()

            k_clusters = int(num_users / 10) + 2  # "Magical numbers that 
            # work the best"
            from sklearn.cluster import KMeans
            kmeans = KMeans(n_clusters=k_clusters)
            clusters = kmeans.fit(ratings_matrix.tocsr())  # Read sklearn
            # docs to read why tocsr() used. THE MAIN KMEANS CLUSTERING

            # Updating the clusters
            Cluster.objects.all().delete()
            new_clusters = {i: Cluster(name=i) for i in range(k_clusters)}
            for cluster in new_clusters.values():
                cluster.save()
            for i, cluster_label in enumerate(clusters.labels_):
                # Add the new users to clusters
                new_clusters[cluster_label].users.add(
                    User.objects.get(username=all_user_names[i])
                )
    
    def eligible_to_update(self, num_ratings):
        """
        Is eligible to update if 
            - new user
            - number of ratings is divisible by 
            our updating steps UPDATE_STEP
            i.e. multiple of UPDATE_STEP

        Parameters
        ----------
        num_ratings
            total number of ratings available

        Returns
        -------
        boolean
            True or False
        """
        return num_ratings % UPDATE_STEP == 0 \
            or self.is_new_user

    def construct_ratings_matrix(self):
        """
        Constructs Ratings Matrix;

        Ratings Matrix is a matrix with:
            - row as each user
            - column as products rated by that user
            - rating value as the values 

        Example:
                PRODUCT1    PRODUCT2    PRODUCT3
        USER1   ( _         _                   )
        USER2   ( _                     _       )
        USER3   ( _         _           _       )

        Parameters
        ----------
        None

        Returns
        -------
        rating_matrix
            :data_type: dok_matrix (a sparse matrix type
            in scipy)
            :height: number of total users in our database
            :width: number of products till maximum rated product id
            (i.e., if 24, 12, 57 rated; max_rated_product_id = 57,
            57 products in this case) + 1
        num_users
            total numbers of users in database [Returned so that it can
            help the callee function]
        all_user_names
            total numbers of users in database [Returned so that it can
            help the callee function]
        """
        all_user_names = list(map(
            lambda user: user.username, User.objects.only("username")
        ))
        all_rated_product_ids = list(map(
            lambda rating: rating.product.id, Rating.objects.only("product")
        ))
        num_users = len(all_user_names)

        # Create a new dok matrix with shape (len(all_user_names),
        # len(max_rated_product_id)) + 1 [See docstring for more details]
        from scipy.sparse import dok_matrix
        import numpy as np
        ratings_matrix = dok_matrix(
            (num_users, max(all_rated_product_ids) + 1),
            dtype=np.float32
        )

        # Fill rating matrix with values
        for i in range(num_users):
            user = User.objects.get(username=all_user_names[i])
            user_ratings = Rating.objects.filter(user=user)
            for user_rating in user_ratings:
                ratings_matrix[i, user_rating.product.id] = \
                    user_rating.rating_value 
        
        return ratings_matrix, num_users, all_user_names
