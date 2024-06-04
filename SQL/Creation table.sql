CREATE TABLE membre (
  ATR VARCHAR(14) PRIMARY KEY NOT NULL,
  Nom varchar(10) NOT NULL,
  Prenom varchar(10) NOT NULL,
  Age int(100) NOT NULL,
  num int(100) NOT NULL,
  RIB int(100) NOT NULL,
  img_URL varchar(100) NOT NULL,
  limite real,
  solde real,
  code int(4)
);
