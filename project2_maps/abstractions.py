"""Data Abstractions"""

def mean(lst):
    """Return the arithmetic mean of a sequence of numbers."""
    assert len(lst) > 0, 'cannot find mean of empty sequence'
    return sum(lst) / len(lst)

# Reviews


def make_review(restaurant_name, rating):
    """Return a review."""
    return [restaurant_name, rating]

def review_restaurant_name(review):
    """Return the reviewed restaurant's name (string)."""
    return review[0]

def review_rating(review):
    """Return the number of stars given (1 to 5)."""
    return review[1]

# Users

def make_user(name, reviews):
    """Return a user."""
    return [name, {review_restaurant_name(r): r for r in reviews}]

def user_name(user):
    """Return the USER's name (string)."""
    return user[0]

def user_reviews(user):
    """Return a dictionary from restaurant names to reviews by the USER."""
    return user[1]
    
""" understanding    
revs_user = [] # all reviews 

rto = make_review('Thai Orchid', 4)
rbs = make_review('Blue Ship', 5)

revs.append(rto)
revs.append(rbs)

restaurant = review_restaurant_name(rto)
rating = review_rating(rto)

reviewer_a = make_user('Jethro179', revs_user)
reviewer_uid = user_name(reviewer_a)
reviewer_revs = user_reviews(reviewer_a) """



"""Data Abstractions"""

def mean(lst):
    """Return the arithmetic mean of a sequence of numbers."""
    assert len(lst) > 0, 'cannot find mean of empty sequence'
    return sum(lst) / len(lst)

# Reviews


def make_review(restaurant_name, rating):
    """Return a review."""
    return [restaurant_name, rating]

def review_restaurant_name(review):
    """Return the reviewed restaurant's name (string)."""
    return review[0]

def review_rating(review):
    """Return the number of stars given (1 to 5)."""
    return review[1]

# Users

def make_user(name, reviews):
    """Return a user."""
    return [name, {review_restaurant_name(r): r for r in reviews}]

def user_name(user):
    """Return the USER's name (string)."""
    return user[0]

def user_reviews(user):
    """Return a dictionary from restaurant names to reviews by the USER."""
    return user[1]
    
### === +++ USER ABSTRACTION BARRIER +++ === ###

def user_reviewed_restaurants(user, restaurants):
    """Return the subset of restaurants reviewed by USER.

    Arguments:
    user -- a user
    restaurants -- a dictionary from restaurant names to restaurants
    """
    names = user_reviews(user).keys()
    return {name: restaurants[name] for name in names if name in restaurants}

def user_rating(user, restaurant_name):
    """Return the rating given for RESTAURANT_NAME by USER."""
    return review_rating(user_reviews(user)[restaurant_name])

# Restaurants

def make_restaurant(name, location, categories, price, reviews):
    """Return a restaurant, implemented as a dictionary."""
    # You may change this starter implementation however you wish, including
    # adding more items to the dictionary below.
    "*** YOUR CODE HERE ***"
    return {'name': name,
            'location': location,
            'categories': categories,
            'price': price,
            'reviews': reviews,
            }

"""
ritz_ratings = [4, 3, 3, 2, 4, 4, 5]
revs = [make_review('Ritz', r) for r in ritz_ratings]

resto1 = make_restaurant('Ritz', 'Berkeley', ['Seafood', 'Expensive', 'Fine dining'], '££££', revs)  
"""

def restaurant_name(restaurant):
    return restaurant['name']

def restaurant_location(restaurant):
    return restaurant['location']

def restaurant_categories(restaurant):
    return restaurant['categories']

def restaurant_price(restaurant):
    return restaurant['price']

def restaurant_ratings(restaurant):
    """Return a list of ratings (numbers from 1 to 5)."""
    "*** YOUR CODE HERE ***"
    return [i[1] for i in restaurant['reviews']]
    
ans = restaurant_ratings(resto1)

### === +++ RESTAURANT ABSTRACTION BARRIER +++ === ###

def restaurant_num_ratings(restaurant):
    """Return the number of ratings for RESTAURANT."""
    "*** YOUR CODE HERE ***"
    return len(restaurant_ratings(restaurant))

def restaurant_mean_rating(restaurant):
    """Return the average rating for RESTAURANT."""
    "*** YOUR CODE HERE ***"
    return sum(restaurant_ratings(restaurant))/restaurant_num_ratings(restaurant)

"""mean = restaurant_mean_rating(resto1)"""
