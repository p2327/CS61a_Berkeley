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

