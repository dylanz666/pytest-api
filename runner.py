import fire
import os
import pytest


# based on win system
class Runner(object):
    def __init__(self):
        self.results_dir = "allure-results"
        self.report_dir = "allure-report"
        self.environment_file = "environment.properties"

    def __str__(self):
        return ""

    def rebuild_results_dir(self):
        os.system(f"rmdir /S /Q {self.results_dir}")
        os.system(f"mkdir {self.results_dir}")
        return self

    def make_history_dir(self):
        if not os.path.exists(f"{self.results_dir}\\history"):
            os.system(f"mkdir {self.results_dir}\\history\\")
        return self

    def copy_history_dir(self):
        os.system(f"xcopy /E /Y {self.report_dir}\\history\\* {self.results_dir}\\history\\")
        return self

    def set_allure_env(self):
        os.system(f"copy {self.environment_file} {self.results_dir}\\")
        return self

    def generate_allure_report(self):
        os.system(f"allure generate {self.results_dir} -o {self.report_dir} --clean")
        return self

    def generate_report(self):
        self.make_history_dir()
        self.copy_history_dir()
        self.set_allure_env()
        self.generate_allure_report()
        self.rebuild_results_dir()
        return self

    def open_report(self):
        os.system("allure open")
        return self

    def collect_cases(self):
        os.system("pytest --collect-only")
        return self

    def run(self, keyword="", mark="", case_files="", concurrency=1, fast_fail=False, maxfail=0, last_failed=False,
            failed_first=False, ignore=""):
        args = ["-v", "-s", '--alluredir', self.results_dir]
        if keyword:
            args.append("-k")
            args.append(keyword)
        if case_files and case_files is tuple:
            args += case_files
        elif case_files:
            args += case_files.split(",")
        if mark:
            args.append("-m")
            args.append(mark)
        if concurrency > 1:
            args.append("-n")
            args.append(str(concurrency))
        if fast_fail:
            args.append("-x")
        if maxfail > 0:
            args.append(f"--maxfail={str(maxfail)}")
        if last_failed is True:
            args.append("--lf")
        if failed_first is True:
            args.append("--ff")
        if ignore:
            args.append(f"--ignore={str(ignore)}")
        print("pytest", " ".join(args))
        pytest.main(args)
        return self


if __name__ == '__main__':
    fire.Fire(Runner)
