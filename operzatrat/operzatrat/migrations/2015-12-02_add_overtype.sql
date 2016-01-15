CREATE TABLE `inputforms_workovertype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(1023) NOT NULL
);

ALTER TABLE `inputforms_worktype` ADD COLUMN `owned_to_id` integer;

ALTER TABLE `inputforms_worktype` ADD CONSTRAINT `owned_to_id_refs_id_d25332b0` FOREIGN KEY (`owned_to_id`) REFERENCES `inputforms_workovertype` (`id`);
