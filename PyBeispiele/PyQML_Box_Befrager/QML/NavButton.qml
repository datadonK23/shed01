import QtQuick 1.1

Item {
    id: navButton
    width: 300
    height: 100

    property alias text: buttonLabel.text
    property color buttonRecColor: "#40c0cb"

    signal buttonClick()
    onButtonClick: {
        // test
        // console.log(buttonLabel.text + " clicked" )
    }

    Rectangle {
        id: buttonRec
        anchors.fill: parent

        border.color: "#8fbe00"
        border.width: 10
        radius: 8

        Text {
            id: buttonLabel
            anchors.centerIn: parent

            FontLoader {id: fontAwesome; source: "../fonts/fontawesome-webfont.ttf"}

            font.pointSize: 45
            font.bold: true
            font.family: fontAwesome.name
            color: "#515151"
            text: "\uf060"
            //             < : \uf060
            //             > : \uf061
        }

        MouseArea {
            id: buttonMouseArea
            anchors.fill: parent

            hoverEnabled: true

            onClicked: buttonClick()
        }

        color: buttonMouseArea.pressed ? Qt.darker(buttonRecColor, 1.5) : buttonRecColor

    }
}


