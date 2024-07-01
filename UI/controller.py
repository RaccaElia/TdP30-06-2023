import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        squadre = DAO.getSquadre()

        self._view._ddmethod.options = list(map(lambda x: ft.dropdown.Option(key=x[0], text=f"{x[1]} ({x[0]})"), squadre))

    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        anni = self._model.creaGrafo(self._view._ddmethod.value)
        self._view._ddyear.options = list(map(lambda x: ft.dropdown.Option(x), anni))
        self._view.txtOut.controls.append(ft.Text(f"nodi: {self._model.grafoDetails()[0]}, archi: {self._model.grafoDetails()[1]}"))
        self._view.update_page()

    def handle_dettagli(self, e):
        dettagli = self._model.getDettagli(int(self._view._ddyear.value))
        for arco in dettagli:
            self._view.txtOut.controls.append(ft.Text(f"{arco[0]} --> {arco[1]} = {arco[2]}"))
            self._view.update_page()

    def handle_search(self, e):
        pass