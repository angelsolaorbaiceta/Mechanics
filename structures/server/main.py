import logging
import os
import pathlib

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, StaticFileHandler

from structures.out.json import structure_solution_to_json
from structures.out.text import structure_solution_to_string
from structures.parse import parse_structure

# To avoid overloading the server (and paying a high cloud coputing fee) there
# is a maximum number of nodes a structure can have.
MAX_NODES = 100

MIME_TXT = "text/plain"
MIME_JSON = "application/json"
MIME_WHATEVER = "*/*"

# Environment configuration
DEV_MODE = os.environ.get("DEV_MODE", "false").lower() == "true"

# Path to static files (compiled Svelte app)
STATIC_PATH = (
    pathlib.Path(__file__).parent.parent / "frontend" / "build"
    if DEV_MODE
    else pathlib.Path(__file__).parent / "static"
)


class CORSMixin:
    def set_cors_headers(self):
        if DEV_MODE:
            self.set_header("Access-Control-Allow-Origin", "*")


class SolveHandler(CORSMixin, RequestHandler):
    async def post(self):
        self.set_cors_headers()

        body = self.request.body.decode("utf-8")
        accept = self.request.headers.get("Accept", MIME_WHATEVER)

        if accept == MIME_TXT:
            wants_text = True
        elif accept in [MIME_JSON, MIME_WHATEVER]:
            wants_text = False
        else:
            self.set_status(406)
            self.write(
                {
                    "message": "Not Acceptable",
                    "availableFormats": [MIME_JSON, MIME_TXT],
                }
            )
            return

        try:
            structure = parse_structure(body)

            if structure.nodes_count > 100:
                self.set_status(400)
                self.write(
                    {
                        "error": {
                            "cause": "definition",
                            "message": f"The structure had more than 100 nodes ({structure.nodes_count})",
                        }
                    }
                )
                return
        except ValueError as e:
            self.set_status(400)
            self.write({"error": {"cause": "definition", "message": str(e)}})
            return
        except RuntimeError as e:
            self.set_status(500)
            self.write({"error": {"cause": "definition", "message": str(e)}})
            return

        solution = structure.solve_structure()

        if wants_text:
            solution_text = structure_solution_to_string(solution)
            self.set_header("Content-Type", MIME_TXT)
            self.write(solution_text)
        else:
            solution_json = structure_solution_to_json(solution)
            self.set_header("Content-Type", MIME_JSON)
            self.write(solution_json)


class IndexFallbackHandler(StaticFileHandler):
    def initialize(self, path, default_filename=None):
        super().initialize(path, default_filename)
        self.root = path
        self.default_filename = default_filename

    def get(self, path, include_body=True):
        # First try to serve the exact file requested
        try:
            return super().get(path, include_body)
        except Exception as e:
            # If that fails, serve the index.html file
            logging.error(f"Error serving {path}: {str(e)}")
            return super().get("index.html", include_body)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s",
    )

    if DEV_MODE:
        logging.info("Running in development mode with CORS enabled for all origins")
    else:
        logging.info("Running in production mode - only same-origin requests allowed")

    logging.info(f"Serving static assets from: {STATIC_PATH}")

    # Setup the application routes
    app = Application(
        [
            (r"/solve", SolveHandler),
            # Serve the Svelte app static files
            (
                r"/(.*)",
                IndexFallbackHandler,
                {"path": str(STATIC_PATH), "default_filename": "index.html"},
            ),
        ]
    )

    port = 8080
    app.listen(port)
    logging.info(f"Server started on port {port}")

    IOLoop.current().start()
