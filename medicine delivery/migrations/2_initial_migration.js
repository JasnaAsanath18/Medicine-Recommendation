const Migrations = artifacts.require("medicine");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
