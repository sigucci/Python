import profile
import subprocess

def extract_wifi_passwords():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('CP866').split('\n')

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
    #print(profiles)

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear')
        print(profile_info)

extract_wifi_passwords()
