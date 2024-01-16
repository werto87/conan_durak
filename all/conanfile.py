from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.build import check_min_cppstd
from conan.tools.files import copy, get
from conan.tools.layout import basic_layout
from conan.tools.microsoft import is_msvc
from conan.tools.scm import Version
import os


class Durak(ConanFile):
    name = "durak"
    homepage = "https://github.com/werto87/durak"
    description = "durak logic"
    topics = ("durak")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    package_type = "header-library"
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True





    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "20")
        self.options["boost"].header_only = True
        self.options["fmt"].header_only = True

    def requirements(self):
        self.requires("pipes/1.0.0")
        self.requires("range-v3/0.12.0")
        self.requires("fmt/9.1.0")
        self.requires("confu_json/1.0.0")
        self.requires("boost/1.83.0", force=True)

    def package(self):
        copy(self, "*.h*", src=os.path.join(self.source_folder, "durak"),
             dst=os.path.join(self.package_folder, "include", "durak"))

