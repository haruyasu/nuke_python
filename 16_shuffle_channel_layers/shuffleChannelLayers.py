import nuke, nukescripts

def uniqueChannelLayerList(nodeToProcess):
    rawChannelList = nodeToProcess.channels()
    channelLayerList = []

    for channel in rawChannelList:
        channelLayer = channel.split(".")
        channelLayerList.append(channelLayer[0])

    return list(set(channelLayerList))

def shuffleChannelLayers():
    selectedNodes = nuke.selectedNodes()

    for readNode in selectedNodes:
        if readNode.Class() == "Read":
            uniqueChannelLayers = uniqueChannelLayerList(readNode)

            for channelLayer in uniqueChannelLayers:
                shuffleNode = nuke.nodes.Shuffle(name="Shuffle_" + channelLayer)
                shuffleNode.knob("in").setValue(channelLayer)
                shuffleNode.setInput(0, readNode)
                curveNode = nuke.nodes.CurveTool(name="AC_" + channelLayer,
                                                    inputs=[shuffleNode],
                                                    operation="Auto Crop")
                curveNode.knob("ROI").setValue([0, 0, shuffleNode.width(), shuffleNode.height()])
                nuke.execute(curveNode, readNode.knob("first").value(), readNode.knob("last").value())
                cropNode = nuke.nodes.Crop(name="Crop_" + channelLayer, inputs=[curveNode])
                cropNode.knob("box").copyAnimations(curveNode.knob("autocropdata").animations())

def selectAllClassNodes():
    nukescripts.clear_selection_recursive()
    userInput = nuke.getInput("What type of node do you want to select? \n" +
                                "(Correct capitalization matters!) \n" +
                                "no spaces", "Crop")

    for node in nuke.allNodes():
        if node.Class() == userInput:
            node.setSelected(True)

    nuke.message("Selected %d %s nodes." % (len(nuke.selectedNodes()), userInput))
