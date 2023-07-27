pragma solidity 0.5.16;

pragma experimental ABIEncoderV2;

contract Election {
    // Model a Candidate
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Store accounts that have voted
    mapping(address => bool) public voters;

    // Store Candidates
    // Fetch Candidate
    mapping(uint256 => Candidate) public candidates;

    // Store Candidates Count
    uint256 public candidatesCount;

    // Election status
    bool public electionStarted;

    // Admin address
    address public adminAddress = 0xb8C078EDd829e1b58Ab4407b288e5850D596472d; // Replace with the desired admin address

    // Modifier: Only admin can perform certain operations
    modifier onlyAdmin() {
        require(msg.sender == adminAddress, "Only admin can perform this operation");
        _;
    }

    // Constructor
    constructor() public {
    }

    // Start the election
    function startElection(string[] memory _candidateNames) public onlyAdmin {
        require(!electionStarted, "Election has already started");

        for (uint256 i = 0; i < _candidateNames.length; i++) {
            candidatesCount++;
            candidates[candidatesCount] = Candidate(candidatesCount, _candidateNames[i], 0);
        }

        electionStarted = true;
    }

    // Vote for a candidate
    function vote(uint256 _candidateId) public {
        require(electionStarted, "Election has not started");
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        require(!voters[msg.sender], "Voter has already voted");

        candidates[_candidateId].voteCount++;
        voters[msg.sender] = true;
    }

    // Get the current election status
    function getElectionStatus() public view returns (bool) {
        return electionStarted;
    }

    // Get the election results
    function getElectionResults() public view returns (string[] memory, uint256[] memory) {
        string[] memory candidateNames = new string[](candidatesCount);
        uint256[] memory voteCounts = new uint256[](candidatesCount);

        for (uint256 i = 1; i <= candidatesCount; i++) {
            Candidate memory candidate = candidates[i];
            candidateNames[i - 1] = candidate.name;
            voteCounts[i - 1] = candidate.voteCount;
        }

        return (candidateNames, voteCounts);
    }

    // End the election
    function endElection() public onlyAdmin {
        require(electionStarted, "Election has not started");
        electionStarted = false;
    }

    // Retrieve candidate ID and name
    function getCandidateIdsAndNames() public view returns (uint256[] memory, string[] memory) {
        uint256[] memory candidateIds = new uint256[](candidatesCount);
        string[] memory candidateNames = new string[](candidatesCount);

        for (uint256 i = 1; i <= candidatesCount; i++) {
            Candidate memory candidate = candidates[i];
            candidateIds[i - 1] = candidate.id;
            candidateNames[i - 1] = candidate.name;
        }

        return (candidateIds, candidateNames);
    }
    // Clear all candidate IDs and names
    function clearCandidates() public onlyAdmin {
        require(!electionStarted, "Election has already started");

        for (uint256 i = 1; i <= candidatesCount; i++) {
            delete candidates[i];
        }

        candidatesCount = 0;
    }
}
