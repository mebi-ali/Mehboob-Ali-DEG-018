# Mehboob-Ali-DEG-018

### Assignment 5
#### Description

Refactor following code:

from typing import List

import pandas as pd

class User:

    sub: bool

def notify(user: User) -> None:

    pass

def notify_users(x: List[User]) -> None:

  #Filter users with subscription and notify them.

  for u in x:

     if u.sub:

      # u.notify()

       notify(u)

### Team Members 
1. Mehboob Ali
2. Ali Umair
