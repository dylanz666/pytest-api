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

    def run(self, fast_fail=False, matcher="", cases="", concurrency=1, mark=""):
        args = ["-v", "-s", '--alluredir', self.results_dir]
        if fast_fail:
            args.append("-x")
        if matcher:
            args.append("-k")
            args.append(matcher)
        if cases:
            if cases is tuple:
                args += cases
            else:
                args += cases.split(",")
        if mark:
            args.append("-m")
            args.append(mark)
        if concurrency > 1:
            args.append("-n")
            args.append(str(concurrency))
        print("pytest", " ".join(args))
        pytest.main(args)
        return self


if __name__ == '__main__':
    fire.Fire(Runner)
