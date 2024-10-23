from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="API_FASTAPI",
    settings_file=["settings.toml", ".secrets.toml"],
    environments=True,
    env_switcher="API_FASTAPI_ENV",
)
