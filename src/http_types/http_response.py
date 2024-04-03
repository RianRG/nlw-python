from typing import Dict

class HttpResponse:
  def __init__(self, body: Dict, statusCode: int):
    self.body = body
    self.statusCode = statusCode