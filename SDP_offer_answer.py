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
    # for vedio channel
    #{
        video_track = VideoStreamTrack()
        self.pc.addTrack(video_track) 
    #}
        offer = await self.pc.createOffer()
        await self.pc.setLocalDescription(offer)
        self.offer = offer
        # print("SDP Offer:")
        # print(offer.sdp)
        return offer

    async def create_answer(self, offer):
        await self.pc.setRemoteDescription(offer)
        answer = await self.pc.createAnswer()
        await self.pc.setLocalDescription(answer)
        self.answer = answer
        # print("SDP Answer:")
        # print(answer.sdp)
        return answer

    async def add_answer(self, answer):
        await self.pc.setRemoteDescription(answer)

    async def main(self):
        

class setup:
    def __init__(self):
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

    def module_chk(self):
        with(open('requirements.txt','r') )as file:
            to_be_installed=set()
            modules=set(str(file.read()).strip().split("\n"))
            to_be_installed.update(modules)
            try :
                import pkg_resources
                # print(1/0)
            except Exception as e:
                print("\n---------------------------------------------------------")
                print("The Define Pakage Module was not found on the internet.\nCheck the \'requirements.txt\' file in the Project Folder\n")
                print("---------------------------------------------------------\n\n")
                error=str(e)
                with(open("error-log.dat",'a')) as er_file:
                    er_file.write("{0}\t--\t{1}".format(error, datetime.datetime.now()))
                    er_file.write("\n")
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


if __name__ == '__main__':
    a=setup()
    app = SDPOfferAnswerGenerator()
    asyncio.get_event_loop().run_until_complete(app.main())