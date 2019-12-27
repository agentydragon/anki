def build_pyuic5(name, src, out):
    # built from: aqt/forms/[thing].py
    native.genrule(
        name = name,
        srcs = [src],
        outs = [out],
        cmd =
            """(echo "# pylint: disable=unsubscriptable-object,unused-import";
	        echo "from anki.lang import _";
		pyuic5 --from-imports $(location """ + src + """) | tail -n +3) | perl -p -e 's/(QtGui\.QApplication\.)?_?translate\(".*?", /_(/; s/, None.*/))/' > "$@" """,
    )
