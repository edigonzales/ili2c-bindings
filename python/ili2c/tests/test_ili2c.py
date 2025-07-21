
from ili2c import Ili2c
import os
import tempfile
import time

TEST_DATA_PATH = "ili2c/tests/data/"

def test_create_ilismeta16_ok():
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Temp dir path:", tmpdir)
        xtf_file = os.path.join(tmpdir, 'SO_ARP_SEin_Konfiguration_20250116.xtf')
        result = Ili2c.create_ilismeta16(TEST_DATA_PATH+"SO_ARP_SEin_Konfiguration_20250116.ili", xtf_file)
        assert result == True

        with open(xtf_file, 'r', encoding='utf-8') as f:
            file_content = f.read()

        search_str = '<IlisMeta16:Role ili:tid="SO_ARP_SEin_Konfiguration_20250115.Grundlagen.Thema_Objektinfo.Thema_R">'
        assert search_str in file_content

# try/finally wohl nicht mehr nötig, weil ich jetzt den FileLogger im Java-Code korrekt schliesse.
def test_compile_model_ok():
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Temp dir path:", tmpdir)
        log_file = os.path.join(tmpdir, 'ili2c.log')
        try:
            result = Ili2c.compile_model(TEST_DATA_PATH+"SO_ARP_SEin_Konfiguration_20250116.ili", log_file)
            assert result == True

            with open(log_file, 'r', encoding='utf-8') as f:
                file_content = f.read()

            search_str = 'Info: ...compiler run done'
            assert search_str in file_content
        finally:
            # Ensure cleanup after test
            if os.path.exists(log_file):
                try:
                    # Retry mechanism to handle potential file locks
                    retries = 5
                    for _ in range(retries):
                        try:
                            os.remove(log_file)
                            break
                        except PermissionError:
                            print("PermissionError while removing log file. Retrying...")
                            time.sleep(0.5)  # Add a small delay before retrying
                    else:
                        print(f"Failed to remove log file after {retries} retries.")
                except Exception as e:
                    print(f"Error removing log file: {e}")

def test_compile_model_fail():
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Temp dir path:", tmpdir)
        log_file = os.path.join(tmpdir, 'ili2c.log')
        try:
            result = Ili2c.compile_model(TEST_DATA_PATH+"Test1.ili", log_file)
            assert result == False

            with open(log_file, 'r', encoding='utf-8') as f:
                file_content = f.read()

            search_str = 'found \'XXCLASS\''
            assert search_str in file_content
            
            search_str = '...compiler run failed'
            assert search_str in file_content
        finally:
            # Ensure cleanup after test
            if os.path.exists(log_file):
                try:
                    # Retry mechanism to handle potential file locks
                    retries = 5
                    for _ in range(retries):
                        try:
                            os.remove(log_file)
                            break
                        except PermissionError:
                            print("PermissionError while removing log file. Retrying...")
                            time.sleep(0.5)  # Add a small delay before retrying
                    else:
                        print(f"Failed to remove log file after {retries} retries.")
                except Exception as e:
                    print(f"Error removing log file: {e}")

def test_pretty_print_ok():
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Temp dir path:", tmpdir)
        log_file = os.path.join(tmpdir, 'ili2c.log')
        result = Ili2c.pretty_print(TEST_DATA_PATH+"SO_ARP_SEin_Konfiguration_20250116.ili")
        assert result == True