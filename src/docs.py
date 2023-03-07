# CAMS Software
# Purpose: Integrated documentation Flask Blueprint
# Date: March 6, 2023 - March 6, 2023
# CTCL 2023

docs_bp = Blueprint("docs_bp", __name__, template_folder="templates/docs", static_folder="static")

# Documentation pages are basically a file browser
@docs_bp.route("/about/<path:path>")
def main_about_docs(path):
    docs_path = f"{docs}/{path}"
    
    if os.path.isdir(docs_path):
        filelist = []
        
        for i in os.listdir(docs_path):
            if os.path.isdir(f"{docs_path}/{i}"):
                tempdict = {"disp": f"{i}/", "link": f"/about/{path}/{i}/"}
                filelist.append(tempdict)
            elif i.endswith(".md"):
                tempdict = {"disp": f"{i}", "link": f"/about/{path}/{i}"}
                filelist.append(tempdict)
    
        return render_template("docs_dir.html", title = f"Documentation - {path}", filelist = filelist)
        
    elif os.path.isfile(docs_path):
        md_converter = Markdown()
        
        with open(docs_path, "r") as f:
            content = md_converter.convert(f.read())
        
        return render_template("docs_file.html", title = f"Documentation - {path}", content = content)
    else:
        return docs_path + " not found", 404
    
