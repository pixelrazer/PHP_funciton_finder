#!/usr/bin/python3

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="PHPinfo URL: eg. https://example.com/phpinfo.php")
parser.add_argument("--file", help="PHPinfo localfile path: eg. dir/phpinfo")
parser.add_argument("--header", help="Custom headers: eg. Special-Dev: only4dev")

args = parser.parse_args()

if(args.url):
    url = args.url

elif(args.file):
    phpinfofile = args.file
    phpinfo = open(phpinfofile,'r').read()

else:
    print(parser.print_help())
    exit()

if args.header:
    header_key, header_value = args.header.split(':', 1)
    custom_header = {header_key.strip(): header_value.strip()}  # Use : instead of , to create a dictionary
else:
    custom_header = {}  # Provide an empty dictionary if no custom header is specified

# Fetch the PHPinfo with headers
phpinfo = requests.get(url, headers=custom_header).text

modules = []
inp = []

inp = phpinfo.split('disable_functions</td><td class="v">')[1].split("</")[0].split(',')[:-1]
# Print the fetched PHPinfo content and the headers
#print(inp)

dangerous_functions = ['pcntl_alarm','pcntl_fork','pcntl_waitpid','pcntl_wait','pcntl_wifexited','pcntl_wifstopped','pcntl_wifsignaled','pcntl_wifcontinued','pcntl_wexitstatus','pcntl_wtermsig','pcntl_wstopsig','pcntl_signal','pcntl_signal_get_handler','pcntl_signal_dispatch','pcntl_get_last_error','pcntl_strerror','pcntl_sigprocmask','pcntl_sigwaitinfo','pcntl_sigtimedwait','pcntl_exec','pcntl_getpriority','pcntl_setpriority','pcntl_async_signals','error_log','system','exec','shell_exec','popen','proc_open','passthru','link','symlink','syslog','ld','mail']
exploitable_functions = []

if "mbstring.ini" in phpinfo:
    modules.append('mbstring')
    dangerous_functions=('mb_send_mail')

if "imap.ini" in phpinfo:
    modules.append('imap')
    dangerous_functions.append('imap_open','imap_mail')

if "libvirt-php.ini" in phpinfo:
    modules.append('libvert')
    dangerous_functions.append('libvirt_connect')

if "gnupg.ini" in phpinfo:
    modules.append('gnupg')
    dangerous_functions.append('gnupg_init')

if "imagick.ini" in phpinfo:
    modules.append('imagick')

for i in inp:
    if i in dangerous_functions:
        modules.append(i)

for i in dangerous_functions:
    if i not in inp:
        exploitable_functions.append(i)

if len(dangerous_functions) == 0:
    print("No exploitable functions found")

else:
    print("These are the exploitable functions!\n")
    print(exploitable_functions)

if "imagic" in modules:
    print("HP-imagick module is present. It can be exploited using LD_PRELOAD method\n")
