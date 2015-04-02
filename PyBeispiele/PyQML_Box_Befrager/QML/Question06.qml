import QtQuick 1.1

Rectangle {
    id: recQ6
    width: mainRec.width
    height: mainRec.height
    color: "#f9f2e7"
    border.color: "#00a8c6"
    border.width: 20
    radius: 20

    Rectangle {
        id: infoRec
        width: 300
        height: 80
        anchors.top: recQ6.top
        anchors.topMargin: 40
        anchors.horizontalCenter: recQ6.horizontalCenter

        color: "#f9f2e7"
        border.color: "#8fbe00"
        border.width: 10
        radius: 8

        Text {
            id: infoText
            anchors.centerIn: infoRec

            text: "6" + " / " + "6"
            font.pointSize: 42
            font.family: "Verdana"
            color: "#515151"
        }
    }

    Grid {
        id: gridQuestion
        columns: 2
        spacing: 20
        anchors.centerIn: recQ6
        anchors.verticalCenterOffset: - recQ6.height / 5

        Rectangle{
            // TITEL
            id: recQTitel

            width: 200
            height: 200

            color: "#F9F2E7"
            border.color: "#00A8C6"
            border.width: 10
            radius: 8


            Text {
                id: titelQ6
                anchors.centerIn: recQTitel
                text: "Q6"
                horizontalAlignment: Text.AlignHCenter
                font.pointSize: 80
                font.bold: true
                font.family: "Verdana"
                color: "#9e9e9e"
            }

        }

        Rectangle {
            // QUESTION
            id: recQ6txt
            width: 800
            height: 200
            color: "#F9F2E7"
            border.color: "#00A8C6"
            border.width: 10
            radius: 8

            Text {
                id: txtQ6
                anchors.fill: recQ6txt
                anchors.leftMargin: 10

                text: "Wie alt sind Sie?"
                wrapMode: Text.WordWrap
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.pointSize: 31
                font.family: "Verdana"
                color: "#515151"
            }
        }
    }

    Grid {
        id: gridButtons
        columns: 6
        spacing: 20
        anchors.centerIn: recQ6
        anchors.verticalCenterOffset: recQ6.height / 7

        Button {
            id: button1
            text: "20-"
            fontSize: 32
            onButtonClick: itemVal06 = 1
        }
        Button {
            id: button2
            text: "20-29"
            fontSize: 32
            onButtonClick: itemVal06 = 2
        }
        Button {
            id: button3
            text: "30-39"
            fontSize: 32
            onButtonClick: itemVal06 = 3
        }
        Button {
            id: button4
            text: "40-49"
            fontSize: 32
            onButtonClick: itemVal06 = 4
        }
        Button {
            id: button5
            text: "50-59"
            fontSize: 32
            onButtonClick: itemVal06 = 5
        }
        Button {
            id: button6
            text: "60+"
            fontSize: 32
            onButtonClick: itemVal06 = 6
        }
    }

    Grid {
        id: gridNavButtons
        columns: 2
        spacing: 500
        anchors.centerIn: recQ6
        anchors.verticalCenterOffset: recQ6.height / 2.5

        NavButton {
            id: navButtonBack
            text: "\uf060"

            onButtonClick: quesDialogChange.source = "./Question05.qml"
        }
        NavButton {
            id: navButtonForw
            text: "\uf061"

            onButtonClick: quesDialogChange.source = "./End.qml"
        }
    }
}
