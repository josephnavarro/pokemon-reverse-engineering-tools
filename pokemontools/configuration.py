"""
Configuration
"""
import os


class ConfigException(Exception):
    """
    Configuration error. Maybe a missing config variable.
    """


class Config:
    """
    The Config class handles all configuration for pokemontools. Other classes
    and functions use a Config object to determine where expected files can be
    located.
    """

    def __init__(self, **kwargs):
        """
        Store all parameters.
        """
        self._config = {}

        for (key, value) in kwargs.items():
            if key not in self.__dict__:
                self._config[key] = value
            else:
                raise ConfigException(
                    f"Can't store \"{key}\" in configuration because the key conflicts with an existing property."
                )

        if "path" not in self._config:
            self._config["path"] = os.getcwd()

        # vba save states go into ./save-states/
        if "save_state_path" not in self._config:
            self._config["save_state_path"] = os.path.join(self._config["path"], "save-states/")

        # assume rom is at ./baserom.gbc
        if "rom" not in self._config:
            self._config["rom_path"] = os.path.join(self._config["path"], "baserom.gbc")

    def __getattr__(self, key):
        """
        Grab the value from the class properties, then check the configuration,
        and raise an exception if nothing works.
        """
        if key in self.__dict__:
            return self.__dict__[key]
        elif key in self._config:
            return self._config[key]
        else:
            raise ConfigException(
                f"no config found for \"{key}\""
            )
