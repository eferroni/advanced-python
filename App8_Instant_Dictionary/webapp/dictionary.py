import justpy as jp
import definition

class Dictionary:
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Dictionary Page", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any english word", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40 border-gray-500")
        input_box = jp.Input(a=input_div, outputdiv=output_div,
                 placeholder="Type in a word here..",
                 classes="m2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:outline-none "
                         "focus:border-purple-500 py-2 px-4 focus:bg-white")
        input_box.on('input', cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = "\n".join(defined)


