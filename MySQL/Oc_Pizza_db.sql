-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Oc_Pizza
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Oc_Pizza
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Oc_Pizza` DEFAULT CHARACTER SET utf8mb4 ;
USE `Oc_Pizza` ;

-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `status` VARCHAR(155) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Address` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(45) NOT NULL,
  `zip_code` VARCHAR(12) NOT NULL,
  `city` VARCHAR(80) NOT NULL,
  `additional_address` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Phone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Phone` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `phone` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Email`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Email` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `mail` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `mail_UNIQUE` (`mail` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Restaurant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Restaurant` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `restaurant_name` VARCHAR(155) NOT NULL,
  `Addresses_id` INT NOT NULL,
  `Phones_id` INT NOT NULL,
  `Emails_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `restaurant_name_UNIQUE` (`restaurant_name` ASC) VISIBLE,
  INDEX `fk_Restaurants_Addresses1_idx` (`Addresses_id` ASC) VISIBLE,
  INDEX `fk_Restaurants_Phones1_idx` (`Phones_id` ASC) VISIBLE,
  INDEX `fk_Restaurants_Emails1_idx` (`Emails_id` ASC) VISIBLE,
  CONSTRAINT `fk_Restaurants_Addresses1`
    FOREIGN KEY (`Addresses_id`)
    REFERENCES `Oc_Pizza`.`Address` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Restaurants_Phones1`
    FOREIGN KEY (`Phones_id`)
    REFERENCES `Oc_Pizza`.`Phone` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Restaurants_Emails1`
    FOREIGN KEY (`Emails_id`)
    REFERENCES `Oc_Pizza`.`Email` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Actor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Actor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(155) NOT NULL,
  `last_name` VARCHAR(155) NOT NULL,
  `authentication_password` VARCHAR(255) NOT NULL,
  `Emails_id` INT NOT NULL,
  `Phones_id` INT NOT NULL,
  `Addresses_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `authentication_password_UNIQUE` (`authentication_password` ASC) VISIBLE,
  INDEX `fk_Actors_Emails1_idx` (`Emails_id` ASC) VISIBLE,
  INDEX `fk_Actors_Phones1_idx` (`Phones_id` ASC) VISIBLE,
  INDEX `fk_Actors_Addresses1_idx` (`Addresses_id` ASC) VISIBLE,
  CONSTRAINT `fk_Actors_Emails1`
    FOREIGN KEY (`Emails_id`)
    REFERENCES `Oc_Pizza`.`Email` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Actors_Phones1`
    FOREIGN KEY (`Phones_id`)
    REFERENCES `Oc_Pizza`.`Phone` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Actors_Addresses1`
    FOREIGN KEY (`Addresses_id`)
    REFERENCES `Oc_Pizza`.`Address` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`employee` (
  `id` INT NOT NULL,
  `social_security_numb` VARCHAR(30) NOT NULL,
  `quality` VARCHAR(100) NOT NULL,
  `date_entry` DATE NOT NULL,
  `Status_id` INT NOT NULL,
  `Restaurants_id` INT NOT NULL,
  `Actors_id` INT NOT NULL,
  UNIQUE INDEX `social_security_numb_UNIQUE` (`social_security_numb` ASC) VISIBLE,
  INDEX `fk_Employee_Status_idx` (`Status_id` ASC) VISIBLE,
  INDEX `fk_Employee_Restaurants1_idx` (`Restaurants_id` ASC) VISIBLE,
  PRIMARY KEY (`Actors_id`, `id`),
  INDEX `fk_Employee_Actors1_idx` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_Employee_Status`
    FOREIGN KEY (`Status_id`)
    REFERENCES `Oc_Pizza`.`Status` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Employee_Restaurants1`
    FOREIGN KEY (`Restaurants_id`)
    REFERENCES `Oc_Pizza`.`Restaurant` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Employee_Actors1`
    FOREIGN KEY (`id`)
    REFERENCES `Oc_Pizza`.`Actor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`payment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`payment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `payment_mode` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_type` VARCHAR(255) NOT NULL,
  `order_date` DATE NOT NULL,
  `Status_id` INT NOT NULL,
  `Actors_id` INT NOT NULL,
  `Restaurants_id` INT NOT NULL,
  `Addresses_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Orders_Status1_idx` (`Status_id` ASC) VISIBLE,
  INDEX `fk_Orders_Actors1_idx` (`Actors_id` ASC) VISIBLE,
  INDEX `fk_Orders_Restaurants1_idx` (`Restaurants_id` ASC) VISIBLE,
  INDEX `fk_Orders_Addresses1_idx` (`Addresses_id` ASC) VISIBLE,
  CONSTRAINT `fk_Orders_Status1`
    FOREIGN KEY (`Status_id`)
    REFERENCES `Oc_Pizza`.`Status` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Orders_Actors1`
    FOREIGN KEY (`Actors_id`)
    REFERENCES `Oc_Pizza`.`Actor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Orders_Restaurants1`
    FOREIGN KEY (`Restaurants_id`)
    REFERENCES `Oc_Pizza`.`Restaurant` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Orders_Addresses1`
    FOREIGN KEY (`Addresses_id`)
    REFERENCES `Oc_Pizza`.`Address` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Invoice` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `invoices_date` DATE NOT NULL,
  `product_type` VARCHAR(155) NOT NULL,
  `product_price` DECIMAL(5,2) NOT NULL,
  `product_tax` DECIMAL(5,2) NOT NULL,
  `payments_id` INT NOT NULL,
  `Addresses_id` INT NOT NULL,
  `Phones_id` INT NOT NULL,
  `Actors_id` INT NOT NULL,
  `Orders_id` INT NOT NULL,
  INDEX `fk_Invoices_payments1_idx` (`id` ASC) VISIBLE,
  INDEX `fk_Invoices_Addresses1_idx` (`Addresses_id` ASC) VISIBLE,
  INDEX `fk_Invoices_Phones1_idx` (`Phones_id` ASC) VISIBLE,
  INDEX `fk_Invoices_Actors1_idx` (`Actors_id` ASC) VISIBLE,
  PRIMARY KEY (`id`, `Orders_id`),
  CONSTRAINT `fk_Invoices_payments1`
    FOREIGN KEY (`id`)
    REFERENCES `Oc_Pizza`.`payment` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Invoices_Addresses1`
    FOREIGN KEY (`Addresses_id`)
    REFERENCES `Oc_Pizza`.`Address` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Invoices_Phones1`
    FOREIGN KEY (`Phones_id`)
    REFERENCES `Oc_Pizza`.`Phone` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Invoices_Actors1`
    FOREIGN KEY (`Actors_id`)
    REFERENCES `Oc_Pizza`.`Actor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Invoices_Orders1`
    FOREIGN KEY (`Orders_id`)
    REFERENCES `Oc_Pizza`.`Order` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Ingredient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Ingredient` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `designation` VARCHAR(255) NOT NULL,
  `weight` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`ProductType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`ProductType` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`Product` (
  `id` BIGINT NOT NULL,
  `product_name` VARCHAR(155) NOT NULL,
  `product_price` DECIMAL(5,2) NOT NULL,
  `ProductType_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Product_ProductType1_idx` (`ProductType_id` ASC) VISIBLE,
  CONSTRAINT `fk_Product_ProductType1`
    FOREIGN KEY (`ProductType_id`)
    REFERENCES `Oc_Pizza`.`ProductType` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`ShoppingCart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`ShoppingCart` (
  `Orders_id` INT NOT NULL,
  `Products_id` BIGINT NOT NULL,
  `article` VARCHAR(255) NOT NULL,
  `quantity` INT NOT NULL,
  `price` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`Orders_id`, `Products_id`),
  INDEX `fk_Orders_has_Products_Products1_idx` (`Products_id` ASC) VISIBLE,
  INDEX `fk_Orders_has_Products_Orders1_idx` (`Orders_id` ASC) VISIBLE,
  CONSTRAINT `fk_Orders_has_Products_Orders1`
    FOREIGN KEY (`Orders_id`)
    REFERENCES `Oc_Pizza`.`Order` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Orders_has_Products_Products1`
    FOREIGN KEY (`Products_id`)
    REFERENCES `Oc_Pizza`.`Product` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`ProductStock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`ProductStock` (
  `Ingredients_id` INT NOT NULL,
  `Restaurants_id` INT NOT NULL,
  `name_product` VARCHAR(155) NOT NULL,
  `weight` DECIMAL(5,2) NOT NULL,
  `conditioning` VARCHAR(255) NOT NULL,
  `quantity` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`Ingredients_id`, `Restaurants_id`),
  INDEX `fk_Ingredients_has_Restaurants_Restaurants1_idx` (`Restaurants_id` ASC) VISIBLE,
  INDEX `fk_Ingredients_has_Restaurants_Ingredients1_idx` (`Ingredients_id` ASC) VISIBLE,
  CONSTRAINT `fk_Ingredients_has_Restaurants_Ingredients1`
    FOREIGN KEY (`Ingredients_id`)
    REFERENCES `Oc_Pizza`.`Ingredient` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Ingredients_has_Restaurants_Restaurants1`
    FOREIGN KEY (`Restaurants_id`)
    REFERENCES `Oc_Pizza`.`Restaurant` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza`.`composition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza`.`composition` (
  `Ingredients_id` INT NOT NULL,
  `Products_id` BIGINT NOT NULL,
  `quantity` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`Ingredients_id`, `Products_id`),
  INDEX `fk_Ingredients_has_Products_Products1_idx` (`Products_id` ASC) VISIBLE,
  INDEX `fk_Ingredients_has_Products_Ingredients1_idx` (`Ingredients_id` ASC) VISIBLE,
  CONSTRAINT `fk_Ingredients_has_Products_Ingredients1`
    FOREIGN KEY (`Ingredients_id`)
    REFERENCES `Oc_Pizza`.`Ingredient` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Ingredients_has_Products_Products1`
    FOREIGN KEY (`Products_id`)
    REFERENCES `Oc_Pizza`.`Product` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
