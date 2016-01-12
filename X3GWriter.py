from UM.Mesh.MeshWriter import MeshWriter
from UM.Logger import Logger
from UM.Application import Application
import io
from subprocess import call
import os

class X3GWriter(MeshWriter):
    def __init__(self):
        super().__init__()
        self._gcode = None

    def write(self, file_name, storage_device, mesh_data):
        if "x3g" in file_name:
            scene = Application.getInstance().getController().getScene()
            gcode_list = getattr(scene, "gcode_list")
            if gcode_list:
                f = storage_device.openFile("output.gcode", "wt")
                Logger.log("d", "Writing X3G to file %s", file_name)
                for gcode in gcode_list:
                    f.write(gcode)
                storage_device.closeFile(f)
                Logger.log("d", "App path: %s", os.getcwd())
                Logger.log("d", "File name: %s", file_name)
                command = "gpx.exe -p -m r1d -c gpx.ini output.gcode "+ file_name
                Logger.log("d", "Command: %s", command)
                call(command, shell=True)
                return True

        return False
