load("@my_deps//:requirements.bzl", "requirement")

package(
    default_visibility = ["//visibility:public"],
)

py_library(
    name = "aqt",
    srcs = [
        "about.py",
        "addcards.py",
        "addons.py",
        "browser.py",
        "clayout.py",
        "customstudy.py",
        "deckbrowser.py",
        "deckchooser.py",
        "deckconf.py",
        "downloader.py",
        "dyndeckconf.py",
        "editcurrent.py",
        "editor.py",
        "errors.py",
        "exporting.py",
        "fields.py",
        "importing.py",
        "__init__.py",
        "main.py",
        "mediasrv.py",
        "modelchooser.py",
        "models.py",
        "overview.py",
        "pinnedmodules.py",
        "preferences.py",
        "profiles.py",
        "progress.py",
        "qt.py",
        "reviewer.py",
        "sound.py",
        "stats.py",
        "studydeck.py",
        "sync.py",
        "tagedit.py",
        "taglimit.py",
        "toolbar.py",
        "update.py",
        "utils.py",
        "webview.py",
        "winpaths.py",
    ],
    deps = [
        requirement("beautifulsoup4"),
        requirement("send2trash"),
        requirement("pyaudio"),
        requirement("requests"),
        requirement("decorator"),
        requirement("markdown"),
        requirement("jsonschema"),
        requirement("typing"),
        requirement("protobuf"),
    ],

    # more requirements:
    #psutil; sys_platform == "win32"
    #distro; sys_platform != "win32" and sys_platform != "darwin"
    #mypy==0.750
    #mypy_protobuf
    ## fixme: when maturin fixes 32 bit support, switch back to pypi
    #git+https://github.com/dae/maturin#egg=maturin; sys_platform == "linux" and platform_machine != "x86_64"
    #maturin; sys_platform != "linux" or platform_machine == "x86_64"
)

#backend_pb2.py
#backend_pb2.pyi
#BUILD
#__init__.pyc
#__pycache__
#template
