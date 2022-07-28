CREATE TABLE body_monitor (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` INT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    wt FLOAT COMMENT '체중',
    smm FLOAT COMMENT '골격근량',
    ffm FLOAT COMMENT '체지방량',
    pbf FLOAT COMMENT '체지방률',
    max_bp INT UNSIGNED COMMENT '최고혈압',
    min_bp INT UNSIGNED COMMENT '최저혈압',
    pulse INT UNSIGNED COMMENT '맥박',
    deleted_at TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `body_monitor_fk_1` (`user_id`),
    CONSTRAINT `body_monitor_fk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
);