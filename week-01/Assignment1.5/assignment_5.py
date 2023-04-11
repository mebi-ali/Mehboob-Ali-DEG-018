## Team Members
# 1. Mehboob Ali
# 2. Ali Umair

from typing import List

class User:
    sub: bool

def notify(user: User) -> None:
    pass


def get_sub_users(users: List[User]) -> List[User]:
    "Filter subsrcibed users"
    return [user for user in users if user.sub]

def notify_sub_users(users: List[User]) -> None:
    "Notify Sub Users"
    for user in get_sub_users(users):
        notify(user)
        
        