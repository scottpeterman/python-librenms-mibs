# SNMP MIB module (WebGraph-Thermometer-NTC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wut\WebGraph-Thermometer-NTC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:31 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wut_ObjectIdentity = ObjectIdentity
wut = _Wut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040)
)
_WtComServer_ObjectIdentity = ObjectIdentity
wtComServer = _WtComServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1)
)
_WtWebio_ObjectIdentity = ObjectIdentity
wtWebio = _WtWebio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2)
)
_WtWebioAn1GraphNtc_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtc = _WtWebioAn1GraphNtc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18)
)
_WtWebioAn1GraphNtcTemp_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcTemp = _WtWebioAn1GraphNtcTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1)
)


class _WtWebioAn1GraphNtcSensors_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphNtcSensors_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcSensors_Object = MibScalar
wtWebioAn1GraphNtcSensors = _WtWebioAn1GraphNtcSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 1),
    _WtWebioAn1GraphNtcSensors_Type()
)
wtWebioAn1GraphNtcSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSensors.setStatus("mandatory")
_WtWebioAn1GraphNtcSensorTable_Object = MibTable
wtWebioAn1GraphNtcSensorTable = _WtWebioAn1GraphNtcSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSensorTable.setStatus("mandatory")
_WtWebioAn1GraphNtcSensorEntry_Object = MibTableRow
wtWebioAn1GraphNtcSensorEntry = _WtWebioAn1GraphNtcSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 2, 1)
)
wtWebioAn1GraphNtcSensorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSensorEntry.setStatus("mandatory")


class _WtWebioAn1GraphNtcSensorNo_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WtWebioAn1GraphNtcSensorNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcSensorNo_Object = MibTableColumn
wtWebioAn1GraphNtcSensorNo = _WtWebioAn1GraphNtcSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 2, 1, 1),
    _WtWebioAn1GraphNtcSensorNo_Type()
)
wtWebioAn1GraphNtcSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSensorNo.setStatus("mandatory")
_WtWebioAn1GraphNtcTempValueTable_Object = MibTable
wtWebioAn1GraphNtcTempValueTable = _WtWebioAn1GraphNtcTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphNtcTempValueEntry_Object = MibTableRow
wtWebioAn1GraphNtcTempValueEntry = _WtWebioAn1GraphNtcTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 3, 1)
)
wtWebioAn1GraphNtcTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTempValueEntry.setStatus("mandatory")


class _WtWebioAn1GraphNtcTempValue_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebioAn1GraphNtcTempValue_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcTempValue_Object = MibTableColumn
wtWebioAn1GraphNtcTempValue = _WtWebioAn1GraphNtcTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 3, 1, 1),
    _WtWebioAn1GraphNtcTempValue_Type()
)
wtWebioAn1GraphNtcTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTempValue.setStatus("mandatory")
_WtWebioAn1GraphNtcBinaryTempValueTable_Object = MibTable
wtWebioAn1GraphNtcBinaryTempValueTable = _WtWebioAn1GraphNtcBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcBinaryTempValueTable.setStatus("mandatory")
_WtWebioAn1GraphNtcBinaryTempValueEntry_Object = MibTableRow
wtWebioAn1GraphNtcBinaryTempValueEntry = _WtWebioAn1GraphNtcBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 4, 1)
)
wtWebioAn1GraphNtcBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcBinaryTempValueEntry.setStatus("mandatory")
_WtWebioAn1GraphNtcBinaryTempValue_Type = Integer32
_WtWebioAn1GraphNtcBinaryTempValue_Object = MibTableColumn
wtWebioAn1GraphNtcBinaryTempValue = _WtWebioAn1GraphNtcBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 4, 1, 1),
    _WtWebioAn1GraphNtcBinaryTempValue_Type()
)
wtWebioAn1GraphNtcBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcBinaryTempValue.setStatus("mandatory")
_WtWebioAn1GraphNtcTempValuePktTable_Object = MibTable
wtWebioAn1GraphNtcTempValuePktTable = _WtWebioAn1GraphNtcTempValuePktTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTempValuePktTable.setStatus("mandatory")
_WtWebioAn1GraphNtcTempValuePktEntry_Object = MibTableRow
wtWebioAn1GraphNtcTempValuePktEntry = _WtWebioAn1GraphNtcTempValuePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 8, 1)
)
wtWebioAn1GraphNtcTempValuePktEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTempValuePktEntry.setStatus("mandatory")


class _WtWebioAn1GraphNtcTempValuePkt_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcTempValuePkt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebioAn1GraphNtcTempValuePkt_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcTempValuePkt_Object = MibTableColumn
wtWebioAn1GraphNtcTempValuePkt = _WtWebioAn1GraphNtcTempValuePkt_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 1, 8, 1, 1),
    _WtWebioAn1GraphNtcTempValuePkt_Type()
)
wtWebioAn1GraphNtcTempValuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTempValuePkt.setStatus("mandatory")
_WtWebioAn1GraphNtcSessCntrl_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcSessCntrl = _WtWebioAn1GraphNtcSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 2)
)
_WtWebioAn1GraphNtcSessCntrlPassword_Type = OctetString
_WtWebioAn1GraphNtcSessCntrlPassword_Object = MibScalar
wtWebioAn1GraphNtcSessCntrlPassword = _WtWebioAn1GraphNtcSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 2, 1),
    _WtWebioAn1GraphNtcSessCntrlPassword_Type()
)
wtWebioAn1GraphNtcSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSessCntrlPassword.setStatus("mandatory")


class _WtWebioAn1GraphNtcSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcSessCntrl-NoSession", 0),
          ("wtWebioAn1GraphNtcSessCntrl-Session", 1))
    )


_WtWebioAn1GraphNtcSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcSessCntrlConfigMode_Object = MibScalar
wtWebioAn1GraphNtcSessCntrlConfigMode = _WtWebioAn1GraphNtcSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 2, 2),
    _WtWebioAn1GraphNtcSessCntrlConfigMode_Type()
)
wtWebioAn1GraphNtcSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSessCntrlConfigMode.setStatus("mandatory")
_WtWebioAn1GraphNtcSessCntrlLogout_Type = Integer32
_WtWebioAn1GraphNtcSessCntrlLogout_Object = MibScalar
wtWebioAn1GraphNtcSessCntrlLogout = _WtWebioAn1GraphNtcSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 2, 3),
    _WtWebioAn1GraphNtcSessCntrlLogout_Type()
)
wtWebioAn1GraphNtcSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSessCntrlLogout.setStatus("mandatory")
_WtWebioAn1GraphNtcSessCntrlAdminPassword_Type = OctetString
_WtWebioAn1GraphNtcSessCntrlAdminPassword_Object = MibScalar
wtWebioAn1GraphNtcSessCntrlAdminPassword = _WtWebioAn1GraphNtcSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 2, 4),
    _WtWebioAn1GraphNtcSessCntrlAdminPassword_Type()
)
wtWebioAn1GraphNtcSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSessCntrlAdminPassword.setStatus("mandatory")
_WtWebioAn1GraphNtcSessCntrlConfigPassword_Type = OctetString
_WtWebioAn1GraphNtcSessCntrlConfigPassword_Object = MibScalar
wtWebioAn1GraphNtcSessCntrlConfigPassword = _WtWebioAn1GraphNtcSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 2, 5),
    _WtWebioAn1GraphNtcSessCntrlConfigPassword_Type()
)
wtWebioAn1GraphNtcSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSessCntrlConfigPassword.setStatus("mandatory")
_WtWebioAn1GraphNtcConfig_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcConfig = _WtWebioAn1GraphNtcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3)
)
_WtWebioAn1GraphNtcDevice_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcDevice = _WtWebioAn1GraphNtcDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1)
)
_WtWebioAn1GraphNtcText_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcText = _WtWebioAn1GraphNtcText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 1)
)
_WtWebioAn1GraphNtcDeviceName_Type = OctetString
_WtWebioAn1GraphNtcDeviceName_Object = MibScalar
wtWebioAn1GraphNtcDeviceName = _WtWebioAn1GraphNtcDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 1, 1),
    _WtWebioAn1GraphNtcDeviceName_Type()
)
wtWebioAn1GraphNtcDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDeviceName.setStatus("mandatory")
_WtWebioAn1GraphNtcDeviceText_Type = OctetString
_WtWebioAn1GraphNtcDeviceText_Object = MibScalar
wtWebioAn1GraphNtcDeviceText = _WtWebioAn1GraphNtcDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 1, 2),
    _WtWebioAn1GraphNtcDeviceText_Type()
)
wtWebioAn1GraphNtcDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDeviceText.setStatus("mandatory")
_WtWebioAn1GraphNtcDeviceLocation_Type = OctetString
_WtWebioAn1GraphNtcDeviceLocation_Object = MibScalar
wtWebioAn1GraphNtcDeviceLocation = _WtWebioAn1GraphNtcDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 1, 3),
    _WtWebioAn1GraphNtcDeviceLocation_Type()
)
wtWebioAn1GraphNtcDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDeviceLocation.setStatus("mandatory")
_WtWebioAn1GraphNtcDeviceContact_Type = OctetString
_WtWebioAn1GraphNtcDeviceContact_Object = MibScalar
wtWebioAn1GraphNtcDeviceContact = _WtWebioAn1GraphNtcDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 1, 4),
    _WtWebioAn1GraphNtcDeviceContact_Type()
)
wtWebioAn1GraphNtcDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDeviceContact.setStatus("mandatory")
_WtWebioAn1GraphNtcTimeDate_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcTimeDate = _WtWebioAn1GraphNtcTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2)
)
_WtWebioAn1GraphNtcTimeZone_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcTimeZone = _WtWebioAn1GraphNtcTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1)
)
_WtWebioAn1GraphNtcTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphNtcTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphNtcTzOffsetHrs = _WtWebioAn1GraphNtcTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 1),
    _WtWebioAn1GraphNtcTzOffsetHrs_Type()
)
wtWebioAn1GraphNtcTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphNtcTzOffsetMin_Type = Integer32
_WtWebioAn1GraphNtcTzOffsetMin_Object = MibScalar
wtWebioAn1GraphNtcTzOffsetMin = _WtWebioAn1GraphNtcTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 2),
    _WtWebioAn1GraphNtcTzOffsetMin_Type()
)
wtWebioAn1GraphNtcTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphNtcTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcTzEnable_Object = MibScalar
wtWebioAn1GraphNtcTzEnable = _WtWebioAn1GraphNtcTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 3),
    _WtWebioAn1GraphNtcTzEnable_Type()
)
wtWebioAn1GraphNtcTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTzEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcStTzOffsetHrs_Type = Integer32
_WtWebioAn1GraphNtcStTzOffsetHrs_Object = MibScalar
wtWebioAn1GraphNtcStTzOffsetHrs = _WtWebioAn1GraphNtcStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 4),
    _WtWebioAn1GraphNtcStTzOffsetHrs_Type()
)
wtWebioAn1GraphNtcStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzOffsetHrs.setStatus("mandatory")
_WtWebioAn1GraphNtcStTzOffsetMin_Type = Integer32
_WtWebioAn1GraphNtcStTzOffsetMin_Object = MibScalar
wtWebioAn1GraphNtcStTzOffsetMin = _WtWebioAn1GraphNtcStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 5),
    _WtWebioAn1GraphNtcStTzOffsetMin_Type()
)
wtWebioAn1GraphNtcStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzOffsetMin.setStatus("mandatory")


class _WtWebioAn1GraphNtcStTzEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcStTzEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcStTzEnable_Object = MibScalar
wtWebioAn1GraphNtcStTzEnable = _WtWebioAn1GraphNtcStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 6),
    _WtWebioAn1GraphNtcStTzEnable_Type()
)
wtWebioAn1GraphNtcStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzEnable.setStatus("mandatory")


class _WtWebioAn1GraphNtcStTzStartMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcStTzStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcStartMonth-January", 1),
          ("wtWebioAn1GraphNtcStartMonth-February", 2),
          ("wtWebioAn1GraphNtcStartMonth-March", 3),
          ("wtWebioAn1GraphNtcStartMonth-April", 4),
          ("wtWebioAn1GraphNtcStartMonth-May", 5),
          ("wtWebioAn1GraphNtcStartMonth-June", 6),
          ("wtWebioAn1GraphNtcStartMonth-July", 7),
          ("wtWebioAn1GraphNtcStartMonth-August", 8),
          ("wtWebioAn1GraphNtcStartMonth-September", 9),
          ("wtWebioAn1GraphNtcStartMonth-October", 10),
          ("wtWebioAn1GraphNtcStartMonth-November", 11),
          ("wtWebioAn1GraphNtcStartMonth-December", 12))
    )


_WtWebioAn1GraphNtcStTzStartMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcStTzStartMonth_Object = MibScalar
wtWebioAn1GraphNtcStTzStartMonth = _WtWebioAn1GraphNtcStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 7),
    _WtWebioAn1GraphNtcStTzStartMonth_Type()
)
wtWebioAn1GraphNtcStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStartMonth.setStatus("mandatory")


class _WtWebioAn1GraphNtcStTzStartMode_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcStTzStartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcStartMode-first", 1),
          ("wtWebioAn1GraphNtcStartMode-second", 2),
          ("wtWebioAn1GraphNtcStartMode-third", 3),
          ("wtWebioAn1GraphNtcStartMode-fourth", 4),
          ("wtWebioAn1GraphNtcStartMode-last", 5))
    )


_WtWebioAn1GraphNtcStTzStartMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcStTzStartMode_Object = MibScalar
wtWebioAn1GraphNtcStTzStartMode = _WtWebioAn1GraphNtcStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 8),
    _WtWebioAn1GraphNtcStTzStartMode_Type()
)
wtWebioAn1GraphNtcStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStartMode.setStatus("mandatory")


class _WtWebioAn1GraphNtcStTzStartWday_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcStTzStartWday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcStartWday-Sunday", 1),
          ("wtWebioAn1GraphNtcStartWday-Monday", 2),
          ("wtWebioAn1GraphNtcStartWday-Tuesday", 3),
          ("wtWebioAn1GraphNtcStartWday-Thursday", 4),
          ("wtWebioAn1GraphNtcStartWday-Wednesday", 5),
          ("wtWebioAn1GraphNtcStartWday-Friday", 6),
          ("wtWebioAn1GraphNtcStartWday-Saturday", 7))
    )


_WtWebioAn1GraphNtcStTzStartWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcStTzStartWday_Object = MibScalar
wtWebioAn1GraphNtcStTzStartWday = _WtWebioAn1GraphNtcStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 9),
    _WtWebioAn1GraphNtcStTzStartWday_Type()
)
wtWebioAn1GraphNtcStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStartWday.setStatus("mandatory")
_WtWebioAn1GraphNtcStTzStartHrs_Type = Integer32
_WtWebioAn1GraphNtcStTzStartHrs_Object = MibScalar
wtWebioAn1GraphNtcStTzStartHrs = _WtWebioAn1GraphNtcStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 10),
    _WtWebioAn1GraphNtcStTzStartHrs_Type()
)
wtWebioAn1GraphNtcStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStartHrs.setStatus("mandatory")
_WtWebioAn1GraphNtcStTzStartMin_Type = Integer32
_WtWebioAn1GraphNtcStTzStartMin_Object = MibScalar
wtWebioAn1GraphNtcStTzStartMin = _WtWebioAn1GraphNtcStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 11),
    _WtWebioAn1GraphNtcStTzStartMin_Type()
)
wtWebioAn1GraphNtcStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStartMin.setStatus("mandatory")


class _WtWebioAn1GraphNtcStTzStopMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcStTzStopMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcStopMonth-January", 1),
          ("wtWebioAn1GraphNtcStopMonth-February", 2),
          ("wtWebioAn1GraphNtcStopMonth-March", 3),
          ("wtWebioAn1GraphNtcStopMonth-April", 4),
          ("wtWebioAn1GraphNtcStopMonth-May", 5),
          ("wtWebioAn1GraphNtcStopMonth-June", 6),
          ("wtWebioAn1GraphNtcStopMonth-July", 7),
          ("wtWebioAn1GraphNtcStopMonth-August", 8),
          ("wtWebioAn1GraphNtcStopMonth-September", 9),
          ("wtWebioAn1GraphNtcStopMonth-October", 10),
          ("wtWebioAn1GraphNtcStopMonth-November", 11),
          ("wtWebioAn1GraphNtcStopMonth-December", 12))
    )


_WtWebioAn1GraphNtcStTzStopMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcStTzStopMonth_Object = MibScalar
wtWebioAn1GraphNtcStTzStopMonth = _WtWebioAn1GraphNtcStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 12),
    _WtWebioAn1GraphNtcStTzStopMonth_Type()
)
wtWebioAn1GraphNtcStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStopMonth.setStatus("mandatory")


class _WtWebioAn1GraphNtcStTzStopMode_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcStTzStopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcStopMode-first", 1),
          ("wtWebioAn1GraphNtcStopMode-second", 2),
          ("wtWebioAn1GraphNtcStopMode-third", 3),
          ("wtWebioAn1GraphNtcStopMode-fourth", 4),
          ("wtWebioAn1GraphNtcStopMode-last", 5))
    )


_WtWebioAn1GraphNtcStTzStopMode_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcStTzStopMode_Object = MibScalar
wtWebioAn1GraphNtcStTzStopMode = _WtWebioAn1GraphNtcStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 13),
    _WtWebioAn1GraphNtcStTzStopMode_Type()
)
wtWebioAn1GraphNtcStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStopMode.setStatus("mandatory")


class _WtWebioAn1GraphNtcStTzStopWday_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcStTzStopWday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcStopWday-Sunday", 1),
          ("wtWebioAn1GraphNtcStopWday-Monday", 2),
          ("wtWebioAn1GraphNtcStopWday-Tuesday", 3),
          ("wtWebioAn1GraphNtcStopWday-Thursday", 4),
          ("wtWebioAn1GraphNtcStopWday-Wednesday", 5),
          ("wtWebioAn1GraphNtcStopWday-Friday", 6),
          ("wtWebioAn1GraphNtcStopWday-Saturday", 7))
    )


_WtWebioAn1GraphNtcStTzStopWday_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcStTzStopWday_Object = MibScalar
wtWebioAn1GraphNtcStTzStopWday = _WtWebioAn1GraphNtcStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 14),
    _WtWebioAn1GraphNtcStTzStopWday_Type()
)
wtWebioAn1GraphNtcStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStopWday.setStatus("mandatory")
_WtWebioAn1GraphNtcStTzStopHrs_Type = Integer32
_WtWebioAn1GraphNtcStTzStopHrs_Object = MibScalar
wtWebioAn1GraphNtcStTzStopHrs = _WtWebioAn1GraphNtcStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 15),
    _WtWebioAn1GraphNtcStTzStopHrs_Type()
)
wtWebioAn1GraphNtcStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStopHrs.setStatus("mandatory")
_WtWebioAn1GraphNtcStTzStopMin_Type = Integer32
_WtWebioAn1GraphNtcStTzStopMin_Object = MibScalar
wtWebioAn1GraphNtcStTzStopMin = _WtWebioAn1GraphNtcStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 1, 16),
    _WtWebioAn1GraphNtcStTzStopMin_Type()
)
wtWebioAn1GraphNtcStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStTzStopMin.setStatus("mandatory")
_WtWebioAn1GraphNtcTimeServer_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcTimeServer = _WtWebioAn1GraphNtcTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 2)
)
_WtWebioAn1GraphNtcTimeServer1_Type = OctetString
_WtWebioAn1GraphNtcTimeServer1_Object = MibScalar
wtWebioAn1GraphNtcTimeServer1 = _WtWebioAn1GraphNtcTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 2, 1),
    _WtWebioAn1GraphNtcTimeServer1_Type()
)
wtWebioAn1GraphNtcTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTimeServer1.setStatus("mandatory")
_WtWebioAn1GraphNtcTimeServer2_Type = OctetString
_WtWebioAn1GraphNtcTimeServer2_Object = MibScalar
wtWebioAn1GraphNtcTimeServer2 = _WtWebioAn1GraphNtcTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 2, 2),
    _WtWebioAn1GraphNtcTimeServer2_Type()
)
wtWebioAn1GraphNtcTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTimeServer2.setStatus("mandatory")


class _WtWebioAn1GraphNtcTsEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcTsEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcTsEnable_Object = MibScalar
wtWebioAn1GraphNtcTsEnable = _WtWebioAn1GraphNtcTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 2, 3),
    _WtWebioAn1GraphNtcTsEnable_Type()
)
wtWebioAn1GraphNtcTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTsEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcTsSyncTime_Type = Integer32
_WtWebioAn1GraphNtcTsSyncTime_Object = MibScalar
wtWebioAn1GraphNtcTsSyncTime = _WtWebioAn1GraphNtcTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 2, 4),
    _WtWebioAn1GraphNtcTsSyncTime_Type()
)
wtWebioAn1GraphNtcTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcTsSyncTime.setStatus("mandatory")
_WtWebioAn1GraphNtcDeviceClock_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcDeviceClock = _WtWebioAn1GraphNtcDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 3)
)


class _WtWebioAn1GraphNtcClockHrs_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebioAn1GraphNtcClockHrs_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcClockHrs_Object = MibScalar
wtWebioAn1GraphNtcClockHrs = _WtWebioAn1GraphNtcClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 3, 1),
    _WtWebioAn1GraphNtcClockHrs_Type()
)
wtWebioAn1GraphNtcClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcClockHrs.setStatus("mandatory")


class _WtWebioAn1GraphNtcClockMin_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebioAn1GraphNtcClockMin_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcClockMin_Object = MibScalar
wtWebioAn1GraphNtcClockMin = _WtWebioAn1GraphNtcClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 3, 2),
    _WtWebioAn1GraphNtcClockMin_Type()
)
wtWebioAn1GraphNtcClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcClockMin.setStatus("mandatory")


class _WtWebioAn1GraphNtcClockDay_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebioAn1GraphNtcClockDay_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcClockDay_Object = MibScalar
wtWebioAn1GraphNtcClockDay = _WtWebioAn1GraphNtcClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 3, 3),
    _WtWebioAn1GraphNtcClockDay_Type()
)
wtWebioAn1GraphNtcClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcClockDay.setStatus("mandatory")


class _WtWebioAn1GraphNtcClockMonth_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcClockMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcClockMonth-January", 1),
          ("wtWebioAn1GraphNtcClockMonth-February", 2),
          ("wtWebioAn1GraphNtcClockMonth-March", 3),
          ("wtWebioAn1GraphNtcClockMonth-April", 4),
          ("wtWebioAn1GraphNtcClockMonth-May", 5),
          ("wtWebioAn1GraphNtcClockMonth-June", 6),
          ("wtWebioAn1GraphNtcClockMonth-July", 7),
          ("wtWebioAn1GraphNtcClockMonth-August", 8),
          ("wtWebioAn1GraphNtcClockMonth-September", 9),
          ("wtWebioAn1GraphNtcClockMonth-October", 10),
          ("wtWebioAn1GraphNtcClockMonth-November", 11),
          ("wtWebioAn1GraphNtcClockMonth-December", 12))
    )


_WtWebioAn1GraphNtcClockMonth_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcClockMonth_Object = MibScalar
wtWebioAn1GraphNtcClockMonth = _WtWebioAn1GraphNtcClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 3, 4),
    _WtWebioAn1GraphNtcClockMonth_Type()
)
wtWebioAn1GraphNtcClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcClockMonth.setStatus("mandatory")


class _WtWebioAn1GraphNtcClockYear_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebioAn1GraphNtcClockYear_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcClockYear_Object = MibScalar
wtWebioAn1GraphNtcClockYear = _WtWebioAn1GraphNtcClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 2, 3, 5),
    _WtWebioAn1GraphNtcClockYear_Type()
)
wtWebioAn1GraphNtcClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcClockYear.setStatus("mandatory")
_WtWebioAn1GraphNtcBasic_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcBasic = _WtWebioAn1GraphNtcBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3)
)
_WtWebioAn1GraphNtcNetwork_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcNetwork = _WtWebioAn1GraphNtcNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 1)
)
_WtWebioAn1GraphNtcIpAddress_Type = IpAddress
_WtWebioAn1GraphNtcIpAddress_Object = MibScalar
wtWebioAn1GraphNtcIpAddress = _WtWebioAn1GraphNtcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 1, 1),
    _WtWebioAn1GraphNtcIpAddress_Type()
)
wtWebioAn1GraphNtcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcIpAddress.setStatus("mandatory")
_WtWebioAn1GraphNtcSubnetMask_Type = IpAddress
_WtWebioAn1GraphNtcSubnetMask_Object = MibScalar
wtWebioAn1GraphNtcSubnetMask = _WtWebioAn1GraphNtcSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 1, 2),
    _WtWebioAn1GraphNtcSubnetMask_Type()
)
wtWebioAn1GraphNtcSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSubnetMask.setStatus("mandatory")
_WtWebioAn1GraphNtcGateway_Type = IpAddress
_WtWebioAn1GraphNtcGateway_Object = MibScalar
wtWebioAn1GraphNtcGateway = _WtWebioAn1GraphNtcGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 1, 3),
    _WtWebioAn1GraphNtcGateway_Type()
)
wtWebioAn1GraphNtcGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGateway.setStatus("mandatory")
_WtWebioAn1GraphNtcDnsServer1_Type = OctetString
_WtWebioAn1GraphNtcDnsServer1_Object = MibScalar
wtWebioAn1GraphNtcDnsServer1 = _WtWebioAn1GraphNtcDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 1, 4),
    _WtWebioAn1GraphNtcDnsServer1_Type()
)
wtWebioAn1GraphNtcDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDnsServer1.setStatus("mandatory")
_WtWebioAn1GraphNtcDnsServer2_Type = OctetString
_WtWebioAn1GraphNtcDnsServer2_Object = MibScalar
wtWebioAn1GraphNtcDnsServer2 = _WtWebioAn1GraphNtcDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 1, 5),
    _WtWebioAn1GraphNtcDnsServer2_Type()
)
wtWebioAn1GraphNtcDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDnsServer2.setStatus("mandatory")
_WtWebioAn1GraphNtcAddConfig_Type = OctetString
_WtWebioAn1GraphNtcAddConfig_Object = MibScalar
wtWebioAn1GraphNtcAddConfig = _WtWebioAn1GraphNtcAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 1, 6),
    _WtWebioAn1GraphNtcAddConfig_Type()
)
wtWebioAn1GraphNtcAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAddConfig.setStatus("mandatory")
_WtWebioAn1GraphNtcHTTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcHTTP = _WtWebioAn1GraphNtcHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 2)
)
_WtWebioAn1GraphNtcStartup_Type = OctetString
_WtWebioAn1GraphNtcStartup_Object = MibScalar
wtWebioAn1GraphNtcStartup = _WtWebioAn1GraphNtcStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 2, 1),
    _WtWebioAn1GraphNtcStartup_Type()
)
wtWebioAn1GraphNtcStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcStartup.setStatus("mandatory")
_WtWebioAn1GraphNtcGetHeaderEnable_Type = OctetString
_WtWebioAn1GraphNtcGetHeaderEnable_Object = MibScalar
wtWebioAn1GraphNtcGetHeaderEnable = _WtWebioAn1GraphNtcGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 2, 2),
    _WtWebioAn1GraphNtcGetHeaderEnable_Type()
)
wtWebioAn1GraphNtcGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGetHeaderEnable.setStatus("mandatory")


class _WtWebioAn1GraphNtcHttpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphNtcHttpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcHttpPort_Object = MibScalar
wtWebioAn1GraphNtcHttpPort = _WtWebioAn1GraphNtcHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 2, 3),
    _WtWebioAn1GraphNtcHttpPort_Type()
)
wtWebioAn1GraphNtcHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcHttpPort.setStatus("mandatory")
_WtWebioAn1GraphNtcMail_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcMail = _WtWebioAn1GraphNtcMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3)
)
_WtWebioAn1GraphNtcMailAdName_Type = OctetString
_WtWebioAn1GraphNtcMailAdName_Object = MibScalar
wtWebioAn1GraphNtcMailAdName = _WtWebioAn1GraphNtcMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 1),
    _WtWebioAn1GraphNtcMailAdName_Type()
)
wtWebioAn1GraphNtcMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailAdName.setStatus("mandatory")
_WtWebioAn1GraphNtcMailReply_Type = OctetString
_WtWebioAn1GraphNtcMailReply_Object = MibScalar
wtWebioAn1GraphNtcMailReply = _WtWebioAn1GraphNtcMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 2),
    _WtWebioAn1GraphNtcMailReply_Type()
)
wtWebioAn1GraphNtcMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailReply.setStatus("mandatory")
_WtWebioAn1GraphNtcMailServer_Type = OctetString
_WtWebioAn1GraphNtcMailServer_Object = MibScalar
wtWebioAn1GraphNtcMailServer = _WtWebioAn1GraphNtcMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 3),
    _WtWebioAn1GraphNtcMailServer_Type()
)
wtWebioAn1GraphNtcMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailServer.setStatus("mandatory")
_WtWebioAn1GraphNtcMailEnable_Type = OctetString
_WtWebioAn1GraphNtcMailEnable_Object = MibScalar
wtWebioAn1GraphNtcMailEnable = _WtWebioAn1GraphNtcMailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 4),
    _WtWebioAn1GraphNtcMailEnable_Type()
)
wtWebioAn1GraphNtcMailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailEnable.setStatus("mandatory")


class _WtWebioAn1GraphNtcMailAuthentication_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcMailAuthentication_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcMailAuthentication_Object = MibScalar
wtWebioAn1GraphNtcMailAuthentication = _WtWebioAn1GraphNtcMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 5),
    _WtWebioAn1GraphNtcMailAuthentication_Type()
)
wtWebioAn1GraphNtcMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailAuthentication.setStatus("mandatory")
_WtWebioAn1GraphNtcMailAuthUser_Type = OctetString
_WtWebioAn1GraphNtcMailAuthUser_Object = MibScalar
wtWebioAn1GraphNtcMailAuthUser = _WtWebioAn1GraphNtcMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 6),
    _WtWebioAn1GraphNtcMailAuthUser_Type()
)
wtWebioAn1GraphNtcMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailAuthUser.setStatus("mandatory")
_WtWebioAn1GraphNtcMailAuthPassword_Type = OctetString
_WtWebioAn1GraphNtcMailAuthPassword_Object = MibScalar
wtWebioAn1GraphNtcMailAuthPassword = _WtWebioAn1GraphNtcMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 7),
    _WtWebioAn1GraphNtcMailAuthPassword_Type()
)
wtWebioAn1GraphNtcMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailAuthPassword.setStatus("mandatory")
_WtWebioAn1GraphNtcMailPop3Server_Type = OctetString
_WtWebioAn1GraphNtcMailPop3Server_Object = MibScalar
wtWebioAn1GraphNtcMailPop3Server = _WtWebioAn1GraphNtcMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 3, 8),
    _WtWebioAn1GraphNtcMailPop3Server_Type()
)
wtWebioAn1GraphNtcMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMailPop3Server.setStatus("mandatory")
_WtWebioAn1GraphNtcSNMP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcSNMP = _WtWebioAn1GraphNtcSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 4)
)
_WtWebioAn1GraphNtcSnmpCommunityStringRead_Type = OctetString
_WtWebioAn1GraphNtcSnmpCommunityStringRead_Object = MibScalar
wtWebioAn1GraphNtcSnmpCommunityStringRead = _WtWebioAn1GraphNtcSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 4, 1),
    _WtWebioAn1GraphNtcSnmpCommunityStringRead_Type()
)
wtWebioAn1GraphNtcSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSnmpCommunityStringRead.setStatus("mandatory")
_WtWebioAn1GraphNtcSnmpCommunityStringReadWrite_Type = OctetString
_WtWebioAn1GraphNtcSnmpCommunityStringReadWrite_Object = MibScalar
wtWebioAn1GraphNtcSnmpCommunityStringReadWrite = _WtWebioAn1GraphNtcSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 4, 2),
    _WtWebioAn1GraphNtcSnmpCommunityStringReadWrite_Type()
)
wtWebioAn1GraphNtcSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebioAn1GraphNtcSystemTrapManagerIP_Type = OctetString
_WtWebioAn1GraphNtcSystemTrapManagerIP_Object = MibScalar
wtWebioAn1GraphNtcSystemTrapManagerIP = _WtWebioAn1GraphNtcSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 4, 3),
    _WtWebioAn1GraphNtcSystemTrapManagerIP_Type()
)
wtWebioAn1GraphNtcSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSystemTrapManagerIP.setStatus("mandatory")


class _WtWebioAn1GraphNtcSystemTrapEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcSystemTrapEnable_Object = MibScalar
wtWebioAn1GraphNtcSystemTrapEnable = _WtWebioAn1GraphNtcSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 4, 4),
    _WtWebioAn1GraphNtcSystemTrapEnable_Type()
)
wtWebioAn1GraphNtcSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSystemTrapEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcSnmpEnable_Type = OctetString
_WtWebioAn1GraphNtcSnmpEnable_Object = MibScalar
wtWebioAn1GraphNtcSnmpEnable = _WtWebioAn1GraphNtcSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 4, 5),
    _WtWebioAn1GraphNtcSnmpEnable_Type()
)
wtWebioAn1GraphNtcSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSnmpEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcSnmpCommunityStringTrap_Type = OctetString
_WtWebioAn1GraphNtcSnmpCommunityStringTrap_Object = MibScalar
wtWebioAn1GraphNtcSnmpCommunityStringTrap = _WtWebioAn1GraphNtcSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 4, 6),
    _WtWebioAn1GraphNtcSnmpCommunityStringTrap_Type()
)
wtWebioAn1GraphNtcSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebioAn1GraphNtcUDP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcUDP = _WtWebioAn1GraphNtcUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 5)
)


class _WtWebioAn1GraphNtcUdpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphNtcUdpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcUdpPort_Object = MibScalar
wtWebioAn1GraphNtcUdpPort = _WtWebioAn1GraphNtcUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 5, 1),
    _WtWebioAn1GraphNtcUdpPort_Type()
)
wtWebioAn1GraphNtcUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcUdpPort.setStatus("mandatory")
_WtWebioAn1GraphNtcUdpEnable_Type = OctetString
_WtWebioAn1GraphNtcUdpEnable_Object = MibScalar
wtWebioAn1GraphNtcUdpEnable = _WtWebioAn1GraphNtcUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 5, 2),
    _WtWebioAn1GraphNtcUdpEnable_Type()
)
wtWebioAn1GraphNtcUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcUdpEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcSyslog_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcSyslog = _WtWebioAn1GraphNtcSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 6)
)
_WtWebioAn1GraphNtcSyslogServerIP_Type = OctetString
_WtWebioAn1GraphNtcSyslogServerIP_Object = MibScalar
wtWebioAn1GraphNtcSyslogServerIP = _WtWebioAn1GraphNtcSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 6, 1),
    _WtWebioAn1GraphNtcSyslogServerIP_Type()
)
wtWebioAn1GraphNtcSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSyslogServerIP.setStatus("mandatory")
_WtWebioAn1GraphNtcSyslogServerPort_Type = Integer32
_WtWebioAn1GraphNtcSyslogServerPort_Object = MibScalar
wtWebioAn1GraphNtcSyslogServerPort = _WtWebioAn1GraphNtcSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 6, 2),
    _WtWebioAn1GraphNtcSyslogServerPort_Type()
)
wtWebioAn1GraphNtcSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSyslogServerPort.setStatus("mandatory")


class _WtWebioAn1GraphNtcSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcSyslogSystemMessagesEnable_Object = MibScalar
wtWebioAn1GraphNtcSyslogSystemMessagesEnable = _WtWebioAn1GraphNtcSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 6, 3),
    _WtWebioAn1GraphNtcSyslogSystemMessagesEnable_Type()
)
wtWebioAn1GraphNtcSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcSyslogEnable_Type = OctetString
_WtWebioAn1GraphNtcSyslogEnable_Object = MibScalar
wtWebioAn1GraphNtcSyslogEnable = _WtWebioAn1GraphNtcSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 6, 4),
    _WtWebioAn1GraphNtcSyslogEnable_Type()
)
wtWebioAn1GraphNtcSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSyslogEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcFTP_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcFTP = _WtWebioAn1GraphNtcFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7)
)
_WtWebioAn1GraphNtcFTPServerIP_Type = OctetString
_WtWebioAn1GraphNtcFTPServerIP_Object = MibScalar
wtWebioAn1GraphNtcFTPServerIP = _WtWebioAn1GraphNtcFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7, 1),
    _WtWebioAn1GraphNtcFTPServerIP_Type()
)
wtWebioAn1GraphNtcFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcFTPServerIP.setStatus("mandatory")
_WtWebioAn1GraphNtcFTPServerControlPort_Type = Integer32
_WtWebioAn1GraphNtcFTPServerControlPort_Object = MibScalar
wtWebioAn1GraphNtcFTPServerControlPort = _WtWebioAn1GraphNtcFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7, 2),
    _WtWebioAn1GraphNtcFTPServerControlPort_Type()
)
wtWebioAn1GraphNtcFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcFTPServerControlPort.setStatus("mandatory")
_WtWebioAn1GraphNtcFTPUserName_Type = OctetString
_WtWebioAn1GraphNtcFTPUserName_Object = MibScalar
wtWebioAn1GraphNtcFTPUserName = _WtWebioAn1GraphNtcFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7, 3),
    _WtWebioAn1GraphNtcFTPUserName_Type()
)
wtWebioAn1GraphNtcFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcFTPUserName.setStatus("mandatory")
_WtWebioAn1GraphNtcFTPPassword_Type = OctetString
_WtWebioAn1GraphNtcFTPPassword_Object = MibScalar
wtWebioAn1GraphNtcFTPPassword = _WtWebioAn1GraphNtcFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7, 4),
    _WtWebioAn1GraphNtcFTPPassword_Type()
)
wtWebioAn1GraphNtcFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcFTPPassword.setStatus("mandatory")
_WtWebioAn1GraphNtcFTPAccount_Type = OctetString
_WtWebioAn1GraphNtcFTPAccount_Object = MibScalar
wtWebioAn1GraphNtcFTPAccount = _WtWebioAn1GraphNtcFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7, 5),
    _WtWebioAn1GraphNtcFTPAccount_Type()
)
wtWebioAn1GraphNtcFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcFTPAccount.setStatus("mandatory")
_WtWebioAn1GraphNtcFTPOption_Type = OctetString
_WtWebioAn1GraphNtcFTPOption_Object = MibScalar
wtWebioAn1GraphNtcFTPOption = _WtWebioAn1GraphNtcFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7, 6),
    _WtWebioAn1GraphNtcFTPOption_Type()
)
wtWebioAn1GraphNtcFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcFTPOption.setStatus("mandatory")
_WtWebioAn1GraphNtcFTPEnable_Type = OctetString
_WtWebioAn1GraphNtcFTPEnable_Object = MibScalar
wtWebioAn1GraphNtcFTPEnable = _WtWebioAn1GraphNtcFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 3, 7, 7),
    _WtWebioAn1GraphNtcFTPEnable_Type()
)
wtWebioAn1GraphNtcFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcFTPEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcDatalogger_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcDatalogger = _WtWebioAn1GraphNtcDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4)
)


class _WtWebioAn1GraphNtcLoggerTimebase_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcLoggerTimebase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcDatalogger-1Min", 1),
          ("wtWebioAn1GraphNtcDatalogger-5Min", 2),
          ("wtWebioAn1GraphNtcDatalogger-15Min", 3),
          ("wtWebioAn1GraphNtcDatalogger-60Min", 4))
    )


_WtWebioAn1GraphNtcLoggerTimebase_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcLoggerTimebase_Object = MibScalar
wtWebioAn1GraphNtcLoggerTimebase = _WtWebioAn1GraphNtcLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 1),
    _WtWebioAn1GraphNtcLoggerTimebase_Type()
)
wtWebioAn1GraphNtcLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcLoggerTimebase.setStatus("mandatory")


class _WtWebioAn1GraphNtcLoggerSensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcLoggerSensorSel_Object = MibScalar
wtWebioAn1GraphNtcLoggerSensorSel = _WtWebioAn1GraphNtcLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 2),
    _WtWebioAn1GraphNtcLoggerSensorSel_Type()
)
wtWebioAn1GraphNtcLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcLoggerSensorSel.setStatus("mandatory")


class _WtWebioAn1GraphNtcDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcDisplaySensorSel_Object = MibScalar
wtWebioAn1GraphNtcDisplaySensorSel = _WtWebioAn1GraphNtcDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 3),
    _WtWebioAn1GraphNtcDisplaySensorSel_Type()
)
wtWebioAn1GraphNtcDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDisplaySensorSel.setStatus("mandatory")
_WtWebioAn1GraphNtcSensorColorTable_Object = MibTable
wtWebioAn1GraphNtcSensorColorTable = _WtWebioAn1GraphNtcSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSensorColorTable.setStatus("mandatory")
_WtWebioAn1GraphNtcSensorColorEntry_Object = MibTableRow
wtWebioAn1GraphNtcSensorColorEntry = _WtWebioAn1GraphNtcSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 4, 1)
)
wtWebioAn1GraphNtcSensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSensorColorEntry.setStatus("mandatory")


class _WtWebioAn1GraphNtcSensorColor_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn1GraphNtcSensorColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcSensorColor_Object = MibTableColumn
wtWebioAn1GraphNtcSensorColor = _WtWebioAn1GraphNtcSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 4, 1, 1),
    _WtWebioAn1GraphNtcSensorColor_Type()
)
wtWebioAn1GraphNtcSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcSensorColor.setStatus("mandatory")
_WtWebioAn1GraphNtcAutoScaleEnable_Type = OctetString
_WtWebioAn1GraphNtcAutoScaleEnable_Object = MibScalar
wtWebioAn1GraphNtcAutoScaleEnable = _WtWebioAn1GraphNtcAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 5),
    _WtWebioAn1GraphNtcAutoScaleEnable_Type()
)
wtWebioAn1GraphNtcAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAutoScaleEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcVerticalUpperLimit_Type = OctetString
_WtWebioAn1GraphNtcVerticalUpperLimit_Object = MibScalar
wtWebioAn1GraphNtcVerticalUpperLimit = _WtWebioAn1GraphNtcVerticalUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 6),
    _WtWebioAn1GraphNtcVerticalUpperLimit_Type()
)
wtWebioAn1GraphNtcVerticalUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcVerticalUpperLimit.setStatus("mandatory")
_WtWebioAn1GraphNtcVerticalLowerLimit_Type = OctetString
_WtWebioAn1GraphNtcVerticalLowerLimit_Object = MibScalar
wtWebioAn1GraphNtcVerticalLowerLimit = _WtWebioAn1GraphNtcVerticalLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 7),
    _WtWebioAn1GraphNtcVerticalLowerLimit_Type()
)
wtWebioAn1GraphNtcVerticalLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcVerticalLowerLimit.setStatus("mandatory")


class _WtWebioAn1GraphNtcHorizontalZoom_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcHorizontalZoom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("wtWebioAn1GraphNtcZoom-25Min", 1),
          ("wtWebioAn1GraphNtcZoom-75Min", 2),
          ("wtWebioAn1GraphNtcZoom-5Std", 3),
          ("wtWebioAn1GraphNtcZoom-30Std", 4),
          ("wtWebioAn1GraphNtcZoom-5Tage", 5),
          ("wtWebioAn1GraphNtcZoom-25Tage", 6))
    )


_WtWebioAn1GraphNtcHorizontalZoom_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcHorizontalZoom_Object = MibScalar
wtWebioAn1GraphNtcHorizontalZoom = _WtWebioAn1GraphNtcHorizontalZoom_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 4, 8),
    _WtWebioAn1GraphNtcHorizontalZoom_Type()
)
wtWebioAn1GraphNtcHorizontalZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcHorizontalZoom.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarm_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcAlarm = _WtWebioAn1GraphNtcAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5)
)


class _WtWebioAn1GraphNtcAlarmCount_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphNtcAlarmCount_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcAlarmCount_Object = MibScalar
wtWebioAn1GraphNtcAlarmCount = _WtWebioAn1GraphNtcAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 1),
    _WtWebioAn1GraphNtcAlarmCount_Type()
)
wtWebioAn1GraphNtcAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmCount.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmIfTable_Object = MibTable
wtWebioAn1GraphNtcAlarmIfTable = _WtWebioAn1GraphNtcAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmIfTable.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmIfEntry_Object = MibTableRow
wtWebioAn1GraphNtcAlarmIfEntry = _WtWebioAn1GraphNtcAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 2, 1)
)
wtWebioAn1GraphNtcAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmIfEntry.setStatus("mandatory")


class _WtWebioAn1GraphNtcAlarmNo_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebioAn1GraphNtcAlarmNo_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcAlarmNo_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmNo = _WtWebioAn1GraphNtcAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 2, 1, 1),
    _WtWebioAn1GraphNtcAlarmNo_Type()
)
wtWebioAn1GraphNtcAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmNo.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmTable_Object = MibTable
wtWebioAn1GraphNtcAlarmTable = _WtWebioAn1GraphNtcAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmTable.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmEntry_Object = MibTableRow
wtWebioAn1GraphNtcAlarmEntry = _WtWebioAn1GraphNtcAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1)
)
wtWebioAn1GraphNtcAlarmEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmEntry.setStatus("mandatory")


class _WtWebioAn1GraphNtcAlarmTrigger_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcAlarmTrigger_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcAlarmTrigger_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmTrigger = _WtWebioAn1GraphNtcAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 1),
    _WtWebioAn1GraphNtcAlarmTrigger_Type()
)
wtWebioAn1GraphNtcAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmTrigger.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmMin_Type = OctetString
_WtWebioAn1GraphNtcAlarmMin_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmMin = _WtWebioAn1GraphNtcAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 2),
    _WtWebioAn1GraphNtcAlarmMin_Type()
)
wtWebioAn1GraphNtcAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmMin.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmMax_Type = OctetString
_WtWebioAn1GraphNtcAlarmMax_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmMax = _WtWebioAn1GraphNtcAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 3),
    _WtWebioAn1GraphNtcAlarmMax_Type()
)
wtWebioAn1GraphNtcAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmMax.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmHysteresis_Type = OctetString
_WtWebioAn1GraphNtcAlarmHysteresis_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmHysteresis = _WtWebioAn1GraphNtcAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 4),
    _WtWebioAn1GraphNtcAlarmHysteresis_Type()
)
wtWebioAn1GraphNtcAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmHysteresis.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmDelay_Type = OctetString
_WtWebioAn1GraphNtcAlarmDelay_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmDelay = _WtWebioAn1GraphNtcAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 5),
    _WtWebioAn1GraphNtcAlarmDelay_Type()
)
wtWebioAn1GraphNtcAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmDelay.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmInterval_Type = OctetString
_WtWebioAn1GraphNtcAlarmInterval_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmInterval = _WtWebioAn1GraphNtcAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 6),
    _WtWebioAn1GraphNtcAlarmInterval_Type()
)
wtWebioAn1GraphNtcAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmInterval.setStatus("mandatory")


class _WtWebioAn1GraphNtcAlarmEnable_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcAlarmEnable_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcAlarmEnable_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmEnable = _WtWebioAn1GraphNtcAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 7),
    _WtWebioAn1GraphNtcAlarmEnable_Type()
)
wtWebioAn1GraphNtcAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmEMailAddr_Type = OctetString
_WtWebioAn1GraphNtcAlarmEMailAddr_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmEMailAddr = _WtWebioAn1GraphNtcAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 8),
    _WtWebioAn1GraphNtcAlarmEMailAddr_Type()
)
wtWebioAn1GraphNtcAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmEMailAddr.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmMailSubject_Type = OctetString
_WtWebioAn1GraphNtcAlarmMailSubject_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmMailSubject = _WtWebioAn1GraphNtcAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 9),
    _WtWebioAn1GraphNtcAlarmMailSubject_Type()
)
wtWebioAn1GraphNtcAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmMailSubject.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmMailText_Type = OctetString
_WtWebioAn1GraphNtcAlarmMailText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmMailText = _WtWebioAn1GraphNtcAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 10),
    _WtWebioAn1GraphNtcAlarmMailText_Type()
)
wtWebioAn1GraphNtcAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmMailText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmManagerIP_Type = OctetString
_WtWebioAn1GraphNtcAlarmManagerIP_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmManagerIP = _WtWebioAn1GraphNtcAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 11),
    _WtWebioAn1GraphNtcAlarmManagerIP_Type()
)
wtWebioAn1GraphNtcAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmManagerIP.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmTrapText_Type = OctetString
_WtWebioAn1GraphNtcAlarmTrapText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmTrapText = _WtWebioAn1GraphNtcAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 12),
    _WtWebioAn1GraphNtcAlarmTrapText_Type()
)
wtWebioAn1GraphNtcAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmTrapText.setStatus("mandatory")


class _WtWebioAn1GraphNtcAlarmMailOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcAlarmMailOptions_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmMailOptions = _WtWebioAn1GraphNtcAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 13),
    _WtWebioAn1GraphNtcAlarmMailOptions_Type()
)
wtWebioAn1GraphNtcAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmMailOptions.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmTcpIpAddr_Type = OctetString
_WtWebioAn1GraphNtcAlarmTcpIpAddr_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmTcpIpAddr = _WtWebioAn1GraphNtcAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 14),
    _WtWebioAn1GraphNtcAlarmTcpIpAddr_Type()
)
wtWebioAn1GraphNtcAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphNtcAlarmTcpPort_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphNtcAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcAlarmTcpPort_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmTcpPort = _WtWebioAn1GraphNtcAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 15),
    _WtWebioAn1GraphNtcAlarmTcpPort_Type()
)
wtWebioAn1GraphNtcAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmTcpPort.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmTcpText_Type = OctetString
_WtWebioAn1GraphNtcAlarmTcpText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmTcpText = _WtWebioAn1GraphNtcAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 16),
    _WtWebioAn1GraphNtcAlarmTcpText_Type()
)
wtWebioAn1GraphNtcAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmTcpText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmClearMailSubject_Type = OctetString
_WtWebioAn1GraphNtcAlarmClearMailSubject_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmClearMailSubject = _WtWebioAn1GraphNtcAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 17),
    _WtWebioAn1GraphNtcAlarmClearMailSubject_Type()
)
wtWebioAn1GraphNtcAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmClearMailSubject.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmClearMailText_Type = OctetString
_WtWebioAn1GraphNtcAlarmClearMailText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmClearMailText = _WtWebioAn1GraphNtcAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 18),
    _WtWebioAn1GraphNtcAlarmClearMailText_Type()
)
wtWebioAn1GraphNtcAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmClearMailText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmClearTrapText_Type = OctetString
_WtWebioAn1GraphNtcAlarmClearTrapText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmClearTrapText = _WtWebioAn1GraphNtcAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 19),
    _WtWebioAn1GraphNtcAlarmClearTrapText_Type()
)
wtWebioAn1GraphNtcAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmClearTrapText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmClearTcpText_Type = OctetString
_WtWebioAn1GraphNtcAlarmClearTcpText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmClearTcpText = _WtWebioAn1GraphNtcAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 20),
    _WtWebioAn1GraphNtcAlarmClearTcpText_Type()
)
wtWebioAn1GraphNtcAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmClearTcpText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmSyslogIpAddr_Type = OctetString
_WtWebioAn1GraphNtcAlarmSyslogIpAddr_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmSyslogIpAddr = _WtWebioAn1GraphNtcAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 21),
    _WtWebioAn1GraphNtcAlarmSyslogIpAddr_Type()
)
wtWebioAn1GraphNtcAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebioAn1GraphNtcAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebioAn1GraphNtcAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebioAn1GraphNtcAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebioAn1GraphNtcAlarmSyslogPort_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmSyslogPort = _WtWebioAn1GraphNtcAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 22),
    _WtWebioAn1GraphNtcAlarmSyslogPort_Type()
)
wtWebioAn1GraphNtcAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmSyslogPort.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmSyslogText_Type = OctetString
_WtWebioAn1GraphNtcAlarmSyslogText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmSyslogText = _WtWebioAn1GraphNtcAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 23),
    _WtWebioAn1GraphNtcAlarmSyslogText_Type()
)
wtWebioAn1GraphNtcAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmSyslogText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmSyslogClearText_Type = OctetString
_WtWebioAn1GraphNtcAlarmSyslogClearText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmSyslogClearText = _WtWebioAn1GraphNtcAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 24),
    _WtWebioAn1GraphNtcAlarmSyslogClearText_Type()
)
wtWebioAn1GraphNtcAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmSyslogClearText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmFtpDataPort_Type = OctetString
_WtWebioAn1GraphNtcAlarmFtpDataPort_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmFtpDataPort = _WtWebioAn1GraphNtcAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 25),
    _WtWebioAn1GraphNtcAlarmFtpDataPort_Type()
)
wtWebioAn1GraphNtcAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmFtpDataPort.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmFtpFileName_Type = OctetString
_WtWebioAn1GraphNtcAlarmFtpFileName_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmFtpFileName = _WtWebioAn1GraphNtcAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 26),
    _WtWebioAn1GraphNtcAlarmFtpFileName_Type()
)
wtWebioAn1GraphNtcAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmFtpFileName.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmFtpText_Type = OctetString
_WtWebioAn1GraphNtcAlarmFtpText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmFtpText = _WtWebioAn1GraphNtcAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 27),
    _WtWebioAn1GraphNtcAlarmFtpText_Type()
)
wtWebioAn1GraphNtcAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmFtpText.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmFtpClearText_Type = OctetString
_WtWebioAn1GraphNtcAlarmFtpClearText_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmFtpClearText = _WtWebioAn1GraphNtcAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 28),
    _WtWebioAn1GraphNtcAlarmFtpClearText_Type()
)
wtWebioAn1GraphNtcAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmFtpClearText.setStatus("mandatory")


class _WtWebioAn1GraphNtcAlarmFtpOptions_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcAlarmFtpOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcAlarmFtpOptions_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcAlarmFtpOptions_Object = MibScalar
wtWebioAn1GraphNtcAlarmFtpOptions = _WtWebioAn1GraphNtcAlarmFtpOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 29),
    _WtWebioAn1GraphNtcAlarmFtpOptions_Type()
)
wtWebioAn1GraphNtcAlarmFtpOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmFtpOptions.setStatus("mandatory")
_WtWebioAn1GraphNtcAlarmTimerCron_Type = OctetString
_WtWebioAn1GraphNtcAlarmTimerCron_Object = MibTableColumn
wtWebioAn1GraphNtcAlarmTimerCron = _WtWebioAn1GraphNtcAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 5, 3, 1, 30),
    _WtWebioAn1GraphNtcAlarmTimerCron_Type()
)
wtWebioAn1GraphNtcAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlarmTimerCron.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphics_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcGraphics = _WtWebioAn1GraphNtcGraphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6)
)
_WtWebioAn1GraphNtcGraphicsBase_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcGraphicsBase = _WtWebioAn1GraphNtcGraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 1)
)
_WtWebioAn1GraphNtcGraphicsBaseEnable_Type = OctetString
_WtWebioAn1GraphNtcGraphicsBaseEnable_Object = MibScalar
wtWebioAn1GraphNtcGraphicsBaseEnable = _WtWebioAn1GraphNtcGraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 1, 1),
    _WtWebioAn1GraphNtcGraphicsBaseEnable_Type()
)
wtWebioAn1GraphNtcGraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsBaseEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsBaseWidth_Type = Integer32
_WtWebioAn1GraphNtcGraphicsBaseWidth_Object = MibScalar
wtWebioAn1GraphNtcGraphicsBaseWidth = _WtWebioAn1GraphNtcGraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 1, 2),
    _WtWebioAn1GraphNtcGraphicsBaseWidth_Type()
)
wtWebioAn1GraphNtcGraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsBaseWidth.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsBaseHeight_Type = Integer32
_WtWebioAn1GraphNtcGraphicsBaseHeight_Object = MibScalar
wtWebioAn1GraphNtcGraphicsBaseHeight = _WtWebioAn1GraphNtcGraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 1, 3),
    _WtWebioAn1GraphNtcGraphicsBaseHeight_Type()
)
wtWebioAn1GraphNtcGraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsBaseHeight.setStatus("mandatory")


class _WtWebioAn1GraphNtcGraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcGraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn1GraphNtcGraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcGraphicsBaseFrameColor_Object = MibScalar
wtWebioAn1GraphNtcGraphicsBaseFrameColor = _WtWebioAn1GraphNtcGraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 1, 4),
    _WtWebioAn1GraphNtcGraphicsBaseFrameColor_Type()
)
wtWebioAn1GraphNtcGraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebioAn1GraphNtcGraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcGraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn1GraphNtcGraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcGraphicsBaseBackgroundColor_Object = MibScalar
wtWebioAn1GraphNtcGraphicsBaseBackgroundColor = _WtWebioAn1GraphNtcGraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 1, 5),
    _WtWebioAn1GraphNtcGraphicsBaseBackgroundColor_Type()
)
wtWebioAn1GraphNtcGraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsBasePollingrate_Type = Integer32
_WtWebioAn1GraphNtcGraphicsBasePollingrate_Object = MibScalar
wtWebioAn1GraphNtcGraphicsBasePollingrate = _WtWebioAn1GraphNtcGraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 1, 6),
    _WtWebioAn1GraphNtcGraphicsBasePollingrate_Type()
)
wtWebioAn1GraphNtcGraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsBasePollingrate.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcGraphicsSelect = _WtWebioAn1GraphNtcGraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 2)
)


class _WtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel = _WtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 2, 1),
    _WtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel_Type()
)
wtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem = _WtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 2, 2),
    _WtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem_Type()
)
wtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebioAn1GraphNtc2SensorColorTable_Object = MibTable
wtWebioAn1GraphNtc2SensorColorTable = _WtWebioAn1GraphNtc2SensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtc2SensorColorTable.setStatus("mandatory")
_WtWebioAn1GraphNtc2SensorColorEntry_Object = MibTableRow
wtWebioAn1GraphNtc2SensorColorEntry = _WtWebioAn1GraphNtc2SensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 2, 3, 1)
)
wtWebioAn1GraphNtc2SensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtc2SensorColorEntry.setStatus("mandatory")


class _WtWebioAn1GraphNtcGraphicsSensorColor_Type(OctetString):
    """Custom type wtWebioAn1GraphNtcGraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebioAn1GraphNtcGraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebioAn1GraphNtcGraphicsSensorColor_Object = MibTableColumn
wtWebioAn1GraphNtcGraphicsSensorColor = _WtWebioAn1GraphNtcGraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 2, 3, 1, 1),
    _WtWebioAn1GraphNtcGraphicsSensorColor_Type()
)
wtWebioAn1GraphNtcGraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsSensorColor.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsSelectScale_Type = OctetString
_WtWebioAn1GraphNtcGraphicsSelectScale_Object = MibTableColumn
wtWebioAn1GraphNtcGraphicsSelectScale = _WtWebioAn1GraphNtcGraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 2, 3, 1, 2),
    _WtWebioAn1GraphNtcGraphicsSelectScale_Type()
)
wtWebioAn1GraphNtcGraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsSelectScale.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcGraphicsScale = _WtWebioAn1GraphNtcGraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3)
)
_WtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable = _WtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 1),
    _WtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable_Type()
)
wtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScaleAutoFitEnable_Type = OctetString
_WtWebioAn1GraphNtcGraphicsScaleAutoFitEnable_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScaleAutoFitEnable = _WtWebioAn1GraphNtcGraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 2),
    _WtWebioAn1GraphNtcGraphicsScaleAutoFitEnable_Type()
)
wtWebioAn1GraphNtcGraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale1Min_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale1Min_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale1Min = _WtWebioAn1GraphNtcGraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 3),
    _WtWebioAn1GraphNtcGraphicsScale1Min_Type()
)
wtWebioAn1GraphNtcGraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale1Min.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale2Min_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale2Min_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale2Min = _WtWebioAn1GraphNtcGraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 4),
    _WtWebioAn1GraphNtcGraphicsScale2Min_Type()
)
wtWebioAn1GraphNtcGraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale2Min.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale3Min_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale3Min_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale3Min = _WtWebioAn1GraphNtcGraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 5),
    _WtWebioAn1GraphNtcGraphicsScale3Min_Type()
)
wtWebioAn1GraphNtcGraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale3Min.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale4Min_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale4Min_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale4Min = _WtWebioAn1GraphNtcGraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 6),
    _WtWebioAn1GraphNtcGraphicsScale4Min_Type()
)
wtWebioAn1GraphNtcGraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale4Min.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale1Max_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale1Max_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale1Max = _WtWebioAn1GraphNtcGraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 7),
    _WtWebioAn1GraphNtcGraphicsScale1Max_Type()
)
wtWebioAn1GraphNtcGraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale1Max.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale2Max_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale2Max_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale2Max = _WtWebioAn1GraphNtcGraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 8),
    _WtWebioAn1GraphNtcGraphicsScale2Max_Type()
)
wtWebioAn1GraphNtcGraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale2Max.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale3Max_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale3Max_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale3Max = _WtWebioAn1GraphNtcGraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 9),
    _WtWebioAn1GraphNtcGraphicsScale3Max_Type()
)
wtWebioAn1GraphNtcGraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale3Max.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale4Max_Type = Integer32
_WtWebioAn1GraphNtcGraphicsScale4Max_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale4Max = _WtWebioAn1GraphNtcGraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 10),
    _WtWebioAn1GraphNtcGraphicsScale4Max_Type()
)
wtWebioAn1GraphNtcGraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale4Max.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale1Unit_Type = OctetString
_WtWebioAn1GraphNtcGraphicsScale1Unit_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale1Unit = _WtWebioAn1GraphNtcGraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 11),
    _WtWebioAn1GraphNtcGraphicsScale1Unit_Type()
)
wtWebioAn1GraphNtcGraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale1Unit.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale2Unit_Type = OctetString
_WtWebioAn1GraphNtcGraphicsScale2Unit_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale2Unit = _WtWebioAn1GraphNtcGraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 12),
    _WtWebioAn1GraphNtcGraphicsScale2Unit_Type()
)
wtWebioAn1GraphNtcGraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale2Unit.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale3Unit_Type = OctetString
_WtWebioAn1GraphNtcGraphicsScale3Unit_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale3Unit = _WtWebioAn1GraphNtcGraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 13),
    _WtWebioAn1GraphNtcGraphicsScale3Unit_Type()
)
wtWebioAn1GraphNtcGraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale3Unit.setStatus("mandatory")
_WtWebioAn1GraphNtcGraphicsScale4Unit_Type = OctetString
_WtWebioAn1GraphNtcGraphicsScale4Unit_Object = MibScalar
wtWebioAn1GraphNtcGraphicsScale4Unit = _WtWebioAn1GraphNtcGraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 1, 6, 3, 14),
    _WtWebioAn1GraphNtcGraphicsScale4Unit_Type()
)
wtWebioAn1GraphNtcGraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcGraphicsScale4Unit.setStatus("mandatory")
_WtWebioAn1GraphNtcPorts_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcPorts = _WtWebioAn1GraphNtcPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2)
)
_WtWebioAn1GraphNtcPortTable_Object = MibTable
wtWebioAn1GraphNtcPortTable = _WtWebioAn1GraphNtcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortTable.setStatus("mandatory")
_WtWebioAn1GraphNtcPortEntry_Object = MibTableRow
wtWebioAn1GraphNtcPortEntry = _WtWebioAn1GraphNtcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1)
)
wtWebioAn1GraphNtcPortEntry.setIndexNames(
    (0, "WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortEntry.setStatus("mandatory")
_WtWebioAn1GraphNtcPortName_Type = OctetString
_WtWebioAn1GraphNtcPortName_Object = MibTableColumn
wtWebioAn1GraphNtcPortName = _WtWebioAn1GraphNtcPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1, 1),
    _WtWebioAn1GraphNtcPortName_Type()
)
wtWebioAn1GraphNtcPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortName.setStatus("mandatory")
_WtWebioAn1GraphNtcPortText_Type = OctetString
_WtWebioAn1GraphNtcPortText_Object = MibTableColumn
wtWebioAn1GraphNtcPortText = _WtWebioAn1GraphNtcPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1, 2),
    _WtWebioAn1GraphNtcPortText_Type()
)
wtWebioAn1GraphNtcPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortText.setStatus("mandatory")
_WtWebioAn1GraphNtcPortOffset1_Type = OctetString
_WtWebioAn1GraphNtcPortOffset1_Object = MibTableColumn
wtWebioAn1GraphNtcPortOffset1 = _WtWebioAn1GraphNtcPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1, 3),
    _WtWebioAn1GraphNtcPortOffset1_Type()
)
wtWebioAn1GraphNtcPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortOffset1.setStatus("mandatory")
_WtWebioAn1GraphNtcPortTemperature1_Type = OctetString
_WtWebioAn1GraphNtcPortTemperature1_Object = MibTableColumn
wtWebioAn1GraphNtcPortTemperature1 = _WtWebioAn1GraphNtcPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1, 4),
    _WtWebioAn1GraphNtcPortTemperature1_Type()
)
wtWebioAn1GraphNtcPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortTemperature1.setStatus("mandatory")
_WtWebioAn1GraphNtcPortOffset2_Type = OctetString
_WtWebioAn1GraphNtcPortOffset2_Object = MibTableColumn
wtWebioAn1GraphNtcPortOffset2 = _WtWebioAn1GraphNtcPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1, 5),
    _WtWebioAn1GraphNtcPortOffset2_Type()
)
wtWebioAn1GraphNtcPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortOffset2.setStatus("mandatory")
_WtWebioAn1GraphNtcPortTemperature2_Type = OctetString
_WtWebioAn1GraphNtcPortTemperature2_Object = MibTableColumn
wtWebioAn1GraphNtcPortTemperature2 = _WtWebioAn1GraphNtcPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1, 6),
    _WtWebioAn1GraphNtcPortTemperature2_Type()
)
wtWebioAn1GraphNtcPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortTemperature2.setStatus("mandatory")
_WtWebioAn1GraphNtcPortComment_Type = OctetString
_WtWebioAn1GraphNtcPortComment_Object = MibTableColumn
wtWebioAn1GraphNtcPortComment = _WtWebioAn1GraphNtcPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 2, 1, 1, 7),
    _WtWebioAn1GraphNtcPortComment_Type()
)
wtWebioAn1GraphNtcPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcPortComment.setStatus("mandatory")
_WtWebioAn1GraphNtcManufact_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcManufact = _WtWebioAn1GraphNtcManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 3)
)
_WtWebioAn1GraphNtcMfName_Type = OctetString
_WtWebioAn1GraphNtcMfName_Object = MibScalar
wtWebioAn1GraphNtcMfName = _WtWebioAn1GraphNtcMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 3, 1),
    _WtWebioAn1GraphNtcMfName_Type()
)
wtWebioAn1GraphNtcMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMfName.setStatus("mandatory")
_WtWebioAn1GraphNtcMfAddr_Type = OctetString
_WtWebioAn1GraphNtcMfAddr_Object = MibScalar
wtWebioAn1GraphNtcMfAddr = _WtWebioAn1GraphNtcMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 3, 2),
    _WtWebioAn1GraphNtcMfAddr_Type()
)
wtWebioAn1GraphNtcMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMfAddr.setStatus("mandatory")
_WtWebioAn1GraphNtcMfHotline_Type = OctetString
_WtWebioAn1GraphNtcMfHotline_Object = MibScalar
wtWebioAn1GraphNtcMfHotline = _WtWebioAn1GraphNtcMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 3, 3),
    _WtWebioAn1GraphNtcMfHotline_Type()
)
wtWebioAn1GraphNtcMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMfHotline.setStatus("mandatory")
_WtWebioAn1GraphNtcMfInternet_Type = OctetString
_WtWebioAn1GraphNtcMfInternet_Object = MibScalar
wtWebioAn1GraphNtcMfInternet = _WtWebioAn1GraphNtcMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 3, 4),
    _WtWebioAn1GraphNtcMfInternet_Type()
)
wtWebioAn1GraphNtcMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMfInternet.setStatus("mandatory")
_WtWebioAn1GraphNtcMfDeviceTyp_Type = OctetString
_WtWebioAn1GraphNtcMfDeviceTyp_Object = MibScalar
wtWebioAn1GraphNtcMfDeviceTyp = _WtWebioAn1GraphNtcMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 3, 5),
    _WtWebioAn1GraphNtcMfDeviceTyp_Type()
)
wtWebioAn1GraphNtcMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMfDeviceTyp.setStatus("mandatory")
_WtWebioAn1GraphNtcMfOrderNo_Type = OctetString
_WtWebioAn1GraphNtcMfOrderNo_Object = MibScalar
wtWebioAn1GraphNtcMfOrderNo = _WtWebioAn1GraphNtcMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 3, 3, 6),
    _WtWebioAn1GraphNtcMfOrderNo_Type()
)
wtWebioAn1GraphNtcMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcMfOrderNo.setStatus("mandatory")
_WtWebioAn1GraphNtcDiag_ObjectIdentity = ObjectIdentity
wtWebioAn1GraphNtcDiag = _WtWebioAn1GraphNtcDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 4)
)
_WtWebioAn1GraphNtcDiagErrorCount_Type = Integer32
_WtWebioAn1GraphNtcDiagErrorCount_Object = MibScalar
wtWebioAn1GraphNtcDiagErrorCount = _WtWebioAn1GraphNtcDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 4, 1),
    _WtWebioAn1GraphNtcDiagErrorCount_Type()
)
wtWebioAn1GraphNtcDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDiagErrorCount.setStatus("mandatory")
_WtWebioAn1GraphNtcDiagBinaryError_Type = OctetString
_WtWebioAn1GraphNtcDiagBinaryError_Object = MibScalar
wtWebioAn1GraphNtcDiagBinaryError = _WtWebioAn1GraphNtcDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 4, 2),
    _WtWebioAn1GraphNtcDiagBinaryError_Type()
)
wtWebioAn1GraphNtcDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDiagBinaryError.setStatus("mandatory")
_WtWebioAn1GraphNtcDiagErrorIndex_Type = Integer32
_WtWebioAn1GraphNtcDiagErrorIndex_Object = MibScalar
wtWebioAn1GraphNtcDiagErrorIndex = _WtWebioAn1GraphNtcDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 4, 3),
    _WtWebioAn1GraphNtcDiagErrorIndex_Type()
)
wtWebioAn1GraphNtcDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDiagErrorIndex.setStatus("mandatory")
_WtWebioAn1GraphNtcDiagErrorMessage_Type = OctetString
_WtWebioAn1GraphNtcDiagErrorMessage_Object = MibScalar
wtWebioAn1GraphNtcDiagErrorMessage = _WtWebioAn1GraphNtcDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 4, 4),
    _WtWebioAn1GraphNtcDiagErrorMessage_Type()
)
wtWebioAn1GraphNtcDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDiagErrorMessage.setStatus("mandatory")
_WtWebioAn1GraphNtcDiagErrorClear_Type = Integer32
_WtWebioAn1GraphNtcDiagErrorClear_Object = MibScalar
wtWebioAn1GraphNtcDiagErrorClear = _WtWebioAn1GraphNtcDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 4, 5),
    _WtWebioAn1GraphNtcDiagErrorClear_Type()
)
wtWebioAn1GraphNtcDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebioAn1GraphNtcAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 31)
)
wtWebioAn1GraphNtcAlert1.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert1.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 32)
)
wtWebioAn1GraphNtcAlert2.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert2.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 33)
)
wtWebioAn1GraphNtcAlert3.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert3.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 34)
)
wtWebioAn1GraphNtcAlert4.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert4.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 35)
)
wtWebioAn1GraphNtcAlert5.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert5.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 36)
)
wtWebioAn1GraphNtcAlert6.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert6.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 37)
)
wtWebioAn1GraphNtcAlert7.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert7.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 38)
)
wtWebioAn1GraphNtcAlert8.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert8.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 91)
)
wtWebioAn1GraphNtcAlert9.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert9.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 92)
)
wtWebioAn1GraphNtcAlert10.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert10.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 93)
)
wtWebioAn1GraphNtcAlert11.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert11.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 94)
)
wtWebioAn1GraphNtcAlert12.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert12.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 95)
)
wtWebioAn1GraphNtcAlert13.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert13.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 96)
)
wtWebioAn1GraphNtcAlert14.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert14.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 97)
)
wtWebioAn1GraphNtcAlert15.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert15.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 98)
)
wtWebioAn1GraphNtcAlert16.setObjects(
    ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlert16.setStatus(
        ""
    )

wtWebioAn1GraphNtcAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 18, 0, 110)
)
wtWebioAn1GraphNtcAlertDiag.setObjects(
      *(("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcDiagErrorIndex"),
        ("WebGraph-Thermometer-NTC-MIB", "wtWebioAn1GraphNtcDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebioAn1GraphNtcAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-Thermometer-NTC-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebioAn1GraphNtc": wtWebioAn1GraphNtc,
       "wtWebioAn1GraphNtcAlert1": wtWebioAn1GraphNtcAlert1,
       "wtWebioAn1GraphNtcAlert2": wtWebioAn1GraphNtcAlert2,
       "wtWebioAn1GraphNtcAlert3": wtWebioAn1GraphNtcAlert3,
       "wtWebioAn1GraphNtcAlert4": wtWebioAn1GraphNtcAlert4,
       "wtWebioAn1GraphNtcAlert5": wtWebioAn1GraphNtcAlert5,
       "wtWebioAn1GraphNtcAlert6": wtWebioAn1GraphNtcAlert6,
       "wtWebioAn1GraphNtcAlert7": wtWebioAn1GraphNtcAlert7,
       "wtWebioAn1GraphNtcAlert8": wtWebioAn1GraphNtcAlert8,
       "wtWebioAn1GraphNtcAlert9": wtWebioAn1GraphNtcAlert9,
       "wtWebioAn1GraphNtcAlert10": wtWebioAn1GraphNtcAlert10,
       "wtWebioAn1GraphNtcAlert11": wtWebioAn1GraphNtcAlert11,
       "wtWebioAn1GraphNtcAlert12": wtWebioAn1GraphNtcAlert12,
       "wtWebioAn1GraphNtcAlert13": wtWebioAn1GraphNtcAlert13,
       "wtWebioAn1GraphNtcAlert14": wtWebioAn1GraphNtcAlert14,
       "wtWebioAn1GraphNtcAlert15": wtWebioAn1GraphNtcAlert15,
       "wtWebioAn1GraphNtcAlert16": wtWebioAn1GraphNtcAlert16,
       "wtWebioAn1GraphNtcAlertDiag": wtWebioAn1GraphNtcAlertDiag,
       "wtWebioAn1GraphNtcTemp": wtWebioAn1GraphNtcTemp,
       "wtWebioAn1GraphNtcSensors": wtWebioAn1GraphNtcSensors,
       "wtWebioAn1GraphNtcSensorTable": wtWebioAn1GraphNtcSensorTable,
       "wtWebioAn1GraphNtcSensorEntry": wtWebioAn1GraphNtcSensorEntry,
       "wtWebioAn1GraphNtcSensorNo": wtWebioAn1GraphNtcSensorNo,
       "wtWebioAn1GraphNtcTempValueTable": wtWebioAn1GraphNtcTempValueTable,
       "wtWebioAn1GraphNtcTempValueEntry": wtWebioAn1GraphNtcTempValueEntry,
       "wtWebioAn1GraphNtcTempValue": wtWebioAn1GraphNtcTempValue,
       "wtWebioAn1GraphNtcBinaryTempValueTable": wtWebioAn1GraphNtcBinaryTempValueTable,
       "wtWebioAn1GraphNtcBinaryTempValueEntry": wtWebioAn1GraphNtcBinaryTempValueEntry,
       "wtWebioAn1GraphNtcBinaryTempValue": wtWebioAn1GraphNtcBinaryTempValue,
       "wtWebioAn1GraphNtcTempValuePktTable": wtWebioAn1GraphNtcTempValuePktTable,
       "wtWebioAn1GraphNtcTempValuePktEntry": wtWebioAn1GraphNtcTempValuePktEntry,
       "wtWebioAn1GraphNtcTempValuePkt": wtWebioAn1GraphNtcTempValuePkt,
       "wtWebioAn1GraphNtcSessCntrl": wtWebioAn1GraphNtcSessCntrl,
       "wtWebioAn1GraphNtcSessCntrlPassword": wtWebioAn1GraphNtcSessCntrlPassword,
       "wtWebioAn1GraphNtcSessCntrlConfigMode": wtWebioAn1GraphNtcSessCntrlConfigMode,
       "wtWebioAn1GraphNtcSessCntrlLogout": wtWebioAn1GraphNtcSessCntrlLogout,
       "wtWebioAn1GraphNtcSessCntrlAdminPassword": wtWebioAn1GraphNtcSessCntrlAdminPassword,
       "wtWebioAn1GraphNtcSessCntrlConfigPassword": wtWebioAn1GraphNtcSessCntrlConfigPassword,
       "wtWebioAn1GraphNtcConfig": wtWebioAn1GraphNtcConfig,
       "wtWebioAn1GraphNtcDevice": wtWebioAn1GraphNtcDevice,
       "wtWebioAn1GraphNtcText": wtWebioAn1GraphNtcText,
       "wtWebioAn1GraphNtcDeviceName": wtWebioAn1GraphNtcDeviceName,
       "wtWebioAn1GraphNtcDeviceText": wtWebioAn1GraphNtcDeviceText,
       "wtWebioAn1GraphNtcDeviceLocation": wtWebioAn1GraphNtcDeviceLocation,
       "wtWebioAn1GraphNtcDeviceContact": wtWebioAn1GraphNtcDeviceContact,
       "wtWebioAn1GraphNtcTimeDate": wtWebioAn1GraphNtcTimeDate,
       "wtWebioAn1GraphNtcTimeZone": wtWebioAn1GraphNtcTimeZone,
       "wtWebioAn1GraphNtcTzOffsetHrs": wtWebioAn1GraphNtcTzOffsetHrs,
       "wtWebioAn1GraphNtcTzOffsetMin": wtWebioAn1GraphNtcTzOffsetMin,
       "wtWebioAn1GraphNtcTzEnable": wtWebioAn1GraphNtcTzEnable,
       "wtWebioAn1GraphNtcStTzOffsetHrs": wtWebioAn1GraphNtcStTzOffsetHrs,
       "wtWebioAn1GraphNtcStTzOffsetMin": wtWebioAn1GraphNtcStTzOffsetMin,
       "wtWebioAn1GraphNtcStTzEnable": wtWebioAn1GraphNtcStTzEnable,
       "wtWebioAn1GraphNtcStTzStartMonth": wtWebioAn1GraphNtcStTzStartMonth,
       "wtWebioAn1GraphNtcStTzStartMode": wtWebioAn1GraphNtcStTzStartMode,
       "wtWebioAn1GraphNtcStTzStartWday": wtWebioAn1GraphNtcStTzStartWday,
       "wtWebioAn1GraphNtcStTzStartHrs": wtWebioAn1GraphNtcStTzStartHrs,
       "wtWebioAn1GraphNtcStTzStartMin": wtWebioAn1GraphNtcStTzStartMin,
       "wtWebioAn1GraphNtcStTzStopMonth": wtWebioAn1GraphNtcStTzStopMonth,
       "wtWebioAn1GraphNtcStTzStopMode": wtWebioAn1GraphNtcStTzStopMode,
       "wtWebioAn1GraphNtcStTzStopWday": wtWebioAn1GraphNtcStTzStopWday,
       "wtWebioAn1GraphNtcStTzStopHrs": wtWebioAn1GraphNtcStTzStopHrs,
       "wtWebioAn1GraphNtcStTzStopMin": wtWebioAn1GraphNtcStTzStopMin,
       "wtWebioAn1GraphNtcTimeServer": wtWebioAn1GraphNtcTimeServer,
       "wtWebioAn1GraphNtcTimeServer1": wtWebioAn1GraphNtcTimeServer1,
       "wtWebioAn1GraphNtcTimeServer2": wtWebioAn1GraphNtcTimeServer2,
       "wtWebioAn1GraphNtcTsEnable": wtWebioAn1GraphNtcTsEnable,
       "wtWebioAn1GraphNtcTsSyncTime": wtWebioAn1GraphNtcTsSyncTime,
       "wtWebioAn1GraphNtcDeviceClock": wtWebioAn1GraphNtcDeviceClock,
       "wtWebioAn1GraphNtcClockHrs": wtWebioAn1GraphNtcClockHrs,
       "wtWebioAn1GraphNtcClockMin": wtWebioAn1GraphNtcClockMin,
       "wtWebioAn1GraphNtcClockDay": wtWebioAn1GraphNtcClockDay,
       "wtWebioAn1GraphNtcClockMonth": wtWebioAn1GraphNtcClockMonth,
       "wtWebioAn1GraphNtcClockYear": wtWebioAn1GraphNtcClockYear,
       "wtWebioAn1GraphNtcBasic": wtWebioAn1GraphNtcBasic,
       "wtWebioAn1GraphNtcNetwork": wtWebioAn1GraphNtcNetwork,
       "wtWebioAn1GraphNtcIpAddress": wtWebioAn1GraphNtcIpAddress,
       "wtWebioAn1GraphNtcSubnetMask": wtWebioAn1GraphNtcSubnetMask,
       "wtWebioAn1GraphNtcGateway": wtWebioAn1GraphNtcGateway,
       "wtWebioAn1GraphNtcDnsServer1": wtWebioAn1GraphNtcDnsServer1,
       "wtWebioAn1GraphNtcDnsServer2": wtWebioAn1GraphNtcDnsServer2,
       "wtWebioAn1GraphNtcAddConfig": wtWebioAn1GraphNtcAddConfig,
       "wtWebioAn1GraphNtcHTTP": wtWebioAn1GraphNtcHTTP,
       "wtWebioAn1GraphNtcStartup": wtWebioAn1GraphNtcStartup,
       "wtWebioAn1GraphNtcGetHeaderEnable": wtWebioAn1GraphNtcGetHeaderEnable,
       "wtWebioAn1GraphNtcHttpPort": wtWebioAn1GraphNtcHttpPort,
       "wtWebioAn1GraphNtcMail": wtWebioAn1GraphNtcMail,
       "wtWebioAn1GraphNtcMailAdName": wtWebioAn1GraphNtcMailAdName,
       "wtWebioAn1GraphNtcMailReply": wtWebioAn1GraphNtcMailReply,
       "wtWebioAn1GraphNtcMailServer": wtWebioAn1GraphNtcMailServer,
       "wtWebioAn1GraphNtcMailEnable": wtWebioAn1GraphNtcMailEnable,
       "wtWebioAn1GraphNtcMailAuthentication": wtWebioAn1GraphNtcMailAuthentication,
       "wtWebioAn1GraphNtcMailAuthUser": wtWebioAn1GraphNtcMailAuthUser,
       "wtWebioAn1GraphNtcMailAuthPassword": wtWebioAn1GraphNtcMailAuthPassword,
       "wtWebioAn1GraphNtcMailPop3Server": wtWebioAn1GraphNtcMailPop3Server,
       "wtWebioAn1GraphNtcSNMP": wtWebioAn1GraphNtcSNMP,
       "wtWebioAn1GraphNtcSnmpCommunityStringRead": wtWebioAn1GraphNtcSnmpCommunityStringRead,
       "wtWebioAn1GraphNtcSnmpCommunityStringReadWrite": wtWebioAn1GraphNtcSnmpCommunityStringReadWrite,
       "wtWebioAn1GraphNtcSystemTrapManagerIP": wtWebioAn1GraphNtcSystemTrapManagerIP,
       "wtWebioAn1GraphNtcSystemTrapEnable": wtWebioAn1GraphNtcSystemTrapEnable,
       "wtWebioAn1GraphNtcSnmpEnable": wtWebioAn1GraphNtcSnmpEnable,
       "wtWebioAn1GraphNtcSnmpCommunityStringTrap": wtWebioAn1GraphNtcSnmpCommunityStringTrap,
       "wtWebioAn1GraphNtcUDP": wtWebioAn1GraphNtcUDP,
       "wtWebioAn1GraphNtcUdpPort": wtWebioAn1GraphNtcUdpPort,
       "wtWebioAn1GraphNtcUdpEnable": wtWebioAn1GraphNtcUdpEnable,
       "wtWebioAn1GraphNtcSyslog": wtWebioAn1GraphNtcSyslog,
       "wtWebioAn1GraphNtcSyslogServerIP": wtWebioAn1GraphNtcSyslogServerIP,
       "wtWebioAn1GraphNtcSyslogServerPort": wtWebioAn1GraphNtcSyslogServerPort,
       "wtWebioAn1GraphNtcSyslogSystemMessagesEnable": wtWebioAn1GraphNtcSyslogSystemMessagesEnable,
       "wtWebioAn1GraphNtcSyslogEnable": wtWebioAn1GraphNtcSyslogEnable,
       "wtWebioAn1GraphNtcFTP": wtWebioAn1GraphNtcFTP,
       "wtWebioAn1GraphNtcFTPServerIP": wtWebioAn1GraphNtcFTPServerIP,
       "wtWebioAn1GraphNtcFTPServerControlPort": wtWebioAn1GraphNtcFTPServerControlPort,
       "wtWebioAn1GraphNtcFTPUserName": wtWebioAn1GraphNtcFTPUserName,
       "wtWebioAn1GraphNtcFTPPassword": wtWebioAn1GraphNtcFTPPassword,
       "wtWebioAn1GraphNtcFTPAccount": wtWebioAn1GraphNtcFTPAccount,
       "wtWebioAn1GraphNtcFTPOption": wtWebioAn1GraphNtcFTPOption,
       "wtWebioAn1GraphNtcFTPEnable": wtWebioAn1GraphNtcFTPEnable,
       "wtWebioAn1GraphNtcDatalogger": wtWebioAn1GraphNtcDatalogger,
       "wtWebioAn1GraphNtcLoggerTimebase": wtWebioAn1GraphNtcLoggerTimebase,
       "wtWebioAn1GraphNtcLoggerSensorSel": wtWebioAn1GraphNtcLoggerSensorSel,
       "wtWebioAn1GraphNtcDisplaySensorSel": wtWebioAn1GraphNtcDisplaySensorSel,
       "wtWebioAn1GraphNtcSensorColorTable": wtWebioAn1GraphNtcSensorColorTable,
       "wtWebioAn1GraphNtcSensorColorEntry": wtWebioAn1GraphNtcSensorColorEntry,
       "wtWebioAn1GraphNtcSensorColor": wtWebioAn1GraphNtcSensorColor,
       "wtWebioAn1GraphNtcAutoScaleEnable": wtWebioAn1GraphNtcAutoScaleEnable,
       "wtWebioAn1GraphNtcVerticalUpperLimit": wtWebioAn1GraphNtcVerticalUpperLimit,
       "wtWebioAn1GraphNtcVerticalLowerLimit": wtWebioAn1GraphNtcVerticalLowerLimit,
       "wtWebioAn1GraphNtcHorizontalZoom": wtWebioAn1GraphNtcHorizontalZoom,
       "wtWebioAn1GraphNtcAlarm": wtWebioAn1GraphNtcAlarm,
       "wtWebioAn1GraphNtcAlarmCount": wtWebioAn1GraphNtcAlarmCount,
       "wtWebioAn1GraphNtcAlarmIfTable": wtWebioAn1GraphNtcAlarmIfTable,
       "wtWebioAn1GraphNtcAlarmIfEntry": wtWebioAn1GraphNtcAlarmIfEntry,
       "wtWebioAn1GraphNtcAlarmNo": wtWebioAn1GraphNtcAlarmNo,
       "wtWebioAn1GraphNtcAlarmTable": wtWebioAn1GraphNtcAlarmTable,
       "wtWebioAn1GraphNtcAlarmEntry": wtWebioAn1GraphNtcAlarmEntry,
       "wtWebioAn1GraphNtcAlarmTrigger": wtWebioAn1GraphNtcAlarmTrigger,
       "wtWebioAn1GraphNtcAlarmMin": wtWebioAn1GraphNtcAlarmMin,
       "wtWebioAn1GraphNtcAlarmMax": wtWebioAn1GraphNtcAlarmMax,
       "wtWebioAn1GraphNtcAlarmHysteresis": wtWebioAn1GraphNtcAlarmHysteresis,
       "wtWebioAn1GraphNtcAlarmDelay": wtWebioAn1GraphNtcAlarmDelay,
       "wtWebioAn1GraphNtcAlarmInterval": wtWebioAn1GraphNtcAlarmInterval,
       "wtWebioAn1GraphNtcAlarmEnable": wtWebioAn1GraphNtcAlarmEnable,
       "wtWebioAn1GraphNtcAlarmEMailAddr": wtWebioAn1GraphNtcAlarmEMailAddr,
       "wtWebioAn1GraphNtcAlarmMailSubject": wtWebioAn1GraphNtcAlarmMailSubject,
       "wtWebioAn1GraphNtcAlarmMailText": wtWebioAn1GraphNtcAlarmMailText,
       "wtWebioAn1GraphNtcAlarmManagerIP": wtWebioAn1GraphNtcAlarmManagerIP,
       "wtWebioAn1GraphNtcAlarmTrapText": wtWebioAn1GraphNtcAlarmTrapText,
       "wtWebioAn1GraphNtcAlarmMailOptions": wtWebioAn1GraphNtcAlarmMailOptions,
       "wtWebioAn1GraphNtcAlarmTcpIpAddr": wtWebioAn1GraphNtcAlarmTcpIpAddr,
       "wtWebioAn1GraphNtcAlarmTcpPort": wtWebioAn1GraphNtcAlarmTcpPort,
       "wtWebioAn1GraphNtcAlarmTcpText": wtWebioAn1GraphNtcAlarmTcpText,
       "wtWebioAn1GraphNtcAlarmClearMailSubject": wtWebioAn1GraphNtcAlarmClearMailSubject,
       "wtWebioAn1GraphNtcAlarmClearMailText": wtWebioAn1GraphNtcAlarmClearMailText,
       "wtWebioAn1GraphNtcAlarmClearTrapText": wtWebioAn1GraphNtcAlarmClearTrapText,
       "wtWebioAn1GraphNtcAlarmClearTcpText": wtWebioAn1GraphNtcAlarmClearTcpText,
       "wtWebioAn1GraphNtcAlarmSyslogIpAddr": wtWebioAn1GraphNtcAlarmSyslogIpAddr,
       "wtWebioAn1GraphNtcAlarmSyslogPort": wtWebioAn1GraphNtcAlarmSyslogPort,
       "wtWebioAn1GraphNtcAlarmSyslogText": wtWebioAn1GraphNtcAlarmSyslogText,
       "wtWebioAn1GraphNtcAlarmSyslogClearText": wtWebioAn1GraphNtcAlarmSyslogClearText,
       "wtWebioAn1GraphNtcAlarmFtpDataPort": wtWebioAn1GraphNtcAlarmFtpDataPort,
       "wtWebioAn1GraphNtcAlarmFtpFileName": wtWebioAn1GraphNtcAlarmFtpFileName,
       "wtWebioAn1GraphNtcAlarmFtpText": wtWebioAn1GraphNtcAlarmFtpText,
       "wtWebioAn1GraphNtcAlarmFtpClearText": wtWebioAn1GraphNtcAlarmFtpClearText,
       "wtWebioAn1GraphNtcAlarmFtpOptions": wtWebioAn1GraphNtcAlarmFtpOptions,
       "wtWebioAn1GraphNtcAlarmTimerCron": wtWebioAn1GraphNtcAlarmTimerCron,
       "wtWebioAn1GraphNtcGraphics": wtWebioAn1GraphNtcGraphics,
       "wtWebioAn1GraphNtcGraphicsBase": wtWebioAn1GraphNtcGraphicsBase,
       "wtWebioAn1GraphNtcGraphicsBaseEnable": wtWebioAn1GraphNtcGraphicsBaseEnable,
       "wtWebioAn1GraphNtcGraphicsBaseWidth": wtWebioAn1GraphNtcGraphicsBaseWidth,
       "wtWebioAn1GraphNtcGraphicsBaseHeight": wtWebioAn1GraphNtcGraphicsBaseHeight,
       "wtWebioAn1GraphNtcGraphicsBaseFrameColor": wtWebioAn1GraphNtcGraphicsBaseFrameColor,
       "wtWebioAn1GraphNtcGraphicsBaseBackgroundColor": wtWebioAn1GraphNtcGraphicsBaseBackgroundColor,
       "wtWebioAn1GraphNtcGraphicsBasePollingrate": wtWebioAn1GraphNtcGraphicsBasePollingrate,
       "wtWebioAn1GraphNtcGraphicsSelect": wtWebioAn1GraphNtcGraphicsSelect,
       "wtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel": wtWebioAn1GraphNtcGraphicsSelectDisplaySensorSel,
       "wtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem": wtWebioAn1GraphNtcGraphicsSelectDisplayShowExtrem,
       "wtWebioAn1GraphNtc2SensorColorTable": wtWebioAn1GraphNtc2SensorColorTable,
       "wtWebioAn1GraphNtc2SensorColorEntry": wtWebioAn1GraphNtc2SensorColorEntry,
       "wtWebioAn1GraphNtcGraphicsSensorColor": wtWebioAn1GraphNtcGraphicsSensorColor,
       "wtWebioAn1GraphNtcGraphicsSelectScale": wtWebioAn1GraphNtcGraphicsSelectScale,
       "wtWebioAn1GraphNtcGraphicsScale": wtWebioAn1GraphNtcGraphicsScale,
       "wtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable": wtWebioAn1GraphNtcGraphicsScaleAutoScaleEnable,
       "wtWebioAn1GraphNtcGraphicsScaleAutoFitEnable": wtWebioAn1GraphNtcGraphicsScaleAutoFitEnable,
       "wtWebioAn1GraphNtcGraphicsScale1Min": wtWebioAn1GraphNtcGraphicsScale1Min,
       "wtWebioAn1GraphNtcGraphicsScale2Min": wtWebioAn1GraphNtcGraphicsScale2Min,
       "wtWebioAn1GraphNtcGraphicsScale3Min": wtWebioAn1GraphNtcGraphicsScale3Min,
       "wtWebioAn1GraphNtcGraphicsScale4Min": wtWebioAn1GraphNtcGraphicsScale4Min,
       "wtWebioAn1GraphNtcGraphicsScale1Max": wtWebioAn1GraphNtcGraphicsScale1Max,
       "wtWebioAn1GraphNtcGraphicsScale2Max": wtWebioAn1GraphNtcGraphicsScale2Max,
       "wtWebioAn1GraphNtcGraphicsScale3Max": wtWebioAn1GraphNtcGraphicsScale3Max,
       "wtWebioAn1GraphNtcGraphicsScale4Max": wtWebioAn1GraphNtcGraphicsScale4Max,
       "wtWebioAn1GraphNtcGraphicsScale1Unit": wtWebioAn1GraphNtcGraphicsScale1Unit,
       "wtWebioAn1GraphNtcGraphicsScale2Unit": wtWebioAn1GraphNtcGraphicsScale2Unit,
       "wtWebioAn1GraphNtcGraphicsScale3Unit": wtWebioAn1GraphNtcGraphicsScale3Unit,
       "wtWebioAn1GraphNtcGraphicsScale4Unit": wtWebioAn1GraphNtcGraphicsScale4Unit,
       "wtWebioAn1GraphNtcPorts": wtWebioAn1GraphNtcPorts,
       "wtWebioAn1GraphNtcPortTable": wtWebioAn1GraphNtcPortTable,
       "wtWebioAn1GraphNtcPortEntry": wtWebioAn1GraphNtcPortEntry,
       "wtWebioAn1GraphNtcPortName": wtWebioAn1GraphNtcPortName,
       "wtWebioAn1GraphNtcPortText": wtWebioAn1GraphNtcPortText,
       "wtWebioAn1GraphNtcPortOffset1": wtWebioAn1GraphNtcPortOffset1,
       "wtWebioAn1GraphNtcPortTemperature1": wtWebioAn1GraphNtcPortTemperature1,
       "wtWebioAn1GraphNtcPortOffset2": wtWebioAn1GraphNtcPortOffset2,
       "wtWebioAn1GraphNtcPortTemperature2": wtWebioAn1GraphNtcPortTemperature2,
       "wtWebioAn1GraphNtcPortComment": wtWebioAn1GraphNtcPortComment,
       "wtWebioAn1GraphNtcManufact": wtWebioAn1GraphNtcManufact,
       "wtWebioAn1GraphNtcMfName": wtWebioAn1GraphNtcMfName,
       "wtWebioAn1GraphNtcMfAddr": wtWebioAn1GraphNtcMfAddr,
       "wtWebioAn1GraphNtcMfHotline": wtWebioAn1GraphNtcMfHotline,
       "wtWebioAn1GraphNtcMfInternet": wtWebioAn1GraphNtcMfInternet,
       "wtWebioAn1GraphNtcMfDeviceTyp": wtWebioAn1GraphNtcMfDeviceTyp,
       "wtWebioAn1GraphNtcMfOrderNo": wtWebioAn1GraphNtcMfOrderNo,
       "wtWebioAn1GraphNtcDiag": wtWebioAn1GraphNtcDiag,
       "wtWebioAn1GraphNtcDiagErrorCount": wtWebioAn1GraphNtcDiagErrorCount,
       "wtWebioAn1GraphNtcDiagBinaryError": wtWebioAn1GraphNtcDiagBinaryError,
       "wtWebioAn1GraphNtcDiagErrorIndex": wtWebioAn1GraphNtcDiagErrorIndex,
       "wtWebioAn1GraphNtcDiagErrorMessage": wtWebioAn1GraphNtcDiagErrorMessage,
       "wtWebioAn1GraphNtcDiagErrorClear": wtWebioAn1GraphNtcDiagErrorClear}
)
