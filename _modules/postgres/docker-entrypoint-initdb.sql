CREATE TABLE IF NOT EXISTS menu
(
   menu_id                SERIAL4 NOT NULL,
   title                  VARCHAR(255) NOT NULL,
   description            VARCHAR(255) NOT NULL,
   load_on                TIMESTAMP DEFAULT now(),
   CONSTRAINT menu_pkey   PRIMARY KEY (menu_id)
);

CREATE TABLE IF NOT EXISTS submenu
(
   submenu_id               SERIAL4 NOT NULL,
   menu_id                  INTEGER NOT NULL,
   title                    VARCHAR(255) NOT NULL,
   description              VARCHAR(255) NOT NULL,
   load_on                  TIMESTAMP DEFAULT now(),
   CONSTRAINT submenu_pkey  PRIMARY KEY (submenu_id),
   CONSTRAINT fk_menu
       FOREIGN KEY(menu_id)
	       REFERENCES menu(menu_id)
);

CREATE TABLE IF NOT EXISTS dish
(
   dish_id               SERIAL4 NOT NULL,
   submenu_id            INTEGER NOT NULL,
   title                 VARCHAR(255) NOT NULL,
   description           VARCHAR(255) NOT NULL,
   price                 FLOAT NOT NULL,
   load_on               TIMESTAMP DEFAULT now(),
   CONSTRAINT dish_pkey  PRIMARY KEY (dish_id),
   CONSTRAINT fk_submenu
       FOREIGN KEY(submenu_id)
	       REFERENCES submenu(submenu_id)
);

