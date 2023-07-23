from .models.menu.model import menu
from .models.submenu.model import submenu
from .models.dish.model import dish

from sqlalchemy.orm import relationship


setattr(menu, '_submenus', relationship(submenu, back_populates='_menu', cascade='all, delete-orphan'))
setattr(submenu, '_menu', relationship(menu, back_populates='_submenus'))
setattr(submenu, '_dishes', relationship(dish, back_populates='_submenu', cascade='all, delete-orphan'))
setattr(dish, '_submenu', relationship(submenu, back_populates='_dishes'))
