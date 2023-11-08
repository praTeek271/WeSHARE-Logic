# run flak server

from app.views import app
from config import setup,ErrorHndle
from threading import Thread


# if __name__ == '__main__':
#     configure_env=Thread(target=setup)
#     configure_env.start()
#     print("\n","Starting Flask Server".center(50,"-"),"\n")
#     try:
#         app.run(debug=True)
#     except Exception as e:
#         ErrorHndle().handle_and_exit(mesaage="Server Stopped",e=str(e))
#     finally:
#         # configure_env.join()
#         print("\n","Server Stopped".center(50,"-"),"\n")


configure_env=Thread(target=setup)
configure_env.start()
print("\n","Starting Flask Server".center(50,"-"),"\n")
try:
    app.run(debug=True)
except Exception as e:
    ErrorHndle().handle_and_exit(mesaage="Server Stopped",e=str(e))
finally:
    # configure_env.join()
    print("\n","Server Stopped".center(50,"-"),"\n")
