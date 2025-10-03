# SNMP MIB module (TERACOM-TCW260-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teracom\TERACOM-TCW260-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:11 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    snmpMIB.setRevisions(
        ("2024-06-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RealValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class DigitalValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class AlarmLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("normal", 1),
          ("indeterminate", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )



class AlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )



class AnalogMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("volt0to10", 0),
          ("ma0to20", 1))
    )



class DigitalMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("openclosed", 0),
          ("risingEdge", 1),
          ("fallingEdge", 2),
          ("bothEdges", 3))
    )



class ChannelParameter1(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("s01", 3),
          ("s02", 4),
          ("s03", 5),
          ("s04", 6),
          ("s05", 7),
          ("s06", 8),
          ("s07", 9),
          ("s08", 10),
          ("s09", 11),
          ("s10", 12),
          ("s11", 13),
          ("s12", 14),
          ("s13", 15),
          ("s14", 16),
          ("s15", 17),
          ("s16", 18),
          ("s17", 19),
          ("s18", 20),
          ("s19", 21),
          ("s20", 22),
          ("s21", 23),
          ("s22", 24),
          ("s23", 25),
          ("s24", 26),
          ("a01", 27),
          ("a02", 28),
          ("a03", 29),
          ("a04", 30),
          ("a05", 31),
          ("a06", 32),
          ("d01", 33),
          ("d02", 34),
          ("d03", 35),
          ("d04", 36))
    )



class ChannelParameter2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("one", 1),
          ("null", 2),
          ("s01", 3),
          ("s02", 4),
          ("s03", 5),
          ("s04", 6),
          ("s05", 7),
          ("s06", 8),
          ("s07", 9),
          ("s08", 10),
          ("s09", 11),
          ("s10", 12),
          ("s11", 13),
          ("s12", 14),
          ("s13", 15),
          ("s14", 16),
          ("s15", 17),
          ("s16", 18),
          ("s17", 19),
          ("s18", 20),
          ("s19", 21),
          ("s20", 22),
          ("s21", 23),
          ("s22", 24),
          ("s23", 25),
          ("s24", 26),
          ("a01", 27),
          ("a02", 28),
          ("a03", 29),
          ("a04", 30),
          ("a05", 31),
          ("a06", 32),
          ("d01", 33),
          ("d02", 34),
          ("d03", 35),
          ("d04", 36))
    )



class ChannelOperand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("multiplication", 1),
          ("division", 2),
          ("sum", 3),
          ("subtract", 4))
    )



class AlarmCondOperand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("larger", 1),
          ("less", 2))
    )



class AlarmChannel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("v01", 1),
          ("v02", 2),
          ("v03", 3),
          ("v04", 4),
          ("v05", 5),
          ("v06", 6),
          ("v07", 7),
          ("v08", 8),
          ("v09", 9),
          ("v10", 10),
          ("v11", 11),
          ("v12", 12),
          ("v13", 13),
          ("v14", 14),
          ("v15", 15),
          ("v16", 16),
          ("v17", 17),
          ("v18", 18),
          ("v19", 19),
          ("v20", 20),
          ("v21", 21),
          ("v22", 22),
          ("v23", 23),
          ("v24", 24))
    )



class AlarmCondLogic(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("and", 1),
          ("or", 2))
    )



class AlarmActionDelay(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class AlarmActionOnReturn(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class AlarmAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trapcond1", 1),
          ("trapcond2", 2),
          ("trapcond1and2", 3),
          ("postiostate", 4),
          ("mail", 5),
          ("mqttpublish", 6))
    )



class DigInputDelay(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )



class ChannelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("general", 0),
          ("cumulative", 1),
          ("discrete", 2),
          ("counter", 3))
    )



class DiscreteAlarmState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )



class MbSenTableIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )



class AnalogInpTableIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )



class DigInpTableIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class ChTableIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )



class AlTableIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )



# MIB Managed Objects in the order of their OIDs

_Teracom_ObjectIdentity = ObjectIdentity
teracom = _Teracom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783)
)
_Tcw260_ObjectIdentity = ObjectIdentity
tcw260 = _Tcw260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_DateTime_Type = DateAndTime
_DateTime_Object = MibScalar
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 1, 3),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 1)
)
_DeviceID_Type = MacAddress
_DeviceID_Object = MibScalar
deviceID = _DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 1, 1),
    _DeviceID_Type()
)
deviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceID.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_DeviceIP_Type = IpAddress
_DeviceIP_Object = MibScalar
deviceIP = _DeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 1, 3),
    _DeviceIP_Type()
)
deviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIP.setStatus("current")
_Parameters_ObjectIdentity = ObjectIdentity
parameters = _Parameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2)
)
_MbSensors_ObjectIdentity = ObjectIdentity
mbSensors = _MbSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1)
)
_MbSensorsTable_Object = MibTable
mbSensorsTable = _MbSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mbSensorsTable.setStatus("current")
_MbSensorsEntry_Object = MibTableRow
mbSensorsEntry = _MbSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1, 1)
)
mbSensorsEntry.setIndexNames(
    (0, "TERACOM-TCW260-MIB", "mbSenIndex"),
)
if mibBuilder.loadTexts:
    mbSensorsEntry.setStatus("current")
_MbSenIndex_Type = MbSenTableIndex
_MbSenIndex_Object = MibTableColumn
mbSenIndex = _MbSenIndex_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1, 1, 1),
    _MbSenIndex_Type()
)
mbSenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbSenIndex.setStatus("current")


class _MbSenDescription_Type(DisplayString):
    """Custom type mbSenDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MbSenDescription_Type.__name__ = "DisplayString"
_MbSenDescription_Object = MibTableColumn
mbSenDescription = _MbSenDescription_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1, 1, 2),
    _MbSenDescription_Type()
)
mbSenDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbSenDescription.setStatus("current")
_MbSenMult_Type = RealValue
_MbSenMult_Object = MibTableColumn
mbSenMult = _MbSenMult_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1, 1, 3),
    _MbSenMult_Type()
)
mbSenMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbSenMult.setStatus("current")
_MbSenOffset_Type = RealValue
_MbSenOffset_Object = MibTableColumn
mbSenOffset = _MbSenOffset_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1, 1, 4),
    _MbSenOffset_Type()
)
mbSenOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbSenOffset.setStatus("current")
_MbSenVal_Type = RealValue
_MbSenVal_Object = MibTableColumn
mbSenVal = _MbSenVal_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1, 1, 5),
    _MbSenVal_Type()
)
mbSenVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbSenVal.setStatus("current")
_MbSenCounter_Type = Counter32
_MbSenCounter_Object = MibTableColumn
mbSenCounter = _MbSenCounter_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 1, 1, 1, 6),
    _MbSenCounter_Type()
)
mbSenCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbSenCounter.setStatus("current")
_AnalogInputs_ObjectIdentity = ObjectIdentity
analogInputs = _AnalogInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2)
)
_AnalogInpTable_Object = MibTable
analogInpTable = _AnalogInpTable_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    analogInpTable.setStatus("current")
_AnalogInpEntry_Object = MibTableRow
analogInpEntry = _AnalogInpEntry_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1, 1)
)
analogInpEntry.setIndexNames(
    (0, "TERACOM-TCW260-MIB", "analogInpIndex"),
)
if mibBuilder.loadTexts:
    analogInpEntry.setStatus("current")
_AnalogInpIndex_Type = AnalogInpTableIndex
_AnalogInpIndex_Object = MibTableColumn
analogInpIndex = _AnalogInpIndex_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1, 1, 1),
    _AnalogInpIndex_Type()
)
analogInpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    analogInpIndex.setStatus("current")


class _AnalogInpDescription_Type(DisplayString):
    """Custom type analogInpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnalogInpDescription_Type.__name__ = "DisplayString"
_AnalogInpDescription_Object = MibTableColumn
analogInpDescription = _AnalogInpDescription_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1, 1, 2),
    _AnalogInpDescription_Type()
)
analogInpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInpDescription.setStatus("current")
_AnalogInpMult_Type = RealValue
_AnalogInpMult_Object = MibTableColumn
analogInpMult = _AnalogInpMult_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1, 1, 3),
    _AnalogInpMult_Type()
)
analogInpMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInpMult.setStatus("current")
_AnalogInpOffset_Type = RealValue
_AnalogInpOffset_Object = MibTableColumn
analogInpOffset = _AnalogInpOffset_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1, 1, 4),
    _AnalogInpOffset_Type()
)
analogInpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInpOffset.setStatus("current")
_AnalogInpMode_Type = AnalogMode
_AnalogInpMode_Object = MibTableColumn
analogInpMode = _AnalogInpMode_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1, 1, 5),
    _AnalogInpMode_Type()
)
analogInpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogInpMode.setStatus("current")
_AnalogInpValue_Type = RealValue
_AnalogInpValue_Object = MibTableColumn
analogInpValue = _AnalogInpValue_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 2, 1, 1, 6),
    _AnalogInpValue_Type()
)
analogInpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogInpValue.setStatus("current")
_DigitalInputs_ObjectIdentity = ObjectIdentity
digitalInputs = _DigitalInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3)
)
_DigitalInpTable_Object = MibTable
digitalInpTable = _DigitalInpTable_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    digitalInpTable.setStatus("current")
_DigitalInpEntry_Object = MibTableRow
digitalInpEntry = _DigitalInpEntry_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1)
)
digitalInpEntry.setIndexNames(
    (0, "TERACOM-TCW260-MIB", "digInpIndex"),
)
if mibBuilder.loadTexts:
    digitalInpEntry.setStatus("current")
_DigInpIndex_Type = DigInpTableIndex
_DigInpIndex_Object = MibTableColumn
digInpIndex = _DigInpIndex_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 1),
    _DigInpIndex_Type()
)
digInpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digInpIndex.setStatus("current")


class _DigInpDescription_Type(DisplayString):
    """Custom type digInpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DigInpDescription_Type.__name__ = "DisplayString"
_DigInpDescription_Object = MibTableColumn
digInpDescription = _DigInpDescription_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 2),
    _DigInpDescription_Type()
)
digInpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digInpDescription.setStatus("current")


class _DigInplowLevel_Type(DisplayString):
    """Custom type digInplowLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DigInplowLevel_Type.__name__ = "DisplayString"
_DigInplowLevel_Object = MibTableColumn
digInplowLevel = _DigInplowLevel_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 3),
    _DigInplowLevel_Type()
)
digInplowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digInplowLevel.setStatus("current")


class _DigInphighLevel_Type(DisplayString):
    """Custom type digInphighLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DigInphighLevel_Type.__name__ = "DisplayString"
_DigInphighLevel_Object = MibTableColumn
digInphighLevel = _DigInphighLevel_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 4),
    _DigInphighLevel_Type()
)
digInphighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digInphighLevel.setStatus("current")
_DigInpMode_Type = DigitalMode
_DigInpMode_Object = MibTableColumn
digInpMode = _DigInpMode_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 5),
    _DigInpMode_Type()
)
digInpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digInpMode.setStatus("current")
_DigInpCloseToOpenDelay_Type = DigInputDelay
_DigInpCloseToOpenDelay_Object = MibTableColumn
digInpCloseToOpenDelay = _DigInpCloseToOpenDelay_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 6),
    _DigInpCloseToOpenDelay_Type()
)
digInpCloseToOpenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digInpCloseToOpenDelay.setStatus("current")
_DigInpOpenToCloseDelay_Type = DigInputDelay
_DigInpOpenToCloseDelay_Object = MibTableColumn
digInpOpenToCloseDelay = _DigInpOpenToCloseDelay_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 7),
    _DigInpOpenToCloseDelay_Type()
)
digInpOpenToCloseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digInpOpenToCloseDelay.setStatus("current")
_DigInpCounterInitValue_Type = Unsigned32
_DigInpCounterInitValue_Object = MibTableColumn
digInpCounterInitValue = _DigInpCounterInitValue_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 8),
    _DigInpCounterInitValue_Type()
)
digInpCounterInitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digInpCounterInitValue.setStatus("current")
_DigInpValue_Type = DigitalValue
_DigInpValue_Object = MibTableColumn
digInpValue = _DigInpValue_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 2, 2, 3, 1, 1, 9),
    _DigInpValue_Type()
)
digInpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digInpValue.setStatus("current")
_MonitorNcontrol_ObjectIdentity = ObjectIdentity
monitorNcontrol = _MonitorNcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3)
)
_Channels_ObjectIdentity = ObjectIdentity
channels = _Channels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1)
)
_ChanTable_Object = MibTable
chanTable = _ChanTable_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    chanTable.setStatus("current")
_ChanEntry_Object = MibTableRow
chanEntry = _ChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1)
)
chanEntry.setIndexNames(
    (0, "TERACOM-TCW260-MIB", "chIndex"),
)
if mibBuilder.loadTexts:
    chanEntry.setStatus("current")
_ChIndex_Type = ChTableIndex
_ChIndex_Object = MibTableColumn
chIndex = _ChIndex_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 1),
    _ChIndex_Type()
)
chIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chIndex.setStatus("current")
_ChType_Type = ChannelType
_ChType_Object = MibTableColumn
chType = _ChType_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 2),
    _ChType_Type()
)
chType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chType.setStatus("current")


class _ChDescription_Type(DisplayString):
    """Custom type chDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChDescription_Type.__name__ = "DisplayString"
_ChDescription_Object = MibTableColumn
chDescription = _ChDescription_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 3),
    _ChDescription_Type()
)
chDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chDescription.setStatus("current")
_ChParam1_Type = ChannelParameter1
_ChParam1_Object = MibTableColumn
chParam1 = _ChParam1_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 4),
    _ChParam1_Type()
)
chParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chParam1.setStatus("current")
_ChOP1_Type = ChannelOperand
_ChOP1_Object = MibTableColumn
chOP1 = _ChOP1_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 5),
    _ChOP1_Type()
)
chOP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chOP1.setStatus("current")
_ChParam2_Type = ChannelParameter2
_ChParam2_Object = MibTableColumn
chParam2 = _ChParam2_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 6),
    _ChParam2_Type()
)
chParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chParam2.setStatus("current")
_ChOP2_Type = ChannelOperand
_ChOP2_Object = MibTableColumn
chOP2 = _ChOP2_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 7),
    _ChOP2_Type()
)
chOP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chOP2.setStatus("current")
_ChCoef1_Type = RealValue
_ChCoef1_Object = MibTableColumn
chCoef1 = _ChCoef1_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 8),
    _ChCoef1_Type()
)
chCoef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCoef1.setStatus("current")
_ChOP3_Type = ChannelOperand
_ChOP3_Object = MibTableColumn
chOP3 = _ChOP3_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 9),
    _ChOP3_Type()
)
chOP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chOP3.setStatus("current")
_ChCoef2_Type = RealValue
_ChCoef2_Object = MibTableColumn
chCoef2 = _ChCoef2_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 10),
    _ChCoef2_Type()
)
chCoef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCoef2.setStatus("current")


class _ChUnit_Type(DisplayString):
    """Custom type chUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChUnit_Type.__name__ = "DisplayString"
_ChUnit_Object = MibTableColumn
chUnit = _ChUnit_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 11),
    _ChUnit_Type()
)
chUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chUnit.setStatus("current")
_ChCumulInitValue_Type = RealValue
_ChCumulInitValue_Object = MibTableColumn
chCumulInitValue = _ChCumulInitValue_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 12),
    _ChCumulInitValue_Type()
)
chCumulInitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chCumulInitValue.setStatus("current")
_ChValue_Type = RealValue
_ChValue_Object = MibTableColumn
chValue = _ChValue_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 13),
    _ChValue_Type()
)
chValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chValue.setStatus("current")
_ChCounter_Type = Counter32
_ChCounter_Object = MibTableColumn
chCounter = _ChCounter_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 14),
    _ChCounter_Type()
)
chCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCounter.setStatus("current")
_ChAlarmStatus_Type = AlarmLevel
_ChAlarmStatus_Object = MibTableColumn
chAlarmStatus = _ChAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 1, 1, 1, 15),
    _ChAlarmStatus_Type()
)
chAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chAlarmStatus.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2)
)
_AlarmsTable_Object = MibTable
alarmsTable = _AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    alarmsTable.setStatus("current")
_AlarmsEntry_Object = MibTableRow
alarmsEntry = _AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1)
)
alarmsEntry.setIndexNames(
    (0, "TERACOM-TCW260-MIB", "alIndex"),
)
if mibBuilder.loadTexts:
    alarmsEntry.setStatus("current")
_AlIndex_Type = AlTableIndex
_AlIndex_Object = MibTableColumn
alIndex = _AlIndex_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 1),
    _AlIndex_Type()
)
alIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alIndex.setStatus("current")


class _AlDescription_Type(DisplayString):
    """Custom type alDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AlDescription_Type.__name__ = "DisplayString"
_AlDescription_Object = MibTableColumn
alDescription = _AlDescription_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 2),
    _AlDescription_Type()
)
alDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alDescription.setStatus("current")
_AlCond1Channel_Type = AlarmChannel
_AlCond1Channel_Object = MibTableColumn
alCond1Channel = _AlCond1Channel_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 3),
    _AlCond1Channel_Type()
)
alCond1Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond1Channel.setStatus("current")
_AlCond1Operand_Type = AlarmCondOperand
_AlCond1Operand_Object = MibTableColumn
alCond1Operand = _AlCond1Operand_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 4),
    _AlCond1Operand_Type()
)
alCond1Operand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond1Operand.setStatus("current")
_AlCond1Limit_Type = RealValue
_AlCond1Limit_Object = MibTableColumn
alCond1Limit = _AlCond1Limit_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 5),
    _AlCond1Limit_Type()
)
alCond1Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond1Limit.setStatus("current")
_AlCond1Hys_Type = RealValue
_AlCond1Hys_Object = MibTableColumn
alCond1Hys = _AlCond1Hys_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 6),
    _AlCond1Hys_Type()
)
alCond1Hys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond1Hys.setStatus("current")
_AlCond1AlarmState_Type = DiscreteAlarmState
_AlCond1AlarmState_Object = MibTableColumn
alCond1AlarmState = _AlCond1AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 7),
    _AlCond1AlarmState_Type()
)
alCond1AlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond1AlarmState.setStatus("current")
_AlCondLogic_Type = AlarmCondLogic
_AlCondLogic_Object = MibTableColumn
alCondLogic = _AlCondLogic_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 8),
    _AlCondLogic_Type()
)
alCondLogic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCondLogic.setStatus("current")
_AlCond2Channel_Type = AlarmChannel
_AlCond2Channel_Object = MibTableColumn
alCond2Channel = _AlCond2Channel_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 9),
    _AlCond2Channel_Type()
)
alCond2Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond2Channel.setStatus("current")
_AlCond2Operand_Type = AlarmCondOperand
_AlCond2Operand_Object = MibTableColumn
alCond2Operand = _AlCond2Operand_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 10),
    _AlCond2Operand_Type()
)
alCond2Operand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond2Operand.setStatus("current")
_AlCond2Limit_Type = RealValue
_AlCond2Limit_Object = MibTableColumn
alCond2Limit = _AlCond2Limit_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 11),
    _AlCond2Limit_Type()
)
alCond2Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond2Limit.setStatus("current")
_AlCond2Hys_Type = RealValue
_AlCond2Hys_Object = MibTableColumn
alCond2Hys = _AlCond2Hys_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 12),
    _AlCond2Hys_Type()
)
alCond2Hys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond2Hys.setStatus("current")
_AlCond2AlarmState_Type = DiscreteAlarmState
_AlCond2AlarmState_Object = MibTableColumn
alCond2AlarmState = _AlCond2AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 13),
    _AlCond2AlarmState_Type()
)
alCond2AlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alCond2AlarmState.setStatus("current")
_AlType_Type = AlarmType
_AlType_Object = MibTableColumn
alType = _AlType_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 14),
    _AlType_Type()
)
alType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alType.setStatus("current")
_AlAssigned_Type = AlarmChannel
_AlAssigned_Object = MibTableColumn
alAssigned = _AlAssigned_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 15),
    _AlAssigned_Type()
)
alAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAssigned.setStatus("current")
_AlActionDelay_Type = AlarmActionDelay
_AlActionDelay_Object = MibTableColumn
alActionDelay = _AlActionDelay_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 16),
    _AlActionDelay_Type()
)
alActionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alActionDelay.setStatus("current")
_AlActionOnReturn_Type = AlarmActionOnReturn
_AlActionOnReturn_Object = MibTableColumn
alActionOnReturn = _AlActionOnReturn_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 17),
    _AlActionOnReturn_Type()
)
alActionOnReturn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alActionOnReturn.setStatus("current")
_AlAction1_Type = AlarmAction
_AlAction1_Object = MibTableColumn
alAction1 = _AlAction1_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 18),
    _AlAction1_Type()
)
alAction1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAction1.setStatus("current")
_AlAction2_Type = AlarmAction
_AlAction2_Object = MibTableColumn
alAction2 = _AlAction2_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 19),
    _AlAction2_Type()
)
alAction2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAction2.setStatus("current")
_AlAction3_Type = AlarmAction
_AlAction3_Object = MibTableColumn
alAction3 = _AlAction3_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 20),
    _AlAction3_Type()
)
alAction3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAction3.setStatus("current")
_AlStatus_Type = AlarmLevel
_AlStatus_Object = MibTableColumn
alStatus = _AlStatus_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 2, 1, 1, 21),
    _AlStatus_Type()
)
alStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alStatus.setStatus("current")


class _ConfigurationSaved_Type(Integer32):
    """Custom type configurationSaved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsaved", 0),
          ("saved", 1))
    )


_ConfigurationSaved_Type.__name__ = "Integer32"
_ConfigurationSaved_Object = MibScalar
configurationSaved = _ConfigurationSaved_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 3),
    _ConfigurationSaved_Type()
)
configurationSaved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationSaved.setStatus("current")


class _RestartDevice_Type(Integer32):
    """Custom type restartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 0),
          ("restart", 1))
    )


_RestartDevice_Type.__name__ = "Integer32"
_RestartDevice_Object = MibScalar
restartDevice = _RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 4),
    _RestartDevice_Type()
)
restartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDevice.setStatus("current")


class _HardwareErr_Type(Integer32):
    """Custom type hardwareErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noErr", 0),
          ("hwErr", 1))
    )


_HardwareErr_Type.__name__ = "Integer32"
_HardwareErr_Object = MibScalar
hardwareErr = _HardwareErr_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6, 3, 5),
    _HardwareErr_Type()
)
hardwareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareErr.setStatus("current")
_Tcw260MIBConformance_ObjectIdentity = ObjectIdentity
tcw260MIBConformance = _Tcw260MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4)
)
_Tcw260MIBCompliances_ObjectIdentity = ObjectIdentity
tcw260MIBCompliances = _Tcw260MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4, 1)
)
_Tcw260MIBGroups_ObjectIdentity = ObjectIdentity
tcw260MIBGroups = _Tcw260MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4, 2)
)

# Managed Objects groups

tcw260ProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4, 2, 1)
)
tcw260ProductGroup.setObjects(
      *(("TERACOM-TCW260-MIB", "name"),
        ("TERACOM-TCW260-MIB", "version"),
        ("TERACOM-TCW260-MIB", "dateTime"))
)
if mibBuilder.loadTexts:
    tcw260ProductGroup.setStatus("current")

tcw260SetupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4, 2, 2)
)
tcw260SetupGroup.setObjects(
      *(("TERACOM-TCW260-MIB", "deviceID"),
        ("TERACOM-TCW260-MIB", "hostName"),
        ("TERACOM-TCW260-MIB", "deviceIP"),
        ("TERACOM-TCW260-MIB", "mbSenDescription"),
        ("TERACOM-TCW260-MIB", "mbSenMult"),
        ("TERACOM-TCW260-MIB", "mbSenOffset"),
        ("TERACOM-TCW260-MIB", "mbSenVal"),
        ("TERACOM-TCW260-MIB", "mbSenCounter"),
        ("TERACOM-TCW260-MIB", "analogInpDescription"),
        ("TERACOM-TCW260-MIB", "analogInpMult"),
        ("TERACOM-TCW260-MIB", "analogInpOffset"),
        ("TERACOM-TCW260-MIB", "analogInpMode"),
        ("TERACOM-TCW260-MIB", "analogInpValue"),
        ("TERACOM-TCW260-MIB", "digInpDescription"),
        ("TERACOM-TCW260-MIB", "digInplowLevel"),
        ("TERACOM-TCW260-MIB", "digInphighLevel"),
        ("TERACOM-TCW260-MIB", "digInpMode"),
        ("TERACOM-TCW260-MIB", "digInpCloseToOpenDelay"),
        ("TERACOM-TCW260-MIB", "digInpOpenToCloseDelay"),
        ("TERACOM-TCW260-MIB", "digInpCounterInitValue"),
        ("TERACOM-TCW260-MIB", "digInpValue"))
)
if mibBuilder.loadTexts:
    tcw260SetupGroup.setStatus("current")

tcw260MonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4, 2, 3)
)
tcw260MonitorGroup.setObjects(
      *(("TERACOM-TCW260-MIB", "chType"),
        ("TERACOM-TCW260-MIB", "chDescription"),
        ("TERACOM-TCW260-MIB", "chParam1"),
        ("TERACOM-TCW260-MIB", "chOP1"),
        ("TERACOM-TCW260-MIB", "chParam2"),
        ("TERACOM-TCW260-MIB", "chOP2"),
        ("TERACOM-TCW260-MIB", "chCoef1"),
        ("TERACOM-TCW260-MIB", "chOP3"),
        ("TERACOM-TCW260-MIB", "chCoef2"),
        ("TERACOM-TCW260-MIB", "chUnit"),
        ("TERACOM-TCW260-MIB", "chCumulInitValue"),
        ("TERACOM-TCW260-MIB", "chValue"),
        ("TERACOM-TCW260-MIB", "chCounter"),
        ("TERACOM-TCW260-MIB", "chAlarmStatus"),
        ("TERACOM-TCW260-MIB", "alDescription"),
        ("TERACOM-TCW260-MIB", "alCond1Channel"),
        ("TERACOM-TCW260-MIB", "alCond1Operand"),
        ("TERACOM-TCW260-MIB", "alCond1Limit"),
        ("TERACOM-TCW260-MIB", "alCond1Hys"),
        ("TERACOM-TCW260-MIB", "alCond1AlarmState"),
        ("TERACOM-TCW260-MIB", "alCondLogic"),
        ("TERACOM-TCW260-MIB", "alCond2Channel"),
        ("TERACOM-TCW260-MIB", "alCond2Operand"),
        ("TERACOM-TCW260-MIB", "alCond2Limit"),
        ("TERACOM-TCW260-MIB", "alCond2Hys"),
        ("TERACOM-TCW260-MIB", "alCond2AlarmState"),
        ("TERACOM-TCW260-MIB", "alType"),
        ("TERACOM-TCW260-MIB", "alAssigned"),
        ("TERACOM-TCW260-MIB", "alActionDelay"),
        ("TERACOM-TCW260-MIB", "alActionOnReturn"),
        ("TERACOM-TCW260-MIB", "alAction1"),
        ("TERACOM-TCW260-MIB", "alAction2"),
        ("TERACOM-TCW260-MIB", "alAction3"),
        ("TERACOM-TCW260-MIB", "alStatus"),
        ("TERACOM-TCW260-MIB", "configurationSaved"),
        ("TERACOM-TCW260-MIB", "restartDevice"),
        ("TERACOM-TCW260-MIB", "hardwareErr"))
)
if mibBuilder.loadTexts:
    tcw260MonitorGroup.setStatus("current")


# Notification objects

snmp_trap_notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 38783, 6, 0, 1)
)
snmp_trap_notification.setObjects(
      *(("TERACOM-TCW260-MIB", "chValue"),
        ("TERACOM-TCW260-MIB", "chCounter"),
        ("TERACOM-TCW260-MIB", "restartDevice"),
        ("TERACOM-TCW260-MIB", "deviceIP"),
        ("TERACOM-TCW260-MIB", "alDescription"))
)
if mibBuilder.loadTexts:
    snmp_trap_notification.setStatus(
        "current"
    )


# Notifications groups

tcw260TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4, 2, 4)
)
tcw260TrapGroup.setObjects(
    ("TERACOM-TCW260-MIB", "snmp-trap-notification")
)
if mibBuilder.loadTexts:
    tcw260TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tcw260MIBCompliances1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 38783, 6, 4, 1, 1)
)
tcw260MIBCompliances1.setObjects(
      *(("TERACOM-TCW260-MIB", "tcw260ProductGroup"),
        ("TERACOM-TCW260-MIB", "tcw260SetupGroup"),
        ("TERACOM-TCW260-MIB", "tcw260MonitorGroup"),
        ("TERACOM-TCW260-MIB", "tcw260TrapGroup"))
)
if mibBuilder.loadTexts:
    tcw260MIBCompliances1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERACOM-TCW260-MIB",
    **{"RealValue": RealValue,
       "DigitalValue": DigitalValue,
       "AlarmLevel": AlarmLevel,
       "AlarmType": AlarmType,
       "AnalogMode": AnalogMode,
       "DigitalMode": DigitalMode,
       "ChannelParameter1": ChannelParameter1,
       "ChannelParameter2": ChannelParameter2,
       "ChannelOperand": ChannelOperand,
       "AlarmCondOperand": AlarmCondOperand,
       "AlarmChannel": AlarmChannel,
       "AlarmCondLogic": AlarmCondLogic,
       "AlarmActionDelay": AlarmActionDelay,
       "AlarmActionOnReturn": AlarmActionOnReturn,
       "AlarmAction": AlarmAction,
       "DigInputDelay": DigInputDelay,
       "ChannelType": ChannelType,
       "DiscreteAlarmState": DiscreteAlarmState,
       "MbSenTableIndex": MbSenTableIndex,
       "AnalogInpTableIndex": AnalogInpTableIndex,
       "DigInpTableIndex": DigInpTableIndex,
       "ChTableIndex": ChTableIndex,
       "AlTableIndex": AlTableIndex,
       "teracom": teracom,
       "tcw260": tcw260,
       "trapNotifications": trapNotifications,
       "snmp-trap-notification": snmp_trap_notification,
       "product": product,
       "name": name,
       "version": version,
       "dateTime": dateTime,
       "setup": setup,
       "network": network,
       "deviceID": deviceID,
       "hostName": hostName,
       "deviceIP": deviceIP,
       "parameters": parameters,
       "mbSensors": mbSensors,
       "mbSensorsTable": mbSensorsTable,
       "mbSensorsEntry": mbSensorsEntry,
       "mbSenIndex": mbSenIndex,
       "mbSenDescription": mbSenDescription,
       "mbSenMult": mbSenMult,
       "mbSenOffset": mbSenOffset,
       "mbSenVal": mbSenVal,
       "mbSenCounter": mbSenCounter,
       "analogInputs": analogInputs,
       "analogInpTable": analogInpTable,
       "analogInpEntry": analogInpEntry,
       "analogInpIndex": analogInpIndex,
       "analogInpDescription": analogInpDescription,
       "analogInpMult": analogInpMult,
       "analogInpOffset": analogInpOffset,
       "analogInpMode": analogInpMode,
       "analogInpValue": analogInpValue,
       "digitalInputs": digitalInputs,
       "digitalInpTable": digitalInpTable,
       "digitalInpEntry": digitalInpEntry,
       "digInpIndex": digInpIndex,
       "digInpDescription": digInpDescription,
       "digInplowLevel": digInplowLevel,
       "digInphighLevel": digInphighLevel,
       "digInpMode": digInpMode,
       "digInpCloseToOpenDelay": digInpCloseToOpenDelay,
       "digInpOpenToCloseDelay": digInpOpenToCloseDelay,
       "digInpCounterInitValue": digInpCounterInitValue,
       "digInpValue": digInpValue,
       "monitorNcontrol": monitorNcontrol,
       "channels": channels,
       "chanTable": chanTable,
       "chanEntry": chanEntry,
       "chIndex": chIndex,
       "chType": chType,
       "chDescription": chDescription,
       "chParam1": chParam1,
       "chOP1": chOP1,
       "chParam2": chParam2,
       "chOP2": chOP2,
       "chCoef1": chCoef1,
       "chOP3": chOP3,
       "chCoef2": chCoef2,
       "chUnit": chUnit,
       "chCumulInitValue": chCumulInitValue,
       "chValue": chValue,
       "chCounter": chCounter,
       "chAlarmStatus": chAlarmStatus,
       "alarms": alarms,
       "alarmsTable": alarmsTable,
       "alarmsEntry": alarmsEntry,
       "alIndex": alIndex,
       "alDescription": alDescription,
       "alCond1Channel": alCond1Channel,
       "alCond1Operand": alCond1Operand,
       "alCond1Limit": alCond1Limit,
       "alCond1Hys": alCond1Hys,
       "alCond1AlarmState": alCond1AlarmState,
       "alCondLogic": alCondLogic,
       "alCond2Channel": alCond2Channel,
       "alCond2Operand": alCond2Operand,
       "alCond2Limit": alCond2Limit,
       "alCond2Hys": alCond2Hys,
       "alCond2AlarmState": alCond2AlarmState,
       "alType": alType,
       "alAssigned": alAssigned,
       "alActionDelay": alActionDelay,
       "alActionOnReturn": alActionOnReturn,
       "alAction1": alAction1,
       "alAction2": alAction2,
       "alAction3": alAction3,
       "alStatus": alStatus,
       "configurationSaved": configurationSaved,
       "restartDevice": restartDevice,
       "hardwareErr": hardwareErr,
       "tcw260MIBConformance": tcw260MIBConformance,
       "tcw260MIBCompliances": tcw260MIBCompliances,
       "tcw260MIBCompliances1": tcw260MIBCompliances1,
       "tcw260MIBGroups": tcw260MIBGroups,
       "tcw260ProductGroup": tcw260ProductGroup,
       "tcw260SetupGroup": tcw260SetupGroup,
       "tcw260MonitorGroup": tcw260MonitorGroup,
       "tcw260TrapGroup": tcw260TrapGroup,
       "snmpMIB": snmpMIB}
)
