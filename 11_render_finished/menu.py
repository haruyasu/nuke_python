import nuke
import renderFinished

nuke.addAfterRender(renderFinished.notify_user)
