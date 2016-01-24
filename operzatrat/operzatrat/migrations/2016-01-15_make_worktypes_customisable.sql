ALTER TABLE inputforms_worktype ADD COLUMN custom boolean;

ALTER TABLE inputforms_worktype MODIFY description longtext;
ALTER TABLE inputforms_worktype MODIFY site varchar(3);