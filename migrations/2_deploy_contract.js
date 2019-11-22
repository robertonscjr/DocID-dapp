var Contract = artifacts.require("./DocIDContract.sol");

module.exports = function(deployer) {
  deployer.deploy(Contract);
};
