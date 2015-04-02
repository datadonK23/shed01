import QtQuick 1.1
import "QML" as Qml

/*
Name: PyQML Box Questionnaire - QML Part
Descripton: Questionnaire app which interacts with Python
Author: donK23 (datadonk23@gmail.com)
*/


Rectangle {
    id: mainRec
    width: 1280
    height: 800

    property int userId: 0
    property int itemVal01: 0
    property int itemVal02: 0
    property int itemVal03: 0
    property int itemVal04: 0
    property int itemVal05: 0
    property int itemVal06: 0

    property variant itemValues: [userId, itemVal01, itemVal02, itemVal03, itemVal04, itemVal05, itemVal06]

    signal clicked()
    signal emitValue(variant itemValues)

    Loader {
        id: quesDialogChange
        source: "./QML/Start.qml"
    }
}
