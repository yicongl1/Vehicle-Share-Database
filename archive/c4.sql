CREATE TABLE Cat(
  intitulé VARCHAR(30) PRIMARY KEY
);

CREATE TABLE QUESTIONS(
  numéro INTEGER, 
  intitulé VATCHAR(255) UNIQUE NOT NULL
  difficulté:INTEGER, date_creation:date, image:string, réponse:string, correct:char(1), catégorie=>Catégorie)
)