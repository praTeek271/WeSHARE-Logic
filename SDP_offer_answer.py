import sys
import subprocess
import datetime
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
import asyncio
import requests

class SDPOfferAnswerGenerator:
    def __init__(self):
        self.pc = RTCPeerConnection()
        self.offer = None
        self.answer = None

    async def create_offer(self):
        try:
        # for vedio channel
        #{
            video_track = VideoStreamTrack()
            self.pc.addTrack(video_track) 
        #}
        except Exception as e:
            ErrorHndle().handle_and_exit(mesaage="Video Track creation ERROR",e=e)
        offer = await self.pc.createOffer()
        await self.pc.setLocalDescription(offer)
        self.offer = offer
        return offer

    async def create_answer(self, offer):
        try:
            await self.pc.setRemoteDescription(offer)
            answer = await self.pc.createAnswer()
            await self.pc.setLocalDescription(answer)
            self.answer = answer
        except Exception as e:
            ErrorHndle().handle(mesaage="Local Offer Was Given")
            answer="None"
        return answer

    async def add_answer(self, answer):
        try:
            await self.pc.setRemoteDescription(answer)
        except Exception as e:
            ErrorHndle().handle(mesaage="Remote Offer Was Given")

    async def main(self):
        await self.create_offer()
        offer=self.offer
        await self.create_answer(offer)
        answer=self.answer
        await self.add_answer(answer)
        print(f"---------->offer -----==\n",offer)
        print(f"---------->answer -----==\n",answer)
        pass
        
class setup:
    def __init__(self):
        self.filepath="requirements.txt"
        self.printME()
        self.check_intr()
        self.module_chk()
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
        reslt=str(requests.get("https://www.motherfuckingwebsite.com/"))
        if ("200" or "201") in reslt:
            print("connected")
            return True

    def module_chk(self,file=self.filepath):
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


if __name__ == '__main__':
    a=setup()
    app = SDPOfferAnswerGenerator()
    asyncio.get_event_loop().run_until_complete(app.main())