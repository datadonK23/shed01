import QtQuick 1.1

Rectangle {
    id: recQ1
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
        anchors.top: recQ1.top
        anchors.topMargin: 40
        anchors.horizontalCenter: recQ1.horizontalCenter

        color: "#f9f2e7"
        border.color: "#8fbe00"
        border.width: 10
        radius: 8

        Text {
            id: infoText
            anchors.centerIn: infoRec

            text: "1" + " / " + "6"
            font.pointSize: 42
            font.family: "Verdana"
            color: "#515151"
        }
    }

    Grid {
        id: gridQuestion
        columns: 2
        spacing: 20
        anchors.centerIn: recQ1
        anchors.verticalCenterOffset: - recQ1.height / 5

        Rectangle{
            // TITEL
            id: recQTitel

            width: 200
            height: 200

            color: "#f9f2e7"
            border.color: "#00a8c6"
            border.width: 10
            radius: 8


            Text {
                id: titelQ1
                anchors.centerIn: recQTitel
                text: "Q1"
                horizontalAlignment: Text.AlignHCenter
                font.pointSize: 80
                font.bold: true
                font.family: "Verdana"
                color: "#9e9e9e"
            }

        }

        Rectangle {
            // QUESTION
            id: recQ1txt
            width: 800
            height: 200
            color: "#F9F2E7"
            border.color: "#00A8C6"
            border.width: 10
            radius: 8

            Text {
                id: txtQ1
                anchors.fill: recQ1txt
                anchors.leftMargin: 10

                text: "Wie wichtig ist Ihnen, selbst Gemüse anzubauen?"
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
        anchors.centerIn: recQ1
        anchors.verticalCenterOffset: recQ1.height / 7

        Button {
            id: button1
            text: "\uf068 \uf068"
            onButtonClick: itemVal01 = 1
        }
        Button {
            id: button2
            text: "\uf068"
            onButtonClick: itemVal01 = 2
        }
        Button {
            id: button3
            text: "\uf10c"
            onButtonClick: itemVal01 = 3
        }
        Button {
            id: button4
            text: "\uf067"
            onButtonClick: itemVal01 = 4
        }
        Button {
            id: button5
            text: "\uf067 \uf067"
            onButtonClick: itemVal01 = 5
        }
    }

    Grid {
        id: gridNavButtons
        columns: 2
        spacing: 500
        anchors.centerIn: recQ1
        anchors.verticalCenterOffset: recQ1.height / 2.5

        NavButton {
            id: navButtonBack
            text: "\uf060"

            onButtonClick: quesDialogChange.source = "./Start.qml"
        }
        NavButton {
            id: navButtonForw
            text: "\uf061"

            onButtonClick: quesDialogChange.source = "./Question02.qml"
        }
    }
}
