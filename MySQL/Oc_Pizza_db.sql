-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Oc_Pizza_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Oc_Pizza_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Oc_Pizza_db` DEFAULT CHARACTER SET utf8mb4 ;
USE `Oc_Pizza_db` ;

-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`acteur`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`acteur` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(155) NOT NULL,
  `prenom` VARCHAR(155) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  UNIQUE INDEX `id_employe_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `password_UNIQUE` (`password` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`telephone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`telephone` (
  `id` VARCHAR(12) NOT NULL,
  `telephone` VARCHAR(20) NULL,
  `acteur_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_telephone_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `téléphone_UNIQUE` (`telephone` ASC) VISIBLE,
  INDEX `fk_telephone_acteur1_idx` (`acteur_id` ASC) VISIBLE,
  CONSTRAINT `fk_telephone_acteur1`
    FOREIGN KEY (`acteur_id`)
    REFERENCES `Oc_Pizza_db`.`acteur` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`statut`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`statut` (
  `id` INT UNSIGNED NOT NULL,
  `statut` VARCHAR(155) NOT NULL,
  UNIQUE INDEX `id_restaurant_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`mail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`mail` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `mail` VARCHAR(255) NOT NULL,
  `acteur_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mail_acteur1_idx` (`acteur_id` ASC) VISIBLE,
  UNIQUE INDEX `mail_UNIQUE` (`mail` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_mail_acteur1`
    FOREIGN KEY (`acteur_id`)
    REFERENCES `Oc_Pizza_db`.`acteur` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`restaurant`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`restaurant` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nom_restaurant` VARCHAR(255) NOT NULL,
  `adresse_id` INT NOT NULL,
  `mail_id` INT UNSIGNED NOT NULL,
  `telephone_id` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_restaurant_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_restaurant_adresse1_idx` (`adresse_id` ASC) VISIBLE,
  INDEX `fk_restaurant_mail1_idx` (`mail_id` ASC) VISIBLE,
  INDEX `fk_restaurant_telephone1_idx` (`telephone_id` ASC) VISIBLE,
  CONSTRAINT `fk_restaurant_adresse1`
    FOREIGN KEY (`adresse_id`)
    REFERENCES `Oc_Pizza_db`.`adresse` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_restaurant_mail1`
    FOREIGN KEY (`mail_id`)
    REFERENCES `Oc_Pizza_db`.`mail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_restaurant_telephone1`
    FOREIGN KEY (`telephone_id`)
    REFERENCES `Oc_Pizza_db`.`telephone` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`commande`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`commande` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `type_produit` VARCHAR(255) NOT NULL,
  `date_commande` DATE NOT NULL,
  `statut_id` INT UNSIGNED NOT NULL,
  `restaurant_id` INT NOT NULL,
  `acteur_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_commande_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_commande_statut1_idx` (`statut_id` ASC) VISIBLE,
  INDEX `fk_commande_restaurant1_idx` (`restaurant_id` ASC) VISIBLE,
  INDEX `fk_commande_acteur1_idx` (`acteur_id` ASC) VISIBLE,
  CONSTRAINT `fk_commande_statut1`
    FOREIGN KEY (`statut_id`)
    REFERENCES `Oc_Pizza_db`.`statut` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_commande_restaurant1`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `Oc_Pizza_db`.`restaurant` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_commande_acteur1`
    FOREIGN KEY (`acteur_id`)
    REFERENCES `Oc_Pizza_db`.`acteur` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`adresse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`adresse` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `adresse` VARCHAR(255) NOT NULL,
  `code_postal` VARCHAR(15) NOT NULL,
  `ville` VARCHAR(255) NOT NULL,
  `adresse_compl` VARCHAR(255) NULL,
  `commande_id` INT UNSIGNED NOT NULL,
  `acteur_id` INT UNSIGNED NOT NULL,
  UNIQUE INDEX `id_adresse_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  INDEX `fk_adresse_commande1_idx` (`commande_id` ASC) VISIBLE,
  INDEX `fk_adresse_acteur1_idx` (`acteur_id` ASC) VISIBLE,
  CONSTRAINT `fk_adresse_commande1`
    FOREIGN KEY (`commande_id`)
    REFERENCES `Oc_Pizza_db`.`commande` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_adresse_acteur1`
    FOREIGN KEY (`acteur_id`)
    REFERENCES `Oc_Pizza_db`.`acteur` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`employe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`employe` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `num_ss_employe` VARCHAR(30) NOT NULL,
  `qualite` VARCHAR(155) NOT NULL,
  `date_entree` DATE NOT NULL,
  `restaurant_id` INT NOT NULL,
  `statut_id` INT UNSIGNED NOT NULL,
  `acteur_id` INT UNSIGNED NOT NULL,
  UNIQUE INDEX `num_ss_UNIQUE` (`num_ss_employe` ASC) VISIBLE,
  INDEX `fk_employe_restaurant1_idx` (`restaurant_id` ASC) VISIBLE,
  INDEX `fk_employe_statut1_idx` (`statut_id` ASC) VISIBLE,
  INDEX `fk_employe_acteur1_idx` (`acteur_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_employe_restaurant1`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `Oc_Pizza_db`.`restaurant` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_employe_statut1`
    FOREIGN KEY (`statut_id`)
    REFERENCES `Oc_Pizza_db`.`statut` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_employe_acteur1`
    FOREIGN KEY (`acteur_id`)
    REFERENCES `Oc_Pizza_db`.`acteur` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`paiement`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`paiement` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `mode` VARCHAR(80) NOT NULL,
  UNIQUE INDEX `id_paiement_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`facture`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`facture` (
  `id` INT UNSIGNED NOT NULL,
  `date_facture` DATE NOT NULL,
  `type_produit` VARCHAR(255) NOT NULL,
  `prix` VARCHAR(45) NOT NULL,
  `tva` REAL NOT NULL,
  `paiement_id` INT NOT NULL,
  `acteur_id` INT UNSIGNED NOT NULL,
  `adresse_id` INT NOT NULL,
  `telephone_id` VARCHAR(12) NOT NULL,
  INDEX `fk_facture_paiement1_idx` (`paiement_id` ASC) VISIBLE,
  INDEX `fk_facture_acteur1_idx` (`acteur_id` ASC) VISIBLE,
  INDEX `fk_facture_adresse1_idx` (`adresse_id` ASC) VISIBLE,
  INDEX `fk_facture_telephone1_idx` (`telephone_id` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_facture_paiement1`
    FOREIGN KEY (`paiement_id`)
    REFERENCES `Oc_Pizza_db`.`paiement` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_facture_acteur1`
    FOREIGN KEY (`acteur_id`)
    REFERENCES `Oc_Pizza_db`.`acteur` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_facture_adresse1`
    FOREIGN KEY (`adresse_id`)
    REFERENCES `Oc_Pizza_db`.`adresse` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_facture_telephone1`
    FOREIGN KEY (`telephone_id`)
    REFERENCES `Oc_Pizza_db`.`telephone` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_commande_id`
    FOREIGN KEY (`id`)
    REFERENCES `Oc_Pizza_db`.`commande` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`ingredient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`ingredient` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `designation` VARCHAR(255) NOT NULL,
  `poids` DECIMAL(5) NOT NULL,
  UNIQUE INDEX `id_paiement_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`typeProduit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`typeProduit` (
  `id` INT NOT NULL,
  `type_produit` VARCHAR(255) NOT NULL,
  UNIQUE INDEX `id_paiement_UNIQUE` (`id` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`produit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`produit` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(155) NOT NULL,
  `prix` DECIMAL(5) NOT NULL,
  `typeProduit_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_produit_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_produit_typeProduit1_idx` (`typeProduit_id` ASC) VISIBLE,
  CONSTRAINT `fk_produit_typeProduit1`
    FOREIGN KEY (`typeProduit_id`)
    REFERENCES `Oc_Pizza_db`.`typeProduit` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`composition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`composition` (
  `ingredient_id` INT NOT NULL,
  `produit_id` INT UNSIGNED NOT NULL,
  `quantite` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`ingredient_id`, `produit_id`),
  INDEX `fk_ingredient_has_produit_produit1_idx` (`produit_id` ASC) VISIBLE,
  INDEX `fk_ingredient_has_produit_ingredient1_idx` (`ingredient_id` ASC) VISIBLE,
  CONSTRAINT `fk_ingredient_has_produit_ingredient1`
    FOREIGN KEY (`ingredient_id`)
    REFERENCES `Oc_Pizza_db`.`ingredient` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_ingredient_has_produit_produit1`
    FOREIGN KEY (`produit_id`)
    REFERENCES `Oc_Pizza_db`.`produit` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`stockProduit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`stockProduit` (
  `ingredient_id` INT NOT NULL,
  `restaurant_id` INT NOT NULL,
  `nom` VARCHAR(255) NOT NULL,
  `poids` DECIMAL(5,2) NOT NULL,
  `conditionnement` VARCHAR(155) NULL,
  `quantite` INT NOT NULL,
  PRIMARY KEY (`ingredient_id`, `restaurant_id`),
  INDEX `fk_ingredient_has_restaurant_restaurant1_idx` (`restaurant_id` ASC) VISIBLE,
  INDEX `fk_ingredient_has_restaurant_ingredient1_idx` (`ingredient_id` ASC) VISIBLE,
  CONSTRAINT `fk_ingredient_has_restaurant_ingredient1`
    FOREIGN KEY (`ingredient_id`)
    REFERENCES `Oc_Pizza_db`.`ingredient` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_ingredient_has_restaurant_restaurant1`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `Oc_Pizza_db`.`restaurant` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Oc_Pizza_db`.`pannier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Oc_Pizza_db`.`pannier` (
  `typeProduit_id` INT NOT NULL,
  `commande_id` INT UNSIGNED NOT NULL,
  `article` VARCHAR(155) NOT NULL,
  `quantite` INT NOT NULL,
  `prix` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`typeProduit_id`, `commande_id`),
  INDEX `fk_typeProduit_has_commande_commande1_idx` (`commande_id` ASC) VISIBLE,
  INDEX `fk_typeProduit_has_commande_typeProduit1_idx` (`typeProduit_id` ASC) VISIBLE,
  CONSTRAINT `fk_typeProduit_has_commande_typeProduit1`
    FOREIGN KEY (`typeProduit_id`)
    REFERENCES `Oc_Pizza_db`.`typeProduit` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_typeProduit_has_commande_commande1`
    FOREIGN KEY (`commande_id`)
    REFERENCES `Oc_Pizza_db`.`commande` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
