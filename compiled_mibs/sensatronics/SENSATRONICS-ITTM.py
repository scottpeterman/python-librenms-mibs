# SNMP MIB module (SENSATRONICS-ITTM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sensatronics\SENSATRONICS-ITTM
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:25 2025
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

(envMonitors,) = mibBuilder.importSymbols(
    "SENSATRONICS-SMI",
    "envMonitors")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

productITTM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1)
)
if mibBuilder.loadTexts:
    productITTM.setRevisions(
        ("2004-02-23 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UnitInfo_ObjectIdentity = ObjectIdentity
unitInfo = _UnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1)
)


class _UnitName_Type(DisplayString):
    """Custom type unitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_UnitName_Type.__name__ = "DisplayString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 1),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")


class _UnitModel_Type(DisplayString):
    """Custom type unitModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UnitModel_Type.__name__ = "DisplayString"
_UnitModel_Object = MibScalar
unitModel = _UnitModel_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 2),
    _UnitModel_Type()
)
unitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitModel.setStatus("current")


class _UnitManufacturer_Type(DisplayString):
    """Custom type unitManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_UnitManufacturer_Type.__name__ = "DisplayString"
_UnitManufacturer_Object = MibScalar
unitManufacturer = _UnitManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 3),
    _UnitManufacturer_Type()
)
unitManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitManufacturer.setStatus("current")


class _UnitWeb_Type(DisplayString):
    """Custom type unitWeb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )
    fixed_length = 28


_UnitWeb_Type.__name__ = "DisplayString"
_UnitWeb_Object = MibScalar
unitWeb = _UnitWeb_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 4),
    _UnitWeb_Type()
)
unitWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitWeb.setStatus("current")


class _UnitFirmware_Type(DisplayString):
    """Custom type unitFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UnitFirmware_Type.__name__ = "DisplayString"
_UnitFirmware_Object = MibScalar
unitFirmware = _UnitFirmware_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 5),
    _UnitFirmware_Type()
)
unitFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitFirmware.setStatus("current")


class _UnitFWReleaseDate_Type(DisplayString):
    """Custom type unitFWReleaseDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )
    fixed_length = 18


_UnitFWReleaseDate_Type.__name__ = "DisplayString"
_UnitFWReleaseDate_Object = MibScalar
unitFWReleaseDate = _UnitFWReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 6),
    _UnitFWReleaseDate_Type()
)
unitFWReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitFWReleaseDate.setStatus("current")


class _UnitSerial_Type(DisplayString):
    """Custom type unitSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_UnitSerial_Type.__name__ = "DisplayString"
_UnitSerial_Object = MibScalar
unitSerial = _UnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 7),
    _UnitSerial_Type()
)
unitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSerial.setStatus("current")


class _UnitConfig_Type(Integer32):
    """Custom type unitConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UnitConfig_Type.__name__ = "Integer32"
_UnitConfig_Object = MibScalar
unitConfig = _UnitConfig_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 8),
    _UnitConfig_Type()
)
unitConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitConfig.setStatus("current")
_ConfigData_ObjectIdentity = ObjectIdentity
configData = _ConfigData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2)
)
_NetInfo_ObjectIdentity = ObjectIdentity
netInfo = _NetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1)
)


class _NetMode_Type(Integer32):
    """Custom type netMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetMode_Type.__name__ = "Integer32"
_NetMode_Object = MibScalar
netMode = _NetMode_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 1),
    _NetMode_Type()
)
netMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMode.setStatus("current")


class _NetIP_Type(DisplayString):
    """Custom type netIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NetIP_Type.__name__ = "DisplayString"
_NetIP_Object = MibScalar
netIP = _NetIP_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 2),
    _NetIP_Type()
)
netIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIP.setStatus("current")


class _NetNM_Type(DisplayString):
    """Custom type netNM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NetNM_Type.__name__ = "DisplayString"
_NetNM_Object = MibScalar
netNM = _NetNM_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 3),
    _NetNM_Type()
)
netNM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netNM.setStatus("current")


class _NetGW_Type(DisplayString):
    """Custom type netGW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NetGW_Type.__name__ = "DisplayString"
_NetGW_Object = MibScalar
netGW = _NetGW_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 4),
    _NetGW_Type()
)
netGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netGW.setStatus("current")


class _NetHTTPPort_Type(Integer32):
    """Custom type netHTTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetHTTPPort_Type.__name__ = "Integer32"
_NetHTTPPort_Object = MibScalar
netHTTPPort = _NetHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 5),
    _NetHTTPPort_Type()
)
netHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netHTTPPort.setStatus("current")
_TrapConfig_ObjectIdentity = ObjectIdentity
trapConfig = _TrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2)
)
_ManagerConfig_ObjectIdentity = ObjectIdentity
managerConfig = _ManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1)
)


class _ManagerIP_Type(DisplayString):
    """Custom type managerIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ManagerIP_Type.__name__ = "DisplayString"
_ManagerIP_Object = MibScalar
managerIP = _ManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1, 1),
    _ManagerIP_Type()
)
managerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIP.setStatus("current")
_MeasurementSystem_ObjectIdentity = ObjectIdentity
measurementSystem = _MeasurementSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3)
)


class _UnitMode_Type(Integer32):
    """Custom type unitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UnitMode_Type.__name__ = "Integer32"
_UnitMode_Object = MibScalar
unitMode = _UnitMode_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3, 1),
    _UnitMode_Type()
)
unitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitMode.setStatus("current")
_SensorInfo_ObjectIdentity = ObjectIdentity
sensorInfo = _SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3)
)
_Sensor1_ObjectIdentity = ObjectIdentity
sensor1 = _Sensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1)
)


class _Sensor1Name_Type(DisplayString):
    """Custom type sensor1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor1Name_Type.__name__ = "DisplayString"
_Sensor1Name_Object = MibScalar
sensor1Name = _Sensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 1),
    _Sensor1Name_Type()
)
sensor1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor1Name.setStatus("current")


class _Sensor1DataStr_Type(DisplayString):
    """Custom type sensor1DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor1DataStr_Type.__name__ = "DisplayString"
_Sensor1DataStr_Object = MibScalar
sensor1DataStr = _Sensor1DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 2),
    _Sensor1DataStr_Type()
)
sensor1DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor1DataStr.setStatus("current")


class _Sensor1DataInt_Type(Integer32):
    """Custom type sensor1DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor1DataInt_Type.__name__ = "Integer32"
_Sensor1DataInt_Object = MibScalar
sensor1DataInt = _Sensor1DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 3),
    _Sensor1DataInt_Type()
)
sensor1DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor1DataInt.setStatus("current")
_Sensor2_ObjectIdentity = ObjectIdentity
sensor2 = _Sensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2)
)


class _Sensor2Name_Type(DisplayString):
    """Custom type sensor2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor2Name_Type.__name__ = "DisplayString"
_Sensor2Name_Object = MibScalar
sensor2Name = _Sensor2Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 1),
    _Sensor2Name_Type()
)
sensor2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor2Name.setStatus("current")


class _Sensor2DataStr_Type(DisplayString):
    """Custom type sensor2DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor2DataStr_Type.__name__ = "DisplayString"
_Sensor2DataStr_Object = MibScalar
sensor2DataStr = _Sensor2DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 2),
    _Sensor2DataStr_Type()
)
sensor2DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor2DataStr.setStatus("current")


class _Sensor2DataInt_Type(Integer32):
    """Custom type sensor2DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor2DataInt_Type.__name__ = "Integer32"
_Sensor2DataInt_Object = MibScalar
sensor2DataInt = _Sensor2DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 3),
    _Sensor2DataInt_Type()
)
sensor2DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor2DataInt.setStatus("current")
_Sensor3_ObjectIdentity = ObjectIdentity
sensor3 = _Sensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3)
)


class _Sensor3Name_Type(DisplayString):
    """Custom type sensor3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor3Name_Type.__name__ = "DisplayString"
_Sensor3Name_Object = MibScalar
sensor3Name = _Sensor3Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 1),
    _Sensor3Name_Type()
)
sensor3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor3Name.setStatus("current")


class _Sensor3DataStr_Type(DisplayString):
    """Custom type sensor3DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor3DataStr_Type.__name__ = "DisplayString"
_Sensor3DataStr_Object = MibScalar
sensor3DataStr = _Sensor3DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 2),
    _Sensor3DataStr_Type()
)
sensor3DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor3DataStr.setStatus("current")


class _Sensor3DataInt_Type(Integer32):
    """Custom type sensor3DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor3DataInt_Type.__name__ = "Integer32"
_Sensor3DataInt_Object = MibScalar
sensor3DataInt = _Sensor3DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 3),
    _Sensor3DataInt_Type()
)
sensor3DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor3DataInt.setStatus("current")
_Sensor4_ObjectIdentity = ObjectIdentity
sensor4 = _Sensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4)
)


class _Sensor4Name_Type(DisplayString):
    """Custom type sensor4Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor4Name_Type.__name__ = "DisplayString"
_Sensor4Name_Object = MibScalar
sensor4Name = _Sensor4Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 1),
    _Sensor4Name_Type()
)
sensor4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor4Name.setStatus("current")


class _Sensor4DataStr_Type(DisplayString):
    """Custom type sensor4DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor4DataStr_Type.__name__ = "DisplayString"
_Sensor4DataStr_Object = MibScalar
sensor4DataStr = _Sensor4DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 2),
    _Sensor4DataStr_Type()
)
sensor4DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor4DataStr.setStatus("current")


class _Sensor4DataInt_Type(Integer32):
    """Custom type sensor4DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor4DataInt_Type.__name__ = "Integer32"
_Sensor4DataInt_Object = MibScalar
sensor4DataInt = _Sensor4DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 3),
    _Sensor4DataInt_Type()
)
sensor4DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor4DataInt.setStatus("current")
_Sensor5_ObjectIdentity = ObjectIdentity
sensor5 = _Sensor5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5)
)


class _Sensor5Name_Type(DisplayString):
    """Custom type sensor5Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor5Name_Type.__name__ = "DisplayString"
_Sensor5Name_Object = MibScalar
sensor5Name = _Sensor5Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 1),
    _Sensor5Name_Type()
)
sensor5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor5Name.setStatus("current")


class _Sensor5DataStr_Type(DisplayString):
    """Custom type sensor5DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor5DataStr_Type.__name__ = "DisplayString"
_Sensor5DataStr_Object = MibScalar
sensor5DataStr = _Sensor5DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 2),
    _Sensor5DataStr_Type()
)
sensor5DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor5DataStr.setStatus("current")


class _Sensor5DataInt_Type(Integer32):
    """Custom type sensor5DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor5DataInt_Type.__name__ = "Integer32"
_Sensor5DataInt_Object = MibScalar
sensor5DataInt = _Sensor5DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 3),
    _Sensor5DataInt_Type()
)
sensor5DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor5DataInt.setStatus("current")
_Sensor6_ObjectIdentity = ObjectIdentity
sensor6 = _Sensor6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6)
)


class _Sensor6Name_Type(DisplayString):
    """Custom type sensor6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor6Name_Type.__name__ = "DisplayString"
_Sensor6Name_Object = MibScalar
sensor6Name = _Sensor6Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 1),
    _Sensor6Name_Type()
)
sensor6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor6Name.setStatus("current")


class _Sensor6DataStr_Type(DisplayString):
    """Custom type sensor6DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor6DataStr_Type.__name__ = "DisplayString"
_Sensor6DataStr_Object = MibScalar
sensor6DataStr = _Sensor6DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 2),
    _Sensor6DataStr_Type()
)
sensor6DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor6DataStr.setStatus("current")


class _Sensor6DataInt_Type(Integer32):
    """Custom type sensor6DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor6DataInt_Type.__name__ = "Integer32"
_Sensor6DataInt_Object = MibScalar
sensor6DataInt = _Sensor6DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 3),
    _Sensor6DataInt_Type()
)
sensor6DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor6DataInt.setStatus("current")
_Sensor7_ObjectIdentity = ObjectIdentity
sensor7 = _Sensor7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7)
)


class _Sensor7Name_Type(DisplayString):
    """Custom type sensor7Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor7Name_Type.__name__ = "DisplayString"
_Sensor7Name_Object = MibScalar
sensor7Name = _Sensor7Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 1),
    _Sensor7Name_Type()
)
sensor7Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor7Name.setStatus("current")


class _Sensor7DataStr_Type(DisplayString):
    """Custom type sensor7DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor7DataStr_Type.__name__ = "DisplayString"
_Sensor7DataStr_Object = MibScalar
sensor7DataStr = _Sensor7DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 2),
    _Sensor7DataStr_Type()
)
sensor7DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor7DataStr.setStatus("current")


class _Sensor7DataInt_Type(Integer32):
    """Custom type sensor7DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor7DataInt_Type.__name__ = "Integer32"
_Sensor7DataInt_Object = MibScalar
sensor7DataInt = _Sensor7DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 3),
    _Sensor7DataInt_Type()
)
sensor7DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor7DataInt.setStatus("current")
_Sensor8_ObjectIdentity = ObjectIdentity
sensor8 = _Sensor8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8)
)


class _Sensor8Name_Type(DisplayString):
    """Custom type sensor8Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor8Name_Type.__name__ = "DisplayString"
_Sensor8Name_Object = MibScalar
sensor8Name = _Sensor8Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 1),
    _Sensor8Name_Type()
)
sensor8Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor8Name.setStatus("current")


class _Sensor8DataStr_Type(DisplayString):
    """Custom type sensor8DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor8DataStr_Type.__name__ = "DisplayString"
_Sensor8DataStr_Object = MibScalar
sensor8DataStr = _Sensor8DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 2),
    _Sensor8DataStr_Type()
)
sensor8DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor8DataStr.setStatus("current")


class _Sensor8DataInt_Type(Integer32):
    """Custom type sensor8DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor8DataInt_Type.__name__ = "Integer32"
_Sensor8DataInt_Object = MibScalar
sensor8DataInt = _Sensor8DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 3),
    _Sensor8DataInt_Type()
)
sensor8DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor8DataInt.setStatus("current")
_Sensor9_ObjectIdentity = ObjectIdentity
sensor9 = _Sensor9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9)
)


class _Sensor9Name_Type(DisplayString):
    """Custom type sensor9Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor9Name_Type.__name__ = "DisplayString"
_Sensor9Name_Object = MibScalar
sensor9Name = _Sensor9Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 1),
    _Sensor9Name_Type()
)
sensor9Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor9Name.setStatus("current")


class _Sensor9DataStr_Type(DisplayString):
    """Custom type sensor9DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor9DataStr_Type.__name__ = "DisplayString"
_Sensor9DataStr_Object = MibScalar
sensor9DataStr = _Sensor9DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 2),
    _Sensor9DataStr_Type()
)
sensor9DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor9DataStr.setStatus("current")


class _Sensor9DataInt_Type(Integer32):
    """Custom type sensor9DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor9DataInt_Type.__name__ = "Integer32"
_Sensor9DataInt_Object = MibScalar
sensor9DataInt = _Sensor9DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 3),
    _Sensor9DataInt_Type()
)
sensor9DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor9DataInt.setStatus("current")
_Sensor10_ObjectIdentity = ObjectIdentity
sensor10 = _Sensor10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10)
)


class _Sensor10Name_Type(DisplayString):
    """Custom type sensor10Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor10Name_Type.__name__ = "DisplayString"
_Sensor10Name_Object = MibScalar
sensor10Name = _Sensor10Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 1),
    _Sensor10Name_Type()
)
sensor10Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor10Name.setStatus("current")


class _Sensor10DataStr_Type(DisplayString):
    """Custom type sensor10DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor10DataStr_Type.__name__ = "DisplayString"
_Sensor10DataStr_Object = MibScalar
sensor10DataStr = _Sensor10DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 2),
    _Sensor10DataStr_Type()
)
sensor10DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor10DataStr.setStatus("current")


class _Sensor10DataInt_Type(Integer32):
    """Custom type sensor10DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor10DataInt_Type.__name__ = "Integer32"
_Sensor10DataInt_Object = MibScalar
sensor10DataInt = _Sensor10DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 3),
    _Sensor10DataInt_Type()
)
sensor10DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor10DataInt.setStatus("current")
_Sensor11_ObjectIdentity = ObjectIdentity
sensor11 = _Sensor11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11)
)


class _Sensor11Name_Type(DisplayString):
    """Custom type sensor11Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor11Name_Type.__name__ = "DisplayString"
_Sensor11Name_Object = MibScalar
sensor11Name = _Sensor11Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 1),
    _Sensor11Name_Type()
)
sensor11Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor11Name.setStatus("current")


class _Sensor11DataStr_Type(DisplayString):
    """Custom type sensor11DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor11DataStr_Type.__name__ = "DisplayString"
_Sensor11DataStr_Object = MibScalar
sensor11DataStr = _Sensor11DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 2),
    _Sensor11DataStr_Type()
)
sensor11DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor11DataStr.setStatus("current")


class _Sensor11DataInt_Type(Integer32):
    """Custom type sensor11DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor11DataInt_Type.__name__ = "Integer32"
_Sensor11DataInt_Object = MibScalar
sensor11DataInt = _Sensor11DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 3),
    _Sensor11DataInt_Type()
)
sensor11DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor11DataInt.setStatus("current")
_Sensor12_ObjectIdentity = ObjectIdentity
sensor12 = _Sensor12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12)
)


class _Sensor12Name_Type(DisplayString):
    """Custom type sensor12Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor12Name_Type.__name__ = "DisplayString"
_Sensor12Name_Object = MibScalar
sensor12Name = _Sensor12Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 1),
    _Sensor12Name_Type()
)
sensor12Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor12Name.setStatus("current")


class _Sensor12DataStr_Type(DisplayString):
    """Custom type sensor12DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor12DataStr_Type.__name__ = "DisplayString"
_Sensor12DataStr_Object = MibScalar
sensor12DataStr = _Sensor12DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 2),
    _Sensor12DataStr_Type()
)
sensor12DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor12DataStr.setStatus("current")


class _Sensor12DataInt_Type(Integer32):
    """Custom type sensor12DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor12DataInt_Type.__name__ = "Integer32"
_Sensor12DataInt_Object = MibScalar
sensor12DataInt = _Sensor12DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 3),
    _Sensor12DataInt_Type()
)
sensor12DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor12DataInt.setStatus("current")
_Sensor13_ObjectIdentity = ObjectIdentity
sensor13 = _Sensor13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13)
)


class _Sensor13Name_Type(DisplayString):
    """Custom type sensor13Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor13Name_Type.__name__ = "DisplayString"
_Sensor13Name_Object = MibScalar
sensor13Name = _Sensor13Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 1),
    _Sensor13Name_Type()
)
sensor13Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor13Name.setStatus("current")


class _Sensor13DataStr_Type(DisplayString):
    """Custom type sensor13DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor13DataStr_Type.__name__ = "DisplayString"
_Sensor13DataStr_Object = MibScalar
sensor13DataStr = _Sensor13DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 2),
    _Sensor13DataStr_Type()
)
sensor13DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor13DataStr.setStatus("current")


class _Sensor13DataInt_Type(Integer32):
    """Custom type sensor13DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor13DataInt_Type.__name__ = "Integer32"
_Sensor13DataInt_Object = MibScalar
sensor13DataInt = _Sensor13DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 3),
    _Sensor13DataInt_Type()
)
sensor13DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor13DataInt.setStatus("current")
_Sensor14_ObjectIdentity = ObjectIdentity
sensor14 = _Sensor14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14)
)


class _Sensor14Name_Type(DisplayString):
    """Custom type sensor14Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor14Name_Type.__name__ = "DisplayString"
_Sensor14Name_Object = MibScalar
sensor14Name = _Sensor14Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 1),
    _Sensor14Name_Type()
)
sensor14Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor14Name.setStatus("current")


class _Sensor14DataStr_Type(DisplayString):
    """Custom type sensor14DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor14DataStr_Type.__name__ = "DisplayString"
_Sensor14DataStr_Object = MibScalar
sensor14DataStr = _Sensor14DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 2),
    _Sensor14DataStr_Type()
)
sensor14DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor14DataStr.setStatus("current")


class _Sensor14DataInt_Type(Integer32):
    """Custom type sensor14DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor14DataInt_Type.__name__ = "Integer32"
_Sensor14DataInt_Object = MibScalar
sensor14DataInt = _Sensor14DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 3),
    _Sensor14DataInt_Type()
)
sensor14DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor14DataInt.setStatus("current")
_Sensor15_ObjectIdentity = ObjectIdentity
sensor15 = _Sensor15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15)
)


class _Sensor15Name_Type(DisplayString):
    """Custom type sensor15Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor15Name_Type.__name__ = "DisplayString"
_Sensor15Name_Object = MibScalar
sensor15Name = _Sensor15Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 1),
    _Sensor15Name_Type()
)
sensor15Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor15Name.setStatus("current")


class _Sensor15DataStr_Type(DisplayString):
    """Custom type sensor15DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor15DataStr_Type.__name__ = "DisplayString"
_Sensor15DataStr_Object = MibScalar
sensor15DataStr = _Sensor15DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 2),
    _Sensor15DataStr_Type()
)
sensor15DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor15DataStr.setStatus("current")


class _Sensor15DataInt_Type(Integer32):
    """Custom type sensor15DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor15DataInt_Type.__name__ = "Integer32"
_Sensor15DataInt_Object = MibScalar
sensor15DataInt = _Sensor15DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 3),
    _Sensor15DataInt_Type()
)
sensor15DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor15DataInt.setStatus("current")
_Sensor16_ObjectIdentity = ObjectIdentity
sensor16 = _Sensor16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16)
)


class _Sensor16Name_Type(DisplayString):
    """Custom type sensor16Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor16Name_Type.__name__ = "DisplayString"
_Sensor16Name_Object = MibScalar
sensor16Name = _Sensor16Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 1),
    _Sensor16Name_Type()
)
sensor16Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor16Name.setStatus("current")


class _Sensor16DataStr_Type(DisplayString):
    """Custom type sensor16DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor16DataStr_Type.__name__ = "DisplayString"
_Sensor16DataStr_Object = MibScalar
sensor16DataStr = _Sensor16DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 2),
    _Sensor16DataStr_Type()
)
sensor16DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor16DataStr.setStatus("current")


class _Sensor16DataInt_Type(Integer32):
    """Custom type sensor16DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor16DataInt_Type.__name__ = "Integer32"
_Sensor16DataInt_Object = MibScalar
sensor16DataInt = _Sensor16DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 3),
    _Sensor16DataInt_Type()
)
sensor16DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor16DataInt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSATRONICS-ITTM",
    **{"productITTM": productITTM,
       "unitInfo": unitInfo,
       "unitName": unitName,
       "unitModel": unitModel,
       "unitManufacturer": unitManufacturer,
       "unitWeb": unitWeb,
       "unitFirmware": unitFirmware,
       "unitFWReleaseDate": unitFWReleaseDate,
       "unitSerial": unitSerial,
       "unitConfig": unitConfig,
       "configData": configData,
       "netInfo": netInfo,
       "netMode": netMode,
       "netIP": netIP,
       "netNM": netNM,
       "netGW": netGW,
       "netHTTPPort": netHTTPPort,
       "trapConfig": trapConfig,
       "managerConfig": managerConfig,
       "managerIP": managerIP,
       "measurementSystem": measurementSystem,
       "unitMode": unitMode,
       "sensorInfo": sensorInfo,
       "sensor1": sensor1,
       "sensor1Name": sensor1Name,
       "sensor1DataStr": sensor1DataStr,
       "sensor1DataInt": sensor1DataInt,
       "sensor2": sensor2,
       "sensor2Name": sensor2Name,
       "sensor2DataStr": sensor2DataStr,
       "sensor2DataInt": sensor2DataInt,
       "sensor3": sensor3,
       "sensor3Name": sensor3Name,
       "sensor3DataStr": sensor3DataStr,
       "sensor3DataInt": sensor3DataInt,
       "sensor4": sensor4,
       "sensor4Name": sensor4Name,
       "sensor4DataStr": sensor4DataStr,
       "sensor4DataInt": sensor4DataInt,
       "sensor5": sensor5,
       "sensor5Name": sensor5Name,
       "sensor5DataStr": sensor5DataStr,
       "sensor5DataInt": sensor5DataInt,
       "sensor6": sensor6,
       "sensor6Name": sensor6Name,
       "sensor6DataStr": sensor6DataStr,
       "sensor6DataInt": sensor6DataInt,
       "sensor7": sensor7,
       "sensor7Name": sensor7Name,
       "sensor7DataStr": sensor7DataStr,
       "sensor7DataInt": sensor7DataInt,
       "sensor8": sensor8,
       "sensor8Name": sensor8Name,
       "sensor8DataStr": sensor8DataStr,
       "sensor8DataInt": sensor8DataInt,
       "sensor9": sensor9,
       "sensor9Name": sensor9Name,
       "sensor9DataStr": sensor9DataStr,
       "sensor9DataInt": sensor9DataInt,
       "sensor10": sensor10,
       "sensor10Name": sensor10Name,
       "sensor10DataStr": sensor10DataStr,
       "sensor10DataInt": sensor10DataInt,
       "sensor11": sensor11,
       "sensor11Name": sensor11Name,
       "sensor11DataStr": sensor11DataStr,
       "sensor11DataInt": sensor11DataInt,
       "sensor12": sensor12,
       "sensor12Name": sensor12Name,
       "sensor12DataStr": sensor12DataStr,
       "sensor12DataInt": sensor12DataInt,
       "sensor13": sensor13,
       "sensor13Name": sensor13Name,
       "sensor13DataStr": sensor13DataStr,
       "sensor13DataInt": sensor13DataInt,
       "sensor14": sensor14,
       "sensor14Name": sensor14Name,
       "sensor14DataStr": sensor14DataStr,
       "sensor14DataInt": sensor14DataInt,
       "sensor15": sensor15,
       "sensor15Name": sensor15Name,
       "sensor15DataStr": sensor15DataStr,
       "sensor15DataInt": sensor15DataInt,
       "sensor16": sensor16,
       "sensor16Name": sensor16Name,
       "sensor16DataStr": sensor16DataStr,
       "sensor16DataInt": sensor16DataInt}
)
