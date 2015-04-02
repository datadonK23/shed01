import QtQuick 1.1

Rectangle {
    id: recQ5
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
        anchors.top: recQ5.top
        anchors.topMargin: 40
        anchors.horizontalCenter: recQ5.horizontalCenter

        color: "#f9f2e7"
        border.color: "#8fbe00"
        border.width: 10
        radius: 8

        Text {
            id: infoText
            anchors.centerIn: infoRec

            text: "5" + " / " + "6"
            font.pointSize: 42
            font.family: "Verdana"
            color: "#515151"
        }
    }

    Grid {
        id: gridQuestion
        columns: 2
        spacing: 20
        anchors.centerIn: recQ5
        anchors.verticalCenterOffset: - recQ5.height / 5

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
                id: titelQ5
                anchors.centerIn: recQTitel
                text: "Q5"
                horizontalAlignment: Text.AlignHCenter
                font.pointSize: 80
                font.bold: true
                font.family: "Verdana"
                color: "#9e9e9e"
            }

        }

        Rectangle {
            // QUESTION
            id: recQ5txt
            width: 800
            height: 200
            color: "#F9F2E7"
            border.color: "#00A8C6"
            border.width: 10
            radius: 8

            Text {
                id: txtQ5
                anchors.fill: recQ5txt
                anchors.leftMargin: 10

                text: "Sind Sie männlich oder weiblich?"
                wrapMode: Text.WordWrap
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                font.pointSize: 31
                font.family: "Verdana"
                color: "#515151"
            }
        }
    }

    Row {
        id: rowButtons
        spacing: 80
        anchors.centerIn: recQ5
        anchors.verticalCenterOffset: recQ5.height / 7

        Button {
            id: buttonMale
            fontSize: 80
            fontBold: false
            text: "\uf183"
            onButtonClick: itemVal05 = 1
        }
        Button {
            id: buttonTransgender
            width: 100
            height: 100
            anchors.bottom: rowButtons.bottom
            fontSize: 12
            fontBold: false
            text: "anderes Geschlecht / keine Antwort"
            onButtonClick: itemVal05 = 3
        }
        Button {
            id: buttonFemale
            fontSize: 80
            fontBold: false
            text: "\uf182"
            onButtonClick: itemVal05 = 2
        }
    }

    Grid {
        id: gridNavButtons
        columns: 2
        spacing: 500
        anchors.centerIn: recQ5
        anchors.verticalCenterOffset: recQ5.height / 2.5

        NavButton {
            id: navButtonBack
            text: "\uf060"

            onButtonClick: quesDialogChange.source = "./Question04.qml"
        }
        NavButton {
            id: navButtonForw
            text: "\uf061"

            onButtonClick: quesDialogChange.source = "./Question06.qml"
        }
    }
}
