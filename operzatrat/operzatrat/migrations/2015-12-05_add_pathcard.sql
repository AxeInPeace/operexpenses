CREATE TABLE `inputforms_pathcard` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `station_id` integer NOT NULL
);
ALTER TABLE `inputforms_pathcard` ADD CONSTRAINT `station_id_refs_id_7d917a41` FOREIGN KEY (`station_id`) REFERENCES `inputforms_station` (`id`);

CREATE TABLE `inputforms_worksonpathcard` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `work_id` integer NOT NULL,
    `pathcard_id` integer NOT NULL,
    `time` integer NOT NULL
);

ALTER TABLE `inputforms_worksonpathcard` ADD CONSTRAINT `work_id_refs_id_778a9a10` FOREIGN KEY (`work_id`) REFERENCES `inputforms_worktype` (`id`);
ALTER TABLE `inputforms_worksonpathcard` ADD CONSTRAINT `pathcard_id_refs_id_692daa74` FOREIGN KEY (`pathcard_id`) REFERENCES `inputforms_pathcard` (`id`);

CREATE INDEX `inputforms_pathcard_5ab29bba` ON `inputforms_pathcard` (`station_id`);
CREATE INDEX `inputforms_worksonpathcard_dfb5c784` ON `inputforms_worksonpathcard` (`work_id`);
CREATE INDEX `inputforms_worksonpathcard_78d55901` ON `inputforms_worksonpathcard` (`pathcard_id`);