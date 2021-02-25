from blabel import LabelWriter

label_writer = LabelWriter("item_template.html", default_stylesheets=("style.css",))
records = [
    {
        "desc": "M3 Flathead Socket Head Cap Screw, 8mm long",
        "vendor": "McMaster-Carr",
        "vendor_num": "92125A128",
        "url": "https://www.mcmaster.com/92125A128",
    }

    # Add more dictionary entries to this list here.
]

label_writer.write_labels(records, target="label.pdf")
