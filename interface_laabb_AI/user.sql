-- Créer la base de données 'users' si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS users;

-- Utiliser la base de données 'users'
USE users;

-- Créer la table 'utilisateurs' si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    mot_de_passe VARCHAR(20) NOT NULL
);

-- Supprimer la colonne 'n' de la table 'utilisateurs' si elle existe
-- ALTER TABLE utilisateurs DROP COLUMN n;

-- Modifier la colonne 'mot_de_passe' pour qu'elle soit NOT NULL si elle existe
ALTER TABLE utilisateurs MODIFY COLUMN mot_de_passe VARCHAR(20) NOT NULL;
