document.addEventListener("DOMContentLoaded", function () {
    const editor = document.getElementById("editor");
    const boldBtn = document.getElementById("bold");
    const italicBtn = document.getElementById("italic");
    const undoBtn = document.getElementById("undo");
    const redoBtn = document.getElementById("redo");
    const addLinkBtn = document.getElementById("add-link");
    const listBtn = document.getElementById("list");
    const fontSizeSelect = document.getElementById("inputGroupSelect01");
    const imageBtn = document.getElementById("image");
    const fullNavbar = document.getElementById("fullNavbar");
    const editingPanel = document.getElementById("editingPanel");
    const publishBtn = this.querySelector("#publish-btn");

    function executeCommand(command, value = null) {
        editor.focus();
        document.execCommand(command, false, value);
    }

    boldBtn.addEventListener("click", () => executeCommand("bold"));
    italicBtn.addEventListener("click", () => executeCommand("italic"));
    undoBtn.addEventListener("click", () => executeCommand("undo"));
    redoBtn.addEventListener("click", () => executeCommand("redo"));

    addLinkBtn.addEventListener("click", () => {
        let url = prompt("Enter URL:");
        if (url) {
            executeCommand("createLink", url);
        }
    });

    listBtn.addEventListener("click", () => {
        executeCommand("insertUnorderedList");
    });

    fontSizeSelect.addEventListener("change", () => {
        let value = fontSizeSelect.value;
        let tag;
        switch (value) {
            case "Title":
                tag = "h2";
                break;
            case "Subtitle":
                tag = "h4";
                break;
            case "Subtitle 2":
                tag = "h5";
                break;
            case "Paragraph":
                tag = "p";
                break;
            default:
                tag = "p";
        }
        executeCommand("formatBlock", tag);
    });

    imageBtn.addEventListener("click", () => {
        let input = document.createElement("input");
        input.type = "file";
        input.accept = "image/*";
        input.addEventListener("change", (event) => {
            let file = event.target.files[0];
            if (file) {
                let reader = new FileReader();
                reader.onload = (e) => {
                    executeCommand("insertImage", e.target.result);
                };
                reader.readAsDataURL(file);
            }
        });
        input.click();
    });

    editor.addEventListener("keydown", (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            if (fontSizeSelect.value === "Subtitle") {
                executeCommand("insertHorizontalRule");
            }
            document.execCommand("insertParagraph");
            fontSizeSelect.value = "Paragraph";
            executeCommand("formatBlock", "p");
        }
    });

    window.addEventListener("scroll", () => {
        if (window.scrollY === 0) {
            editingPanel.style.backgroundColor = "rgba(31, 30, 30, 0)";
        } else if (fullNavbar.getBoundingClientRect().top <= 0) {
            editingPanel.style.backgroundColor = "rgba(31, 30, 30, 0.6)";
        } else {
            editingPanel.style.backgroundColor = "rgba(31, 30, 30, 0)";
        }
    });
    publishBtn.addEventListener("click", (e) => {
        e.preventDefault();
        let content = editor.innerHTML;
        let title = document.getElementById("title").value;
        let category = document.getElementById("category").value;
        let description = document.getElementById("description").value;
        
        let data = {
            title: title,
            category: category,
            description: description,
            content: content,
        };
        fetch("/create-article", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    alert("Post published successfully!");
                    window.location.href = "/";
                } else {
                    alert("Post could not be published!");
                }
            });
    });
});