import json
import os

class ConfigReader:
    """
    Central configuration reader for the automation framework.

    Responsibilities:
    - Load environment configurations (env_config.json)
    - Load execution configurations (execution_config.json)
    - Provide helper methods to access:
        - Base URL
        - Credentials
        - Timeouts
        - Browser and viewport settings
        - Reporting and artifacts
        - Retries, parallelism, trace, and video settings
    """

    # -----------------------------
    # Paths
    # -----------------------------
    PROJECT_ROOT = os.getcwd()
    CONFIG_DIR = os.path.join(PROJECT_ROOT, "config")

    # -----------------------------
    # Private method to read JSON files
    # -----------------------------
    @staticmethod
    def _read_json(file_name: str) -> dict:
        """
        Reads a JSON file from the config directory.

        :param file_name: Name of the JSON config file
        :return: Dictionary with config values
        """
        file_path = os.path.join(ConfigReader.CONFIG_DIR, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Config file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    # -----------------------------
    # Environment config
    # -----------------------------
    @staticmethod
    def get_env_config() -> dict:
        """Returns the environment configuration JSON as a dictionary."""
        return ConfigReader._read_json("env_config.json")

    @staticmethod
    def get_base_url(env: str = None) -> str:
        """
        Returns the base URL for the given environment.

        :param env: Environment name (qa, uat, prod). If None, default_env is used.
        """
        env_config = ConfigReader.get_env_config()
        env = env or env_config.get("default_env")
        return env_config["environments"][env]["base_url"]

    @staticmethod
    def get_credentials(env: str = None) -> dict:
        """
        Returns credentials (username & password) for the given environment.

        :param env: Environment name. If None, default_env is used.
        """
        env_config = ConfigReader.get_env_config()
        env = env or env_config.get("default_env")
        return env_config["environments"][env]["credentials"]

    @staticmethod
    def get_timeouts(env: str = None) -> dict:
        """
        Returns timeouts (page load, element) for the given environment.

        :param env: Environment name. If None, default_env is used.
        """
        env_config = ConfigReader.get_env_config()
        env = env or env_config.get("default_env")
        return env_config["environments"][env]["timeouts"]

    # -----------------------------
    # Execution config
    # -----------------------------
    @staticmethod
    def get_execution_config() -> dict:
        """Returns the execution configuration JSON as a dictionary."""
        return ConfigReader._read_json("execution_config.json")

    @staticmethod
    def get_browser() -> str:
        """Returns the browser type to use (chromium, firefox, webkit)."""
        return ConfigReader.get_execution_config().get("browser", "chromium")

    @staticmethod
    def is_headless() -> bool:
        """Returns True if tests should run in headless mode."""
        return ConfigReader.get_execution_config().get("headless", True)

    @staticmethod
    def get_slow_mo() -> int:
        """Returns Playwright slowMo option in milliseconds."""
        return ConfigReader.get_execution_config().get("slow_mo", 0)

    @staticmethod
    def get_viewport() -> dict:
        """Returns viewport settings (width and height)."""
        return ConfigReader.get_execution_config().get("viewport", {"width": 1280, "height": 720})

    @staticmethod
    def get_artifacts_dir() -> str:
        """Returns the path where reports, videos, traces, and screenshots should be saved."""
        return ConfigReader.get_execution_config().get("artifacts_dir", "test-results")

    @staticmethod
    def get_retries() -> int:
        """Returns the number of retries for failed tests."""
        return ConfigReader.get_execution_config().get("retries", 0)

    @staticmethod
    def get_parallel_workers() -> int:
        """Returns the number of parallel workers for test execution."""
        return ConfigReader.get_execution_config().get("parallel_workers", 1)

    @staticmethod
    def get_trace() -> str:
        """Returns the trace mode for Playwright (on, off, on-failure)."""
        return ConfigReader.get_execution_config().get("trace", "off")

    @staticmethod
    def get_video() -> str:
        """Returns the video recording setting for Playwright (on, off, on-failure)."""
        return ConfigReader.get_execution_config().get("video", "off")
