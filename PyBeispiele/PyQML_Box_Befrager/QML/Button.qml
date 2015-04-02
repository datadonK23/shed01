import QtQuick 1.1

Item {
    id: buttonQ
    width: 150
    height: 150

    property alias text: buttonLabel.text
    property alias fontSize: buttonLabel.font.pointSize
    property alias fontBold: buttonLabel.font.bold
    property color buttonRecColor: "#40c0cb"

    signal buttonClick()
    onButtonClick: {
        // test
        // console.log(buttonLabel.text + " clicked" )
    }

    Rectangle {
        id: buttonRec
        anchors.fill: parent

        border.color: "#aee239"
        border.width: 10
        radius: 8

        Text {
            id: buttonLabel
            anchors.fill: parent
            anchors.margins: 5

            FontLoader {id: fontAwesome; source: "../fonts/fontawesome-webfont.ttf"}

            font.pointSize: 45
            font.bold: true
            font.family: fontAwesome.name
            color: "#515151"
            text: "\uf10c"
            //             + : \uf067
            //             - : \uf068
            //             o : \uf10c
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.Wrap
        }

        MouseArea {
            id: buttonMouseArea
            anchors.fill: parent

            hoverEnabled: true

            onClicked:
                buttonClick()
        }

        color: buttonMouseArea.pressed ? Qt.darker(buttonRecColor, 1.5) : buttonRecColor

    }
}
