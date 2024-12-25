from conan import ConanFile
from conan.tools.build import check_min_cppstd
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import get


class Durak(ConanFile):
    name = "durak"
    homepage = "https://github.com/werto87/durak"
    description = "durak logic"
    topics = ("durak")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")

    def requirements(self):
        self.requires("confu_json/[<2]")
        self.requires("boost/[<2]")

    def layout(self):
        cmake_layout(self, src_folder=self.name+"-"+str(self.version))

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.components[self.name].requires = ["boost::headers","confu_json::confu_json"]
