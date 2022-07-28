CREATE TABLE user (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    age INT UNSIGNED NOT NULL,
    ht FLOAT NOT NULL,
    gender nvarchar(8),
    PRIMARY KEY (`id`)
);