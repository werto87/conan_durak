from conans import ConanFile, tools
from conans.tools import check_min_cppstd
import os


class Durak(ConanFile):
    name = "durak"
    homepage = "https://github.com/werto87/durak"
    description = "durak logic"
    topics = ("durak")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "compiler"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")
        self.options["boost"].header_only = True
        self.options["fmt"].header_only = True

    def requirements(self):
        self.requires("magic_enum/0.7.2")
        self.requires("pipes/1.0.0")
        self.requires("range-v3/0.11.0")
        self.requires("fmt/7.1.3")
        self.requires("boost/1.76.0")

    def package(self):
        self.copy(pattern="*", dst="include",
                  src=os.path.join(self._source_subfolder))

    def package_id(self):
        self.info.header_only()
