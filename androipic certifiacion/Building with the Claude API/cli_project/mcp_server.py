from mcp.server.fastmcp import FastMCP
from pydantic import Field
mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool(name = "read_doc_contents", description = "Read the contents of a document and return it as a string")
def read_doc_contents(
    doc_id: str = Field(description="The ID of the document to read")
):
      if doc_id not in docs:
        return f"Document with ID '{doc_id}' not found."
      return docs[doc_id]


@mcp.tool(name = "edit_doc", description = "Edit the document by replacing a string in the document with a new string")
def edit_doc(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_string: str = Field(description="The text to replace. Most match exactly, including whilespace."),
    new_string: str = Field(description="The text new text to insert in pleace of the old text")
    ):
        if doc_id not in docs:
            return f"Document with ID '{doc_id}' not found."
        docs[doc_id] = docs[doc_id].replace(old_string, new_string)
        

@mcp.resource(
     "docs://documents",
     mime_type="application/json",
    )
def list_docs() -> list[str]:
    return list(docs.keys())


@mcp.resource(
     "docs://documents/{doc_id}",
     mime_type="text/plain",
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        return f"Document with ID '{doc_id}' not found."
    return docs[doc_id]

# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
