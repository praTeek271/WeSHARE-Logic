import sys
import subprocess
import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class setup:
    net_c=0
    def __init__(self):
        self.printME()
        if self.check_intr():
            self.module_chk()
        else:
            ErrorHndle.handle_and_exit(mesaage="Internet Connection Not Found")

        self.missing=set()

    def printME(self):
        
            print("""
    ██████╗ ██████╗  █████╗ ████████╗███████╗███████╗██╗  ██╗    ██████╗ ███████╗ ██╗
    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝██║ ██╔╝    ╚════██╗╚════██║███║
    ██████╔╝██████╔╝███████║   ██║   █████╗  █████╗  █████╔╝      █████╔╝    ██╔╝╚██║
    ██╔═══╝ ██╔══██╗██╔══██║   ██║   ██╔══╝  ██╔══╝  ██╔═██╗     ██╔═══╝    ██╔╝  ██║
    ██║     ██║  ██║██║  ██║   ██║   ███████╗███████╗██║  ██╗    ███████╗   ██║   ██║
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝   ╚═╝   ╚═╝
    """)

    def check_intr(self):

        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        try:
            reslt=str(session.get("https://www.motherfuckingwebsite.com/"))
        except Exception as e:
            ErrorHndle().handle_and_exit(mesaage="Internet Connection Not Found",e="Retry Check exceeded")

        if ("200" or "201") in reslt:
            print("connected")
            return True
        else:
            print('Not Connected')
            return False

    def module_chk(self,file="requirements.txt"):
        with(open('requirements.txt','r') )as file:
            to_be_installed=set()
            modules=set(str(file.read()).strip().split("\n"))
            to_be_installed.update(modules)
            try :
                import pkg_resources
                # print(1/0)
            except Exception as errorV:
                ErrorHndle().handle(mesaage="Package ERROR",e=errorV)
                sys.exit()
            finally:
                installed = {pkg.key for pkg in pkg_resources.working_set}
                self.missing = to_be_installed - installed

        self.install()

    def install(self):
        if len(self.missing)==0:
            print("All Installed ....")
        else:
            print(f"Some left , now installing [............]\n{str(self.missing)}")
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *self.missing], stdout=subprocess.DEVNULL)
            # self.module_chk()

class ErrorHndle:
    def handle(self,mesaage="",e=""):
        print("\n---------------------------------------------------------")
        print(f"The Define Pakage Module has encountered an ERROR.\nCheck the \'requirements.txt\'or your code file in the Project Folder\n{mesaage}\n---------->{str(e).upper()}<------")
        print("---------------------------------------------------------\n\n")
        error=str(e)
        if error=="None" or error==" "or error=="":
            error=f"None--{mesaage}"
        with(open("error-log.dat",'a')) as er_file:
            er_file.write("{0}\t--\t{1}".format(error, datetime.datetime.now()))
            er_file.write("\n")
        
    def handle_and_exit(self,mesaage="",e=""):
        self.handle(mesaage,e)
        sys.exit()


if __name__=='__main__':
    setup().check_intr()
