# PHP_funciton_finder
It is the updated version of Dfunc-Bypasser. Find vulnerable functions from the phpinfo page.

# Installation

git clone https://github.com/teambi0s/dfunc-bypasser

# Usage

There are two options to input the disable_functions list:

1. For help on the parameters: python dfunc-bypasser.py -h
2. Provide the phpinfo url: python dfunc-bypasser.py --url https://example.com/phpinfo.php
3. Provide the local phpinfo file: python dfunc-bypasser.py --file dir/phpinfo
4. Profide a custom header in the request: php_bypass_finder.py --url https://example.com/phpinfo.php --header "Custome: Header"
