CREATE DATABASE IF NOT EXISTS spravce_ukolu;

CREATE DATABASE IF NOT EXISTS spravce_ukolu_test;

USE spravce_ukolu;

CREATE TABLE IF NOT EXISTS ukoly (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazev VARCHAR(255) NOT NULL,
    popis TEXT NOT NULL,
    stav VARCHAR(20) DEFAULT 'Nezahájeno',
    datum_vytvoreni TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);