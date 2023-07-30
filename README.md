# VoteTrust - Blockchain Voting App
VoteTrust is a blockchain-based voting application that enables secure and transparent voting for various elections and polls. The app utilizes blockchain technology to record each vote as a transaction on the blockchain, ensuring immutability and integrity of the voting process.

## How It Works
Smart Contracts: VoteTrust uses smart contracts to manage the voting process. Smart contracts are self-executing contracts with the terms of the agreement directly written into code. These contracts facilitate the voting and ensure that each vote is securely recorded on the blockchain.

Blockchain Integration: The backend of VoteTrust is built using Python and Flask. It communicates with the blockchain using the web3.py library, which enables interaction with the Ethereum blockchain. This integration allows the app to invoke smart contract functions and record votes on the blockchain.

User Authentication: VoteTrust incorporates user authentication using Twilio's API. When users sign up or log in, they receive a one-time verification code through SMS to their registered phone number. This two-factor authentication process ensures that only eligible voters can participate in the election.

Election Management: The app allows an admin to start and end an election. Once an election is started, eligible voters can cast their votes for their preferred candidates or options.

Transparency and Immutability: Every vote cast is recorded as a transaction on the blockchain. This ensures transparency, as anyone can verify the voting results on the public blockchain. Additionally, the immutability of the blockchain prevents any unauthorized changes to the voting data.

## Getting Started
To get VoteTrust up and running on your local machine, follow these steps:

1. Prerequisites: Make sure you have Python and Flask installed on your system.

2. Clone the Repository: Clone the VoteTrust repository from GitHub to your local machine.

3. Install Dependencies: Navigate to the project directory and install the required dependencies by running the following command: `pip install -r requirements.txt`

4. Configure Environment: Create a .env file in the root directory and set the necessary environment variables, such as the Ethereum node URL, admin credentials, and Twilio API keys.

5. Start the App: Run the following command to start the Flask development server:`flask run`


6. Access the App: Once the server is running, you can access the VoteTrust app by visiting http://localhost:5000 in your web browser.

## Important Note
VoteTrust is a demo application and should not be used for real-world elections without further security and auditing measures. The app is intended for educational purposes to demonstrate the capabilities of blockchain technology in voting systems.
