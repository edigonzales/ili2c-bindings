
from ili2c import Ili2c
import os
import tempfile

TEST_DATA_PATH = "ili2c/tests/data/"

def test_create_ilismetas16_ok():
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Temp dir path:", tmpdir)
        xtf_file = os.path.join(tmpdir, 'SO_ARP_SEin_Konfiguration_20250116.xtf')
        try:
            result = Ili2c.create_ilismetas16(TEST_DATA_PATH+"SO_ARP_SEin_Konfiguration_20250116.ili", xtf_file)
            assert result == True

            with open(xtf_file, 'r', encoding='utf-8') as f:
                file_content = f.read()

            search_str = '<IlisMeta16:Role ili:tid="SO_ARP_SEin_Konfiguration_20250115.Grundlagen.Thema_Objektinfo.Thema_R">'
            assert search_str in file_content
        finally:
            # Make sure the log file is explicitly closed and handled before cleanup
            if os.path.exists(log_file):
                os.remove(log_file)

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
            # Make sure the log file is explicitly closed and handled before cleanup
            if os.path.exists(log_file):
                os.remove(log_file)

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
            # Make sure the log file is explicitly closed and handled before cleanup
            if os.path.exists(log_file):
                os.remove(log_file)

def test_pretty_print_ok():
    with tempfile.TemporaryDirectory() as tmpdir:
        print("Temp dir path:", tmpdir)
        log_file = os.path.join(tmpdir, 'ili2c.log')
        result = Ili2c.pretty_print(TEST_DATA_PATH+"SO_ARP_SEin_Konfiguration_20250116.ili")
        assert result == True