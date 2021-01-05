from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from .models import User, Blog, Topic


def create():
    u1 = User.objects.create(first_name='u1', last_name='u1')
    u2 = User.objects.create(first_name='u2', last_name='u2')
    u3 = User.objects.create(first_name='u3', last_name='u3')

    b1 = Blog.objects.create(title='blog1', author='u1')
    b2 = Blog.objects.create(title='blog2', author='u1')

    b1.subscribers.add(u1, u2)
    b2.subscribers.add(u2)

    t1 = Topic.objects.create(title='topic1', blog='blog1', author='u1')
    t2 = Topic.objects.create(title='topic2_content', blog='blog1', author='u1', created='2017-01-01')

    t1.likes(u1, u2, u3)
def edit_all():
    User.objects.all().edit_all(first_name='uu1')

def edit_u1_u2():
    User.objects.filter(Q(first_name='u1') | Q(first_name='u2')).update(first_name='uu1')


def delete_u1():
    User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    u = User.objects.get(first_name='u2')
    u.subscriptions.clear()


def get_topic_created_grated():
    pass


def get_topic_title_ended():
    pass


def get_user_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
