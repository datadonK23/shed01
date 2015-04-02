import QtQuick 1.1

Rectangle {
    id: recEnd
    width: mainRec.width
    height: mainRec.height
    color: "#f9f2e7"
    border.color: "#00a8c6"
    border.width: 20
    radius: 20

    Text {
        id: txtEnd
        anchors.centerIn: recEnd
        text: "Danke für Ihre Teilnahme!"
        wrapMode: Text.Wrap
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 42
        font.italic: true
        font.bold: false
        font.family: "Verdana"
        color: "#515151"
    }

    Text {
        id: txtKlickBenutzer
        anchors.horizontalCenter: recEnd.horizontalCenter
        anchors.top: txtEnd.bottom
        anchors.topMargin: 60
        text: "Neuer Benutzer?"
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 28
        font.italic: true
        font.bold: true
        font.family: "Verdana"
        color: "#515151"
    }

    Text {
        id: txtKlickNeu
        anchors.horizontalCenter: txtKlickBenutzer.horizontalCenter
        anchors.top: txtKlickBenutzer.bottom
        text: "Klicken Sie auf den Bildschirm"
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 28
        font.italic: true
        font.family: "Verdana"
        color: "#515151"
    }

    MouseArea {
        id: mouseEnd
        anchors.fill: parent
        onClicked: {
            //console.log(itemValues)
            emitValue(itemValues)

            quesDialogChange.source = "./Start.qml"
            //console.log("ende")
            //Qt.quit()
        }
    }
}
