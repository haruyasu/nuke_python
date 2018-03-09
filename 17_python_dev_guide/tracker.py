import nuke
import nuke.rotopaint as rp

node = nuke.toNode('RotoPaint1')
shapeName = 'Bezier1'

curveKnob = node['curves']
shape = curveKnob.toElement(shapeName)

if isinstance(shape, rp.Stroke):
    cubicCurve = shape.evaluate(nuke.frame())
elif isinstance(shape, rp.Shape):
    cubicCurve = shape.evaluate(0, nuke.frame())

fRange = nuke.FrameRange(nuke.getInput('Track Range', '%s-%s' % (nuke.root().firstFrame(), nuke.root().lastFrame())))

tracker = nuke.createNode('Tracker3')
tracker['label'].setValue('tracking %s in %s' % (shape.name, node.name()))
t = tracker['track1']
t.setAnimated()
