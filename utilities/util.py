import json
import streamlit as st


DEFAULT_ACCESS_CONTROL = {
	"allow_new_users": True,
	"new_user_block_message": "RSVPs are now closed to new guests.",
	"login_notice": "Sign in is currently limited to guests who are already in the system.",
}

@st.cache_data
def getConfig(config_name:str):
	with open(f"configs/{config_name}.json") as config:
		return json.load(config)


def getAccessControlConfig() -> dict[str, str | bool]:
	try:
		with open("configs/access_control.json") as config_file:
			config = json.load(config_file)
	except FileNotFoundError:
		return dict(DEFAULT_ACCESS_CONTROL)

	return {
		"allow_new_users": bool(config.get("allow_new_users", DEFAULT_ACCESS_CONTROL["allow_new_users"])),
		"new_user_block_message": str(config.get("new_user_block_message", DEFAULT_ACCESS_CONTROL["new_user_block_message"])),
		"login_notice": str(config.get("login_notice", DEFAULT_ACCESS_CONTROL["login_notice"])),
	}
