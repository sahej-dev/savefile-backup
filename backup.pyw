from time import sleep
import credentials
import subprocess
import psutil

# return true if the process 'name' is running, else returns false
def game_running(name):

    for task in psutil.process_iter(attrs = ['name']):
        if game in task.info['name']:
            return True

    return False
    

if __name__ == '__main__':

    wait = 900  #in secs, 15 mins
    game = "witcher3"
    usr_name = credentials.name

    # An infinite loop to keep the script running
    while True:
        # Game is not yet running
        while True:
            if game_running(game):
                break
            sleep(wait)

        # Game is now running
        while True:
            if not game_running(game):
                break
            sleep(wait)

        # Game has now been closed
        file = '.\\' + game + '.bat'
        subprocess.call([file, usr_name])
