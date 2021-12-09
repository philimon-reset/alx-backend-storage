-- Creating a new table 2
CREATE TABLE IF NOT EXISTS users(
    `id` INT AUTO_INCREMENT NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') DEFAULT 'US',
    PRIMARY KEY(id)
);