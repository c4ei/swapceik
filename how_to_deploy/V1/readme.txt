cd /home/dev/www/uniswapV2/how_to_deploy/V1/v1-contracts
pip3 install virtualenv
virtualenv -p python3 env
source env/bin/activate
    Install dependencies
pip install -r requirements.txt



        (Optional) Switch Vyper compiler to version used in Uniswap verification
        cd vyper
        git reset --hard 35038d20bd9946a35261c4c4fbcb27fe61e65f78
        cd ..
        Run tests
        pytest -v tests/

cd /home/dev/www/uniswapV2/how_to_deploy/V1
git reset --hard 35038d20bd9946a35261c4c4fbcb27fe61e65f78
cd /home/dev/www/uniswapV2/how_to_deploy/V1/v1-contracts
pytest -v tests/
