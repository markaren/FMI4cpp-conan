import os

from conans import ConanFile, CMake, tools


class Fmi4cppTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    requires = (
        "FMI4cpp/0.7.0-RC2@FMI4cpp/testing"
    )

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.pdb", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="bin", keep_path=False)
        self.copy('*.so*', dst='bin', keep_path=False)

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%sexample" % os.sep)
