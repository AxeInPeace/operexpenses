BEGIN;
CREATE TABLE `inputforms_project` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `start_date` date NOT NULL,
    `end_date` date NOT NULL,
    `name` varchar(255) NOT NULL
)
;
CREATE TABLE `inputforms_stationtype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL UNIQUE
)
;
CREATE TABLE `inputforms_station` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `station_id` integer NOT NULL,
    `project_id` integer NOT NULL
)
;
ALTER TABLE `inputforms_station` ADD CONSTRAINT `station_id_refs_id_14beca0f` FOREIGN KEY (`station_id`) REFERENCES `inputforms_stationtype` (`id`);
ALTER TABLE `inputforms_station` ADD CONSTRAINT `project_id_refs_id_81a8b2b7` FOREIGN KEY (`project_id`) REFERENCES `inputforms_project` (`id`);
CREATE TABLE `inputforms_worktype_stationType` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `worktype_id` integer NOT NULL,
    `stationtype_id` integer NOT NULL,
    UNIQUE (`worktype_id`, `stationtype_id`)
)
;
ALTER TABLE `inputforms_worktype_stationType` ADD CONSTRAINT `stationtype_id_refs_id_ba9f40c7` FOREIGN KEY (`stationtype_id`) REFERENCES `inputforms_stationtype` (`id`);
CREATE TABLE `inputforms_worktype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(1023) NOT NULL,
    `description` longtext NOT NULL,
    `site` varchar(3) NOT NULL
)
;
ALTER TABLE `inputforms_worktype_stationType` ADD CONSTRAINT `worktype_id_refs_id_8b357adb` FOREIGN KEY (`worktype_id`) REFERENCES `inputforms_worktype` (`id`);

CREATE INDEX `inputforms_station_5ab29bba` ON `inputforms_station` (`station_id`);
CREATE INDEX `inputforms_station_37952554` ON `inputforms_station` (`project_id`);
CREATE INDEX `inputforms_worktype_stationType_c1d69940` ON `inputforms_worktype_stationType` (`worktype_id`);
CREATE INDEX `inputforms_worktype_stationType_089b696a` ON `inputforms_worktype_stationType` (`stationtype_id`);

COMMIT;
