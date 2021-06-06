import json
import random

from .models import UserViews, Product

class PreferenceRecommendation:
    """
    This class is used for preference based recommendation which specifically
    meaning that recommendations will be made on the basis of wishlist and
    number of views. It consists of many major conditions though not all
    conditions and situations of different number of wishlists and number
    of subcategories viewed.

    Public Function
    ---------------
    recommend(): computes the recommendations product objects on the basis
    of views and wishlist

    Public Attribute
    ---------------
    self.recommended_products: can be found set with product recommendations
    after calling the self.recommend() method. Consists of product objects.
    """
    def __init__(self, user, wishlist):
        """
        Parameters
        ----------
        user - user object to compute preference based recommendation of
        wishlist - wishlist of the user
        """
        self.user = user
        self.wishlist = wishlist
        self.viewed_subcategories = []
        self.recommended_products = []
        self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY = 2

    def recommend_products(self):
        """
        Recommends product based on views and
        wishlist. Recommends 4 products:
            - From views solely, if no wishlist
            - if wishlist, hybrid from wishlist and views
        Summary: Set self.recommended_products

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        if self.wishlist:
            self.recommend_by_hybrid_with_wishlist()
        else:
            self.recommend_by_views()

    def recommend_by_hybrid_with_wishlist(self):
        """
        Recommends products as such
            - 1 product randomly selected
            from user's most viewed subcategory
            and 1 from secondmost viewed.
                - if no 2 subcategories, just one
                subcategory viewed; then, recommend
                2 from that one and rest from wishlist.
            - if wishlist has 1 subcategory products
                - select 2 random products from the
                subcategory
            - if 2 subcategory products
                - select 1-1 random product from each
                subcategory
            - if >2 subcategory products
                - select 2 random subcategories from
                'n' number of subcategories and select
                1-1 random product from each subcategory
        
        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        num_subcategories = self.parse_subcategories()
        if (num_subcategories == 1):
            self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY = 2
            self.recommend_only_one_subcategory_present_from_id(
                self.viewed_subcategories[0]['subcategory']
            )
            self.recommend_remaining_from_wishlist()
        else:
            self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY = 1
            self.recommend_two_most_viewed_subcategories()
            self.recommend_remaining_from_wishlist()
    
    def recommend_remaining_from_wishlist(self):
        """
        Recommends 2 remaining products from wishlist as such
            - if wishlist has 1 subcategory products
                - select 2 random products from the
                subcategory
            - if 2 subcategory products
                - select 1-1 random product from each
                subcategory
            - if >2 subcategory products
                - select 2 random subcategories from
                'n' number of subcategories and select
                1-1 random product from each subcategory
        
        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        num_wishlist = len(self.wishlist)

        if num_wishlist == 1:
            self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY = 2
            self.recommend_only_one_subcategory_present_from_id(
                self.wishlist[0]['sub_category']
            )

        else:
            # Number of wishlist is >=2
            selected_ids = [0, 0]
            if num_wishlist == 2:
                selected_ids[0] = self.wishlist[0]['sub_category']
                selected_ids[1] = self.wishlist[1]['sub_category']
            else:
                selected_ids[0], selected_ids[1] = \
                    self.select_two_random_wishlists()

            self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY = 1
            self.recommend_only_one_subcategory_present_from_id(
                selected_ids[0]
            )

            self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY = 1
            self.recommend_only_one_subcategory_present_from_id(
                selected_ids[1]
            )

    def select_two_random_wishlists(self):
        """
        Selects and returns id of two wishlist randomly selected from wishlist.
        
        Parameters
        ----------
        None

        Returns
        -------
            tuple (ints)
                random_wishlists: two randomly selected wishlists
        """
        wishlistids = []
        for wish in self.wishlist:
            wishlistids.append(wish['sub_category'])

        random_wishlists = random.sample(
            wishlistids, 
            k=2  # need two samples from available wishlists.
        )

        return tuple(random_wishlists) 


    def recommend_only_one_subcategory_present_from_id(self, id):
        """
        Used if only subcategory is present, recommend that product from id

        WARNING: USES GLOBAL VARIABLE "N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY"
        TO RECOMMEND N number of products from each subcategory

        Recommends N products each from two most viewed subcategories
        Sets recommended products
        
        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        # Get all product ids of that subcategory
        product_ids = list(Product.objects.filter(
            sub_category_id = id
        ).values_list('id', flat=True))
        
        # Collect 1 sample with n products from it
        recomm_product_samples = random.sample(
            product_ids, 
            k=self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY
        )

        # Set recommended products from samples
        self.recommend_products_from_samples(recomm_product_samples, num_product_samples=2)


    def recommend_by_views(self):
        """
        Recommends solely by views 
            - if user has viewed more than 2 subcategory products
                - 2 products randomly selected from user's most 
                subcategory and 2 from secondmost viewed. 
            - else donot set recommended products. [Actually, the
            recommendation will be empty, thus user will be simply
            shown trending products.]
        
        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        num_subcategories = self.parse_subcategories()
        if (num_subcategories >= 2):
            N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY = 2
            self.recommend_two_most_viewed_subcategories()

    def recommend_two_most_viewed_subcategories(self):
        
        """
        WARNING: USES GLOBAL VARIABLE "N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY"
        TO RECOMMEND N number of products from each subcategory

        Recommends N products each from two most viewed subcategories
        Sets recommended products

        Parameters
        ----------
        None

        Returns
        -------
        Nothing
        """
        # Get all product ids of the two most viewed subcategories
        subcategory_product_ids = \
            self.get_products_two_most_viewed_subcategories()
        
        # Collect 2 samples with n products from it
        recomm_product_samples = random.sample(
            subcategory_product_ids[0], 
            k=self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY
        )
        recomm_product_samples += (random.sample(
            subcategory_product_ids[1], 
            k=self.N_PRODUCT_TO_RECOMMEND_FROM_SUBCATEGORY
        ))

        # Set recommended products from samples
        self.recommend_products_from_samples(recomm_product_samples, num_product_samples=2)

    def recommend_products_from_samples(
        self, recomm_product_samples,
        num_product_samples=1
    ):
        """
        Recommends products from num_product_samples.
        Pass if number of product samples > 1.

        Parameters
        ----------
        recomm_product_samples:
            list or list of lists (recommended product samples)
        num_product_samples:
            default=1 (number of product samples)

        Returns
        -------
        Nothing
        """
        product_objects_to_recommend = '' 
        if num_product_samples == 1:
            # Use id based django filter
            product_objects_to_recommend = \
                Product.objects.filter(
                    id = recomm_product_samples
                )
        else:
            # Use id list based django filter
            product_objects_to_recommend = \
                Product.objects.filter(
                    id__in = recomm_product_samples
                )   
        if self.recommended_products:
            # If already recommended products present,
            # union with current product objects.
            self.recommended_products = self.recommended_products.union(
                product_objects_to_recommend
            )
        else:
            self.recommended_products = product_objects_to_recommend

    def parse_subcategories(self):
        """
        Why parse? User views are stored in database as stringified
        JSON objects thus needed to be parsed to extract data.

        Extracts subcategories from views JSON string.
        Sets viewed_subcategories
            - if subcategory is already there in viewed subcategories,
            then just increase the subcategory_views
            - else make a dictionary and append the new subcategory and
            it's views
        
        Parameters
        ----------
        None

        Returns
        -------
        int
            num_subcategories: number of subcategories viewed by
            users
        """
        try:
            user_views_object = UserViews.objects.get(user=self.user)
            user_views = json.loads(user_views_object.views)

            for user_view in user_views:
                subcat_there, index = self.subcategory_in_viewed_subcategories(user_view)
                if subcat_there:
                    self.viewed_subcategories[index]['subcategory_views'] += \
                        user_view['user_views']
                else:
                    self.viewed_subcategories.append({
                        'subcategory': user_view['subcategory_id'],
                        'subcategory_views': user_view['user_views']
                    })
        except Exception as e:
            print(e)
            return 0
        return len(self.viewed_subcategories)

    def subcategory_in_viewed_subcategories(self, user_view):
        """
        Checks if the current user_view's subcategory is already in
        viewed_subcategories.
        
        Parameters
        ----------
        user_view
            a single object for a single product's view from frontend

        Returns
        -------
        boolean
            True or False
        int
            index: additional parameter of index where the subcategory was
            found
        """
        if (self.viewed_subcategories):
            for index, viewed_subcategory in enumerate(self.viewed_subcategories):
                if viewed_subcategory['subcategory'] == \
                    user_view['subcategory_id']:
                    return (True, index)

        return (False, None)


    def get_products_two_most_viewed_subcategories(self):
        """
        Fetch all the products in two most viewed subcategories.
        
        Parameters
        ----------
        None

        Returns
        -------
        list of lists
            subcategory_product_ids: 
                [0]: all product ids of most viewed subcategory
                [1]: all product ids of second most viewed subcategory
        """
        most_viewed_subcategories = [0, 0]
        most_views = [0 ,0]

        # max computation
        for subcategory in self.viewed_subcategories:
            if subcategory['subcategory_views'] > most_views[0]:
                most_views[0] = subcategory['subcategory_views']
                most_viewed_subcategories[0] = \
                    subcategory['subcategory']
        
        # second max computation
        for subcategory in self.viewed_subcategories:
            if subcategory['subcategory_views'] < most_views[0] and \
            subcategory['subcategory_views'] > most_views[1]:
                most_views[1] = subcategory['subcategory_views']
                most_viewed_subcategories[1] = \
                    subcategory['subcategory']

        subcategory_product_ids = []
        max_viewed_products = list(Product.objects.filter(
            sub_category_id = most_viewed_subcategories[0]
        ).values_list('id', flat=True))
        subcategory_product_ids.append(max_viewed_products)
        second_most_viewed = list(Product.objects.filter(
            sub_category_id = most_viewed_subcategories[1]
        ).values_list('id', flat=True))
        subcategory_product_ids.append(second_most_viewed)

        return subcategory_product_ids
