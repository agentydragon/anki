load("@my_deps//:requirements.bzl", "requirement")

py_library(
    name = "anki",
    srcs = [
        "backend.py",
        "cards.py",
        "collection.py",
        "consts.py",
        "db.py",
        "decks.py",
        "errors.py",
        "exporting.py",
        "find.py",
        "lang.py",
        "latex.py",
        "media.py",
        "models.py",
        "mpv.py",
        "notes.py",
        "sched.py",
        "schedv2.py",
        "sound.py",
        "statsbg.py",
        "stats.py",
        "stdmodels.py",
        "storage.py",
        "sync.py",
        "tags.py",
        "types.py",
        "utils.py",
        "hooks.py",
        "__init__.py",
        "//anki/importing:anki2.py",
        "//anki/importing:apkg.py",
        "//anki/importing:base.py",
        "//anki/importing:csvfile.py",
        "//anki/importing:__init__.py",
        "//anki/importing:mnemo.py",
        "//anki/importing:noteimp.py",
        "//anki/importing:pauker.py",
        "//anki/importing:supermemo_xml.py",
        "//anki/template:hint.py",
        "//anki/template:furigana.py",
        "//anki/template:template.py",
        "//anki/template:view.py",
        "//anki/template:__init__.py",
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
