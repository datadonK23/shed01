import QtQuick 1.1

Rectangle {
    id: recQ4
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
        anchors.top: recQ4.top
        anchors.topMargin: 40
        anchors.horizontalCenter: recQ4.horizontalCenter

        color: "#f9f2e7"
        border.color: "#8fbe00"
        border.width: 10
        radius: 8

        Text {
            id: infoText
            anchors.centerIn: infoRec

            text: "4" + " / " + "6"
            font.pointSize: 42
            font.family: "Verdana"
            color: "#515151"
        }
    }

    Grid {
        id: gridQuestion
        columns: 2
        spacing: 20
        anchors.centerIn: recQ4
        anchors.verticalCenterOffset: - recQ4.height / 5

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
                id: titelQ4
                anchors.centerIn: recQTitel
                text: "Q4"
                horizontalAlignment: Text.AlignHCenter
                font.pointSize: 80
                font.bold: true
                font.family: "Verdana"
                color: "#9e9e9e"
            }

        }

        Rectangle {
            // QUESTION
            id: recQ4txt
            width: 800
            height: 200
            color: "#F9F2E7"
            border.color: "#00A8C6"
            border.width: 10
            radius: 8

            Text {
                id: txtQ4
                anchors.fill: recQ4txt
                anchors.leftMargin: 10

                text: "Wieviele Einwohner hat Ihre Gemeinde?"
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
        columns: 5
        spacing: 20
        anchors.centerIn: recQ4
        anchors.verticalCenterOffset: recQ4.height / 7

        Button {
            id: button1
            text: "< 1.000"
            fontSize: 16
            onButtonClick: itemVal04 = 1
        }
        Button {
            id: button2
            text: "1.000-2.500"
            fontSize: 14
            onButtonClick: itemVal04 = 2
        }
        Button {
            id: button3
            text: "2.500-5.000"
            fontSize: 14
            onButtonClick: itemVal04 = 3
        }
        Button {
            id: button4
            text: "5.000-30.000"
            fontSize: 14
            onButtonClick: itemVal04 = 4
        }
        Button {
            id: button5
            text: "> 30.000"
            fontSize: 16
            onButtonClick: itemVal04 = 5
        }
    }

    Grid {
        id: gridNavButtons
        columns: 2
        spacing: 500
        anchors.centerIn: recQ4
        anchors.verticalCenterOffset: recQ4.height / 2.5

        NavButton {
            id: navButtonBack
            text: "\uf060"

            onButtonClick: quesDialogChange.source = "./Question03.qml"
        }
        NavButton {
            id: navButtonForw
            text: "\uf061"

            onButtonClick: quesDialogChange.source = "./Question05.qml"
        }
    }
}
