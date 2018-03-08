import nuke
import nukescripts


class ModalFramePanel(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, "Go to Frame", "uk.co.thefoundry.FramePanel")
        self.frame = nuke.Int_Knob("frame", "Frame:")
        self.addKnob(self.frame)
        self.frame.setValue(nuke.frame())

    def showModalDialog(self):
        result = nukescripts.PythonPanel.showModalDialog(self)
        if result:
            nuke.frame(self.frame.value())


def testModalPanel():
    return ModalFramePanel().showModalDialog()


testModalPanel()
menubar = nuke.menu("Nuke")
menubar.addCommand("&File/Show My Panel", testModalPanel)
