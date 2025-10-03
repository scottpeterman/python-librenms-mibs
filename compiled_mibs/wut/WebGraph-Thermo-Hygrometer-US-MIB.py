# SNMP MIB module (WebGraph-Thermo-Hygrometer-US-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wut\WebGraph-Thermo-Hygrometer-US-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:29 2025
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
_WtWebGraphThermoHygro_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygro = _WtWebGraphThermoHygro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42)
)
_WtWebGraphThermoHygroTemp_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroTemp = _WtWebGraphThermoHygroTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1)
)


class _WtWebGraphThermoHygroSensors_Type(Integer32):
    """Custom type wtWebGraphThermoHygroSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphThermoHygroSensors_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroSensors_Object = MibScalar
wtWebGraphThermoHygroSensors = _WtWebGraphThermoHygroSensors_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 1),
    _WtWebGraphThermoHygroSensors_Type()
)
wtWebGraphThermoHygroSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSensors.setStatus("mandatory")
_WtWebGraphThermoHygroSensorTable_Object = MibTable
wtWebGraphThermoHygroSensorTable = _WtWebGraphThermoHygroSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSensorTable.setStatus("mandatory")
_WtWebGraphThermoHygroSensorEntry_Object = MibTableRow
wtWebGraphThermoHygroSensorEntry = _WtWebGraphThermoHygroSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 2, 1)
)
wtWebGraphThermoHygroSensorEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSensorEntry.setStatus("mandatory")


class _WtWebGraphThermoHygroSensorNo_Type(Integer32):
    """Custom type wtWebGraphThermoHygroSensorNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WtWebGraphThermoHygroSensorNo_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroSensorNo_Object = MibTableColumn
wtWebGraphThermoHygroSensorNo = _WtWebGraphThermoHygroSensorNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 2, 1, 1),
    _WtWebGraphThermoHygroSensorNo_Type()
)
wtWebGraphThermoHygroSensorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSensorNo.setStatus("mandatory")
_WtWebGraphThermoHygroTempValueTable_Object = MibTable
wtWebGraphThermoHygroTempValueTable = _WtWebGraphThermoHygroTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTempValueTable.setStatus("mandatory")
_WtWebGraphThermoHygroTempValueEntry_Object = MibTableRow
wtWebGraphThermoHygroTempValueEntry = _WtWebGraphThermoHygroTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 3, 1)
)
wtWebGraphThermoHygroTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTempValueEntry.setStatus("mandatory")


class _WtWebGraphThermoHygroTempValue_Type(OctetString):
    """Custom type wtWebGraphThermoHygroTempValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebGraphThermoHygroTempValue_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroTempValue_Object = MibTableColumn
wtWebGraphThermoHygroTempValue = _WtWebGraphThermoHygroTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 3, 1, 1),
    _WtWebGraphThermoHygroTempValue_Type()
)
wtWebGraphThermoHygroTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTempValue.setStatus("mandatory")
_WtWebGraphThermoHygroBinaryTempValueTable_Object = MibTable
wtWebGraphThermoHygroBinaryTempValueTable = _WtWebGraphThermoHygroBinaryTempValueTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 4)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroBinaryTempValueTable.setStatus("mandatory")
_WtWebGraphThermoHygroBinaryTempValueEntry_Object = MibTableRow
wtWebGraphThermoHygroBinaryTempValueEntry = _WtWebGraphThermoHygroBinaryTempValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 4, 1)
)
wtWebGraphThermoHygroBinaryTempValueEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroBinaryTempValueEntry.setStatus("mandatory")
_WtWebGraphThermoHygroBinaryTempValue_Type = Integer32
_WtWebGraphThermoHygroBinaryTempValue_Object = MibTableColumn
wtWebGraphThermoHygroBinaryTempValue = _WtWebGraphThermoHygroBinaryTempValue_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 4, 1, 1),
    _WtWebGraphThermoHygroBinaryTempValue_Type()
)
wtWebGraphThermoHygroBinaryTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroBinaryTempValue.setStatus("mandatory")
_WtWebGraphThermoHygroTempValuePktTable_Object = MibTable
wtWebGraphThermoHygroTempValuePktTable = _WtWebGraphThermoHygroTempValuePktTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 8)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTempValuePktTable.setStatus("mandatory")
_WtWebGraphThermoHygroTempValuePktEntry_Object = MibTableRow
wtWebGraphThermoHygroTempValuePktEntry = _WtWebGraphThermoHygroTempValuePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 8, 1)
)
wtWebGraphThermoHygroTempValuePktEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTempValuePktEntry.setStatus("mandatory")


class _WtWebGraphThermoHygroTempValuePkt_Type(OctetString):
    """Custom type wtWebGraphThermoHygroTempValuePkt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_WtWebGraphThermoHygroTempValuePkt_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroTempValuePkt_Object = MibTableColumn
wtWebGraphThermoHygroTempValuePkt = _WtWebGraphThermoHygroTempValuePkt_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 1, 8, 1, 1),
    _WtWebGraphThermoHygroTempValuePkt_Type()
)
wtWebGraphThermoHygroTempValuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTempValuePkt.setStatus("mandatory")
_WtWebGraphThermoHygroSessCntrl_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroSessCntrl = _WtWebGraphThermoHygroSessCntrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 2)
)
_WtWebGraphThermoHygroSessCntrlPassword_Type = OctetString
_WtWebGraphThermoHygroSessCntrlPassword_Object = MibScalar
wtWebGraphThermoHygroSessCntrlPassword = _WtWebGraphThermoHygroSessCntrlPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 2, 1),
    _WtWebGraphThermoHygroSessCntrlPassword_Type()
)
wtWebGraphThermoHygroSessCntrlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSessCntrlPassword.setStatus("mandatory")


class _WtWebGraphThermoHygroSessCntrlConfigMode_Type(Integer32):
    """Custom type wtWebGraphThermoHygroSessCntrlConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wtWebGraphThermoHygroSessCntrl-NoSession", 0),
          ("wtWebGraphThermoHygroSessCntrl-Session", 1))
    )


_WtWebGraphThermoHygroSessCntrlConfigMode_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroSessCntrlConfigMode_Object = MibScalar
wtWebGraphThermoHygroSessCntrlConfigMode = _WtWebGraphThermoHygroSessCntrlConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 2, 2),
    _WtWebGraphThermoHygroSessCntrlConfigMode_Type()
)
wtWebGraphThermoHygroSessCntrlConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSessCntrlConfigMode.setStatus("mandatory")
_WtWebGraphThermoHygroSessCntrlLogout_Type = Integer32
_WtWebGraphThermoHygroSessCntrlLogout_Object = MibScalar
wtWebGraphThermoHygroSessCntrlLogout = _WtWebGraphThermoHygroSessCntrlLogout_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 2, 3),
    _WtWebGraphThermoHygroSessCntrlLogout_Type()
)
wtWebGraphThermoHygroSessCntrlLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSessCntrlLogout.setStatus("mandatory")
_WtWebGraphThermoHygroSessCntrlAdminPassword_Type = OctetString
_WtWebGraphThermoHygroSessCntrlAdminPassword_Object = MibScalar
wtWebGraphThermoHygroSessCntrlAdminPassword = _WtWebGraphThermoHygroSessCntrlAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 2, 4),
    _WtWebGraphThermoHygroSessCntrlAdminPassword_Type()
)
wtWebGraphThermoHygroSessCntrlAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSessCntrlAdminPassword.setStatus("mandatory")
_WtWebGraphThermoHygroSessCntrlConfigPassword_Type = OctetString
_WtWebGraphThermoHygroSessCntrlConfigPassword_Object = MibScalar
wtWebGraphThermoHygroSessCntrlConfigPassword = _WtWebGraphThermoHygroSessCntrlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 2, 5),
    _WtWebGraphThermoHygroSessCntrlConfigPassword_Type()
)
wtWebGraphThermoHygroSessCntrlConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSessCntrlConfigPassword.setStatus("mandatory")
_WtWebGraphThermoHygroConfig_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroConfig = _WtWebGraphThermoHygroConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3)
)
_WtWebGraphThermoHygroDevice_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroDevice = _WtWebGraphThermoHygroDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1)
)
_WtWebGraphThermoHygroText_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroText = _WtWebGraphThermoHygroText_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 1)
)
_WtWebGraphThermoHygroDeviceName_Type = OctetString
_WtWebGraphThermoHygroDeviceName_Object = MibScalar
wtWebGraphThermoHygroDeviceName = _WtWebGraphThermoHygroDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 1, 1),
    _WtWebGraphThermoHygroDeviceName_Type()
)
wtWebGraphThermoHygroDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDeviceName.setStatus("mandatory")
_WtWebGraphThermoHygroDeviceText_Type = OctetString
_WtWebGraphThermoHygroDeviceText_Object = MibScalar
wtWebGraphThermoHygroDeviceText = _WtWebGraphThermoHygroDeviceText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 1, 2),
    _WtWebGraphThermoHygroDeviceText_Type()
)
wtWebGraphThermoHygroDeviceText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDeviceText.setStatus("mandatory")
_WtWebGraphThermoHygroDeviceLocation_Type = OctetString
_WtWebGraphThermoHygroDeviceLocation_Object = MibScalar
wtWebGraphThermoHygroDeviceLocation = _WtWebGraphThermoHygroDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 1, 3),
    _WtWebGraphThermoHygroDeviceLocation_Type()
)
wtWebGraphThermoHygroDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDeviceLocation.setStatus("mandatory")
_WtWebGraphThermoHygroDeviceContact_Type = OctetString
_WtWebGraphThermoHygroDeviceContact_Object = MibScalar
wtWebGraphThermoHygroDeviceContact = _WtWebGraphThermoHygroDeviceContact_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 1, 4),
    _WtWebGraphThermoHygroDeviceContact_Type()
)
wtWebGraphThermoHygroDeviceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDeviceContact.setStatus("mandatory")
_WtWebGraphThermoHygroTimeDate_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroTimeDate = _WtWebGraphThermoHygroTimeDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2)
)
_WtWebGraphThermoHygroTimeZone_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroTimeZone = _WtWebGraphThermoHygroTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1)
)
_WtWebGraphThermoHygroTzOffsetHrs_Type = Integer32
_WtWebGraphThermoHygroTzOffsetHrs_Object = MibScalar
wtWebGraphThermoHygroTzOffsetHrs = _WtWebGraphThermoHygroTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 1),
    _WtWebGraphThermoHygroTzOffsetHrs_Type()
)
wtWebGraphThermoHygroTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTzOffsetHrs.setStatus("mandatory")
_WtWebGraphThermoHygroTzOffsetMin_Type = Integer32
_WtWebGraphThermoHygroTzOffsetMin_Object = MibScalar
wtWebGraphThermoHygroTzOffsetMin = _WtWebGraphThermoHygroTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 2),
    _WtWebGraphThermoHygroTzOffsetMin_Type()
)
wtWebGraphThermoHygroTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTzOffsetMin.setStatus("mandatory")


class _WtWebGraphThermoHygroTzEnable_Type(OctetString):
    """Custom type wtWebGraphThermoHygroTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroTzEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroTzEnable_Object = MibScalar
wtWebGraphThermoHygroTzEnable = _WtWebGraphThermoHygroTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 3),
    _WtWebGraphThermoHygroTzEnable_Type()
)
wtWebGraphThermoHygroTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTzEnable.setStatus("mandatory")
_WtWebGraphThermoHygroStTzOffsetHrs_Type = Integer32
_WtWebGraphThermoHygroStTzOffsetHrs_Object = MibScalar
wtWebGraphThermoHygroStTzOffsetHrs = _WtWebGraphThermoHygroStTzOffsetHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 4),
    _WtWebGraphThermoHygroStTzOffsetHrs_Type()
)
wtWebGraphThermoHygroStTzOffsetHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzOffsetHrs.setStatus("mandatory")
_WtWebGraphThermoHygroStTzOffsetMin_Type = Integer32
_WtWebGraphThermoHygroStTzOffsetMin_Object = MibScalar
wtWebGraphThermoHygroStTzOffsetMin = _WtWebGraphThermoHygroStTzOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 5),
    _WtWebGraphThermoHygroStTzOffsetMin_Type()
)
wtWebGraphThermoHygroStTzOffsetMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzOffsetMin.setStatus("mandatory")


class _WtWebGraphThermoHygroStTzEnable_Type(OctetString):
    """Custom type wtWebGraphThermoHygroStTzEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroStTzEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroStTzEnable_Object = MibScalar
wtWebGraphThermoHygroStTzEnable = _WtWebGraphThermoHygroStTzEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 6),
    _WtWebGraphThermoHygroStTzEnable_Type()
)
wtWebGraphThermoHygroStTzEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzEnable.setStatus("mandatory")


class _WtWebGraphThermoHygroStTzStartMonth_Type(Integer32):
    """Custom type wtWebGraphThermoHygroStTzStartMonth based on Integer32"""
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
        *(("wtWebGraphThermoHygroStartMonth-January", 1),
          ("wtWebGraphThermoHygroStartMonth-February", 2),
          ("wtWebGraphThermoHygroStartMonth-March", 3),
          ("wtWebGraphThermoHygroStartMonth-April", 4),
          ("wtWebGraphThermoHygroStartMonth-May", 5),
          ("wtWebGraphThermoHygroStartMonth-June", 6),
          ("wtWebGraphThermoHygroStartMonth-July", 7),
          ("wtWebGraphThermoHygroStartMonth-August", 8),
          ("wtWebGraphThermoHygroStartMonth-September", 9),
          ("wtWebGraphThermoHygroStartMonth-October", 10),
          ("wtWebGraphThermoHygroStartMonth-November", 11),
          ("wtWebGraphThermoHygroStartMonth-December", 12))
    )


_WtWebGraphThermoHygroStTzStartMonth_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroStTzStartMonth_Object = MibScalar
wtWebGraphThermoHygroStTzStartMonth = _WtWebGraphThermoHygroStTzStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 7),
    _WtWebGraphThermoHygroStTzStartMonth_Type()
)
wtWebGraphThermoHygroStTzStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStartMonth.setStatus("mandatory")


class _WtWebGraphThermoHygroStTzStartMode_Type(Integer32):
    """Custom type wtWebGraphThermoHygroStTzStartMode based on Integer32"""
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
        *(("wtWebGraphThermoHygroStartMode-first", 1),
          ("wtWebGraphThermoHygroStartMode-second", 2),
          ("wtWebGraphThermoHygroStartMode-third", 3),
          ("wtWebGraphThermoHygroStartMode-fourth", 4),
          ("wtWebGraphThermoHygroStartMode-last", 5))
    )


_WtWebGraphThermoHygroStTzStartMode_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroStTzStartMode_Object = MibScalar
wtWebGraphThermoHygroStTzStartMode = _WtWebGraphThermoHygroStTzStartMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 8),
    _WtWebGraphThermoHygroStTzStartMode_Type()
)
wtWebGraphThermoHygroStTzStartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStartMode.setStatus("mandatory")


class _WtWebGraphThermoHygroStTzStartWday_Type(Integer32):
    """Custom type wtWebGraphThermoHygroStTzStartWday based on Integer32"""
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
        *(("wtWebGraphThermoHygroStartWday-Sunday", 1),
          ("wtWebGraphThermoHygroStartWday-Monday", 2),
          ("wtWebGraphThermoHygroStartWday-Tuesday", 3),
          ("wtWebGraphThermoHygroStartWday-Thursday", 4),
          ("wtWebGraphThermoHygroStartWday-Wednesday", 5),
          ("wtWebGraphThermoHygroStartWday-Friday", 6),
          ("wtWebGraphThermoHygroStartWday-Saturday", 7))
    )


_WtWebGraphThermoHygroStTzStartWday_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroStTzStartWday_Object = MibScalar
wtWebGraphThermoHygroStTzStartWday = _WtWebGraphThermoHygroStTzStartWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 9),
    _WtWebGraphThermoHygroStTzStartWday_Type()
)
wtWebGraphThermoHygroStTzStartWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStartWday.setStatus("mandatory")
_WtWebGraphThermoHygroStTzStartHrs_Type = Integer32
_WtWebGraphThermoHygroStTzStartHrs_Object = MibScalar
wtWebGraphThermoHygroStTzStartHrs = _WtWebGraphThermoHygroStTzStartHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 10),
    _WtWebGraphThermoHygroStTzStartHrs_Type()
)
wtWebGraphThermoHygroStTzStartHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStartHrs.setStatus("mandatory")
_WtWebGraphThermoHygroStTzStartMin_Type = Integer32
_WtWebGraphThermoHygroStTzStartMin_Object = MibScalar
wtWebGraphThermoHygroStTzStartMin = _WtWebGraphThermoHygroStTzStartMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 11),
    _WtWebGraphThermoHygroStTzStartMin_Type()
)
wtWebGraphThermoHygroStTzStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStartMin.setStatus("mandatory")


class _WtWebGraphThermoHygroStTzStopMonth_Type(Integer32):
    """Custom type wtWebGraphThermoHygroStTzStopMonth based on Integer32"""
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
        *(("wtWebGraphThermoHygroStopMonth-January", 1),
          ("wtWebGraphThermoHygroStopMonth-February", 2),
          ("wtWebGraphThermoHygroStopMonth-March", 3),
          ("wtWebGraphThermoHygroStopMonth-April", 4),
          ("wtWebGraphThermoHygroStopMonth-May", 5),
          ("wtWebGraphThermoHygroStopMonth-June", 6),
          ("wtWebGraphThermoHygroStopMonth-July", 7),
          ("wtWebGraphThermoHygroStopMonth-August", 8),
          ("wtWebGraphThermoHygroStopMonth-September", 9),
          ("wtWebGraphThermoHygroStopMonth-October", 10),
          ("wtWebGraphThermoHygroStopMonth-November", 11),
          ("wtWebGraphThermoHygroStopMonth-December", 12))
    )


_WtWebGraphThermoHygroStTzStopMonth_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroStTzStopMonth_Object = MibScalar
wtWebGraphThermoHygroStTzStopMonth = _WtWebGraphThermoHygroStTzStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 12),
    _WtWebGraphThermoHygroStTzStopMonth_Type()
)
wtWebGraphThermoHygroStTzStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStopMonth.setStatus("mandatory")


class _WtWebGraphThermoHygroStTzStopMode_Type(Integer32):
    """Custom type wtWebGraphThermoHygroStTzStopMode based on Integer32"""
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
        *(("wtWebGraphThermoHygroStopMode-first", 1),
          ("wtWebGraphThermoHygroStopMode-second", 2),
          ("wtWebGraphThermoHygroStopMode-third", 3),
          ("wtWebGraphThermoHygroStopMode-fourth", 4),
          ("wtWebGraphThermoHygroStopMode-last", 5))
    )


_WtWebGraphThermoHygroStTzStopMode_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroStTzStopMode_Object = MibScalar
wtWebGraphThermoHygroStTzStopMode = _WtWebGraphThermoHygroStTzStopMode_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 13),
    _WtWebGraphThermoHygroStTzStopMode_Type()
)
wtWebGraphThermoHygroStTzStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStopMode.setStatus("mandatory")


class _WtWebGraphThermoHygroStTzStopWday_Type(Integer32):
    """Custom type wtWebGraphThermoHygroStTzStopWday based on Integer32"""
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
        *(("wtWebGraphThermoHygroStopWday-Sunday", 1),
          ("wtWebGraphThermoHygroStopWday-Monday", 2),
          ("wtWebGraphThermoHygroStopWday-Tuesday", 3),
          ("wtWebGraphThermoHygroStopWday-Thursday", 4),
          ("wtWebGraphThermoHygroStopWday-Wednesday", 5),
          ("wtWebGraphThermoHygroStopWday-Friday", 6),
          ("wtWebGraphThermoHygroStopWday-Saturday", 7))
    )


_WtWebGraphThermoHygroStTzStopWday_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroStTzStopWday_Object = MibScalar
wtWebGraphThermoHygroStTzStopWday = _WtWebGraphThermoHygroStTzStopWday_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 14),
    _WtWebGraphThermoHygroStTzStopWday_Type()
)
wtWebGraphThermoHygroStTzStopWday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStopWday.setStatus("mandatory")
_WtWebGraphThermoHygroStTzStopHrs_Type = Integer32
_WtWebGraphThermoHygroStTzStopHrs_Object = MibScalar
wtWebGraphThermoHygroStTzStopHrs = _WtWebGraphThermoHygroStTzStopHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 15),
    _WtWebGraphThermoHygroStTzStopHrs_Type()
)
wtWebGraphThermoHygroStTzStopHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStopHrs.setStatus("mandatory")
_WtWebGraphThermoHygroStTzStopMin_Type = Integer32
_WtWebGraphThermoHygroStTzStopMin_Object = MibScalar
wtWebGraphThermoHygroStTzStopMin = _WtWebGraphThermoHygroStTzStopMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 1, 16),
    _WtWebGraphThermoHygroStTzStopMin_Type()
)
wtWebGraphThermoHygroStTzStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStTzStopMin.setStatus("mandatory")
_WtWebGraphThermoHygroTimeServer_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroTimeServer = _WtWebGraphThermoHygroTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 2)
)
_WtWebGraphThermoHygroTimeServer1_Type = OctetString
_WtWebGraphThermoHygroTimeServer1_Object = MibScalar
wtWebGraphThermoHygroTimeServer1 = _WtWebGraphThermoHygroTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 2, 1),
    _WtWebGraphThermoHygroTimeServer1_Type()
)
wtWebGraphThermoHygroTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTimeServer1.setStatus("mandatory")
_WtWebGraphThermoHygroTimeServer2_Type = OctetString
_WtWebGraphThermoHygroTimeServer2_Object = MibScalar
wtWebGraphThermoHygroTimeServer2 = _WtWebGraphThermoHygroTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 2, 2),
    _WtWebGraphThermoHygroTimeServer2_Type()
)
wtWebGraphThermoHygroTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTimeServer2.setStatus("mandatory")


class _WtWebGraphThermoHygroTsEnable_Type(OctetString):
    """Custom type wtWebGraphThermoHygroTsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroTsEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroTsEnable_Object = MibScalar
wtWebGraphThermoHygroTsEnable = _WtWebGraphThermoHygroTsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 2, 3),
    _WtWebGraphThermoHygroTsEnable_Type()
)
wtWebGraphThermoHygroTsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTsEnable.setStatus("mandatory")
_WtWebGraphThermoHygroTsSyncTime_Type = Integer32
_WtWebGraphThermoHygroTsSyncTime_Object = MibScalar
wtWebGraphThermoHygroTsSyncTime = _WtWebGraphThermoHygroTsSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 2, 4),
    _WtWebGraphThermoHygroTsSyncTime_Type()
)
wtWebGraphThermoHygroTsSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroTsSyncTime.setStatus("mandatory")
_WtWebGraphThermoHygroDeviceClock_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroDeviceClock = _WtWebGraphThermoHygroDeviceClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 3)
)


class _WtWebGraphThermoHygroClockHrs_Type(Integer32):
    """Custom type wtWebGraphThermoHygroClockHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_WtWebGraphThermoHygroClockHrs_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroClockHrs_Object = MibScalar
wtWebGraphThermoHygroClockHrs = _WtWebGraphThermoHygroClockHrs_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 3, 1),
    _WtWebGraphThermoHygroClockHrs_Type()
)
wtWebGraphThermoHygroClockHrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroClockHrs.setStatus("mandatory")


class _WtWebGraphThermoHygroClockMin_Type(Integer32):
    """Custom type wtWebGraphThermoHygroClockMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_WtWebGraphThermoHygroClockMin_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroClockMin_Object = MibScalar
wtWebGraphThermoHygroClockMin = _WtWebGraphThermoHygroClockMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 3, 2),
    _WtWebGraphThermoHygroClockMin_Type()
)
wtWebGraphThermoHygroClockMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroClockMin.setStatus("mandatory")


class _WtWebGraphThermoHygroClockDay_Type(Integer32):
    """Custom type wtWebGraphThermoHygroClockDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WtWebGraphThermoHygroClockDay_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroClockDay_Object = MibScalar
wtWebGraphThermoHygroClockDay = _WtWebGraphThermoHygroClockDay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 3, 3),
    _WtWebGraphThermoHygroClockDay_Type()
)
wtWebGraphThermoHygroClockDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroClockDay.setStatus("mandatory")


class _WtWebGraphThermoHygroClockMonth_Type(Integer32):
    """Custom type wtWebGraphThermoHygroClockMonth based on Integer32"""
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
        *(("wtWebGraphThermoHygroClockMonth-January", 1),
          ("wtWebGraphThermoHygroClockMonth-February", 2),
          ("wtWebGraphThermoHygroClockMonth-March", 3),
          ("wtWebGraphThermoHygroClockMonth-April", 4),
          ("wtWebGraphThermoHygroClockMonth-May", 5),
          ("wtWebGraphThermoHygroClockMonth-June", 6),
          ("wtWebGraphThermoHygroClockMonth-July", 7),
          ("wtWebGraphThermoHygroClockMonth-August", 8),
          ("wtWebGraphThermoHygroClockMonth-September", 9),
          ("wtWebGraphThermoHygroClockMonth-October", 10),
          ("wtWebGraphThermoHygroClockMonth-November", 11),
          ("wtWebGraphThermoHygroClockMonth-December", 12))
    )


_WtWebGraphThermoHygroClockMonth_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroClockMonth_Object = MibScalar
wtWebGraphThermoHygroClockMonth = _WtWebGraphThermoHygroClockMonth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 3, 4),
    _WtWebGraphThermoHygroClockMonth_Type()
)
wtWebGraphThermoHygroClockMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroClockMonth.setStatus("mandatory")


class _WtWebGraphThermoHygroClockYear_Type(Integer32):
    """Custom type wtWebGraphThermoHygroClockYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WtWebGraphThermoHygroClockYear_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroClockYear_Object = MibScalar
wtWebGraphThermoHygroClockYear = _WtWebGraphThermoHygroClockYear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 2, 3, 5),
    _WtWebGraphThermoHygroClockYear_Type()
)
wtWebGraphThermoHygroClockYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroClockYear.setStatus("mandatory")
_WtWebGraphThermoHygroBasic_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroBasic = _WtWebGraphThermoHygroBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3)
)
_WtWebGraphThermoHygroNetwork_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroNetwork = _WtWebGraphThermoHygroNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 1)
)
_WtWebGraphThermoHygroIpAddress_Type = IpAddress
_WtWebGraphThermoHygroIpAddress_Object = MibScalar
wtWebGraphThermoHygroIpAddress = _WtWebGraphThermoHygroIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 1, 1),
    _WtWebGraphThermoHygroIpAddress_Type()
)
wtWebGraphThermoHygroIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroIpAddress.setStatus("mandatory")
_WtWebGraphThermoHygroSubnetMask_Type = IpAddress
_WtWebGraphThermoHygroSubnetMask_Object = MibScalar
wtWebGraphThermoHygroSubnetMask = _WtWebGraphThermoHygroSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 1, 2),
    _WtWebGraphThermoHygroSubnetMask_Type()
)
wtWebGraphThermoHygroSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSubnetMask.setStatus("mandatory")
_WtWebGraphThermoHygroGateway_Type = IpAddress
_WtWebGraphThermoHygroGateway_Object = MibScalar
wtWebGraphThermoHygroGateway = _WtWebGraphThermoHygroGateway_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 1, 3),
    _WtWebGraphThermoHygroGateway_Type()
)
wtWebGraphThermoHygroGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGateway.setStatus("mandatory")
_WtWebGraphThermoHygroDnsServer1_Type = OctetString
_WtWebGraphThermoHygroDnsServer1_Object = MibScalar
wtWebGraphThermoHygroDnsServer1 = _WtWebGraphThermoHygroDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 1, 4),
    _WtWebGraphThermoHygroDnsServer1_Type()
)
wtWebGraphThermoHygroDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDnsServer1.setStatus("mandatory")
_WtWebGraphThermoHygroDnsServer2_Type = OctetString
_WtWebGraphThermoHygroDnsServer2_Object = MibScalar
wtWebGraphThermoHygroDnsServer2 = _WtWebGraphThermoHygroDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 1, 5),
    _WtWebGraphThermoHygroDnsServer2_Type()
)
wtWebGraphThermoHygroDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDnsServer2.setStatus("mandatory")
_WtWebGraphThermoHygroAddConfig_Type = OctetString
_WtWebGraphThermoHygroAddConfig_Object = MibScalar
wtWebGraphThermoHygroAddConfig = _WtWebGraphThermoHygroAddConfig_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 1, 6),
    _WtWebGraphThermoHygroAddConfig_Type()
)
wtWebGraphThermoHygroAddConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAddConfig.setStatus("mandatory")
_WtWebGraphThermoHygroHTTP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroHTTP = _WtWebGraphThermoHygroHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 2)
)
_WtWebGraphThermoHygroStartup_Type = OctetString
_WtWebGraphThermoHygroStartup_Object = MibScalar
wtWebGraphThermoHygroStartup = _WtWebGraphThermoHygroStartup_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 2, 1),
    _WtWebGraphThermoHygroStartup_Type()
)
wtWebGraphThermoHygroStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroStartup.setStatus("mandatory")
_WtWebGraphThermoHygroGetHeaderEnable_Type = OctetString
_WtWebGraphThermoHygroGetHeaderEnable_Object = MibScalar
wtWebGraphThermoHygroGetHeaderEnable = _WtWebGraphThermoHygroGetHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 2, 2),
    _WtWebGraphThermoHygroGetHeaderEnable_Type()
)
wtWebGraphThermoHygroGetHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGetHeaderEnable.setStatus("mandatory")


class _WtWebGraphThermoHygroHttpPort_Type(Integer32):
    """Custom type wtWebGraphThermoHygroHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoHygroHttpPort_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroHttpPort_Object = MibScalar
wtWebGraphThermoHygroHttpPort = _WtWebGraphThermoHygroHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 2, 3),
    _WtWebGraphThermoHygroHttpPort_Type()
)
wtWebGraphThermoHygroHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroHttpPort.setStatus("mandatory")
_WtWebGraphThermoHygroMail_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroMail = _WtWebGraphThermoHygroMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3)
)
_WtWebGraphThermoHygroMailAdName_Type = OctetString
_WtWebGraphThermoHygroMailAdName_Object = MibScalar
wtWebGraphThermoHygroMailAdName = _WtWebGraphThermoHygroMailAdName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 1),
    _WtWebGraphThermoHygroMailAdName_Type()
)
wtWebGraphThermoHygroMailAdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMailAdName.setStatus("mandatory")
_WtWebGraphThermoHygroMailReply_Type = OctetString
_WtWebGraphThermoHygroMailReply_Object = MibScalar
wtWebGraphThermoHygroMailReply = _WtWebGraphThermoHygroMailReply_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 2),
    _WtWebGraphThermoHygroMailReply_Type()
)
wtWebGraphThermoHygroMailReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMailReply.setStatus("mandatory")
_WtWebGraphThermoHygroMailServer_Type = OctetString
_WtWebGraphThermoHygroMailServer_Object = MibScalar
wtWebGraphThermoHygroMailServer = _WtWebGraphThermoHygroMailServer_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 3),
    _WtWebGraphThermoHygroMailServer_Type()
)
wtWebGraphThermoHygroMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMailServer.setStatus("mandatory")
_WtWebioAn1MailEnable_Type = OctetString
_WtWebioAn1MailEnable_Object = MibScalar
wtWebioAn1MailEnable = _WtWebioAn1MailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 4),
    _WtWebioAn1MailEnable_Type()
)
wtWebioAn1MailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebioAn1MailEnable.setStatus("mandatory")


class _WtWebGraphThermoHygroMailAuthentication_Type(OctetString):
    """Custom type wtWebGraphThermoHygroMailAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroMailAuthentication_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroMailAuthentication_Object = MibScalar
wtWebGraphThermoHygroMailAuthentication = _WtWebGraphThermoHygroMailAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 5),
    _WtWebGraphThermoHygroMailAuthentication_Type()
)
wtWebGraphThermoHygroMailAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMailAuthentication.setStatus("mandatory")
_WtWebGraphThermoHygroMailAuthUser_Type = OctetString
_WtWebGraphThermoHygroMailAuthUser_Object = MibScalar
wtWebGraphThermoHygroMailAuthUser = _WtWebGraphThermoHygroMailAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 6),
    _WtWebGraphThermoHygroMailAuthUser_Type()
)
wtWebGraphThermoHygroMailAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMailAuthUser.setStatus("mandatory")
_WtWebGraphThermoHygroMailAuthPassword_Type = OctetString
_WtWebGraphThermoHygroMailAuthPassword_Object = MibScalar
wtWebGraphThermoHygroMailAuthPassword = _WtWebGraphThermoHygroMailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 7),
    _WtWebGraphThermoHygroMailAuthPassword_Type()
)
wtWebGraphThermoHygroMailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMailAuthPassword.setStatus("mandatory")
_WtWebGraphThermoHygroMailPop3Server_Type = OctetString
_WtWebGraphThermoHygroMailPop3Server_Object = MibScalar
wtWebGraphThermoHygroMailPop3Server = _WtWebGraphThermoHygroMailPop3Server_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 3, 8),
    _WtWebGraphThermoHygroMailPop3Server_Type()
)
wtWebGraphThermoHygroMailPop3Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMailPop3Server.setStatus("mandatory")
_WtWebGraphThermoHygroSNMP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroSNMP = _WtWebGraphThermoHygroSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4)
)
_WtWebGraphThermoHygroSnmpCommunityStringRead_Type = OctetString
_WtWebGraphThermoHygroSnmpCommunityStringRead_Object = MibScalar
wtWebGraphThermoHygroSnmpCommunityStringRead = _WtWebGraphThermoHygroSnmpCommunityStringRead_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4, 1),
    _WtWebGraphThermoHygroSnmpCommunityStringRead_Type()
)
wtWebGraphThermoHygroSnmpCommunityStringRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSnmpCommunityStringRead.setStatus("mandatory")
_WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Type = OctetString
_WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Object = MibScalar
wtWebGraphThermoHygroSnmpCommunityStringReadWrite = _WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4, 2),
    _WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Type()
)
wtWebGraphThermoHygroSnmpCommunityStringReadWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSnmpCommunityStringReadWrite.setStatus("mandatory")
_WtWebGraphThermoHygroSystemTrapManagerIP_Type = OctetString
_WtWebGraphThermoHygroSystemTrapManagerIP_Object = MibScalar
wtWebGraphThermoHygroSystemTrapManagerIP = _WtWebGraphThermoHygroSystemTrapManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4, 3),
    _WtWebGraphThermoHygroSystemTrapManagerIP_Type()
)
wtWebGraphThermoHygroSystemTrapManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSystemTrapManagerIP.setStatus("mandatory")


class _WtWebGraphThermoHygroSystemTrapEnable_Type(OctetString):
    """Custom type wtWebGraphThermoHygroSystemTrapEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroSystemTrapEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroSystemTrapEnable_Object = MibScalar
wtWebGraphThermoHygroSystemTrapEnable = _WtWebGraphThermoHygroSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4, 4),
    _WtWebGraphThermoHygroSystemTrapEnable_Type()
)
wtWebGraphThermoHygroSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSystemTrapEnable.setStatus("mandatory")
_WtWebGraphThermoHygroSnmpEnable_Type = OctetString
_WtWebGraphThermoHygroSnmpEnable_Object = MibScalar
wtWebGraphThermoHygroSnmpEnable = _WtWebGraphThermoHygroSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4, 5),
    _WtWebGraphThermoHygroSnmpEnable_Type()
)
wtWebGraphThermoHygroSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSnmpEnable.setStatus("mandatory")
_WtWebGraphThermoHygroSnmpCommunityStringTrap_Type = OctetString
_WtWebGraphThermoHygroSnmpCommunityStringTrap_Object = MibScalar
wtWebGraphThermoHygroSnmpCommunityStringTrap = _WtWebGraphThermoHygroSnmpCommunityStringTrap_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4, 6),
    _WtWebGraphThermoHygroSnmpCommunityStringTrap_Type()
)
wtWebGraphThermoHygroSnmpCommunityStringTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSnmpCommunityStringTrap.setStatus("mandatory")
_WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Type = Integer32
_WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Object = MibScalar
wtWebGraphThermoHygroSnmpSystemTrapManagerPort = _WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 4, 7),
    _WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Type()
)
wtWebGraphThermoHygroSnmpSystemTrapManagerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSnmpSystemTrapManagerPort.setStatus("mandatory")
_WtWebGraphThermoHygroUDP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroUDP = _WtWebGraphThermoHygroUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 5)
)


class _WtWebGraphThermoHygroUdpPort_Type(Integer32):
    """Custom type wtWebGraphThermoHygroUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoHygroUdpPort_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroUdpPort_Object = MibScalar
wtWebGraphThermoHygroUdpPort = _WtWebGraphThermoHygroUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 5, 1),
    _WtWebGraphThermoHygroUdpPort_Type()
)
wtWebGraphThermoHygroUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroUdpPort.setStatus("mandatory")
_WtWebGraphThermoHygroUdpEnable_Type = OctetString
_WtWebGraphThermoHygroUdpEnable_Object = MibScalar
wtWebGraphThermoHygroUdpEnable = _WtWebGraphThermoHygroUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 5, 2),
    _WtWebGraphThermoHygroUdpEnable_Type()
)
wtWebGraphThermoHygroUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroUdpEnable.setStatus("mandatory")
_WtWebGraphThermoHygroSyslog_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroSyslog = _WtWebGraphThermoHygroSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 6)
)
_WtWebGraphThermoHygroSyslogServerIP_Type = OctetString
_WtWebGraphThermoHygroSyslogServerIP_Object = MibScalar
wtWebGraphThermoHygroSyslogServerIP = _WtWebGraphThermoHygroSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 6, 1),
    _WtWebGraphThermoHygroSyslogServerIP_Type()
)
wtWebGraphThermoHygroSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSyslogServerIP.setStatus("mandatory")
_WtWebGraphThermoHygroSyslogServerPort_Type = Integer32
_WtWebGraphThermoHygroSyslogServerPort_Object = MibScalar
wtWebGraphThermoHygroSyslogServerPort = _WtWebGraphThermoHygroSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 6, 2),
    _WtWebGraphThermoHygroSyslogServerPort_Type()
)
wtWebGraphThermoHygroSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSyslogServerPort.setStatus("mandatory")


class _WtWebGraphThermoHygroSyslogSystemMessagesEnable_Type(OctetString):
    """Custom type wtWebGraphThermoHygroSyslogSystemMessagesEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroSyslogSystemMessagesEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroSyslogSystemMessagesEnable_Object = MibScalar
wtWebGraphThermoHygroSyslogSystemMessagesEnable = _WtWebGraphThermoHygroSyslogSystemMessagesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 6, 3),
    _WtWebGraphThermoHygroSyslogSystemMessagesEnable_Type()
)
wtWebGraphThermoHygroSyslogSystemMessagesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSyslogSystemMessagesEnable.setStatus("mandatory")
_WtWebGraphThermoHygroSyslogEnable_Type = OctetString
_WtWebGraphThermoHygroSyslogEnable_Object = MibScalar
wtWebGraphThermoHygroSyslogEnable = _WtWebGraphThermoHygroSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 6, 4),
    _WtWebGraphThermoHygroSyslogEnable_Type()
)
wtWebGraphThermoHygroSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSyslogEnable.setStatus("mandatory")
_WtWebGraphThermoHygroFTP_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroFTP = _WtWebGraphThermoHygroFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7)
)
_WtWebGraphThermoHygroFTPServerIP_Type = OctetString
_WtWebGraphThermoHygroFTPServerIP_Object = MibScalar
wtWebGraphThermoHygroFTPServerIP = _WtWebGraphThermoHygroFTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7, 1),
    _WtWebGraphThermoHygroFTPServerIP_Type()
)
wtWebGraphThermoHygroFTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroFTPServerIP.setStatus("mandatory")
_WtWebGraphThermoHygroFTPServerControlPort_Type = Integer32
_WtWebGraphThermoHygroFTPServerControlPort_Object = MibScalar
wtWebGraphThermoHygroFTPServerControlPort = _WtWebGraphThermoHygroFTPServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7, 2),
    _WtWebGraphThermoHygroFTPServerControlPort_Type()
)
wtWebGraphThermoHygroFTPServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroFTPServerControlPort.setStatus("mandatory")
_WtWebGraphThermoHygroFTPUserName_Type = OctetString
_WtWebGraphThermoHygroFTPUserName_Object = MibScalar
wtWebGraphThermoHygroFTPUserName = _WtWebGraphThermoHygroFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7, 3),
    _WtWebGraphThermoHygroFTPUserName_Type()
)
wtWebGraphThermoHygroFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroFTPUserName.setStatus("mandatory")
_WtWebGraphThermoHygroFTPPassword_Type = OctetString
_WtWebGraphThermoHygroFTPPassword_Object = MibScalar
wtWebGraphThermoHygroFTPPassword = _WtWebGraphThermoHygroFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7, 4),
    _WtWebGraphThermoHygroFTPPassword_Type()
)
wtWebGraphThermoHygroFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroFTPPassword.setStatus("mandatory")
_WtWebGraphThermoHygroFTPAccount_Type = OctetString
_WtWebGraphThermoHygroFTPAccount_Object = MibScalar
wtWebGraphThermoHygroFTPAccount = _WtWebGraphThermoHygroFTPAccount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7, 5),
    _WtWebGraphThermoHygroFTPAccount_Type()
)
wtWebGraphThermoHygroFTPAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroFTPAccount.setStatus("mandatory")
_WtWebGraphThermoHygroFTPOption_Type = OctetString
_WtWebGraphThermoHygroFTPOption_Object = MibScalar
wtWebGraphThermoHygroFTPOption = _WtWebGraphThermoHygroFTPOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7, 6),
    _WtWebGraphThermoHygroFTPOption_Type()
)
wtWebGraphThermoHygroFTPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroFTPOption.setStatus("mandatory")
_WtWebGraphThermoHygroFTPEnable_Type = OctetString
_WtWebGraphThermoHygroFTPEnable_Object = MibScalar
wtWebGraphThermoHygroFTPEnable = _WtWebGraphThermoHygroFTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 7, 7),
    _WtWebGraphThermoHygroFTPEnable_Type()
)
wtWebGraphThermoHygroFTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroFTPEnable.setStatus("mandatory")
_WtWebGraphThermoHygroRSS_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroRSS = _WtWebGraphThermoHygroRSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8)
)
_WtWebGraphThermoHygroRSSChannelTitle_Type = OctetString
_WtWebGraphThermoHygroRSSChannelTitle_Object = MibScalar
wtWebGraphThermoHygroRSSChannelTitle = _WtWebGraphThermoHygroRSSChannelTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 1),
    _WtWebGraphThermoHygroRSSChannelTitle_Type()
)
wtWebGraphThermoHygroRSSChannelTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelTitle.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelLink_Type = OctetString
_WtWebGraphThermoHygroRSSChannelLink_Object = MibScalar
wtWebGraphThermoHygroRSSChannelLink = _WtWebGraphThermoHygroRSSChannelLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 2),
    _WtWebGraphThermoHygroRSSChannelLink_Type()
)
wtWebGraphThermoHygroRSSChannelLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelLink.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelDescription_Type = OctetString
_WtWebGraphThermoHygroRSSChannelDescription_Object = MibScalar
wtWebGraphThermoHygroRSSChannelDescription = _WtWebGraphThermoHygroRSSChannelDescription_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 3),
    _WtWebGraphThermoHygroRSSChannelDescription_Type()
)
wtWebGraphThermoHygroRSSChannelDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelDescription.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelImage_Type = OctetString
_WtWebGraphThermoHygroRSSChannelImage_Object = MibScalar
wtWebGraphThermoHygroRSSChannelImage = _WtWebGraphThermoHygroRSSChannelImage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 4),
    _WtWebGraphThermoHygroRSSChannelImage_Type()
)
wtWebGraphThermoHygroRSSChannelImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelImage.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelImageTitle_Type = OctetString
_WtWebGraphThermoHygroRSSChannelImageTitle_Object = MibScalar
wtWebGraphThermoHygroRSSChannelImageTitle = _WtWebGraphThermoHygroRSSChannelImageTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 5),
    _WtWebGraphThermoHygroRSSChannelImageTitle_Type()
)
wtWebGraphThermoHygroRSSChannelImageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelImageTitle.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelImageLink_Type = OctetString
_WtWebGraphThermoHygroRSSChannelImageLink_Object = MibScalar
wtWebGraphThermoHygroRSSChannelImageLink = _WtWebGraphThermoHygroRSSChannelImageLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 6),
    _WtWebGraphThermoHygroRSSChannelImageLink_Type()
)
wtWebGraphThermoHygroRSSChannelImageLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelImageLink.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelItemTitle_Type = OctetString
_WtWebGraphThermoHygroRSSChannelItemTitle_Object = MibScalar
wtWebGraphThermoHygroRSSChannelItemTitle = _WtWebGraphThermoHygroRSSChannelItemTitle_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 7),
    _WtWebGraphThermoHygroRSSChannelItemTitle_Type()
)
wtWebGraphThermoHygroRSSChannelItemTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelItemTitle.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelItemLink_Type = OctetString
_WtWebGraphThermoHygroRSSChannelItemLink_Object = MibScalar
wtWebGraphThermoHygroRSSChannelItemLink = _WtWebGraphThermoHygroRSSChannelItemLink_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 8),
    _WtWebGraphThermoHygroRSSChannelItemLink_Type()
)
wtWebGraphThermoHygroRSSChannelItemLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelItemLink.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelItemDescription_Type = OctetString
_WtWebGraphThermoHygroRSSChannelItemDescription_Object = MibScalar
wtWebGraphThermoHygroRSSChannelItemDescription = _WtWebGraphThermoHygroRSSChannelItemDescription_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 9),
    _WtWebGraphThermoHygroRSSChannelItemDescription_Type()
)
wtWebGraphThermoHygroRSSChannelItemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelItemDescription.setStatus("mandatory")
_WtWebGraphThermoHygroRSSChannelItemQuantity_Type = OctetString
_WtWebGraphThermoHygroRSSChannelItemQuantity_Object = MibScalar
wtWebGraphThermoHygroRSSChannelItemQuantity = _WtWebGraphThermoHygroRSSChannelItemQuantity_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 8, 10),
    _WtWebGraphThermoHygroRSSChannelItemQuantity_Type()
)
wtWebGraphThermoHygroRSSChannelItemQuantity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRSSChannelItemQuantity.setStatus("mandatory")
_WtWebGraphThermoHygroLanguage_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroLanguage = _WtWebGraphThermoHygroLanguage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 9)
)
_WtWebGraphThermoHygroLanguageSelect_Type = OctetString
_WtWebGraphThermoHygroLanguageSelect_Object = MibScalar
wtWebGraphThermoHygroLanguageSelect = _WtWebGraphThermoHygroLanguageSelect_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 9, 1),
    _WtWebGraphThermoHygroLanguageSelect_Type()
)
wtWebGraphThermoHygroLanguageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroLanguageSelect.setStatus("mandatory")
_WtWebGraphThermoHygroMQTT_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroMQTT = _WtWebGraphThermoHygroMQTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12)
)
_WtWebGraphThermoHygroMQTTEnable_Type = OctetString
_WtWebGraphThermoHygroMQTTEnable_Object = MibScalar
wtWebGraphThermoHygroMQTTEnable = _WtWebGraphThermoHygroMQTTEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 1),
    _WtWebGraphThermoHygroMQTTEnable_Type()
)
wtWebGraphThermoHygroMQTTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTEnable.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTBrockerIP_Type = OctetString
_WtWebGraphThermoHygroMQTTBrockerIP_Object = MibScalar
wtWebGraphThermoHygroMQTTBrockerIP = _WtWebGraphThermoHygroMQTTBrockerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 2),
    _WtWebGraphThermoHygroMQTTBrockerIP_Type()
)
wtWebGraphThermoHygroMQTTBrockerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTBrockerIP.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTUserName_Type = OctetString
_WtWebGraphThermoHygroMQTTUserName_Object = MibScalar
wtWebGraphThermoHygroMQTTUserName = _WtWebGraphThermoHygroMQTTUserName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 3),
    _WtWebGraphThermoHygroMQTTUserName_Type()
)
wtWebGraphThermoHygroMQTTUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTUserName.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTPassword_Type = OctetString
_WtWebGraphThermoHygroMQTTPassword_Object = MibScalar
wtWebGraphThermoHygroMQTTPassword = _WtWebGraphThermoHygroMQTTPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 4),
    _WtWebGraphThermoHygroMQTTPassword_Type()
)
wtWebGraphThermoHygroMQTTPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTPassword.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTLocalPort_Type = Integer32
_WtWebGraphThermoHygroMQTTLocalPort_Object = MibScalar
wtWebGraphThermoHygroMQTTLocalPort = _WtWebGraphThermoHygroMQTTLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 5),
    _WtWebGraphThermoHygroMQTTLocalPort_Type()
)
wtWebGraphThermoHygroMQTTLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLocalPort.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTBrokerServerPort_Type = Integer32
_WtWebGraphThermoHygroMQTTBrokerServerPort_Object = MibScalar
wtWebGraphThermoHygroMQTTBrokerServerPort = _WtWebGraphThermoHygroMQTTBrokerServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 6),
    _WtWebGraphThermoHygroMQTTBrokerServerPort_Type()
)
wtWebGraphThermoHygroMQTTBrokerServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTBrokerServerPort.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTInterval_Type = Integer32
_WtWebGraphThermoHygroMQTTInterval_Object = MibScalar
wtWebGraphThermoHygroMQTTInterval = _WtWebGraphThermoHygroMQTTInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 7),
    _WtWebGraphThermoHygroMQTTInterval_Type()
)
wtWebGraphThermoHygroMQTTInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTInterval.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTLastWillEnable_Type = OctetString
_WtWebGraphThermoHygroMQTTLastWillEnable_Object = MibScalar
wtWebGraphThermoHygroMQTTLastWillEnable = _WtWebGraphThermoHygroMQTTLastWillEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 8),
    _WtWebGraphThermoHygroMQTTLastWillEnable_Type()
)
wtWebGraphThermoHygroMQTTLastWillEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLastWillEnable.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTLastWillTopic_Type = OctetString
_WtWebGraphThermoHygroMQTTLastWillTopic_Object = MibScalar
wtWebGraphThermoHygroMQTTLastWillTopic = _WtWebGraphThermoHygroMQTTLastWillTopic_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 9),
    _WtWebGraphThermoHygroMQTTLastWillTopic_Type()
)
wtWebGraphThermoHygroMQTTLastWillTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLastWillTopic.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTLastWillMsg_Type = OctetString
_WtWebGraphThermoHygroMQTTLastWillMsg_Object = MibScalar
wtWebGraphThermoHygroMQTTLastWillMsg = _WtWebGraphThermoHygroMQTTLastWillMsg_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 10),
    _WtWebGraphThermoHygroMQTTLastWillMsg_Type()
)
wtWebGraphThermoHygroMQTTLastWillMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLastWillMsg.setStatus("mandatory")


class _WtWebGraphThermoHygroMQTTLastWillQoS_Type(OctetString):
    """Custom type wtWebGraphThermoHygroMQTTLastWillQoS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroMQTTLastWillQoS_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroMQTTLastWillQoS_Object = MibScalar
wtWebGraphThermoHygroMQTTLastWillQoS = _WtWebGraphThermoHygroMQTTLastWillQoS_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 11),
    _WtWebGraphThermoHygroMQTTLastWillQoS_Type()
)
wtWebGraphThermoHygroMQTTLastWillQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLastWillQoS.setStatus("mandatory")


class _WtWebGraphThermoHygroMQTTLastWillRetain_Type(OctetString):
    """Custom type wtWebGraphThermoHygroMQTTLastWillRetain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroMQTTLastWillRetain_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroMQTTLastWillRetain_Object = MibScalar
wtWebGraphThermoHygroMQTTLastWillRetain = _WtWebGraphThermoHygroMQTTLastWillRetain_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 12),
    _WtWebGraphThermoHygroMQTTLastWillRetain_Type()
)
wtWebGraphThermoHygroMQTTLastWillRetain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLastWillRetain.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTLastWillConnectEnable_Type = OctetString
_WtWebGraphThermoHygroMQTTLastWillConnectEnable_Object = MibScalar
wtWebGraphThermoHygroMQTTLastWillConnectEnable = _WtWebGraphThermoHygroMQTTLastWillConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 13),
    _WtWebGraphThermoHygroMQTTLastWillConnectEnable_Type()
)
wtWebGraphThermoHygroMQTTLastWillConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLastWillConnectEnable.setStatus("mandatory")
_WtWebGraphThermoHygroMQTTLastWillConnectMsg_Type = OctetString
_WtWebGraphThermoHygroMQTTLastWillConnectMsg_Object = MibScalar
wtWebGraphThermoHygroMQTTLastWillConnectMsg = _WtWebGraphThermoHygroMQTTLastWillConnectMsg_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 12, 14),
    _WtWebGraphThermoHygroMQTTLastWillConnectMsg_Type()
)
wtWebGraphThermoHygroMQTTLastWillConnectMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMQTTLastWillConnectMsg.setStatus("mandatory")
_WtWebGraphThermoHygroREST_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroREST = _WtWebGraphThermoHygroREST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 13)
)
_WtWebGraphThermoHygroRESTEnable_Type = OctetString
_WtWebGraphThermoHygroRESTEnable_Object = MibScalar
wtWebGraphThermoHygroRESTEnable = _WtWebGraphThermoHygroRESTEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 13, 1),
    _WtWebGraphThermoHygroRESTEnable_Type()
)
wtWebGraphThermoHygroRESTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRESTEnable.setStatus("mandatory")
_WtWebGraphThermoHygroRESTDigestAuthEnable_Type = OctetString
_WtWebGraphThermoHygroRESTDigestAuthEnable_Object = MibScalar
wtWebGraphThermoHygroRESTDigestAuthEnable = _WtWebGraphThermoHygroRESTDigestAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 3, 13, 2),
    _WtWebGraphThermoHygroRESTDigestAuthEnable_Type()
)
wtWebGraphThermoHygroRESTDigestAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroRESTDigestAuthEnable.setStatus("mandatory")
_WtWebGraphThermoHygroDatalogger_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroDatalogger = _WtWebGraphThermoHygroDatalogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 4)
)


class _WtWebGraphThermoHygroLoggerTimebase_Type(Integer32):
    """Custom type wtWebGraphThermoHygroLoggerTimebase based on Integer32"""
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
        *(("wtWebGraphThermoHygroDatalogger-1Min", 1),
          ("wtWebGraphThermoHygroDatalogger-5Min", 2),
          ("wtWebGraphThermoHygroDatalogger-15Min", 3),
          ("wtWebGraphThermoHygroDatalogger-60Min", 4))
    )


_WtWebGraphThermoHygroLoggerTimebase_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroLoggerTimebase_Object = MibScalar
wtWebGraphThermoHygroLoggerTimebase = _WtWebGraphThermoHygroLoggerTimebase_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 4, 1),
    _WtWebGraphThermoHygroLoggerTimebase_Type()
)
wtWebGraphThermoHygroLoggerTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroLoggerTimebase.setStatus("mandatory")


class _WtWebGraphThermoHygroLoggerSensorSel_Type(OctetString):
    """Custom type wtWebGraphThermoHygroLoggerSensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroLoggerSensorSel_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroLoggerSensorSel_Object = MibScalar
wtWebGraphThermoHygroLoggerSensorSel = _WtWebGraphThermoHygroLoggerSensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 4, 2),
    _WtWebGraphThermoHygroLoggerSensorSel_Type()
)
wtWebGraphThermoHygroLoggerSensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroLoggerSensorSel.setStatus("mandatory")
_WtWebGraphThermoHygroAlarm_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroAlarm = _WtWebGraphThermoHygroAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5)
)


class _WtWebGraphThermoHygroAlarmCount_Type(Integer32):
    """Custom type wtWebGraphThermoHygroAlarmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphThermoHygroAlarmCount_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroAlarmCount_Object = MibScalar
wtWebGraphThermoHygroAlarmCount = _WtWebGraphThermoHygroAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 1),
    _WtWebGraphThermoHygroAlarmCount_Type()
)
wtWebGraphThermoHygroAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmCount.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmIfTable_Object = MibTable
wtWebGraphThermoHygroAlarmIfTable = _WtWebGraphThermoHygroAlarmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmIfTable.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmIfEntry_Object = MibTableRow
wtWebGraphThermoHygroAlarmIfEntry = _WtWebGraphThermoHygroAlarmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 2, 1)
)
wtWebGraphThermoHygroAlarmIfEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmIfEntry.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmNo_Type(Integer32):
    """Custom type wtWebGraphThermoHygroAlarmNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WtWebGraphThermoHygroAlarmNo_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroAlarmNo_Object = MibTableColumn
wtWebGraphThermoHygroAlarmNo = _WtWebGraphThermoHygroAlarmNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 2, 1, 1),
    _WtWebGraphThermoHygroAlarmNo_Type()
)
wtWebGraphThermoHygroAlarmNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmNo.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmTable_Object = MibTable
wtWebGraphThermoHygroAlarmTable = _WtWebGraphThermoHygroAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmTable.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmEntry_Object = MibTableRow
wtWebGraphThermoHygroAlarmEntry = _WtWebGraphThermoHygroAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1)
)
wtWebGraphThermoHygroAlarmEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmEntry.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmTrigger_Type(OctetString):
    """Custom type wtWebGraphThermoHygroAlarmTrigger based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroAlarmTrigger_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroAlarmTrigger_Object = MibTableColumn
wtWebGraphThermoHygroAlarmTrigger = _WtWebGraphThermoHygroAlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 1),
    _WtWebGraphThermoHygroAlarmTrigger_Type()
)
wtWebGraphThermoHygroAlarmTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmTrigger.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmMin_Type = OctetString
_WtWebGraphThermoHygroAlarmMin_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMin = _WtWebGraphThermoHygroAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 2),
    _WtWebGraphThermoHygroAlarmMin_Type()
)
wtWebGraphThermoHygroAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMin.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmMax_Type = OctetString
_WtWebGraphThermoHygroAlarmMax_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMax = _WtWebGraphThermoHygroAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 3),
    _WtWebGraphThermoHygroAlarmMax_Type()
)
wtWebGraphThermoHygroAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMax.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmHysteresis_Type = OctetString
_WtWebGraphThermoHygroAlarmHysteresis_Object = MibTableColumn
wtWebGraphThermoHygroAlarmHysteresis = _WtWebGraphThermoHygroAlarmHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 4),
    _WtWebGraphThermoHygroAlarmHysteresis_Type()
)
wtWebGraphThermoHygroAlarmHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmHysteresis.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmDelay_Type = OctetString
_WtWebGraphThermoHygroAlarmDelay_Object = MibTableColumn
wtWebGraphThermoHygroAlarmDelay = _WtWebGraphThermoHygroAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 5),
    _WtWebGraphThermoHygroAlarmDelay_Type()
)
wtWebGraphThermoHygroAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmDelay.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmInterval_Type = OctetString
_WtWebGraphThermoHygroAlarmInterval_Object = MibTableColumn
wtWebGraphThermoHygroAlarmInterval = _WtWebGraphThermoHygroAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 6),
    _WtWebGraphThermoHygroAlarmInterval_Type()
)
wtWebGraphThermoHygroAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmInterval.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmEnable_Type(OctetString):
    """Custom type wtWebGraphThermoHygroAlarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroAlarmEnable_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroAlarmEnable_Object = MibTableColumn
wtWebGraphThermoHygroAlarmEnable = _WtWebGraphThermoHygroAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 7),
    _WtWebGraphThermoHygroAlarmEnable_Type()
)
wtWebGraphThermoHygroAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmEnable.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmEMailAddr_Type = OctetString
_WtWebGraphThermoHygroAlarmEMailAddr_Object = MibTableColumn
wtWebGraphThermoHygroAlarmEMailAddr = _WtWebGraphThermoHygroAlarmEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 8),
    _WtWebGraphThermoHygroAlarmEMailAddr_Type()
)
wtWebGraphThermoHygroAlarmEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmEMailAddr.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmMailSubject_Type = OctetString
_WtWebGraphThermoHygroAlarmMailSubject_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMailSubject = _WtWebGraphThermoHygroAlarmMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 9),
    _WtWebGraphThermoHygroAlarmMailSubject_Type()
)
wtWebGraphThermoHygroAlarmMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMailSubject.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmMailText_Type = OctetString
_WtWebGraphThermoHygroAlarmMailText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMailText = _WtWebGraphThermoHygroAlarmMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 10),
    _WtWebGraphThermoHygroAlarmMailText_Type()
)
wtWebGraphThermoHygroAlarmMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMailText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmManagerIP_Type = OctetString
_WtWebGraphThermoHygroAlarmManagerIP_Object = MibTableColumn
wtWebGraphThermoHygroAlarmManagerIP = _WtWebGraphThermoHygroAlarmManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 11),
    _WtWebGraphThermoHygroAlarmManagerIP_Type()
)
wtWebGraphThermoHygroAlarmManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmManagerIP.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmTrapText_Type = OctetString
_WtWebGraphThermoHygroAlarmTrapText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmTrapText = _WtWebGraphThermoHygroAlarmTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 12),
    _WtWebGraphThermoHygroAlarmTrapText_Type()
)
wtWebGraphThermoHygroAlarmTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmTrapText.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmMailOptions_Type(OctetString):
    """Custom type wtWebGraphThermoHygroAlarmMailOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroAlarmMailOptions_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroAlarmMailOptions_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMailOptions = _WtWebGraphThermoHygroAlarmMailOptions_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 13),
    _WtWebGraphThermoHygroAlarmMailOptions_Type()
)
wtWebGraphThermoHygroAlarmMailOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMailOptions.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmTcpIpAddr_Type = OctetString
_WtWebGraphThermoHygroAlarmTcpIpAddr_Object = MibTableColumn
wtWebGraphThermoHygroAlarmTcpIpAddr = _WtWebGraphThermoHygroAlarmTcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 14),
    _WtWebGraphThermoHygroAlarmTcpIpAddr_Type()
)
wtWebGraphThermoHygroAlarmTcpIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmTcpIpAddr.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmTcpPort_Type(Integer32):
    """Custom type wtWebGraphThermoHygroAlarmTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoHygroAlarmTcpPort_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroAlarmTcpPort_Object = MibTableColumn
wtWebGraphThermoHygroAlarmTcpPort = _WtWebGraphThermoHygroAlarmTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 15),
    _WtWebGraphThermoHygroAlarmTcpPort_Type()
)
wtWebGraphThermoHygroAlarmTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmTcpPort.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmTcpText_Type = OctetString
_WtWebGraphThermoHygroAlarmTcpText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmTcpText = _WtWebGraphThermoHygroAlarmTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 16),
    _WtWebGraphThermoHygroAlarmTcpText_Type()
)
wtWebGraphThermoHygroAlarmTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmTcpText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmClearMailSubject_Type = OctetString
_WtWebGraphThermoHygroAlarmClearMailSubject_Object = MibTableColumn
wtWebGraphThermoHygroAlarmClearMailSubject = _WtWebGraphThermoHygroAlarmClearMailSubject_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 17),
    _WtWebGraphThermoHygroAlarmClearMailSubject_Type()
)
wtWebGraphThermoHygroAlarmClearMailSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmClearMailSubject.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmClearMailText_Type = OctetString
_WtWebGraphThermoHygroAlarmClearMailText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmClearMailText = _WtWebGraphThermoHygroAlarmClearMailText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 18),
    _WtWebGraphThermoHygroAlarmClearMailText_Type()
)
wtWebGraphThermoHygroAlarmClearMailText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmClearMailText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmClearTrapText_Type = OctetString
_WtWebGraphThermoHygroAlarmClearTrapText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmClearTrapText = _WtWebGraphThermoHygroAlarmClearTrapText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 19),
    _WtWebGraphThermoHygroAlarmClearTrapText_Type()
)
wtWebGraphThermoHygroAlarmClearTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmClearTrapText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmClearTcpText_Type = OctetString
_WtWebGraphThermoHygroAlarmClearTcpText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmClearTcpText = _WtWebGraphThermoHygroAlarmClearTcpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 20),
    _WtWebGraphThermoHygroAlarmClearTcpText_Type()
)
wtWebGraphThermoHygroAlarmClearTcpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmClearTcpText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmDeltaTemp_Type = OctetString
_WtWebGraphThermoHygroAlarmDeltaTemp_Object = MibTableColumn
wtWebGraphThermoHygroAlarmDeltaTemp = _WtWebGraphThermoHygroAlarmDeltaTemp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 21),
    _WtWebGraphThermoHygroAlarmDeltaTemp_Type()
)
wtWebGraphThermoHygroAlarmDeltaTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmDeltaTemp.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmRHMin_Type = OctetString
_WtWebGraphThermoHygroAlarmRHMin_Object = MibTableColumn
wtWebGraphThermoHygroAlarmRHMin = _WtWebGraphThermoHygroAlarmRHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 22),
    _WtWebGraphThermoHygroAlarmRHMin_Type()
)
wtWebGraphThermoHygroAlarmRHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmRHMin.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmRHMax_Type = OctetString
_WtWebGraphThermoHygroAlarmRHMax_Object = MibTableColumn
wtWebGraphThermoHygroAlarmRHMax = _WtWebGraphThermoHygroAlarmRHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 23),
    _WtWebGraphThermoHygroAlarmRHMax_Type()
)
wtWebGraphThermoHygroAlarmRHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmRHMax.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmRHHysteresis_Type = OctetString
_WtWebGraphThermoHygroAlarmRHHysteresis_Object = MibTableColumn
wtWebGraphThermoHygroAlarmRHHysteresis = _WtWebGraphThermoHygroAlarmRHHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 24),
    _WtWebGraphThermoHygroAlarmRHHysteresis_Type()
)
wtWebGraphThermoHygroAlarmRHHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmRHHysteresis.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmAHMin_Type = OctetString
_WtWebGraphThermoHygroAlarmAHMin_Object = MibTableColumn
wtWebGraphThermoHygroAlarmAHMin = _WtWebGraphThermoHygroAlarmAHMin_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 25),
    _WtWebGraphThermoHygroAlarmAHMin_Type()
)
wtWebGraphThermoHygroAlarmAHMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmAHMin.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmAHMax_Type = OctetString
_WtWebGraphThermoHygroAlarmAHMax_Object = MibTableColumn
wtWebGraphThermoHygroAlarmAHMax = _WtWebGraphThermoHygroAlarmAHMax_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 26),
    _WtWebGraphThermoHygroAlarmAHMax_Type()
)
wtWebGraphThermoHygroAlarmAHMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmAHMax.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmSyslogIpAddr_Type = OctetString
_WtWebGraphThermoHygroAlarmSyslogIpAddr_Object = MibTableColumn
wtWebGraphThermoHygroAlarmSyslogIpAddr = _WtWebGraphThermoHygroAlarmSyslogIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 27),
    _WtWebGraphThermoHygroAlarmSyslogIpAddr_Type()
)
wtWebGraphThermoHygroAlarmSyslogIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmSyslogIpAddr.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmSyslogPort_Type(Integer32):
    """Custom type wtWebGraphThermoHygroAlarmSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoHygroAlarmSyslogPort_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroAlarmSyslogPort_Object = MibTableColumn
wtWebGraphThermoHygroAlarmSyslogPort = _WtWebGraphThermoHygroAlarmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 28),
    _WtWebGraphThermoHygroAlarmSyslogPort_Type()
)
wtWebGraphThermoHygroAlarmSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmSyslogPort.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmSyslogText_Type = OctetString
_WtWebGraphThermoHygroAlarmSyslogText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmSyslogText = _WtWebGraphThermoHygroAlarmSyslogText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 29),
    _WtWebGraphThermoHygroAlarmSyslogText_Type()
)
wtWebGraphThermoHygroAlarmSyslogText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmSyslogText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmSyslogClearText_Type = OctetString
_WtWebGraphThermoHygroAlarmSyslogClearText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmSyslogClearText = _WtWebGraphThermoHygroAlarmSyslogClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 30),
    _WtWebGraphThermoHygroAlarmSyslogClearText_Type()
)
wtWebGraphThermoHygroAlarmSyslogClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmSyslogClearText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmFtpDataPort_Type = OctetString
_WtWebGraphThermoHygroAlarmFtpDataPort_Object = MibTableColumn
wtWebGraphThermoHygroAlarmFtpDataPort = _WtWebGraphThermoHygroAlarmFtpDataPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 31),
    _WtWebGraphThermoHygroAlarmFtpDataPort_Type()
)
wtWebGraphThermoHygroAlarmFtpDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmFtpDataPort.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmFtpFileName_Type = OctetString
_WtWebGraphThermoHygroAlarmFtpFileName_Object = MibTableColumn
wtWebGraphThermoHygroAlarmFtpFileName = _WtWebGraphThermoHygroAlarmFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 32),
    _WtWebGraphThermoHygroAlarmFtpFileName_Type()
)
wtWebGraphThermoHygroAlarmFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmFtpFileName.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmFtpText_Type = OctetString
_WtWebGraphThermoHygroAlarmFtpText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmFtpText = _WtWebGraphThermoHygroAlarmFtpText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 33),
    _WtWebGraphThermoHygroAlarmFtpText_Type()
)
wtWebGraphThermoHygroAlarmFtpText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmFtpText.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmFtpClearText_Type = OctetString
_WtWebGraphThermoHygroAlarmFtpClearText_Object = MibTableColumn
wtWebGraphThermoHygroAlarmFtpClearText = _WtWebGraphThermoHygroAlarmFtpClearText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 34),
    _WtWebGraphThermoHygroAlarmFtpClearText_Type()
)
wtWebGraphThermoHygroAlarmFtpClearText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmFtpClearText.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmFtpOption_Type(OctetString):
    """Custom type wtWebGraphThermoHygroAlarmFtpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroAlarmFtpOption_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroAlarmFtpOption_Object = MibTableColumn
wtWebGraphThermoHygroAlarmFtpOption = _WtWebGraphThermoHygroAlarmFtpOption_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 35),
    _WtWebGraphThermoHygroAlarmFtpOption_Type()
)
wtWebGraphThermoHygroAlarmFtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmFtpOption.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmTimerCron_Type = OctetString
_WtWebGraphThermoHygroAlarmTimerCron_Object = MibTableColumn
wtWebGraphThermoHygroAlarmTimerCron = _WtWebGraphThermoHygroAlarmTimerCron_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 36),
    _WtWebGraphThermoHygroAlarmTimerCron_Type()
)
wtWebGraphThermoHygroAlarmTimerCron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmTimerCron.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmName_Type = OctetString
_WtWebGraphThermoHygroAlarmName_Object = MibTableColumn
wtWebGraphThermoHygroAlarmName = _WtWebGraphThermoHygroAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 39),
    _WtWebGraphThermoHygroAlarmName_Type()
)
wtWebGraphThermoHygroAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmName.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmActive_Type = OctetString
_WtWebGraphThermoHygroAlarmActive_Object = MibTableColumn
wtWebGraphThermoHygroAlarmActive = _WtWebGraphThermoHygroAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 40),
    _WtWebGraphThermoHygroAlarmActive_Type()
)
wtWebGraphThermoHygroAlarmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmActive.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Type = OctetString
_WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Object = MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqAuthEnable = _WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 61),
    _WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Type()
)
wtWebGraphThermoHygroAlarmHttpReqAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmHttpReqAuthEnable.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmHttpReqAuthUser_Type = OctetString
_WtWebGraphThermoHygroAlarmHttpReqAuthUser_Object = MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqAuthUser = _WtWebGraphThermoHygroAlarmHttpReqAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 62),
    _WtWebGraphThermoHygroAlarmHttpReqAuthUser_Type()
)
wtWebGraphThermoHygroAlarmHttpReqAuthUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmHttpReqAuthUser.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Type = OctetString
_WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Object = MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqAuthPassword = _WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 63),
    _WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Type()
)
wtWebGraphThermoHygroAlarmHttpReqAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmHttpReqAuthPassword.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmHttpReqSetUrl_Type = OctetString
_WtWebGraphThermoHygroAlarmHttpReqSetUrl_Object = MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqSetUrl = _WtWebGraphThermoHygroAlarmHttpReqSetUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 64),
    _WtWebGraphThermoHygroAlarmHttpReqSetUrl_Type()
)
wtWebGraphThermoHygroAlarmHttpReqSetUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmHttpReqSetUrl.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmHttpReqClearUrl_Type = OctetString
_WtWebGraphThermoHygroAlarmHttpReqClearUrl_Object = MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqClearUrl = _WtWebGraphThermoHygroAlarmHttpReqClearUrl_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 65),
    _WtWebGraphThermoHygroAlarmHttpReqClearUrl_Type()
)
wtWebGraphThermoHygroAlarmHttpReqClearUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmHttpReqClearUrl.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmHttpReqServerPort_Type(Integer32):
    """Custom type wtWebGraphThermoHygroAlarmHttpReqServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WtWebGraphThermoHygroAlarmHttpReqServerPort_Type.__name__ = "Integer32"
_WtWebGraphThermoHygroAlarmHttpReqServerPort_Object = MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqServerPort = _WtWebGraphThermoHygroAlarmHttpReqServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 66),
    _WtWebGraphThermoHygroAlarmHttpReqServerPort_Type()
)
wtWebGraphThermoHygroAlarmHttpReqServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmHttpReqServerPort.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmMqttTopicPath_Type = OctetString
_WtWebGraphThermoHygroAlarmMqttTopicPath_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMqttTopicPath = _WtWebGraphThermoHygroAlarmMqttTopicPath_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 67),
    _WtWebGraphThermoHygroAlarmMqttTopicPath_Type()
)
wtWebGraphThermoHygroAlarmMqttTopicPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMqttTopicPath.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Type = OctetString
_WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMqttTopicSetTopic = _WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 68),
    _WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Type()
)
wtWebGraphThermoHygroAlarmMqttTopicSetTopic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMqttTopicSetTopic.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmMqttTopicClear_Type = OctetString
_WtWebGraphThermoHygroAlarmMqttTopicClear_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMqttTopicClear = _WtWebGraphThermoHygroAlarmMqttTopicClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 69),
    _WtWebGraphThermoHygroAlarmMqttTopicClear_Type()
)
wtWebGraphThermoHygroAlarmMqttTopicClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMqttTopicClear.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmSensorLostSelection_Type = OctetString
_WtWebGraphThermoHygroAlarmSensorLostSelection_Object = MibTableColumn
wtWebGraphThermoHygroAlarmSensorLostSelection = _WtWebGraphThermoHygroAlarmSensorLostSelection_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 70),
    _WtWebGraphThermoHygroAlarmSensorLostSelection_Type()
)
wtWebGraphThermoHygroAlarmSensorLostSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmSensorLostSelection.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmLimitWindow_Type = OctetString
_WtWebGraphThermoHygroAlarmLimitWindow_Object = MibTableColumn
wtWebGraphThermoHygroAlarmLimitWindow = _WtWebGraphThermoHygroAlarmLimitWindow_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 71),
    _WtWebGraphThermoHygroAlarmLimitWindow_Type()
)
wtWebGraphThermoHygroAlarmLimitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmLimitWindow.setStatus("mandatory")
_WtWebGraphThermoHygroAlarmSnmpManagerPort_Type = Integer32
_WtWebGraphThermoHygroAlarmSnmpManagerPort_Object = MibTableColumn
wtWebGraphThermoHygroAlarmSnmpManagerPort = _WtWebGraphThermoHygroAlarmSnmpManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 76),
    _WtWebGraphThermoHygroAlarmSnmpManagerPort_Type()
)
wtWebGraphThermoHygroAlarmSnmpManagerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmSnmpManagerPort.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmMqttQoS_Type(OctetString):
    """Custom type wtWebGraphThermoHygroAlarmMqttQoS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroAlarmMqttQoS_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroAlarmMqttQoS_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMqttQoS = _WtWebGraphThermoHygroAlarmMqttQoS_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 77),
    _WtWebGraphThermoHygroAlarmMqttQoS_Type()
)
wtWebGraphThermoHygroAlarmMqttQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMqttQoS.setStatus("mandatory")


class _WtWebGraphThermoHygroAlarmMqttRetain_Type(OctetString):
    """Custom type wtWebGraphThermoHygroAlarmMqttRetain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroAlarmMqttRetain_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroAlarmMqttRetain_Object = MibTableColumn
wtWebGraphThermoHygroAlarmMqttRetain = _WtWebGraphThermoHygroAlarmMqttRetain_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 5, 3, 1, 78),
    _WtWebGraphThermoHygroAlarmMqttRetain_Type()
)
wtWebGraphThermoHygroAlarmMqttRetain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlarmMqttRetain.setStatus("mandatory")
_WtWebGraphThermoHygroGraphics_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroGraphics = _WtWebGraphThermoHygroGraphics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6)
)
_WtWebGraphThermoHygroGraphicsBase_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroGraphicsBase = _WtWebGraphThermoHygroGraphicsBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 1)
)
_WtWebGraphThermoHygroGraphicsBaseEnable_Type = OctetString
_WtWebGraphThermoHygroGraphicsBaseEnable_Object = MibScalar
wtWebGraphThermoHygroGraphicsBaseEnable = _WtWebGraphThermoHygroGraphicsBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 1, 1),
    _WtWebGraphThermoHygroGraphicsBaseEnable_Type()
)
wtWebGraphThermoHygroGraphicsBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsBaseEnable.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsBaseWidth_Type = Integer32
_WtWebGraphThermoHygroGraphicsBaseWidth_Object = MibScalar
wtWebGraphThermoHygroGraphicsBaseWidth = _WtWebGraphThermoHygroGraphicsBaseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 1, 2),
    _WtWebGraphThermoHygroGraphicsBaseWidth_Type()
)
wtWebGraphThermoHygroGraphicsBaseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsBaseWidth.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsBaseHeight_Type = Integer32
_WtWebGraphThermoHygroGraphicsBaseHeight_Object = MibScalar
wtWebGraphThermoHygroGraphicsBaseHeight = _WtWebGraphThermoHygroGraphicsBaseHeight_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 1, 3),
    _WtWebGraphThermoHygroGraphicsBaseHeight_Type()
)
wtWebGraphThermoHygroGraphicsBaseHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsBaseHeight.setStatus("mandatory")


class _WtWebGraphThermoHygroGraphicsBaseFrameColor_Type(OctetString):
    """Custom type wtWebGraphThermoHygroGraphicsBaseFrameColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphThermoHygroGraphicsBaseFrameColor_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroGraphicsBaseFrameColor_Object = MibScalar
wtWebGraphThermoHygroGraphicsBaseFrameColor = _WtWebGraphThermoHygroGraphicsBaseFrameColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 1, 4),
    _WtWebGraphThermoHygroGraphicsBaseFrameColor_Type()
)
wtWebGraphThermoHygroGraphicsBaseFrameColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsBaseFrameColor.setStatus("mandatory")


class _WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Type(OctetString):
    """Custom type wtWebGraphThermoHygroGraphicsBaseBackgroundColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Object = MibScalar
wtWebGraphThermoHygroGraphicsBaseBackgroundColor = _WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 1, 5),
    _WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Type()
)
wtWebGraphThermoHygroGraphicsBaseBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsBaseBackgroundColor.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsBasePollingrate_Type = Integer32
_WtWebGraphThermoHygroGraphicsBasePollingrate_Object = MibScalar
wtWebGraphThermoHygroGraphicsBasePollingrate = _WtWebGraphThermoHygroGraphicsBasePollingrate_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 1, 6),
    _WtWebGraphThermoHygroGraphicsBasePollingrate_Type()
)
wtWebGraphThermoHygroGraphicsBasePollingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsBasePollingrate.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsSelect_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroGraphicsSelect = _WtWebGraphThermoHygroGraphicsSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 2)
)


class _WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Type(OctetString):
    """Custom type wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Object = MibScalar
wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel = _WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 2, 1),
    _WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Type()
)
wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel.setStatus("mandatory")


class _WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Type(OctetString):
    """Custom type wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Object = MibScalar
wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem = _WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 2, 2),
    _WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Type()
)
wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem.setStatus("mandatory")
_WtWebGraphThermoHygroSensorColorTable_Object = MibTable
wtWebGraphThermoHygroSensorColorTable = _WtWebGraphThermoHygroSensorColorTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSensorColorTable.setStatus("mandatory")
_WtWebGraphThermoHygroSensorColorEntry_Object = MibTableRow
wtWebGraphThermoHygroSensorColorEntry = _WtWebGraphThermoHygroSensorColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 2, 3, 1)
)
wtWebGraphThermoHygroSensorColorEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroSensorColorEntry.setStatus("mandatory")


class _WtWebGraphThermoHygroGraphicsSensorColor_Type(OctetString):
    """Custom type wtWebGraphThermoHygroGraphicsSensorColor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_WtWebGraphThermoHygroGraphicsSensorColor_Type.__name__ = "OctetString"
_WtWebGraphThermoHygroGraphicsSensorColor_Object = MibTableColumn
wtWebGraphThermoHygroGraphicsSensorColor = _WtWebGraphThermoHygroGraphicsSensorColor_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 2, 3, 1, 1),
    _WtWebGraphThermoHygroGraphicsSensorColor_Type()
)
wtWebGraphThermoHygroGraphicsSensorColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsSensorColor.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsSelectScale_Type = OctetString
_WtWebGraphThermoHygroGraphicsSelectScale_Object = MibTableColumn
wtWebGraphThermoHygroGraphicsSelectScale = _WtWebGraphThermoHygroGraphicsSelectScale_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 2, 3, 1, 2),
    _WtWebGraphThermoHygroGraphicsSelectScale_Type()
)
wtWebGraphThermoHygroGraphicsSelectScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsSelectScale.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroGraphicsScale = _WtWebGraphThermoHygroGraphicsScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3)
)
_WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Type = OctetString
_WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Object = MibScalar
wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable = _WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 1),
    _WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Type()
)
wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Type = OctetString
_WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Object = MibScalar
wtWebGraphThermoHygroGraphicsScaleAutoFitEnable = _WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 2),
    _WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Type()
)
wtWebGraphThermoHygroGraphicsScaleAutoFitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScaleAutoFitEnable.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale1Min_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale1Min_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale1Min = _WtWebGraphThermoHygroGraphicsScale1Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 3),
    _WtWebGraphThermoHygroGraphicsScale1Min_Type()
)
wtWebGraphThermoHygroGraphicsScale1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale1Min.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale2Min_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale2Min_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale2Min = _WtWebGraphThermoHygroGraphicsScale2Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 4),
    _WtWebGraphThermoHygroGraphicsScale2Min_Type()
)
wtWebGraphThermoHygroGraphicsScale2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale2Min.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale3Min_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale3Min_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale3Min = _WtWebGraphThermoHygroGraphicsScale3Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 5),
    _WtWebGraphThermoHygroGraphicsScale3Min_Type()
)
wtWebGraphThermoHygroGraphicsScale3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale3Min.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale4Min_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale4Min_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale4Min = _WtWebGraphThermoHygroGraphicsScale4Min_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 6),
    _WtWebGraphThermoHygroGraphicsScale4Min_Type()
)
wtWebGraphThermoHygroGraphicsScale4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale4Min.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale1Max_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale1Max_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale1Max = _WtWebGraphThermoHygroGraphicsScale1Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 7),
    _WtWebGraphThermoHygroGraphicsScale1Max_Type()
)
wtWebGraphThermoHygroGraphicsScale1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale1Max.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale2Max_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale2Max_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale2Max = _WtWebGraphThermoHygroGraphicsScale2Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 8),
    _WtWebGraphThermoHygroGraphicsScale2Max_Type()
)
wtWebGraphThermoHygroGraphicsScale2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale2Max.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale3Max_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale3Max_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale3Max = _WtWebGraphThermoHygroGraphicsScale3Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 9),
    _WtWebGraphThermoHygroGraphicsScale3Max_Type()
)
wtWebGraphThermoHygroGraphicsScale3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale3Max.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale4Max_Type = Integer32
_WtWebGraphThermoHygroGraphicsScale4Max_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale4Max = _WtWebGraphThermoHygroGraphicsScale4Max_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 10),
    _WtWebGraphThermoHygroGraphicsScale4Max_Type()
)
wtWebGraphThermoHygroGraphicsScale4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale4Max.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale1Unit_Type = OctetString
_WtWebGraphThermoHygroGraphicsScale1Unit_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale1Unit = _WtWebGraphThermoHygroGraphicsScale1Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 11),
    _WtWebGraphThermoHygroGraphicsScale1Unit_Type()
)
wtWebGraphThermoHygroGraphicsScale1Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale1Unit.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale2Unit_Type = OctetString
_WtWebGraphThermoHygroGraphicsScale2Unit_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale2Unit = _WtWebGraphThermoHygroGraphicsScale2Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 12),
    _WtWebGraphThermoHygroGraphicsScale2Unit_Type()
)
wtWebGraphThermoHygroGraphicsScale2Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale2Unit.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale3Unit_Type = OctetString
_WtWebGraphThermoHygroGraphicsScale3Unit_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale3Unit = _WtWebGraphThermoHygroGraphicsScale3Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 13),
    _WtWebGraphThermoHygroGraphicsScale3Unit_Type()
)
wtWebGraphThermoHygroGraphicsScale3Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale3Unit.setStatus("mandatory")
_WtWebGraphThermoHygroGraphicsScale4Unit_Type = OctetString
_WtWebGraphThermoHygroGraphicsScale4Unit_Object = MibScalar
wtWebGraphThermoHygroGraphicsScale4Unit = _WtWebGraphThermoHygroGraphicsScale4Unit_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 1, 6, 3, 14),
    _WtWebGraphThermoHygroGraphicsScale4Unit_Type()
)
wtWebGraphThermoHygroGraphicsScale4Unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroGraphicsScale4Unit.setStatus("mandatory")
_WtWebGraphThermoHygroPorts_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroPorts = _WtWebGraphThermoHygroPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2)
)
_WtWebGraphThermoHygroPortTable_Object = MibTable
wtWebGraphThermoHygroPortTable = _WtWebGraphThermoHygroPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1)
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortTable.setStatus("mandatory")
_WtWebGraphThermoHygroPortEntry_Object = MibTableRow
wtWebGraphThermoHygroPortEntry = _WtWebGraphThermoHygroPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1)
)
wtWebGraphThermoHygroPortEntry.setIndexNames(
    (0, "WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroSensorNo"),
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortEntry.setStatus("mandatory")
_WtWebGraphThermoHygroPortName_Type = OctetString
_WtWebGraphThermoHygroPortName_Object = MibTableColumn
wtWebGraphThermoHygroPortName = _WtWebGraphThermoHygroPortName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1, 1),
    _WtWebGraphThermoHygroPortName_Type()
)
wtWebGraphThermoHygroPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortName.setStatus("mandatory")
_WtWebGraphThermoHygroPortText_Type = OctetString
_WtWebGraphThermoHygroPortText_Object = MibTableColumn
wtWebGraphThermoHygroPortText = _WtWebGraphThermoHygroPortText_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1, 2),
    _WtWebGraphThermoHygroPortText_Type()
)
wtWebGraphThermoHygroPortText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortText.setStatus("mandatory")
_WtWebGraphThermoHygroPortOffset1_Type = OctetString
_WtWebGraphThermoHygroPortOffset1_Object = MibTableColumn
wtWebGraphThermoHygroPortOffset1 = _WtWebGraphThermoHygroPortOffset1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1, 3),
    _WtWebGraphThermoHygroPortOffset1_Type()
)
wtWebGraphThermoHygroPortOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortOffset1.setStatus("mandatory")
_WtWebGraphThermoHygroPortTemperature1_Type = OctetString
_WtWebGraphThermoHygroPortTemperature1_Object = MibTableColumn
wtWebGraphThermoHygroPortTemperature1 = _WtWebGraphThermoHygroPortTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1, 4),
    _WtWebGraphThermoHygroPortTemperature1_Type()
)
wtWebGraphThermoHygroPortTemperature1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortTemperature1.setStatus("mandatory")
_WtWebGraphThermoHygroPortOffset2_Type = OctetString
_WtWebGraphThermoHygroPortOffset2_Object = MibTableColumn
wtWebGraphThermoHygroPortOffset2 = _WtWebGraphThermoHygroPortOffset2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1, 5),
    _WtWebGraphThermoHygroPortOffset2_Type()
)
wtWebGraphThermoHygroPortOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortOffset2.setStatus("mandatory")
_WtWebGraphThermoHygroPortTemperature2_Type = OctetString
_WtWebGraphThermoHygroPortTemperature2_Object = MibTableColumn
wtWebGraphThermoHygroPortTemperature2 = _WtWebGraphThermoHygroPortTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1, 6),
    _WtWebGraphThermoHygroPortTemperature2_Type()
)
wtWebGraphThermoHygroPortTemperature2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortTemperature2.setStatus("mandatory")
_WtWebGraphThermoHygroPortComment_Type = OctetString
_WtWebGraphThermoHygroPortComment_Object = MibTableColumn
wtWebGraphThermoHygroPortComment = _WtWebGraphThermoHygroPortComment_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 1, 1, 7),
    _WtWebGraphThermoHygroPortComment_Type()
)
wtWebGraphThermoHygroPortComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortComment.setStatus("mandatory")
_WtWebGraphThermoHygroPortAltidude_Type = OctetString
_WtWebGraphThermoHygroPortAltidude_Object = MibScalar
wtWebGraphThermoHygroPortAltidude = _WtWebGraphThermoHygroPortAltidude_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 2, 2),
    _WtWebGraphThermoHygroPortAltidude_Type()
)
wtWebGraphThermoHygroPortAltidude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroPortAltidude.setStatus("mandatory")
_WtWebGraphThermoHygroManufact_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroManufact = _WtWebGraphThermoHygroManufact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 3)
)
_WtWebGraphThermoHygroMfName_Type = OctetString
_WtWebGraphThermoHygroMfName_Object = MibScalar
wtWebGraphThermoHygroMfName = _WtWebGraphThermoHygroMfName_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 3, 1),
    _WtWebGraphThermoHygroMfName_Type()
)
wtWebGraphThermoHygroMfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMfName.setStatus("mandatory")
_WtWebGraphThermoHygroMfAddr_Type = OctetString
_WtWebGraphThermoHygroMfAddr_Object = MibScalar
wtWebGraphThermoHygroMfAddr = _WtWebGraphThermoHygroMfAddr_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 3, 2),
    _WtWebGraphThermoHygroMfAddr_Type()
)
wtWebGraphThermoHygroMfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMfAddr.setStatus("mandatory")
_WtWebGraphThermoHygroMfHotline_Type = OctetString
_WtWebGraphThermoHygroMfHotline_Object = MibScalar
wtWebGraphThermoHygroMfHotline = _WtWebGraphThermoHygroMfHotline_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 3, 3),
    _WtWebGraphThermoHygroMfHotline_Type()
)
wtWebGraphThermoHygroMfHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMfHotline.setStatus("mandatory")
_WtWebGraphThermoHygroMfInternet_Type = OctetString
_WtWebGraphThermoHygroMfInternet_Object = MibScalar
wtWebGraphThermoHygroMfInternet = _WtWebGraphThermoHygroMfInternet_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 3, 4),
    _WtWebGraphThermoHygroMfInternet_Type()
)
wtWebGraphThermoHygroMfInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMfInternet.setStatus("mandatory")
_WtWebGraphThermoHygroMfDeviceTyp_Type = OctetString
_WtWebGraphThermoHygroMfDeviceTyp_Object = MibScalar
wtWebGraphThermoHygroMfDeviceTyp = _WtWebGraphThermoHygroMfDeviceTyp_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 3, 5),
    _WtWebGraphThermoHygroMfDeviceTyp_Type()
)
wtWebGraphThermoHygroMfDeviceTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMfDeviceTyp.setStatus("mandatory")
_WtWebGraphThermoHygroMfOrderNo_Type = OctetString
_WtWebGraphThermoHygroMfOrderNo_Object = MibScalar
wtWebGraphThermoHygroMfOrderNo = _WtWebGraphThermoHygroMfOrderNo_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 3, 3, 6),
    _WtWebGraphThermoHygroMfOrderNo_Type()
)
wtWebGraphThermoHygroMfOrderNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroMfOrderNo.setStatus("mandatory")
_WtWebGraphThermoHygroDiag_ObjectIdentity = ObjectIdentity
wtWebGraphThermoHygroDiag = _WtWebGraphThermoHygroDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 4)
)
_WtWebGraphThermoHygroDiagErrorCount_Type = Integer32
_WtWebGraphThermoHygroDiagErrorCount_Object = MibScalar
wtWebGraphThermoHygroDiagErrorCount = _WtWebGraphThermoHygroDiagErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 4, 1),
    _WtWebGraphThermoHygroDiagErrorCount_Type()
)
wtWebGraphThermoHygroDiagErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDiagErrorCount.setStatus("mandatory")
_WtWebGraphThermoHygroDiagBinaryError_Type = OctetString
_WtWebGraphThermoHygroDiagBinaryError_Object = MibScalar
wtWebGraphThermoHygroDiagBinaryError = _WtWebGraphThermoHygroDiagBinaryError_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 4, 2),
    _WtWebGraphThermoHygroDiagBinaryError_Type()
)
wtWebGraphThermoHygroDiagBinaryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDiagBinaryError.setStatus("mandatory")
_WtWebGraphThermoHygroDiagErrorIndex_Type = Integer32
_WtWebGraphThermoHygroDiagErrorIndex_Object = MibScalar
wtWebGraphThermoHygroDiagErrorIndex = _WtWebGraphThermoHygroDiagErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 4, 3),
    _WtWebGraphThermoHygroDiagErrorIndex_Type()
)
wtWebGraphThermoHygroDiagErrorIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDiagErrorIndex.setStatus("mandatory")
_WtWebGraphThermoHygroDiagErrorMessage_Type = OctetString
_WtWebGraphThermoHygroDiagErrorMessage_Object = MibScalar
wtWebGraphThermoHygroDiagErrorMessage = _WtWebGraphThermoHygroDiagErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 4, 4),
    _WtWebGraphThermoHygroDiagErrorMessage_Type()
)
wtWebGraphThermoHygroDiagErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDiagErrorMessage.setStatus("mandatory")
_WtWebGraphThermoHygroDiagErrorClear_Type = Integer32
_WtWebGraphThermoHygroDiagErrorClear_Object = MibScalar
wtWebGraphThermoHygroDiagErrorClear = _WtWebGraphThermoHygroDiagErrorClear_Object(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 4, 5),
    _WtWebGraphThermoHygroDiagErrorClear_Type()
)
wtWebGraphThermoHygroDiagErrorClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroDiagErrorClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wtWebGraphThermoHygroAlert1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 31)
)
wtWebGraphThermoHygroAlert1.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert1.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 32)
)
wtWebGraphThermoHygroAlert2.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert2.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 33)
)
wtWebGraphThermoHygroAlert3.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert3.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 34)
)
wtWebGraphThermoHygroAlert4.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert4.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 35)
)
wtWebGraphThermoHygroAlert5.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert5.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 36)
)
wtWebGraphThermoHygroAlert6.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert6.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 37)
)
wtWebGraphThermoHygroAlert7.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert7.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 38)
)
wtWebGraphThermoHygroAlert8.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert8.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 91)
)
wtWebGraphThermoHygroAlert9.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert9.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 92)
)
wtWebGraphThermoHygroAlert10.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert10.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 93)
)
wtWebGraphThermoHygroAlert11.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert11.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 94)
)
wtWebGraphThermoHygroAlert12.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert12.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 95)
)
wtWebGraphThermoHygroAlert13.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert13.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 96)
)
wtWebGraphThermoHygroAlert14.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert14.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 97)
)
wtWebGraphThermoHygroAlert15.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert15.setStatus(
        ""
    )

wtWebGraphThermoHygroAlert16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 98)
)
wtWebGraphThermoHygroAlert16.setObjects(
    ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroAlarmClearTrapText")
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlert16.setStatus(
        ""
    )

wtWebGraphThermoHygroAlertDiag = NotificationType(
    (1, 3, 6, 1, 4, 1, 5040, 1, 2, 42, 0, 110)
)
wtWebGraphThermoHygroAlertDiag.setObjects(
      *(("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroDiagErrorIndex"),
        ("WebGraph-Thermo-Hygrometer-US-MIB", "wtWebGraphThermoHygroDiagErrorMessage"))
)
if mibBuilder.loadTexts:
    wtWebGraphThermoHygroAlertDiag.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebGraph-Thermo-Hygrometer-US-MIB",
    **{"wut": wut,
       "wtComServer": wtComServer,
       "wtWebio": wtWebio,
       "wtWebGraphThermoHygro": wtWebGraphThermoHygro,
       "wtWebGraphThermoHygroAlert1": wtWebGraphThermoHygroAlert1,
       "wtWebGraphThermoHygroAlert2": wtWebGraphThermoHygroAlert2,
       "wtWebGraphThermoHygroAlert3": wtWebGraphThermoHygroAlert3,
       "wtWebGraphThermoHygroAlert4": wtWebGraphThermoHygroAlert4,
       "wtWebGraphThermoHygroAlert5": wtWebGraphThermoHygroAlert5,
       "wtWebGraphThermoHygroAlert6": wtWebGraphThermoHygroAlert6,
       "wtWebGraphThermoHygroAlert7": wtWebGraphThermoHygroAlert7,
       "wtWebGraphThermoHygroAlert8": wtWebGraphThermoHygroAlert8,
       "wtWebGraphThermoHygroAlert9": wtWebGraphThermoHygroAlert9,
       "wtWebGraphThermoHygroAlert10": wtWebGraphThermoHygroAlert10,
       "wtWebGraphThermoHygroAlert11": wtWebGraphThermoHygroAlert11,
       "wtWebGraphThermoHygroAlert12": wtWebGraphThermoHygroAlert12,
       "wtWebGraphThermoHygroAlert13": wtWebGraphThermoHygroAlert13,
       "wtWebGraphThermoHygroAlert14": wtWebGraphThermoHygroAlert14,
       "wtWebGraphThermoHygroAlert15": wtWebGraphThermoHygroAlert15,
       "wtWebGraphThermoHygroAlert16": wtWebGraphThermoHygroAlert16,
       "wtWebGraphThermoHygroAlertDiag": wtWebGraphThermoHygroAlertDiag,
       "wtWebGraphThermoHygroTemp": wtWebGraphThermoHygroTemp,
       "wtWebGraphThermoHygroSensors": wtWebGraphThermoHygroSensors,
       "wtWebGraphThermoHygroSensorTable": wtWebGraphThermoHygroSensorTable,
       "wtWebGraphThermoHygroSensorEntry": wtWebGraphThermoHygroSensorEntry,
       "wtWebGraphThermoHygroSensorNo": wtWebGraphThermoHygroSensorNo,
       "wtWebGraphThermoHygroTempValueTable": wtWebGraphThermoHygroTempValueTable,
       "wtWebGraphThermoHygroTempValueEntry": wtWebGraphThermoHygroTempValueEntry,
       "wtWebGraphThermoHygroTempValue": wtWebGraphThermoHygroTempValue,
       "wtWebGraphThermoHygroBinaryTempValueTable": wtWebGraphThermoHygroBinaryTempValueTable,
       "wtWebGraphThermoHygroBinaryTempValueEntry": wtWebGraphThermoHygroBinaryTempValueEntry,
       "wtWebGraphThermoHygroBinaryTempValue": wtWebGraphThermoHygroBinaryTempValue,
       "wtWebGraphThermoHygroTempValuePktTable": wtWebGraphThermoHygroTempValuePktTable,
       "wtWebGraphThermoHygroTempValuePktEntry": wtWebGraphThermoHygroTempValuePktEntry,
       "wtWebGraphThermoHygroTempValuePkt": wtWebGraphThermoHygroTempValuePkt,
       "wtWebGraphThermoHygroSessCntrl": wtWebGraphThermoHygroSessCntrl,
       "wtWebGraphThermoHygroSessCntrlPassword": wtWebGraphThermoHygroSessCntrlPassword,
       "wtWebGraphThermoHygroSessCntrlConfigMode": wtWebGraphThermoHygroSessCntrlConfigMode,
       "wtWebGraphThermoHygroSessCntrlLogout": wtWebGraphThermoHygroSessCntrlLogout,
       "wtWebGraphThermoHygroSessCntrlAdminPassword": wtWebGraphThermoHygroSessCntrlAdminPassword,
       "wtWebGraphThermoHygroSessCntrlConfigPassword": wtWebGraphThermoHygroSessCntrlConfigPassword,
       "wtWebGraphThermoHygroConfig": wtWebGraphThermoHygroConfig,
       "wtWebGraphThermoHygroDevice": wtWebGraphThermoHygroDevice,
       "wtWebGraphThermoHygroText": wtWebGraphThermoHygroText,
       "wtWebGraphThermoHygroDeviceName": wtWebGraphThermoHygroDeviceName,
       "wtWebGraphThermoHygroDeviceText": wtWebGraphThermoHygroDeviceText,
       "wtWebGraphThermoHygroDeviceLocation": wtWebGraphThermoHygroDeviceLocation,
       "wtWebGraphThermoHygroDeviceContact": wtWebGraphThermoHygroDeviceContact,
       "wtWebGraphThermoHygroTimeDate": wtWebGraphThermoHygroTimeDate,
       "wtWebGraphThermoHygroTimeZone": wtWebGraphThermoHygroTimeZone,
       "wtWebGraphThermoHygroTzOffsetHrs": wtWebGraphThermoHygroTzOffsetHrs,
       "wtWebGraphThermoHygroTzOffsetMin": wtWebGraphThermoHygroTzOffsetMin,
       "wtWebGraphThermoHygroTzEnable": wtWebGraphThermoHygroTzEnable,
       "wtWebGraphThermoHygroStTzOffsetHrs": wtWebGraphThermoHygroStTzOffsetHrs,
       "wtWebGraphThermoHygroStTzOffsetMin": wtWebGraphThermoHygroStTzOffsetMin,
       "wtWebGraphThermoHygroStTzEnable": wtWebGraphThermoHygroStTzEnable,
       "wtWebGraphThermoHygroStTzStartMonth": wtWebGraphThermoHygroStTzStartMonth,
       "wtWebGraphThermoHygroStTzStartMode": wtWebGraphThermoHygroStTzStartMode,
       "wtWebGraphThermoHygroStTzStartWday": wtWebGraphThermoHygroStTzStartWday,
       "wtWebGraphThermoHygroStTzStartHrs": wtWebGraphThermoHygroStTzStartHrs,
       "wtWebGraphThermoHygroStTzStartMin": wtWebGraphThermoHygroStTzStartMin,
       "wtWebGraphThermoHygroStTzStopMonth": wtWebGraphThermoHygroStTzStopMonth,
       "wtWebGraphThermoHygroStTzStopMode": wtWebGraphThermoHygroStTzStopMode,
       "wtWebGraphThermoHygroStTzStopWday": wtWebGraphThermoHygroStTzStopWday,
       "wtWebGraphThermoHygroStTzStopHrs": wtWebGraphThermoHygroStTzStopHrs,
       "wtWebGraphThermoHygroStTzStopMin": wtWebGraphThermoHygroStTzStopMin,
       "wtWebGraphThermoHygroTimeServer": wtWebGraphThermoHygroTimeServer,
       "wtWebGraphThermoHygroTimeServer1": wtWebGraphThermoHygroTimeServer1,
       "wtWebGraphThermoHygroTimeServer2": wtWebGraphThermoHygroTimeServer2,
       "wtWebGraphThermoHygroTsEnable": wtWebGraphThermoHygroTsEnable,
       "wtWebGraphThermoHygroTsSyncTime": wtWebGraphThermoHygroTsSyncTime,
       "wtWebGraphThermoHygroDeviceClock": wtWebGraphThermoHygroDeviceClock,
       "wtWebGraphThermoHygroClockHrs": wtWebGraphThermoHygroClockHrs,
       "wtWebGraphThermoHygroClockMin": wtWebGraphThermoHygroClockMin,
       "wtWebGraphThermoHygroClockDay": wtWebGraphThermoHygroClockDay,
       "wtWebGraphThermoHygroClockMonth": wtWebGraphThermoHygroClockMonth,
       "wtWebGraphThermoHygroClockYear": wtWebGraphThermoHygroClockYear,
       "wtWebGraphThermoHygroBasic": wtWebGraphThermoHygroBasic,
       "wtWebGraphThermoHygroNetwork": wtWebGraphThermoHygroNetwork,
       "wtWebGraphThermoHygroIpAddress": wtWebGraphThermoHygroIpAddress,
       "wtWebGraphThermoHygroSubnetMask": wtWebGraphThermoHygroSubnetMask,
       "wtWebGraphThermoHygroGateway": wtWebGraphThermoHygroGateway,
       "wtWebGraphThermoHygroDnsServer1": wtWebGraphThermoHygroDnsServer1,
       "wtWebGraphThermoHygroDnsServer2": wtWebGraphThermoHygroDnsServer2,
       "wtWebGraphThermoHygroAddConfig": wtWebGraphThermoHygroAddConfig,
       "wtWebGraphThermoHygroHTTP": wtWebGraphThermoHygroHTTP,
       "wtWebGraphThermoHygroStartup": wtWebGraphThermoHygroStartup,
       "wtWebGraphThermoHygroGetHeaderEnable": wtWebGraphThermoHygroGetHeaderEnable,
       "wtWebGraphThermoHygroHttpPort": wtWebGraphThermoHygroHttpPort,
       "wtWebGraphThermoHygroMail": wtWebGraphThermoHygroMail,
       "wtWebGraphThermoHygroMailAdName": wtWebGraphThermoHygroMailAdName,
       "wtWebGraphThermoHygroMailReply": wtWebGraphThermoHygroMailReply,
       "wtWebGraphThermoHygroMailServer": wtWebGraphThermoHygroMailServer,
       "wtWebioAn1MailEnable": wtWebioAn1MailEnable,
       "wtWebGraphThermoHygroMailAuthentication": wtWebGraphThermoHygroMailAuthentication,
       "wtWebGraphThermoHygroMailAuthUser": wtWebGraphThermoHygroMailAuthUser,
       "wtWebGraphThermoHygroMailAuthPassword": wtWebGraphThermoHygroMailAuthPassword,
       "wtWebGraphThermoHygroMailPop3Server": wtWebGraphThermoHygroMailPop3Server,
       "wtWebGraphThermoHygroSNMP": wtWebGraphThermoHygroSNMP,
       "wtWebGraphThermoHygroSnmpCommunityStringRead": wtWebGraphThermoHygroSnmpCommunityStringRead,
       "wtWebGraphThermoHygroSnmpCommunityStringReadWrite": wtWebGraphThermoHygroSnmpCommunityStringReadWrite,
       "wtWebGraphThermoHygroSystemTrapManagerIP": wtWebGraphThermoHygroSystemTrapManagerIP,
       "wtWebGraphThermoHygroSystemTrapEnable": wtWebGraphThermoHygroSystemTrapEnable,
       "wtWebGraphThermoHygroSnmpEnable": wtWebGraphThermoHygroSnmpEnable,
       "wtWebGraphThermoHygroSnmpCommunityStringTrap": wtWebGraphThermoHygroSnmpCommunityStringTrap,
       "wtWebGraphThermoHygroSnmpSystemTrapManagerPort": wtWebGraphThermoHygroSnmpSystemTrapManagerPort,
       "wtWebGraphThermoHygroUDP": wtWebGraphThermoHygroUDP,
       "wtWebGraphThermoHygroUdpPort": wtWebGraphThermoHygroUdpPort,
       "wtWebGraphThermoHygroUdpEnable": wtWebGraphThermoHygroUdpEnable,
       "wtWebGraphThermoHygroSyslog": wtWebGraphThermoHygroSyslog,
       "wtWebGraphThermoHygroSyslogServerIP": wtWebGraphThermoHygroSyslogServerIP,
       "wtWebGraphThermoHygroSyslogServerPort": wtWebGraphThermoHygroSyslogServerPort,
       "wtWebGraphThermoHygroSyslogSystemMessagesEnable": wtWebGraphThermoHygroSyslogSystemMessagesEnable,
       "wtWebGraphThermoHygroSyslogEnable": wtWebGraphThermoHygroSyslogEnable,
       "wtWebGraphThermoHygroFTP": wtWebGraphThermoHygroFTP,
       "wtWebGraphThermoHygroFTPServerIP": wtWebGraphThermoHygroFTPServerIP,
       "wtWebGraphThermoHygroFTPServerControlPort": wtWebGraphThermoHygroFTPServerControlPort,
       "wtWebGraphThermoHygroFTPUserName": wtWebGraphThermoHygroFTPUserName,
       "wtWebGraphThermoHygroFTPPassword": wtWebGraphThermoHygroFTPPassword,
       "wtWebGraphThermoHygroFTPAccount": wtWebGraphThermoHygroFTPAccount,
       "wtWebGraphThermoHygroFTPOption": wtWebGraphThermoHygroFTPOption,
       "wtWebGraphThermoHygroFTPEnable": wtWebGraphThermoHygroFTPEnable,
       "wtWebGraphThermoHygroRSS": wtWebGraphThermoHygroRSS,
       "wtWebGraphThermoHygroRSSChannelTitle": wtWebGraphThermoHygroRSSChannelTitle,
       "wtWebGraphThermoHygroRSSChannelLink": wtWebGraphThermoHygroRSSChannelLink,
       "wtWebGraphThermoHygroRSSChannelDescription": wtWebGraphThermoHygroRSSChannelDescription,
       "wtWebGraphThermoHygroRSSChannelImage": wtWebGraphThermoHygroRSSChannelImage,
       "wtWebGraphThermoHygroRSSChannelImageTitle": wtWebGraphThermoHygroRSSChannelImageTitle,
       "wtWebGraphThermoHygroRSSChannelImageLink": wtWebGraphThermoHygroRSSChannelImageLink,
       "wtWebGraphThermoHygroRSSChannelItemTitle": wtWebGraphThermoHygroRSSChannelItemTitle,
       "wtWebGraphThermoHygroRSSChannelItemLink": wtWebGraphThermoHygroRSSChannelItemLink,
       "wtWebGraphThermoHygroRSSChannelItemDescription": wtWebGraphThermoHygroRSSChannelItemDescription,
       "wtWebGraphThermoHygroRSSChannelItemQuantity": wtWebGraphThermoHygroRSSChannelItemQuantity,
       "wtWebGraphThermoHygroLanguage": wtWebGraphThermoHygroLanguage,
       "wtWebGraphThermoHygroLanguageSelect": wtWebGraphThermoHygroLanguageSelect,
       "wtWebGraphThermoHygroMQTT": wtWebGraphThermoHygroMQTT,
       "wtWebGraphThermoHygroMQTTEnable": wtWebGraphThermoHygroMQTTEnable,
       "wtWebGraphThermoHygroMQTTBrockerIP": wtWebGraphThermoHygroMQTTBrockerIP,
       "wtWebGraphThermoHygroMQTTUserName": wtWebGraphThermoHygroMQTTUserName,
       "wtWebGraphThermoHygroMQTTPassword": wtWebGraphThermoHygroMQTTPassword,
       "wtWebGraphThermoHygroMQTTLocalPort": wtWebGraphThermoHygroMQTTLocalPort,
       "wtWebGraphThermoHygroMQTTBrokerServerPort": wtWebGraphThermoHygroMQTTBrokerServerPort,
       "wtWebGraphThermoHygroMQTTInterval": wtWebGraphThermoHygroMQTTInterval,
       "wtWebGraphThermoHygroMQTTLastWillEnable": wtWebGraphThermoHygroMQTTLastWillEnable,
       "wtWebGraphThermoHygroMQTTLastWillTopic": wtWebGraphThermoHygroMQTTLastWillTopic,
       "wtWebGraphThermoHygroMQTTLastWillMsg": wtWebGraphThermoHygroMQTTLastWillMsg,
       "wtWebGraphThermoHygroMQTTLastWillQoS": wtWebGraphThermoHygroMQTTLastWillQoS,
       "wtWebGraphThermoHygroMQTTLastWillRetain": wtWebGraphThermoHygroMQTTLastWillRetain,
       "wtWebGraphThermoHygroMQTTLastWillConnectEnable": wtWebGraphThermoHygroMQTTLastWillConnectEnable,
       "wtWebGraphThermoHygroMQTTLastWillConnectMsg": wtWebGraphThermoHygroMQTTLastWillConnectMsg,
       "wtWebGraphThermoHygroREST": wtWebGraphThermoHygroREST,
       "wtWebGraphThermoHygroRESTEnable": wtWebGraphThermoHygroRESTEnable,
       "wtWebGraphThermoHygroRESTDigestAuthEnable": wtWebGraphThermoHygroRESTDigestAuthEnable,
       "wtWebGraphThermoHygroDatalogger": wtWebGraphThermoHygroDatalogger,
       "wtWebGraphThermoHygroLoggerTimebase": wtWebGraphThermoHygroLoggerTimebase,
       "wtWebGraphThermoHygroLoggerSensorSel": wtWebGraphThermoHygroLoggerSensorSel,
       "wtWebGraphThermoHygroAlarm": wtWebGraphThermoHygroAlarm,
       "wtWebGraphThermoHygroAlarmCount": wtWebGraphThermoHygroAlarmCount,
       "wtWebGraphThermoHygroAlarmIfTable": wtWebGraphThermoHygroAlarmIfTable,
       "wtWebGraphThermoHygroAlarmIfEntry": wtWebGraphThermoHygroAlarmIfEntry,
       "wtWebGraphThermoHygroAlarmNo": wtWebGraphThermoHygroAlarmNo,
       "wtWebGraphThermoHygroAlarmTable": wtWebGraphThermoHygroAlarmTable,
       "wtWebGraphThermoHygroAlarmEntry": wtWebGraphThermoHygroAlarmEntry,
       "wtWebGraphThermoHygroAlarmTrigger": wtWebGraphThermoHygroAlarmTrigger,
       "wtWebGraphThermoHygroAlarmMin": wtWebGraphThermoHygroAlarmMin,
       "wtWebGraphThermoHygroAlarmMax": wtWebGraphThermoHygroAlarmMax,
       "wtWebGraphThermoHygroAlarmHysteresis": wtWebGraphThermoHygroAlarmHysteresis,
       "wtWebGraphThermoHygroAlarmDelay": wtWebGraphThermoHygroAlarmDelay,
       "wtWebGraphThermoHygroAlarmInterval": wtWebGraphThermoHygroAlarmInterval,
       "wtWebGraphThermoHygroAlarmEnable": wtWebGraphThermoHygroAlarmEnable,
       "wtWebGraphThermoHygroAlarmEMailAddr": wtWebGraphThermoHygroAlarmEMailAddr,
       "wtWebGraphThermoHygroAlarmMailSubject": wtWebGraphThermoHygroAlarmMailSubject,
       "wtWebGraphThermoHygroAlarmMailText": wtWebGraphThermoHygroAlarmMailText,
       "wtWebGraphThermoHygroAlarmManagerIP": wtWebGraphThermoHygroAlarmManagerIP,
       "wtWebGraphThermoHygroAlarmTrapText": wtWebGraphThermoHygroAlarmTrapText,
       "wtWebGraphThermoHygroAlarmMailOptions": wtWebGraphThermoHygroAlarmMailOptions,
       "wtWebGraphThermoHygroAlarmTcpIpAddr": wtWebGraphThermoHygroAlarmTcpIpAddr,
       "wtWebGraphThermoHygroAlarmTcpPort": wtWebGraphThermoHygroAlarmTcpPort,
       "wtWebGraphThermoHygroAlarmTcpText": wtWebGraphThermoHygroAlarmTcpText,
       "wtWebGraphThermoHygroAlarmClearMailSubject": wtWebGraphThermoHygroAlarmClearMailSubject,
       "wtWebGraphThermoHygroAlarmClearMailText": wtWebGraphThermoHygroAlarmClearMailText,
       "wtWebGraphThermoHygroAlarmClearTrapText": wtWebGraphThermoHygroAlarmClearTrapText,
       "wtWebGraphThermoHygroAlarmClearTcpText": wtWebGraphThermoHygroAlarmClearTcpText,
       "wtWebGraphThermoHygroAlarmDeltaTemp": wtWebGraphThermoHygroAlarmDeltaTemp,
       "wtWebGraphThermoHygroAlarmRHMin": wtWebGraphThermoHygroAlarmRHMin,
       "wtWebGraphThermoHygroAlarmRHMax": wtWebGraphThermoHygroAlarmRHMax,
       "wtWebGraphThermoHygroAlarmRHHysteresis": wtWebGraphThermoHygroAlarmRHHysteresis,
       "wtWebGraphThermoHygroAlarmAHMin": wtWebGraphThermoHygroAlarmAHMin,
       "wtWebGraphThermoHygroAlarmAHMax": wtWebGraphThermoHygroAlarmAHMax,
       "wtWebGraphThermoHygroAlarmSyslogIpAddr": wtWebGraphThermoHygroAlarmSyslogIpAddr,
       "wtWebGraphThermoHygroAlarmSyslogPort": wtWebGraphThermoHygroAlarmSyslogPort,
       "wtWebGraphThermoHygroAlarmSyslogText": wtWebGraphThermoHygroAlarmSyslogText,
       "wtWebGraphThermoHygroAlarmSyslogClearText": wtWebGraphThermoHygroAlarmSyslogClearText,
       "wtWebGraphThermoHygroAlarmFtpDataPort": wtWebGraphThermoHygroAlarmFtpDataPort,
       "wtWebGraphThermoHygroAlarmFtpFileName": wtWebGraphThermoHygroAlarmFtpFileName,
       "wtWebGraphThermoHygroAlarmFtpText": wtWebGraphThermoHygroAlarmFtpText,
       "wtWebGraphThermoHygroAlarmFtpClearText": wtWebGraphThermoHygroAlarmFtpClearText,
       "wtWebGraphThermoHygroAlarmFtpOption": wtWebGraphThermoHygroAlarmFtpOption,
       "wtWebGraphThermoHygroAlarmTimerCron": wtWebGraphThermoHygroAlarmTimerCron,
       "wtWebGraphThermoHygroAlarmName": wtWebGraphThermoHygroAlarmName,
       "wtWebGraphThermoHygroAlarmActive": wtWebGraphThermoHygroAlarmActive,
       "wtWebGraphThermoHygroAlarmHttpReqAuthEnable": wtWebGraphThermoHygroAlarmHttpReqAuthEnable,
       "wtWebGraphThermoHygroAlarmHttpReqAuthUser": wtWebGraphThermoHygroAlarmHttpReqAuthUser,
       "wtWebGraphThermoHygroAlarmHttpReqAuthPassword": wtWebGraphThermoHygroAlarmHttpReqAuthPassword,
       "wtWebGraphThermoHygroAlarmHttpReqSetUrl": wtWebGraphThermoHygroAlarmHttpReqSetUrl,
       "wtWebGraphThermoHygroAlarmHttpReqClearUrl": wtWebGraphThermoHygroAlarmHttpReqClearUrl,
       "wtWebGraphThermoHygroAlarmHttpReqServerPort": wtWebGraphThermoHygroAlarmHttpReqServerPort,
       "wtWebGraphThermoHygroAlarmMqttTopicPath": wtWebGraphThermoHygroAlarmMqttTopicPath,
       "wtWebGraphThermoHygroAlarmMqttTopicSetTopic": wtWebGraphThermoHygroAlarmMqttTopicSetTopic,
       "wtWebGraphThermoHygroAlarmMqttTopicClear": wtWebGraphThermoHygroAlarmMqttTopicClear,
       "wtWebGraphThermoHygroAlarmSensorLostSelection": wtWebGraphThermoHygroAlarmSensorLostSelection,
       "wtWebGraphThermoHygroAlarmLimitWindow": wtWebGraphThermoHygroAlarmLimitWindow,
       "wtWebGraphThermoHygroAlarmSnmpManagerPort": wtWebGraphThermoHygroAlarmSnmpManagerPort,
       "wtWebGraphThermoHygroAlarmMqttQoS": wtWebGraphThermoHygroAlarmMqttQoS,
       "wtWebGraphThermoHygroAlarmMqttRetain": wtWebGraphThermoHygroAlarmMqttRetain,
       "wtWebGraphThermoHygroGraphics": wtWebGraphThermoHygroGraphics,
       "wtWebGraphThermoHygroGraphicsBase": wtWebGraphThermoHygroGraphicsBase,
       "wtWebGraphThermoHygroGraphicsBaseEnable": wtWebGraphThermoHygroGraphicsBaseEnable,
       "wtWebGraphThermoHygroGraphicsBaseWidth": wtWebGraphThermoHygroGraphicsBaseWidth,
       "wtWebGraphThermoHygroGraphicsBaseHeight": wtWebGraphThermoHygroGraphicsBaseHeight,
       "wtWebGraphThermoHygroGraphicsBaseFrameColor": wtWebGraphThermoHygroGraphicsBaseFrameColor,
       "wtWebGraphThermoHygroGraphicsBaseBackgroundColor": wtWebGraphThermoHygroGraphicsBaseBackgroundColor,
       "wtWebGraphThermoHygroGraphicsBasePollingrate": wtWebGraphThermoHygroGraphicsBasePollingrate,
       "wtWebGraphThermoHygroGraphicsSelect": wtWebGraphThermoHygroGraphicsSelect,
       "wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel": wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel,
       "wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem": wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem,
       "wtWebGraphThermoHygroSensorColorTable": wtWebGraphThermoHygroSensorColorTable,
       "wtWebGraphThermoHygroSensorColorEntry": wtWebGraphThermoHygroSensorColorEntry,
       "wtWebGraphThermoHygroGraphicsSensorColor": wtWebGraphThermoHygroGraphicsSensorColor,
       "wtWebGraphThermoHygroGraphicsSelectScale": wtWebGraphThermoHygroGraphicsSelectScale,
       "wtWebGraphThermoHygroGraphicsScale": wtWebGraphThermoHygroGraphicsScale,
       "wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable": wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable,
       "wtWebGraphThermoHygroGraphicsScaleAutoFitEnable": wtWebGraphThermoHygroGraphicsScaleAutoFitEnable,
       "wtWebGraphThermoHygroGraphicsScale1Min": wtWebGraphThermoHygroGraphicsScale1Min,
       "wtWebGraphThermoHygroGraphicsScale2Min": wtWebGraphThermoHygroGraphicsScale2Min,
       "wtWebGraphThermoHygroGraphicsScale3Min": wtWebGraphThermoHygroGraphicsScale3Min,
       "wtWebGraphThermoHygroGraphicsScale4Min": wtWebGraphThermoHygroGraphicsScale4Min,
       "wtWebGraphThermoHygroGraphicsScale1Max": wtWebGraphThermoHygroGraphicsScale1Max,
       "wtWebGraphThermoHygroGraphicsScale2Max": wtWebGraphThermoHygroGraphicsScale2Max,
       "wtWebGraphThermoHygroGraphicsScale3Max": wtWebGraphThermoHygroGraphicsScale3Max,
       "wtWebGraphThermoHygroGraphicsScale4Max": wtWebGraphThermoHygroGraphicsScale4Max,
       "wtWebGraphThermoHygroGraphicsScale1Unit": wtWebGraphThermoHygroGraphicsScale1Unit,
       "wtWebGraphThermoHygroGraphicsScale2Unit": wtWebGraphThermoHygroGraphicsScale2Unit,
       "wtWebGraphThermoHygroGraphicsScale3Unit": wtWebGraphThermoHygroGraphicsScale3Unit,
       "wtWebGraphThermoHygroGraphicsScale4Unit": wtWebGraphThermoHygroGraphicsScale4Unit,
       "wtWebGraphThermoHygroPorts": wtWebGraphThermoHygroPorts,
       "wtWebGraphThermoHygroPortTable": wtWebGraphThermoHygroPortTable,
       "wtWebGraphThermoHygroPortEntry": wtWebGraphThermoHygroPortEntry,
       "wtWebGraphThermoHygroPortName": wtWebGraphThermoHygroPortName,
       "wtWebGraphThermoHygroPortText": wtWebGraphThermoHygroPortText,
       "wtWebGraphThermoHygroPortOffset1": wtWebGraphThermoHygroPortOffset1,
       "wtWebGraphThermoHygroPortTemperature1": wtWebGraphThermoHygroPortTemperature1,
       "wtWebGraphThermoHygroPortOffset2": wtWebGraphThermoHygroPortOffset2,
       "wtWebGraphThermoHygroPortTemperature2": wtWebGraphThermoHygroPortTemperature2,
       "wtWebGraphThermoHygroPortComment": wtWebGraphThermoHygroPortComment,
       "wtWebGraphThermoHygroPortAltidude": wtWebGraphThermoHygroPortAltidude,
       "wtWebGraphThermoHygroManufact": wtWebGraphThermoHygroManufact,
       "wtWebGraphThermoHygroMfName": wtWebGraphThermoHygroMfName,
       "wtWebGraphThermoHygroMfAddr": wtWebGraphThermoHygroMfAddr,
       "wtWebGraphThermoHygroMfHotline": wtWebGraphThermoHygroMfHotline,
       "wtWebGraphThermoHygroMfInternet": wtWebGraphThermoHygroMfInternet,
       "wtWebGraphThermoHygroMfDeviceTyp": wtWebGraphThermoHygroMfDeviceTyp,
       "wtWebGraphThermoHygroMfOrderNo": wtWebGraphThermoHygroMfOrderNo,
       "wtWebGraphThermoHygroDiag": wtWebGraphThermoHygroDiag,
       "wtWebGraphThermoHygroDiagErrorCount": wtWebGraphThermoHygroDiagErrorCount,
       "wtWebGraphThermoHygroDiagBinaryError": wtWebGraphThermoHygroDiagBinaryError,
       "wtWebGraphThermoHygroDiagErrorIndex": wtWebGraphThermoHygroDiagErrorIndex,
       "wtWebGraphThermoHygroDiagErrorMessage": wtWebGraphThermoHygroDiagErrorMessage,
       "wtWebGraphThermoHygroDiagErrorClear": wtWebGraphThermoHygroDiagErrorClear}
)
