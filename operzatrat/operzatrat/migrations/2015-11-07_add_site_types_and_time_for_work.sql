CREATE TABLE `inputforms_sitetype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(1023) NOT NULL,
    `site` varchar(3) NOT NULL
);

CREATE TABLE `inputforms_timeforwork` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `work_type_id` integer NOT NULL,
    `site_type_id` integer NOT NULL,
    `time` integer NOT NULL
);
ALTER TABLE `inputforms_timeforwork` ADD CONSTRAINT `work_type_id_refs_id_0afedbd9` FOREIGN KEY (`work_type_id`) REFERENCES `inputforms_worktype` (`id`);
ALTER TABLE `inputforms_timeforwork` ADD CONSTRAINT `site_type_id_refs_id_12471a81` FOREIGN KEY (`site_type_id`) REFERENCES `inputforms_sitetype` (`id`);

CREATE INDEX `inputforms_timeforwork_2d4747f1` ON `inputforms_timeforwork` (`work_type_id`);
CREATE INDEX `inputforms_timeforwork_b303b3c4` ON `inputforms_timeforwork` (`site_type_id`);