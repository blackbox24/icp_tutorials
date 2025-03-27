# icp_tutorials
ICP tutorials on web3

### USING PYTHON SDK AS BACKEND FOR ICP
- Install wsl
- Use the following  dependencies:
    - Python 3.10.7
    - dfx 0.23.0
    - Python VS Code Extension
```sh
    # install pyenv
    curl https://pyenv.run | bash

    # install Python 3.10.7
    ~/.pyenv/bin/pyenv install 3.10.7
```

- Run the following command to install dfx 0.23.0: 
```sh
DFX_VERSION=0.23.0 sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
```

- If after trying to run dfx commands you encounter an error such as dfx: command not found, you might need to add $HOME/bin to your path. Here's an example of doing this in your .bashrc:
```sh
echo 'export PATH="$PATH:$HOME/bin"' >> "$HOME/.bashrc"
```

- It is highly recommended to use VS Code and to install the Microsoft Python extension to get full type checking support from within the editor:
    - Extension `VS Code -> Preferences -> Extensions -> Search for Python by Microsoft and install it`
    - Set python.analysis.typeCheckingMode Set the setting python.analysis.typeCheckingMode to strict:
        `VS Code -> Preferences -> Settings -> Search for python.analysis.typeCheckingMode and set it to strict`

- Assuming you're starting completely from scratch, run these commands to setup your project's directory and file structure:
```sh
mkdir kybra_hello_world
cd kybra_hello_world

mkdir src

touch src/main.py
touch dfx.json

```
- Now create and source a virtual environment:
```sh
python3 -m venv venv
# or
~/.pyenv/versions/3.10.7/bin/python -m venv venv
source venv/bin/activate

```
- Now install Kybra and the Kybra dfx extension:
```sh
pip install kybra
python -m kybra install-dfx-extension
```

- Here's the main code of the project, which you should put in the kybra_hello_world/src/main.py file of your canister:
```py
from kybra import query, update void

message:str = ""


@query
def get_message()->str:
    return message

@update
def set_message(new_message:str)->void:
    global message
    message = new_message
```

- Create the following in kybra_hello_world/dfx.json:
```json
{
    "canisters": {
        "kybra_hello_world": {
            "type": "kybra",
            "main": "src/main.py"
        }
    }
}

```

- Let's deploy to our local replica. First startup the replica:
```sh
dfx start --background
# If you want an extra speedy deploy:

dfx start --background --artificial-delay 0
# Then deploy the canister:

dfx canister create kybra_hello_world

dfx build

dfx deploy
```
- Interacting with your canister from the command line. Once we've deployed we can ask for our message:
```sh
dfx canister call kybra_hello_world get_message
# We should see ("") representing an empty message.

# Now let's yell Hello World!:

dfx canister call kybra_hello_world set_message '("Hello World!")'
# Retrieve the message:

dfx canister call kybra_hello_world get_message
# We should see ("Hello World!").
```

- Interacting with your canister from the web UI. After deploying your canister, you should see output similar to the following in your terminal:
```
Deployed canisters.
URLs:
  Backend canister via Candid interface:
    kybra_hello_world: http://127.0.0.1:8000/?canisterId=ryjl3-tyaaa-aaaaa-aaaba-cai&id=rr
```