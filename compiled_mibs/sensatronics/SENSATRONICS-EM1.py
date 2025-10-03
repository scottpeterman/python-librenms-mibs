# SNMP MIB module (SENSATRONICS-EM1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sensatronics\SENSATRONICS-EM1
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:23 2025
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

productEM1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3)
)
if mibBuilder.loadTexts:
    productEM1.setRevisions(
        ("2004-09-13 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UnitInfo_ObjectIdentity = ObjectIdentity
unitInfo = _UnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1)
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 8),
    _UnitConfig_Type()
)
unitConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitConfig.setStatus("current")
_ConfigData_ObjectIdentity = ObjectIdentity
configData = _ConfigData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2)
)
_NetInfo_ObjectIdentity = ObjectIdentity
netInfo = _NetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 5),
    _NetHTTPPort_Type()
)
netHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netHTTPPort.setStatus("current")
_TrapConfig_ObjectIdentity = ObjectIdentity
trapConfig = _TrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2)
)
_ManagerConfig_ObjectIdentity = ObjectIdentity
managerConfig = _ManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2, 1, 1),
    _ManagerIP_Type()
)
managerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIP.setStatus("current")
_MeasurementSystem_ObjectIdentity = ObjectIdentity
measurementSystem = _MeasurementSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 3)
)


class _UnitMode_Type(DisplayString):
    """Custom type unitMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UnitMode_Type.__name__ = "DisplayString"
_UnitMode_Object = MibScalar
unitMode = _UnitMode_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 3, 1),
    _UnitMode_Type()
)
unitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitMode.setStatus("current")
_SensorInfo_ObjectIdentity = ObjectIdentity
sensorInfo = _SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3)
)
_Group1_ObjectIdentity = ObjectIdentity
group1 = _Group1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1)
)


class _Group1Name_Type(DisplayString):
    """Custom type group1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1Name_Type.__name__ = "DisplayString"
_Group1Name_Object = MibScalar
group1Name = _Group1Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 1),
    _Group1Name_Type()
)
group1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1Name.setStatus("current")


class _Group1TempName_Type(DisplayString):
    """Custom type group1TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1TempName_Type.__name__ = "DisplayString"
_Group1TempName_Object = MibScalar
group1TempName = _Group1TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 2),
    _Group1TempName_Type()
)
group1TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1TempName.setStatus("current")


class _Group1TempDataStr_Type(DisplayString):
    """Custom type group1TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group1TempDataStr_Type.__name__ = "DisplayString"
_Group1TempDataStr_Object = MibScalar
group1TempDataStr = _Group1TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 3),
    _Group1TempDataStr_Type()
)
group1TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1TempDataStr.setStatus("current")


class _Group1TempDataInt_Type(Integer32):
    """Custom type group1TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group1TempDataInt_Type.__name__ = "Integer32"
_Group1TempDataInt_Object = MibScalar
group1TempDataInt = _Group1TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 4),
    _Group1TempDataInt_Type()
)
group1TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1TempDataInt.setStatus("current")


class _Group1HumidName_Type(DisplayString):
    """Custom type group1HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1HumidName_Type.__name__ = "DisplayString"
_Group1HumidName_Object = MibScalar
group1HumidName = _Group1HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 5),
    _Group1HumidName_Type()
)
group1HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1HumidName.setStatus("current")


class _Group1HumidDataStr_Type(DisplayString):
    """Custom type group1HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group1HumidDataStr_Type.__name__ = "DisplayString"
_Group1HumidDataStr_Object = MibScalar
group1HumidDataStr = _Group1HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 6),
    _Group1HumidDataStr_Type()
)
group1HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1HumidDataStr.setStatus("current")


class _Group1HumidDataInt_Type(Integer32):
    """Custom type group1HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group1HumidDataInt_Type.__name__ = "Integer32"
_Group1HumidDataInt_Object = MibScalar
group1HumidDataInt = _Group1HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 7),
    _Group1HumidDataInt_Type()
)
group1HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1HumidDataInt.setStatus("current")


class _Group1WetName_Type(DisplayString):
    """Custom type group1WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1WetName_Type.__name__ = "DisplayString"
_Group1WetName_Object = MibScalar
group1WetName = _Group1WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 8),
    _Group1WetName_Type()
)
group1WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1WetName.setStatus("current")


class _Group1WetDataStr_Type(DisplayString):
    """Custom type group1WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group1WetDataStr_Type.__name__ = "DisplayString"
_Group1WetDataStr_Object = MibScalar
group1WetDataStr = _Group1WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 9),
    _Group1WetDataStr_Type()
)
group1WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1WetDataStr.setStatus("current")


class _Group1WetDataInt_Type(Integer32):
    """Custom type group1WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group1WetDataInt_Type.__name__ = "Integer32"
_Group1WetDataInt_Object = MibScalar
group1WetDataInt = _Group1WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 10),
    _Group1WetDataInt_Type()
)
group1WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1WetDataInt.setStatus("current")
_Group2_ObjectIdentity = ObjectIdentity
group2 = _Group2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2)
)


class _Group2Name_Type(DisplayString):
    """Custom type group2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2Name_Type.__name__ = "DisplayString"
_Group2Name_Object = MibScalar
group2Name = _Group2Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 1),
    _Group2Name_Type()
)
group2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2Name.setStatus("current")


class _Group2TempName_Type(DisplayString):
    """Custom type group2TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2TempName_Type.__name__ = "DisplayString"
_Group2TempName_Object = MibScalar
group2TempName = _Group2TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 2),
    _Group2TempName_Type()
)
group2TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2TempName.setStatus("current")


class _Group2TempDataStr_Type(DisplayString):
    """Custom type group2TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group2TempDataStr_Type.__name__ = "DisplayString"
_Group2TempDataStr_Object = MibScalar
group2TempDataStr = _Group2TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 3),
    _Group2TempDataStr_Type()
)
group2TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2TempDataStr.setStatus("current")


class _Group2TempDataInt_Type(Integer32):
    """Custom type group2TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group2TempDataInt_Type.__name__ = "Integer32"
_Group2TempDataInt_Object = MibScalar
group2TempDataInt = _Group2TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 4),
    _Group2TempDataInt_Type()
)
group2TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2TempDataInt.setStatus("current")


class _Group2HumidName_Type(DisplayString):
    """Custom type group2HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2HumidName_Type.__name__ = "DisplayString"
_Group2HumidName_Object = MibScalar
group2HumidName = _Group2HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 5),
    _Group2HumidName_Type()
)
group2HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2HumidName.setStatus("current")


class _Group2HumidDataStr_Type(DisplayString):
    """Custom type group2HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group2HumidDataStr_Type.__name__ = "DisplayString"
_Group2HumidDataStr_Object = MibScalar
group2HumidDataStr = _Group2HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 6),
    _Group2HumidDataStr_Type()
)
group2HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2HumidDataStr.setStatus("current")


class _Group2HumidDataInt_Type(Integer32):
    """Custom type group2HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group2HumidDataInt_Type.__name__ = "Integer32"
_Group2HumidDataInt_Object = MibScalar
group2HumidDataInt = _Group2HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 7),
    _Group2HumidDataInt_Type()
)
group2HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2HumidDataInt.setStatus("current")


class _Group2WetName_Type(DisplayString):
    """Custom type group2WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2WetName_Type.__name__ = "DisplayString"
_Group2WetName_Object = MibScalar
group2WetName = _Group2WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 8),
    _Group2WetName_Type()
)
group2WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2WetName.setStatus("current")


class _Group2WetDataStr_Type(DisplayString):
    """Custom type group2WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group2WetDataStr_Type.__name__ = "DisplayString"
_Group2WetDataStr_Object = MibScalar
group2WetDataStr = _Group2WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 9),
    _Group2WetDataStr_Type()
)
group2WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2WetDataStr.setStatus("current")


class _Group2WetDataInt_Type(Integer32):
    """Custom type group2WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group2WetDataInt_Type.__name__ = "Integer32"
_Group2WetDataInt_Object = MibScalar
group2WetDataInt = _Group2WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 10),
    _Group2WetDataInt_Type()
)
group2WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2WetDataInt.setStatus("current")
_Group3_ObjectIdentity = ObjectIdentity
group3 = _Group3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3)
)


class _Group3Name_Type(DisplayString):
    """Custom type group3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3Name_Type.__name__ = "DisplayString"
_Group3Name_Object = MibScalar
group3Name = _Group3Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 1),
    _Group3Name_Type()
)
group3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3Name.setStatus("current")


class _Group3TempName_Type(DisplayString):
    """Custom type group3TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3TempName_Type.__name__ = "DisplayString"
_Group3TempName_Object = MibScalar
group3TempName = _Group3TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 2),
    _Group3TempName_Type()
)
group3TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3TempName.setStatus("current")


class _Group3TempDataStr_Type(DisplayString):
    """Custom type group3TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group3TempDataStr_Type.__name__ = "DisplayString"
_Group3TempDataStr_Object = MibScalar
group3TempDataStr = _Group3TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 3),
    _Group3TempDataStr_Type()
)
group3TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3TempDataStr.setStatus("current")


class _Group3TempDataInt_Type(Integer32):
    """Custom type group3TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group3TempDataInt_Type.__name__ = "Integer32"
_Group3TempDataInt_Object = MibScalar
group3TempDataInt = _Group3TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 4),
    _Group3TempDataInt_Type()
)
group3TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3TempDataInt.setStatus("current")


class _Group3HumidName_Type(DisplayString):
    """Custom type group3HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3HumidName_Type.__name__ = "DisplayString"
_Group3HumidName_Object = MibScalar
group3HumidName = _Group3HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 5),
    _Group3HumidName_Type()
)
group3HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3HumidName.setStatus("current")


class _Group3HumidDataStr_Type(DisplayString):
    """Custom type group3HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group3HumidDataStr_Type.__name__ = "DisplayString"
_Group3HumidDataStr_Object = MibScalar
group3HumidDataStr = _Group3HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 6),
    _Group3HumidDataStr_Type()
)
group3HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3HumidDataStr.setStatus("current")


class _Group3HumidDataInt_Type(Integer32):
    """Custom type group3HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group3HumidDataInt_Type.__name__ = "Integer32"
_Group3HumidDataInt_Object = MibScalar
group3HumidDataInt = _Group3HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 7),
    _Group3HumidDataInt_Type()
)
group3HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3HumidDataInt.setStatus("current")


class _Group3WetName_Type(DisplayString):
    """Custom type group3WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3WetName_Type.__name__ = "DisplayString"
_Group3WetName_Object = MibScalar
group3WetName = _Group3WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 8),
    _Group3WetName_Type()
)
group3WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3WetName.setStatus("current")


class _Group3WetDataStr_Type(DisplayString):
    """Custom type group3WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group3WetDataStr_Type.__name__ = "DisplayString"
_Group3WetDataStr_Object = MibScalar
group3WetDataStr = _Group3WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 9),
    _Group3WetDataStr_Type()
)
group3WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3WetDataStr.setStatus("current")


class _Group3WetDataInt_Type(Integer32):
    """Custom type group3WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group3WetDataInt_Type.__name__ = "Integer32"
_Group3WetDataInt_Object = MibScalar
group3WetDataInt = _Group3WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 10),
    _Group3WetDataInt_Type()
)
group3WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3WetDataInt.setStatus("current")
_Group4_ObjectIdentity = ObjectIdentity
group4 = _Group4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4)
)


class _Group4Name_Type(DisplayString):
    """Custom type group4Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4Name_Type.__name__ = "DisplayString"
_Group4Name_Object = MibScalar
group4Name = _Group4Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 1),
    _Group4Name_Type()
)
group4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4Name.setStatus("current")


class _Group4TempName_Type(DisplayString):
    """Custom type group4TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4TempName_Type.__name__ = "DisplayString"
_Group4TempName_Object = MibScalar
group4TempName = _Group4TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 2),
    _Group4TempName_Type()
)
group4TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4TempName.setStatus("current")


class _Group4TempDataStr_Type(DisplayString):
    """Custom type group4TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group4TempDataStr_Type.__name__ = "DisplayString"
_Group4TempDataStr_Object = MibScalar
group4TempDataStr = _Group4TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 3),
    _Group4TempDataStr_Type()
)
group4TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4TempDataStr.setStatus("current")


class _Group4TempDataInt_Type(Integer32):
    """Custom type group4TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group4TempDataInt_Type.__name__ = "Integer32"
_Group4TempDataInt_Object = MibScalar
group4TempDataInt = _Group4TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 4),
    _Group4TempDataInt_Type()
)
group4TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4TempDataInt.setStatus("current")


class _Group4HumidName_Type(DisplayString):
    """Custom type group4HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4HumidName_Type.__name__ = "DisplayString"
_Group4HumidName_Object = MibScalar
group4HumidName = _Group4HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 5),
    _Group4HumidName_Type()
)
group4HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4HumidName.setStatus("current")


class _Group4HumidDataStr_Type(DisplayString):
    """Custom type group4HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group4HumidDataStr_Type.__name__ = "DisplayString"
_Group4HumidDataStr_Object = MibScalar
group4HumidDataStr = _Group4HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 6),
    _Group4HumidDataStr_Type()
)
group4HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4HumidDataStr.setStatus("current")


class _Group4HumidDataInt_Type(Integer32):
    """Custom type group4HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group4HumidDataInt_Type.__name__ = "Integer32"
_Group4HumidDataInt_Object = MibScalar
group4HumidDataInt = _Group4HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 7),
    _Group4HumidDataInt_Type()
)
group4HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4HumidDataInt.setStatus("current")


class _Group4WetName_Type(DisplayString):
    """Custom type group4WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4WetName_Type.__name__ = "DisplayString"
_Group4WetName_Object = MibScalar
group4WetName = _Group4WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 8),
    _Group4WetName_Type()
)
group4WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4WetName.setStatus("current")


class _Group4WetDataStr_Type(DisplayString):
    """Custom type group4WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group4WetDataStr_Type.__name__ = "DisplayString"
_Group4WetDataStr_Object = MibScalar
group4WetDataStr = _Group4WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 9),
    _Group4WetDataStr_Type()
)
group4WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4WetDataStr.setStatus("current")


class _Group4WetDataInt_Type(Integer32):
    """Custom type group4WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group4WetDataInt_Type.__name__ = "Integer32"
_Group4WetDataInt_Object = MibScalar
group4WetDataInt = _Group4WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 10),
    _Group4WetDataInt_Type()
)
group4WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4WetDataInt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSATRONICS-EM1",
    **{"productEM1": productEM1,
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
       "group1": group1,
       "group1Name": group1Name,
       "group1TempName": group1TempName,
       "group1TempDataStr": group1TempDataStr,
       "group1TempDataInt": group1TempDataInt,
       "group1HumidName": group1HumidName,
       "group1HumidDataStr": group1HumidDataStr,
       "group1HumidDataInt": group1HumidDataInt,
       "group1WetName": group1WetName,
       "group1WetDataStr": group1WetDataStr,
       "group1WetDataInt": group1WetDataInt,
       "group2": group2,
       "group2Name": group2Name,
       "group2TempName": group2TempName,
       "group2TempDataStr": group2TempDataStr,
       "group2TempDataInt": group2TempDataInt,
       "group2HumidName": group2HumidName,
       "group2HumidDataStr": group2HumidDataStr,
       "group2HumidDataInt": group2HumidDataInt,
       "group2WetName": group2WetName,
       "group2WetDataStr": group2WetDataStr,
       "group2WetDataInt": group2WetDataInt,
       "group3": group3,
       "group3Name": group3Name,
       "group3TempName": group3TempName,
       "group3TempDataStr": group3TempDataStr,
       "group3TempDataInt": group3TempDataInt,
       "group3HumidName": group3HumidName,
       "group3HumidDataStr": group3HumidDataStr,
       "group3HumidDataInt": group3HumidDataInt,
       "group3WetName": group3WetName,
       "group3WetDataStr": group3WetDataStr,
       "group3WetDataInt": group3WetDataInt,
       "group4": group4,
       "group4Name": group4Name,
       "group4TempName": group4TempName,
       "group4TempDataStr": group4TempDataStr,
       "group4TempDataInt": group4TempDataInt,
       "group4HumidName": group4HumidName,
       "group4HumidDataStr": group4HumidDataStr,
       "group4HumidDataInt": group4HumidDataInt,
       "group4WetName": group4WetName,
       "group4WetDataStr": group4WetDataStr,
       "group4WetDataInt": group4WetDataInt}
)
