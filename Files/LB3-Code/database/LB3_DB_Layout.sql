-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema testdatabase
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema testdatabase
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `testdatabase` DEFAULT CHARACTER SET utf8 ;
USE `testdatabase` ;

-- -----------------------------------------------------
-- Table `testdatabase`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testdatabase`.`users` (
  `id` CHAR(38) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `email` VARCHAR(150) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdatabase`.`priority`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testdatabase`.`priority` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdatabase`.`task`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testdatabase`.`task` (
  `id` INT NOT NULL,
  `name` VARCHAR(150) NOT NULL,
  `createdAt` VARCHAR(45) NULL,
  `priority_id` INT NOT NULL,
  PRIMARY KEY (`id`, `priority_id`),
  INDEX `fk_task_priority1_idx` (`priority_id` ASC) VISIBLE,
  CONSTRAINT `fk_task_priority1`
    FOREIGN KEY (`priority_id`)
    REFERENCES `testdatabase`.`priority` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testdatabase`.`users_has_task`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testdatabase`.`users_has_task` (
  `users_id` CHAR(38) NOT NULL,
  `task_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `task_id`),
  INDEX `fk_users_has_task_task1_idx` (`task_id` ASC) VISIBLE,
  INDEX `fk_users_has_task_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_task_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `testdatabase`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_task_task1`
    FOREIGN KEY (`task_id`)
    REFERENCES `testdatabase`.`task` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
