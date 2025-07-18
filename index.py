import os
from flask import Flask
from dotenv import load_dotenv
import ldclient
from ldclient.config import Config
from ldclient.context import Context


load_dotenv()

#sdk_key = os.getenv("LAUNCHDARKLY_SDK_KEY")


app = Flask(__name__)

ldclient.set_config(Config("sdk-13c430e2-ab20-4c87-9206-d7042340ff24"))


@app.route("/")
def home():
    context = Context.builder("amitabh123").kind("user").name("amitabh").build()
    is_active = ldclient.get().variation("Is_Active", context, False)

    return "The feature is ACTIVE " if is_active else "The feature is INACTIVE "

if __name__ == "__main__":
    app.run(port=8080)
