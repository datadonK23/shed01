import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.XmlListModel 2.0

/*
Name: WahlenVis_EUinSR
Descripton: Visualize results of EU elections 2014 in Steyr (Austria)
Author: donK23 (datadonk23@gmail.com)
Made in Steyr
*/

Window {
    id: rootWin
    visible: true
    width: Screen.width
    height: Screen.height

    Component{
        id: compListHeader
        Grid{
            id: gridPartei
            columns: 4
            rows: 2

            Rectangle{
                id: col01
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Image {
                    id: imgFlag
                    anchors.centerIn: parent
                    width: parent.width - 30
                    height: parent.height - 60
                    source: "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/1200px-Flag_of_Europe.svg.png"
                }
            }

            Rectangle{
                id: col02
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Text {
                    id: ueberErgebn
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 40
                    font.letterSpacing: - 1
                    font.bold: true
                    font.family: "sans-serif"
                    horizontalAlignment: Text.AlignRight
                    color: "white"
                    smooth: true
                    text: "Ergebnisse"
                }
            }

            Rectangle{
                id: col03
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Text {
                    id: ueberJahr
                    anchors.left: parent.left
                    anchors.leftMargin: 5
                    anchors.verticalCenter: parent.verticalCenter
                    font.pixelSize: 40
                    font.letterSpacing: -3
                    font.bold: true
                    font.family: "sans-serif"
                    horizontalAlignment: Text.AlignLeft
                    color: "white"
                    smooth: true
                    text: "2014"
                }
            }

            Rectangle{
                id: col04
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Image {
                    id: imgSR
                    anchors.centerIn: parent
                    width: parent.width
                    height: parent.height
                    source: "qrc:/data/map_SRNamen.png"
                }
            }

            Rectangle{
                id: col1
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ff8800"
                Text {
                    id: namePartei
                    anchors.centerIn: parent
                    font.pixelSize: 55
                    font.family: "sans-serif"
                    font.bold: true
                    color: "white"
                    smooth: true
                    text: "Partei"
                }
            }

            Rectangle{
                id: col2
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ff8800"
                Text {
                    id: stimmenPartei
                    anchors.centerIn: parent
                    font.pixelSize: 40
                    font.letterSpacing: -4
                    font.family: "sans-serif"
                    color: "white"
                    smooth: true
                    text: "Stimmen"
                }
            }

            Rectangle{
                id: col3
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ff8800"
                Text {
                    id: prozPartei
                    anchors.centerIn: parent
                    font.pixelSize: 40
                    font.family: "sans-serif"
                    color: "white"
                    smooth: true
                    text: "%"
                }
            }

            Rectangle{
                id: col4
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ff8800"
                Text {
                    id: diffPartei
                    anchors.centerIn: parent
                    font.pixelSize: 37
                    font.letterSpacing: -4
                    font.family: "sans-serif"
                    lineHeight: 0.7
                    horizontalAlignment: Text.AlignHCenter
                    color: "white"
                    smooth: true
                    text: "Diff. \n 2009"
                }
            }
        }
    }

    Component {
        id: listDel
        Grid{
            id: gridPartei
            columns: 4
            spacing: 5

            Rectangle{
                id: col1
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Text {
                    id: namePartei
                    anchors.centerIn: parent
                    font.pixelSize: 50
                    font.letterSpacing: -4
                    font.family: "sans-serif"
                    color: "white"
                    smooth: true
                    text: name
                }
            }

            Rectangle{
                id: col2
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Text {
                    id: stimmenPartei
                    anchors.centerIn: parent
                    font.pixelSize: 50
                    font.family: "sans-serif"
                    color: "white"
                    smooth: true
                    text: stimmen
                }
            }

            Rectangle{
                id: col3
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Text {
                    id: prozPartei
                    anchors.centerIn: parent
                    font.pixelSize: 50
                    font.family: "sans-serif"
                    color: "white"
                    smooth: true
                    text: prozent
                }
            }

            Rectangle{
                id: col4
                width: rootWin.width / 4
                height: rootWin.height / 6
                color: "#ffbb33"
                Text {
                    id: diffPartei
                    anchors.centerIn: parent
                    font.pixelSize: 50
                    font.family: "sans-serif"
                    color: "white"
                    smooth: true
                    text: diff
                }
            }
        }
    }

    ListView {
        id: listMain
        anchors.fill: parent
        spacing: 8

        header: compListHeader
        model: xmlModel
        delegate: listDel
    }

    XmlListModel {
        id: xmlModel
        source: "qrc:/data/euw14SR.xml"
        query: "/dataset/partei"

        XmlRole { name: "name"; query: "name/string()" }
        XmlRole { name: "stimmen"; query: "stimmen/string()" }
        XmlRole { name: "prozent"; query: "prozent/string()" }
        XmlRole { name: "diff"; query: "diff1409/string()"}
    }
}
