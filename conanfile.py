from conans import ConanFile, CMake, tools


class Fmi4cppConan(ConanFile):
    name = "FMI4cpp"
    version = "0.7.0-RC2"
    license = "MIT"
    author = "Lars Ivar Hatledal larsivarhatledal@gmail.com"
    url = "https://github.com/NTNU-IHB/FMI4cpp"
    description = "FMI 2.0 implementation written in modern C++"
    topics = ("FMI", "co-simulation", "model exchange")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "curl": [True, False]
    }
    default_options = (
        "shared=True",
        "curl=False",
        "boost:shared=True",
        "libzip:shared=True"
    )
    generators = "cmake"

    requires = (
        "boost/1.66.0@conan/stable",
        "libzip/1.5.1@bincrafters/stable"
    )
       
    def source(self):
        self.run("git clone https://github.com/NTNU-IHB/FMI4cpp.git")
        self.run("cd FMI4cpp && git checkout v" + self.version)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder = "FMI4cpp",
        defs = {
            "FMI4CPP_USING_CONAN": "ON",
            "FMI4CPP_BUILD_TESTS": "OFF",
            "FMI4CPP_BUILD_EXAMPLES": "OFF",
            "FMI4CPP_BUILD_TOOL": "OFF",
            "FMI4CPP_WITH_CURL": "ON" if self.options.curl else "OFF"
        })
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["fmi4cpp"]
