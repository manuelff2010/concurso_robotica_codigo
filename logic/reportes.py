class Txtmanager:

    def __init__(self, route):
        self.route = route
        self.file = None

    def open(self, mode='r'):
        self.file = open(self.route, mode, encoding='utf-8')
        return True
    
    def close(self):
        if self.file and not self.file.closed:
            self.file.close()
            self.file = None
            return True
        return False

    def add(self, text):
        if self.file and not self.file.closed:
            self.file.write(text + "\n")
            return True
        return False

    def write_list(self, lines_list):
        if self.file and not self.file.closed:
            lines_with_newlines = [line + "\n" for line in lines_list]
            self.file.writelines(lines_with_newlines)
            return True
        return False

class report():
    def __init__(self, name: str, historial: list[str], estadicticas: dict):
        self.historial = historial
        self.name = name 
        self.estadisticas = estadicticas
        self.manager = Txtmanager(f"./reportes/{name}_report.txt")
    def write(self):
        self.manager.open("w")
        self.manager.write_list(self.historial)

tung = report("tung tung", ["hola cabron"], {})
