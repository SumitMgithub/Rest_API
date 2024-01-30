from flask import Flask, request, jsonify
from docx import Document

app = Flask(__name__)


@app.route('/read_doc', methods=['POST'])
def read_doc():
    try:
        # Assuming the uploaded file is in 'doc_file' form field
        uploaded_file = request.files['doc_file']

        # Check if the file is a DOC file
        if uploaded_file.filename.endswith('.docx'):
            # Read the DOCX file
            doc = Document(uploaded_file)

            # Extract text from paragraphs
            content = ""
            for paragraph in doc.paragraphs:
                content += paragraph.text + '\n'

            return jsonify({"content": content})
        else:
            return jsonify({"error": "Invalid file format. Please upload a DOCX file."})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
