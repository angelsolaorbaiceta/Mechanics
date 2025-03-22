import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

from structures.out.json import structure_solution_to_json
from structures.out.text import structure_solution_to_string
from structures.parse import parse_structure

# To avoid overloading the server (and paying a high cloud coputing fee) there
# is a maximum number of nodes a structure can have.
MAX_NODES = 100

MIME_TXT = "text/plain"
MIME_JSON = "application/json"
MIME_WHATEVER = "*/*"


class SolveHandler(RequestHandler):
    async def post(self):
        body = self.request.body.decode("utf-8")
        accept = self.request.headers["Accept"]

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

        try:
            structure = parse_structure(body)
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


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s",
    )

    app = Application([(r"/solve", SolveHandler)])
    port = 8080
    app.listen(port)
    logging.info(f"Server started on port {port}")

    IOLoop.current().start()
    IOLoop.current().start()
