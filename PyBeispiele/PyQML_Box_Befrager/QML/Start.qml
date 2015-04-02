import QtQuick 1.1

Rectangle {
    id: recStart
    width: mainRec.width
    height: mainRec.height
    color: "#f9f2e7"
    border.color: "#00a8c6"
    border.width: 20
    radius: 20

    Text {
        id: txtWillkommen
        width: recStart.width
        anchors.horizontalCenter: recStart.horizontalCenter
        anchors.top: recStart.top
        anchors.topMargin: 200
        text: "Willkommen zur Befragung"
        wrapMode: Text.Wrap
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 40
        font.family: "Verdana"
        color: "#515151"
    }

    Text {
        id: txtThema
        width: recStart.width
        anchors.horizontalCenter: recStart.horizontalCenter
        anchors.top: txtWillkommen.bottom
        anchors.topMargin: 20
        text: '"Selbstversorgung mit Nahrungsmittel \n in Oberösterreich"'
        wrapMode: Text.Wrap
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 40
        font.bold: true
        font.family: "Verdana"
        color: "#515151"
    }

    Text {
        id: txtKlickStart
        anchors.horizontalCenter: recStart.horizontalCenter
        anchors.top: txtThema.bottom
        anchors.topMargin: 60
        text: "Klicken Sie auf den Bildschirm um zu starten"
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 28
        font.italic: true
        font.family: "Verdana"
        color: "#515151"
    }

    MouseArea {
        id: mouseStart
        anchors.fill: parent
        onClicked: {
            itemVal01 = 0; itemVal02 = 0; itemVal03 = 0; itemVal04 = 0; itemVal05 = 0; itemVal06 = 0;
            userId += 1
            quesDialogChange.source = "./Question01.qml"
            // console.log(userId)
        }
    }
}
