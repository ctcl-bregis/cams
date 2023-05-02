# CAMS Software - CTCL 2021-2023
# March 23, 2023 - May 1    , 2023
# Purpose: Flask Blueprint for the integrated documentation feature

from flask import Blueprint, render_template, abort
from flask_mdeditor import MDEditor
from os import listdir, stat
from os.path import isfile, join, isdir
from datetime import datetime
from markdown import markdown

docs_bp = Blueprint("docs", __name__, template_folder = "templates")

# TODO: Document editing should be only available when the admin user is logged in

# If a file extension is not defined in this dictionary, ".<extension> file" is shown instead for "Type"
filetypes = {"md": "Markdown", "txt": "Text"}


@docs_bp.route("/", defaults = {"path": ""})
@docs_bp.route("/<path:path>")
def index(path):
    basepath = "docs/"
    docspath = basepath + path
    
    # TODO: Have this read from user preferences in DB
    theme = "themes/dark_flat.css"
    
    # Is the path the browser is requesting a file?
    if isfile(basepath + path):
        
        title = f"Documentation - /{path} - View"
        
        with open(docspath) as f:
            content = f.read() 
        
        if path.split(".")[-1] == "md":
            content = markdown(content)
        elif path.split(".")[-1] == "txt":
            content = f"<p>{content}</p>"
        elif len(content) > 1000000:
            # Prevent sending too much data to the browser
            content = "File too long"
        else:
            # Show this instead of having binary data shown in the browser
            content = "File cannot be read"
        
        return render_template("docs_view.jinja2", content = content, title = title, theme = theme)
        
    else:
        title = f"Documentation - /{path}"
    
    contents = []
    for i in listdir(docspath):
        if isfile(f"{docspath}/{i}"):
            mod = datetime.fromtimestamp(stat(docspath).st_mtime).strftime("%X, %b %m, %Y")
        
            # Split by "."
            # This would have, for example, ".tar.gz" show as ".gz file"
            # Those files should not even be in the "docs" directory anyway.
            ftype = i.split(".")[-1]
            # KeyError is raised if a key does not exist in a dictionary
            try:
                ftype = filetypes[ftype]
            except KeyError:
                ftype = f".{ftype} file"
        
            fsize = stat(f"{docspath}/{i}").st_size
            contents.append({"file": i, "type": ftype, "mod": mod, "size": fsize})
        elif isdir(f"{docspath}/{i}"):
            mod = datetime.fromtimestamp(stat(docspath).st_mtime).strftime("%X, %b %m, %Y")
            contents.append({"file": i, "type": "Directory", "mod": mod, "size": ""})
    
    return render_template("docs_browse.jinja2", contents = contents, title = title, theme = theme)
