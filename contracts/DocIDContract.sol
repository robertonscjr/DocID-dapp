pragma solidity >=0.5.0 <0.7.0;

contract DocIDContract {
    
    struct Identity {
        string firstName;
        string lastName;
        string dateOfBirth;
        string homeAddress;
    }
    
    struct Document {
        string name;
        string description;
        int year;
    }

    address public owner;

    mapping(address => Identity) public identities;
    mapping(address => Document) public documents;
    
    constructor() public {
        owner = msg.sender;
    }



    function registerIdentity(
        string memory _firstName,
        string memory _lastName,
        string memory _dateOfBirth,
        string memory _homeAddress) public payable 
    {
        identities[msg.sender] = Identity({
            firstName: _firstName,
            lastName: _lastName,
            dateOfBirth: _dateOfBirth,
            homeAddress: _homeAddress
        });

    }
    
    function registerDocument(
        string memory _name,
        string memory _description,
        int _year,
        address _identity) public payable 
    {
        require(msg.sender == owner);

        documents[_identity] = Document({
            name: _name,
            description: _description,
            year: _year
        });

    }

}
