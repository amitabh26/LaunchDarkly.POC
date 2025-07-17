import os
from flask import Flask
from dotenv import load_dotenv
import ldclient
from ldclient.config import Config
from ldclient.context import Context

load_dotenv()

app = Flask(__name__)

sdk_key = os.getenv("LAUNCHDARKLY_SDK_KEY")
ldclient.set_config(Config(sdk_key))


@app.route("/")
def home():
    context = Context.builder("amitabh123").kind("user").name("amitabh").build()
    is_active = ldclient.get().variation("Is_Active", context, False)

    return "The feature is ACTIVE 🎉" if is_active else "The feature is INACTIVE 🚫"

if __name__ == "__main__":
    app.run(debug=True)
