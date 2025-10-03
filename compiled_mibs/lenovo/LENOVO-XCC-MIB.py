# SNMP MIB module (LENOVO-XCC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\lenovo\LENOVO-XCC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:27 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(lenovoServerMibs,) = mibBuilder.importSymbols(
    "LENOVO-SMI-MIB",
    "lenovoServerMibs")

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

lenovoXCCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1)
)
if mibBuilder.loadTexts:
    lenovoXCCMIB.setRevisions(
        ("2017-07-19 00:00",)
    )


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Monitors_ObjectIdentity = ObjectIdentity
monitors = _Monitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1)
)
_TempNumber_Type = Integer32
_TempNumber_Object = MibScalar
tempNumber = _TempNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 1),
    _TempNumber_Type()
)
tempNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNumber.setStatus("mandatory")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("mandatory")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1)
)
tempEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("mandatory")


class _TempIndex_Type(Integer32):
    """Custom type tempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("mandatory")


class _TempDescr_Type(DisplayString):
    """Custom type tempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempDescr_Type.__name__ = "DisplayString"
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 2),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("mandatory")


class _TempReading_Type(DisplayString):
    """Custom type tempReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempReading_Type.__name__ = "DisplayString"
_TempReading_Object = MibTableColumn
tempReading = _TempReading_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 3),
    _TempReading_Type()
)
tempReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempReading.setUnits("Degrees Celsius")


class _TempNominalReading_Type(DisplayString):
    """Custom type tempNominalReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempNominalReading_Type.__name__ = "DisplayString"
_TempNominalReading_Object = MibTableColumn
tempNominalReading = _TempNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 4),
    _TempNominalReading_Type()
)
tempNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNominalReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNominalReading.setUnits("Degrees Celsius")


class _TempNonRecovLimitHigh_Type(DisplayString):
    """Custom type tempNonRecovLimitHigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempNonRecovLimitHigh_Type.__name__ = "DisplayString"
_TempNonRecovLimitHigh_Object = MibTableColumn
tempNonRecovLimitHigh = _TempNonRecovLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 5),
    _TempNonRecovLimitHigh_Type()
)
tempNonRecovLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonRecovLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonRecovLimitHigh.setUnits("Degrees Celsius")


class _TempCritLimitHigh_Type(DisplayString):
    """Custom type tempCritLimitHigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempCritLimitHigh_Type.__name__ = "DisplayString"
_TempCritLimitHigh_Object = MibTableColumn
tempCritLimitHigh = _TempCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 6),
    _TempCritLimitHigh_Type()
)
tempCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempCritLimitHigh.setUnits("Degrees Celsius")


class _TempNonCritLimitHigh_Type(DisplayString):
    """Custom type tempNonCritLimitHigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempNonCritLimitHigh_Type.__name__ = "DisplayString"
_TempNonCritLimitHigh_Object = MibTableColumn
tempNonCritLimitHigh = _TempNonCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 7),
    _TempNonCritLimitHigh_Type()
)
tempNonCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonCritLimitHigh.setUnits("Degrees Celsius")


class _TempNonRecovLimitLow_Type(DisplayString):
    """Custom type tempNonRecovLimitLow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempNonRecovLimitLow_Type.__name__ = "DisplayString"
_TempNonRecovLimitLow_Object = MibTableColumn
tempNonRecovLimitLow = _TempNonRecovLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 8),
    _TempNonRecovLimitLow_Type()
)
tempNonRecovLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonRecovLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonRecovLimitLow.setUnits("Degrees Celsius")


class _TempCritLimitLow_Type(DisplayString):
    """Custom type tempCritLimitLow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempCritLimitLow_Type.__name__ = "DisplayString"
_TempCritLimitLow_Object = MibTableColumn
tempCritLimitLow = _TempCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 9),
    _TempCritLimitLow_Type()
)
tempCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempCritLimitLow.setUnits("Degrees Celsius")


class _TempNonCritLimitLow_Type(DisplayString):
    """Custom type tempNonCritLimitLow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempNonCritLimitLow_Type.__name__ = "DisplayString"
_TempNonCritLimitLow_Object = MibTableColumn
tempNonCritLimitLow = _TempNonCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 10),
    _TempNonCritLimitLow_Type()
)
tempNonCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonCritLimitLow.setUnits("Degrees Celsius")


class _TempHealthStatus_Type(DisplayString):
    """Custom type tempHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempHealthStatus_Type.__name__ = "DisplayString"
_TempHealthStatus_Object = MibTableColumn
tempHealthStatus = _TempHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 1, 2, 1, 11),
    _TempHealthStatus_Type()
)
tempHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHealthStatus.setStatus("mandatory")
_Voltage_ObjectIdentity = ObjectIdentity
voltage = _Voltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2)
)
_VoltNumber_Type = Integer32
_VoltNumber_Object = MibScalar
voltNumber = _VoltNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 1),
    _VoltNumber_Type()
)
voltNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNumber.setStatus("mandatory")
_VoltTable_Object = MibTable
voltTable = _VoltTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    voltTable.setStatus("mandatory")
_VoltEntry_Object = MibTableRow
voltEntry = _VoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1)
)
voltEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "voltIndex"),
)
if mibBuilder.loadTexts:
    voltEntry.setStatus("mandatory")


class _VoltIndex_Type(Integer32):
    """Custom type voltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VoltIndex_Type.__name__ = "Integer32"
_VoltIndex_Object = MibTableColumn
voltIndex = _VoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 1),
    _VoltIndex_Type()
)
voltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltIndex.setStatus("mandatory")


class _VoltDescr_Type(DisplayString):
    """Custom type voltDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltDescr_Type.__name__ = "DisplayString"
_VoltDescr_Object = MibTableColumn
voltDescr = _VoltDescr_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 2),
    _VoltDescr_Type()
)
voltDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltDescr.setStatus("mandatory")


class _VoltReading_Type(DisplayString):
    """Custom type voltReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltReading_Type.__name__ = "DisplayString"
_VoltReading_Object = MibTableColumn
voltReading = _VoltReading_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 3),
    _VoltReading_Type()
)
voltReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltReading.setUnits("Millivolts")


class _VoltNominalReading_Type(DisplayString):
    """Custom type voltNominalReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltNominalReading_Type.__name__ = "DisplayString"
_VoltNominalReading_Object = MibTableColumn
voltNominalReading = _VoltNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 4),
    _VoltNominalReading_Type()
)
voltNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNominalReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNominalReading.setUnits("Millivolts")


class _VoltNonRecovLimitHigh_Type(DisplayString):
    """Custom type voltNonRecovLimitHigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltNonRecovLimitHigh_Type.__name__ = "DisplayString"
_VoltNonRecovLimitHigh_Object = MibTableColumn
voltNonRecovLimitHigh = _VoltNonRecovLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 5),
    _VoltNonRecovLimitHigh_Type()
)
voltNonRecovLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonRecovLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonRecovLimitHigh.setUnits("Millivolts")


class _VoltCritLimitHigh_Type(DisplayString):
    """Custom type voltCritLimitHigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltCritLimitHigh_Type.__name__ = "DisplayString"
_VoltCritLimitHigh_Object = MibTableColumn
voltCritLimitHigh = _VoltCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 6),
    _VoltCritLimitHigh_Type()
)
voltCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltCritLimitHigh.setUnits("Millivolts")


class _VoltNonCritLimitHigh_Type(DisplayString):
    """Custom type voltNonCritLimitHigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltNonCritLimitHigh_Type.__name__ = "DisplayString"
_VoltNonCritLimitHigh_Object = MibTableColumn
voltNonCritLimitHigh = _VoltNonCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 7),
    _VoltNonCritLimitHigh_Type()
)
voltNonCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonCritLimitHigh.setUnits("Millivolts")


class _VoltNonRecovLimitLow_Type(DisplayString):
    """Custom type voltNonRecovLimitLow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltNonRecovLimitLow_Type.__name__ = "DisplayString"
_VoltNonRecovLimitLow_Object = MibTableColumn
voltNonRecovLimitLow = _VoltNonRecovLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 8),
    _VoltNonRecovLimitLow_Type()
)
voltNonRecovLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonRecovLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonRecovLimitLow.setUnits("Millivolts")


class _VoltCritLimitLow_Type(DisplayString):
    """Custom type voltCritLimitLow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltCritLimitLow_Type.__name__ = "DisplayString"
_VoltCritLimitLow_Object = MibTableColumn
voltCritLimitLow = _VoltCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 9),
    _VoltCritLimitLow_Type()
)
voltCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltCritLimitLow.setUnits("Millivolts")


class _VoltNonCritLimitLow_Type(DisplayString):
    """Custom type voltNonCritLimitLow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltNonCritLimitLow_Type.__name__ = "DisplayString"
_VoltNonCritLimitLow_Object = MibTableColumn
voltNonCritLimitLow = _VoltNonCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 10),
    _VoltNonCritLimitLow_Type()
)
voltNonCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonCritLimitLow.setUnits("Millivolts")


class _VoltHealthStatus_Type(DisplayString):
    """Custom type voltHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltHealthStatus_Type.__name__ = "DisplayString"
_VoltHealthStatus_Object = MibTableColumn
voltHealthStatus = _VoltHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 2, 2, 1, 11),
    _VoltHealthStatus_Type()
)
voltHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltHealthStatus.setStatus("mandatory")
_Fans_ObjectIdentity = ObjectIdentity
fans = _Fans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3)
)
_FanNumber_Type = Integer32
_FanNumber_Object = MibScalar
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("mandatory")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("mandatory")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1)
)
fanEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("mandatory")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("mandatory")


class _FanDescr_Type(DisplayString):
    """Custom type fanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanDescr_Type.__name__ = "DisplayString"
_FanDescr_Object = MibTableColumn
fanDescr = _FanDescr_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 2),
    _FanDescr_Type()
)
fanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDescr.setStatus("mandatory")
_FanSpeed_Type = OctetString
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 3),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("mandatory")
_FanNonRecovLimitHigh_Type = Gauge32
_FanNonRecovLimitHigh_Object = MibTableColumn
fanNonRecovLimitHigh = _FanNonRecovLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 4),
    _FanNonRecovLimitHigh_Type()
)
fanNonRecovLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonRecovLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonRecovLimitHigh.setUnits("RPM")
_FanCritLimitHigh_Type = Gauge32
_FanCritLimitHigh_Object = MibTableColumn
fanCritLimitHigh = _FanCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 5),
    _FanCritLimitHigh_Type()
)
fanCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanCritLimitHigh.setUnits("RPM")
_FanNonCritLimitHigh_Type = Gauge32
_FanNonCritLimitHigh_Object = MibTableColumn
fanNonCritLimitHigh = _FanNonCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 6),
    _FanNonCritLimitHigh_Type()
)
fanNonCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonCritLimitHigh.setUnits("RPM")
_FanNonRecovLimitLow_Type = Gauge32
_FanNonRecovLimitLow_Object = MibTableColumn
fanNonRecovLimitLow = _FanNonRecovLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 7),
    _FanNonRecovLimitLow_Type()
)
fanNonRecovLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonRecovLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonRecovLimitLow.setUnits("RPM")
_FanCritLimitLow_Type = Gauge32
_FanCritLimitLow_Object = MibTableColumn
fanCritLimitLow = _FanCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 8),
    _FanCritLimitLow_Type()
)
fanCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanCritLimitLow.setUnits("RPM")
_FanNonCritLimitLow_Type = Gauge32
_FanNonCritLimitLow_Object = MibTableColumn
fanNonCritLimitLow = _FanNonCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 9),
    _FanNonCritLimitLow_Type()
)
fanNonCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonCritLimitLow.setUnits("RPM")


class _FanHealthStatus_Type(DisplayString):
    """Custom type fanHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanHealthStatus_Type.__name__ = "DisplayString"
_FanHealthStatus_Object = MibTableColumn
fanHealthStatus = _FanHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 3, 2, 1, 10),
    _FanHealthStatus_Type()
)
fanHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanHealthStatus.setStatus("mandatory")
_SystemHealth_ObjectIdentity = ObjectIdentity
systemHealth = _SystemHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 4)
)


class _SystemHealthStat_Type(Integer32):
    """Custom type systemHealthStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("nonRecoverable", 0),
          ("critical", 2),
          ("nonCritical", 4),
          ("normal", 255))
    )


_SystemHealthStat_Type.__name__ = "Integer32"
_SystemHealthStat_Object = MibScalar
systemHealthStat = _SystemHealthStat_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 4, 1),
    _SystemHealthStat_Type()
)
systemHealthStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthStat.setStatus("mandatory")
_SystemHealthSummaryTable_Object = MibTable
systemHealthSummaryTable = _SystemHealthSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    systemHealthSummaryTable.setStatus("mandatory")
_SystemHealthSummaryEntry_Object = MibTableRow
systemHealthSummaryEntry = _SystemHealthSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 4, 2, 1)
)
systemHealthSummaryEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "systemHealthSummaryIndex"),
)
if mibBuilder.loadTexts:
    systemHealthSummaryEntry.setStatus("mandatory")


class _SystemHealthSummaryIndex_Type(Integer32):
    """Custom type systemHealthSummaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SystemHealthSummaryIndex_Type.__name__ = "Integer32"
_SystemHealthSummaryIndex_Object = MibTableColumn
systemHealthSummaryIndex = _SystemHealthSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 4, 2, 1, 1),
    _SystemHealthSummaryIndex_Type()
)
systemHealthSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummaryIndex.setStatus("mandatory")
_SystemHealthSummarySeverity_Type = OctetString
_SystemHealthSummarySeverity_Object = MibTableColumn
systemHealthSummarySeverity = _SystemHealthSummarySeverity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 4, 2, 1, 2),
    _SystemHealthSummarySeverity_Type()
)
systemHealthSummarySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummarySeverity.setStatus("mandatory")
_SystemHealthSummaryDescription_Type = OctetString
_SystemHealthSummaryDescription_Object = MibTableColumn
systemHealthSummaryDescription = _SystemHealthSummaryDescription_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 4, 2, 1, 3),
    _SystemHealthSummaryDescription_Type()
)
systemHealthSummaryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummaryDescription.setStatus("mandatory")
_VpdInformation_ObjectIdentity = ObjectIdentity
vpdInformation = _VpdInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5)
)
_XccVpdTable_Object = MibTable
xccVpdTable = _XccVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    xccVpdTable.setStatus("mandatory")
_XccVpdEntry_Object = MibTableRow
xccVpdEntry = _XccVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 1, 1)
)
xccVpdEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "xccVpdIndex"),
)
if mibBuilder.loadTexts:
    xccVpdEntry.setStatus("mandatory")


class _XccVpdIndex_Type(Integer32):
    """Custom type xccVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_XccVpdIndex_Type.__name__ = "Integer32"
_XccVpdIndex_Object = MibTableColumn
xccVpdIndex = _XccVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 1, 1, 1),
    _XccVpdIndex_Type()
)
xccVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccVpdIndex.setStatus("mandatory")
_XccVpdType_Type = OctetString
_XccVpdType_Object = MibTableColumn
xccVpdType = _XccVpdType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 1, 1, 2),
    _XccVpdType_Type()
)
xccVpdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccVpdType.setStatus("mandatory")
_XccVpdVersionString_Type = OctetString
_XccVpdVersionString_Object = MibTableColumn
xccVpdVersionString = _XccVpdVersionString_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 1, 1, 3),
    _XccVpdVersionString_Type()
)
xccVpdVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccVpdVersionString.setStatus("mandatory")
_XccVpdReleaseDate_Type = OctetString
_XccVpdReleaseDate_Object = MibTableColumn
xccVpdReleaseDate = _XccVpdReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 1, 1, 4),
    _XccVpdReleaseDate_Type()
)
xccVpdReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccVpdReleaseDate.setStatus("mandatory")
_MachineVpd_ObjectIdentity = ObjectIdentity
machineVpd = _MachineVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 2)
)
_MachineLevelVpd_ObjectIdentity = ObjectIdentity
machineLevelVpd = _MachineLevelVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 2, 1)
)
_MachineLevelVpdMachineType_Type = OctetString
_MachineLevelVpdMachineType_Object = MibScalar
machineLevelVpdMachineType = _MachineLevelVpdMachineType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 2, 1, 1),
    _MachineLevelVpdMachineType_Type()
)
machineLevelVpdMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelVpdMachineType.setStatus("mandatory")
_MachineLevelVpdMachineModel_Type = OctetString
_MachineLevelVpdMachineModel_Object = MibScalar
machineLevelVpdMachineModel = _MachineLevelVpdMachineModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 2, 1, 2),
    _MachineLevelVpdMachineModel_Type()
)
machineLevelVpdMachineModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelVpdMachineModel.setStatus("mandatory")
_MachineLevelSerialNumber_Type = OctetString
_MachineLevelSerialNumber_Object = MibScalar
machineLevelSerialNumber = _MachineLevelSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 2, 1, 3),
    _MachineLevelSerialNumber_Type()
)
machineLevelSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelSerialNumber.setStatus("mandatory")
_MachineLevelUUID_Type = OctetString
_MachineLevelUUID_Object = MibScalar
machineLevelUUID = _MachineLevelUUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 2, 1, 4),
    _MachineLevelUUID_Type()
)
machineLevelUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelUUID.setStatus("mandatory")
_MachineLevelProductName_Type = OctetString
_MachineLevelProductName_Object = MibScalar
machineLevelProductName = _MachineLevelProductName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 2, 1, 5),
    _MachineLevelProductName_Type()
)
machineLevelProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelProductName.setStatus("mandatory")
_SystemComponentLevelVpdTable_Object = MibTable
systemComponentLevelVpdTable = _SystemComponentLevelVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 17)
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdTable.setStatus("mandatory")
_SystemComponentLevelVpdEntry_Object = MibTableRow
systemComponentLevelVpdEntry = _SystemComponentLevelVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 17, 1)
)
systemComponentLevelVpdEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "componentLevelVpdIndex"),
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdEntry.setStatus("mandatory")


class _ComponentLevelVpdIndex_Type(Integer32):
    """Custom type componentLevelVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ComponentLevelVpdIndex_Type.__name__ = "Integer32"
_ComponentLevelVpdIndex_Object = MibTableColumn
componentLevelVpdIndex = _ComponentLevelVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 17, 1, 1),
    _ComponentLevelVpdIndex_Type()
)
componentLevelVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdIndex.setStatus("mandatory")
_ComponentLevelVpdFruNumber_Type = OctetString
_ComponentLevelVpdFruNumber_Object = MibTableColumn
componentLevelVpdFruNumber = _ComponentLevelVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 17, 1, 2),
    _ComponentLevelVpdFruNumber_Type()
)
componentLevelVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdFruNumber.setStatus("mandatory")
_ComponentLevelVpdFruName_Type = OctetString
_ComponentLevelVpdFruName_Object = MibTableColumn
componentLevelVpdFruName = _ComponentLevelVpdFruName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 17, 1, 3),
    _ComponentLevelVpdFruName_Type()
)
componentLevelVpdFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdFruName.setStatus("mandatory")
_ComponentLevelVpdSerialNumber_Type = OctetString
_ComponentLevelVpdSerialNumber_Object = MibTableColumn
componentLevelVpdSerialNumber = _ComponentLevelVpdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 17, 1, 4),
    _ComponentLevelVpdSerialNumber_Type()
)
componentLevelVpdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdSerialNumber.setStatus("mandatory")
_ComponentLevelVpdManufacturingId_Type = OctetString
_ComponentLevelVpdManufacturingId_Object = MibTableColumn
componentLevelVpdManufacturingId = _ComponentLevelVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 17, 1, 5),
    _ComponentLevelVpdManufacturingId_Type()
)
componentLevelVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdManufacturingId.setStatus("mandatory")
_SystemComponentLevelVpdTrackingTable_Object = MibTable
systemComponentLevelVpdTrackingTable = _SystemComponentLevelVpdTrackingTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18)
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdTrackingTable.setStatus("mandatory")
_SystemComponentLevelVpdTrackingEntry_Object = MibTableRow
systemComponentLevelVpdTrackingEntry = _SystemComponentLevelVpdTrackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1)
)
systemComponentLevelVpdTrackingEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "componentLevelVpdTrackingIndex"),
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdTrackingEntry.setStatus("mandatory")


class _ComponentLevelVpdTrackingIndex_Type(Integer32):
    """Custom type componentLevelVpdTrackingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ComponentLevelVpdTrackingIndex_Type.__name__ = "Integer32"
_ComponentLevelVpdTrackingIndex_Object = MibTableColumn
componentLevelVpdTrackingIndex = _ComponentLevelVpdTrackingIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1, 1),
    _ComponentLevelVpdTrackingIndex_Type()
)
componentLevelVpdTrackingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingIndex.setStatus("mandatory")
_ComponentLevelVpdTrackingFruNumber_Type = OctetString
_ComponentLevelVpdTrackingFruNumber_Object = MibTableColumn
componentLevelVpdTrackingFruNumber = _ComponentLevelVpdTrackingFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1, 2),
    _ComponentLevelVpdTrackingFruNumber_Type()
)
componentLevelVpdTrackingFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingFruNumber.setStatus("mandatory")
_ComponentLevelVpdTrackingFruName_Type = OctetString
_ComponentLevelVpdTrackingFruName_Object = MibTableColumn
componentLevelVpdTrackingFruName = _ComponentLevelVpdTrackingFruName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1, 3),
    _ComponentLevelVpdTrackingFruName_Type()
)
componentLevelVpdTrackingFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingFruName.setStatus("mandatory")
_ComponentLevelVpdTrackingSerialNumber_Type = OctetString
_ComponentLevelVpdTrackingSerialNumber_Object = MibTableColumn
componentLevelVpdTrackingSerialNumber = _ComponentLevelVpdTrackingSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1, 4),
    _ComponentLevelVpdTrackingSerialNumber_Type()
)
componentLevelVpdTrackingSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingSerialNumber.setStatus("mandatory")
_ComponentLevelVpdTrackingManufacturingId_Type = OctetString
_ComponentLevelVpdTrackingManufacturingId_Object = MibTableColumn
componentLevelVpdTrackingManufacturingId = _ComponentLevelVpdTrackingManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1, 5),
    _ComponentLevelVpdTrackingManufacturingId_Type()
)
componentLevelVpdTrackingManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingManufacturingId.setStatus("mandatory")
_ComponentLevelVpdTrackingAction_Type = OctetString
_ComponentLevelVpdTrackingAction_Object = MibTableColumn
componentLevelVpdTrackingAction = _ComponentLevelVpdTrackingAction_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1, 6),
    _ComponentLevelVpdTrackingAction_Type()
)
componentLevelVpdTrackingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingAction.setStatus("mandatory")
_ComponentLevelVpdTrackingTimestamp_Type = OctetString
_ComponentLevelVpdTrackingTimestamp_Object = MibTableColumn
componentLevelVpdTrackingTimestamp = _ComponentLevelVpdTrackingTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 18, 1, 7),
    _ComponentLevelVpdTrackingTimestamp_Type()
)
componentLevelVpdTrackingTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingTimestamp.setStatus("mandatory")
_HostMACAddressTable_Object = MibTable
hostMACAddressTable = _HostMACAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 19)
)
if mibBuilder.loadTexts:
    hostMACAddressTable.setStatus("mandatory")
_HostMACAddressEntry_Object = MibTableRow
hostMACAddressEntry = _HostMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 19, 1)
)
hostMACAddressEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "hostMACAddressIndex"),
)
if mibBuilder.loadTexts:
    hostMACAddressEntry.setStatus("mandatory")


class _HostMACAddressIndex_Type(Integer32):
    """Custom type hostMACAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HostMACAddressIndex_Type.__name__ = "Integer32"
_HostMACAddressIndex_Object = MibTableColumn
hostMACAddressIndex = _HostMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 19, 1, 1),
    _HostMACAddressIndex_Type()
)
hostMACAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMACAddressIndex.setStatus("mandatory")
_HostMACAddressDescription_Type = DisplayString
_HostMACAddressDescription_Object = MibTableColumn
hostMACAddressDescription = _HostMACAddressDescription_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 19, 1, 2),
    _HostMACAddressDescription_Type()
)
hostMACAddressDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMACAddressDescription.setStatus("mandatory")
_HostMACAddress_Type = DisplayString
_HostMACAddress_Object = MibTableColumn
hostMACAddress = _HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 19, 1, 3),
    _HostMACAddress_Type()
)
hostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMACAddress.setStatus("mandatory")
_SystemCPUVpdTable_Object = MibTable
systemCPUVpdTable = _SystemCPUVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20)
)
if mibBuilder.loadTexts:
    systemCPUVpdTable.setStatus("mandatory")
_SystemCPUVpdEntry_Object = MibTableRow
systemCPUVpdEntry = _SystemCPUVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1)
)
systemCPUVpdEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "cpuVpdIndex"),
)
if mibBuilder.loadTexts:
    systemCPUVpdEntry.setStatus("mandatory")


class _CpuVpdIndex_Type(Integer32):
    """Custom type cpuVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CpuVpdIndex_Type.__name__ = "Integer32"
_CpuVpdIndex_Object = MibTableColumn
cpuVpdIndex = _CpuVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 1),
    _CpuVpdIndex_Type()
)
cpuVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdIndex.setStatus("mandatory")
_CpuVpdDescription_Type = DisplayString
_CpuVpdDescription_Object = MibTableColumn
cpuVpdDescription = _CpuVpdDescription_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 2),
    _CpuVpdDescription_Type()
)
cpuVpdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdDescription.setStatus("mandatory")
_CpuVpdSpeed_Type = Integer32
_CpuVpdSpeed_Object = MibTableColumn
cpuVpdSpeed = _CpuVpdSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 3),
    _CpuVpdSpeed_Type()
)
cpuVpdSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdSpeed.setStatus("mandatory")
_CpuVpdIdentifier_Type = DisplayString
_CpuVpdIdentifier_Object = MibTableColumn
cpuVpdIdentifier = _CpuVpdIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 4),
    _CpuVpdIdentifier_Type()
)
cpuVpdIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdIdentifier.setStatus("mandatory")
_CpuVpdType_Type = DisplayString
_CpuVpdType_Object = MibTableColumn
cpuVpdType = _CpuVpdType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 5),
    _CpuVpdType_Type()
)
cpuVpdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdType.setStatus("mandatory")
_CpuVpdFamily_Type = DisplayString
_CpuVpdFamily_Object = MibTableColumn
cpuVpdFamily = _CpuVpdFamily_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 6),
    _CpuVpdFamily_Type()
)
cpuVpdFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdFamily.setStatus("mandatory")
_CpuVpdCores_Type = Integer32
_CpuVpdCores_Object = MibTableColumn
cpuVpdCores = _CpuVpdCores_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 7),
    _CpuVpdCores_Type()
)
cpuVpdCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdCores.setStatus("mandatory")
_CpuVpdThreads_Type = Integer32
_CpuVpdThreads_Object = MibTableColumn
cpuVpdThreads = _CpuVpdThreads_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 8),
    _CpuVpdThreads_Type()
)
cpuVpdThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdThreads.setStatus("mandatory")
_CpuVpdVoltage_Type = Integer32
_CpuVpdVoltage_Object = MibTableColumn
cpuVpdVoltage = _CpuVpdVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 9),
    _CpuVpdVoltage_Type()
)
cpuVpdVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdVoltage.setStatus("mandatory")
_CpuVpdDataWidth_Type = Integer32
_CpuVpdDataWidth_Object = MibTableColumn
cpuVpdDataWidth = _CpuVpdDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 10),
    _CpuVpdDataWidth_Type()
)
cpuVpdDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdDataWidth.setStatus("mandatory")
_CpuVpdHealthStatus_Type = DisplayString
_CpuVpdHealthStatus_Object = MibTableColumn
cpuVpdHealthStatus = _CpuVpdHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 11),
    _CpuVpdHealthStatus_Type()
)
cpuVpdHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdHealthStatus.setStatus("mandatory")
_CpuVpdCpuModel_Type = DisplayString
_CpuVpdCpuModel_Object = MibTableColumn
cpuVpdCpuModel = _CpuVpdCpuModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 20, 1, 12),
    _CpuVpdCpuModel_Type()
)
cpuVpdCpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdCpuModel.setStatus("mandatory")
_SystemMemoryVpdTable_Object = MibTable
systemMemoryVpdTable = _SystemMemoryVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21)
)
if mibBuilder.loadTexts:
    systemMemoryVpdTable.setStatus("mandatory")
_SystemMemoryVpdEntry_Object = MibTableRow
systemMemoryVpdEntry = _SystemMemoryVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1)
)
systemMemoryVpdEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "memoryVpdIndex"),
)
if mibBuilder.loadTexts:
    systemMemoryVpdEntry.setStatus("mandatory")


class _MemoryVpdIndex_Type(Integer32):
    """Custom type memoryVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MemoryVpdIndex_Type.__name__ = "Integer32"
_MemoryVpdIndex_Object = MibTableColumn
memoryVpdIndex = _MemoryVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 1),
    _MemoryVpdIndex_Type()
)
memoryVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdIndex.setStatus("mandatory")
_MemoryVpdDescription_Type = DisplayString
_MemoryVpdDescription_Object = MibTableColumn
memoryVpdDescription = _MemoryVpdDescription_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 2),
    _MemoryVpdDescription_Type()
)
memoryVpdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdDescription.setStatus("mandatory")
_MemoryVpdPartNumber_Type = DisplayString
_MemoryVpdPartNumber_Object = MibTableColumn
memoryVpdPartNumber = _MemoryVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 3),
    _MemoryVpdPartNumber_Type()
)
memoryVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdPartNumber.setStatus("mandatory")
_MemoryVpdFRUSerialNumber_Type = DisplayString
_MemoryVpdFRUSerialNumber_Object = MibTableColumn
memoryVpdFRUSerialNumber = _MemoryVpdFRUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 4),
    _MemoryVpdFRUSerialNumber_Type()
)
memoryVpdFRUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdFRUSerialNumber.setStatus("mandatory")
_MemoryVpdManufactureDate_Type = DisplayString
_MemoryVpdManufactureDate_Object = MibTableColumn
memoryVpdManufactureDate = _MemoryVpdManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 5),
    _MemoryVpdManufactureDate_Type()
)
memoryVpdManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdManufactureDate.setStatus("mandatory")
_MemoryVpdType_Type = DisplayString
_MemoryVpdType_Object = MibTableColumn
memoryVpdType = _MemoryVpdType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 6),
    _MemoryVpdType_Type()
)
memoryVpdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdType.setStatus("mandatory")
_MemoryVpdSize_Type = Integer32
_MemoryVpdSize_Object = MibTableColumn
memoryVpdSize = _MemoryVpdSize_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 7),
    _MemoryVpdSize_Type()
)
memoryVpdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdSize.setStatus("mandatory")


class _MemoryHealthStatus_Type(DisplayString):
    """Custom type memoryHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MemoryHealthStatus_Type.__name__ = "DisplayString"
_MemoryHealthStatus_Object = MibTableColumn
memoryHealthStatus = _MemoryHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 8),
    _MemoryHealthStatus_Type()
)
memoryHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryHealthStatus.setStatus("mandatory")
_MemoryConfigSpeed_Type = Integer32
_MemoryConfigSpeed_Object = MibTableColumn
memoryConfigSpeed = _MemoryConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 9),
    _MemoryConfigSpeed_Type()
)
memoryConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryConfigSpeed.setStatus("mandatory")
_MemoryRatedSpeed_Type = Integer32
_MemoryRatedSpeed_Object = MibTableColumn
memoryRatedSpeed = _MemoryRatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 10),
    _MemoryRatedSpeed_Type()
)
memoryRatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryRatedSpeed.setStatus("mandatory")
_MemoryLenovoPartNumber_Type = DisplayString
_MemoryLenovoPartNumber_Object = MibTableColumn
memoryLenovoPartNumber = _MemoryLenovoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 11),
    _MemoryLenovoPartNumber_Type()
)
memoryLenovoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryLenovoPartNumber.setStatus("mandatory")
_MemoryVpdAEPFlag_Type = Integer32
_MemoryVpdAEPFlag_Object = MibTableColumn
memoryVpdAEPFlag = _MemoryVpdAEPFlag_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 21, 1, 12),
    _MemoryVpdAEPFlag_Type()
)
memoryVpdAEPFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdAEPFlag.setStatus("mandatory")
_SystemAepDIMMVpdTable_Object = MibTable
systemAepDIMMVpdTable = _SystemAepDIMMVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22)
)
if mibBuilder.loadTexts:
    systemAepDIMMVpdTable.setStatus("mandatory")
_SystemAepDIMMVpdEntry_Object = MibTableRow
systemAepDIMMVpdEntry = _SystemAepDIMMVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1)
)
systemAepDIMMVpdEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "aepDIMMVpdIndex"),
)
if mibBuilder.loadTexts:
    systemAepDIMMVpdEntry.setStatus("mandatory")


class _AepDIMMVpdIndex_Type(Integer32):
    """Custom type aepDIMMVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AepDIMMVpdIndex_Type.__name__ = "Integer32"
_AepDIMMVpdIndex_Object = MibTableColumn
aepDIMMVpdIndex = _AepDIMMVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 1),
    _AepDIMMVpdIndex_Type()
)
aepDIMMVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdIndex.setStatus("mandatory")
_AepDIMMVpdMemory_Type = DisplayString
_AepDIMMVpdMemory_Object = MibTableColumn
aepDIMMVpdMemory = _AepDIMMVpdMemory_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 2),
    _AepDIMMVpdMemory_Type()
)
aepDIMMVpdMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdMemory.setStatus("mandatory")
_AepDIMMVpdBankLocator_Type = DisplayString
_AepDIMMVpdBankLocator_Object = MibTableColumn
aepDIMMVpdBankLocator = _AepDIMMVpdBankLocator_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 3),
    _AepDIMMVpdBankLocator_Type()
)
aepDIMMVpdBankLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdBankLocator.setStatus("mandatory")
_AepDIMMVpdMaxSpeed_Type = DisplayString
_AepDIMMVpdMaxSpeed_Object = MibTableColumn
aepDIMMVpdMaxSpeed = _AepDIMMVpdMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 4),
    _AepDIMMVpdMaxSpeed_Type()
)
aepDIMMVpdMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdMaxSpeed.setStatus("mandatory")
_AepDIMMVpdClockSpeed_Type = DisplayString
_AepDIMMVpdClockSpeed_Object = MibTableColumn
aepDIMMVpdClockSpeed = _AepDIMMVpdClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 5),
    _AepDIMMVpdClockSpeed_Type()
)
aepDIMMVpdClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdClockSpeed.setStatus("mandatory")
_AepDIMMVpdManufacturer_Type = DisplayString
_AepDIMMVpdManufacturer_Object = MibTableColumn
aepDIMMVpdManufacturer = _AepDIMMVpdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 6),
    _AepDIMMVpdManufacturer_Type()
)
aepDIMMVpdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdManufacturer.setStatus("mandatory")
_AepDIMMVpdSerialNumber_Type = DisplayString
_AepDIMMVpdSerialNumber_Object = MibTableColumn
aepDIMMVpdSerialNumber = _AepDIMMVpdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 7),
    _AepDIMMVpdSerialNumber_Type()
)
aepDIMMVpdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdSerialNumber.setStatus("mandatory")
_AepDIMMVpdPartNumber_Type = DisplayString
_AepDIMMVpdPartNumber_Object = MibTableColumn
aepDIMMVpdPartNumber = _AepDIMMVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 8),
    _AepDIMMVpdPartNumber_Type()
)
aepDIMMVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdPartNumber.setStatus("mandatory")
_AepDIMMVpdRawCapacity_Type = DisplayString
_AepDIMMVpdRawCapacity_Object = MibTableColumn
aepDIMMVpdRawCapacity = _AepDIMMVpdRawCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 9),
    _AepDIMMVpdRawCapacity_Type()
)
aepDIMMVpdRawCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdRawCapacity.setStatus("mandatory")
_AepDIMMVpdMemoryCapacity_Type = DisplayString
_AepDIMMVpdMemoryCapacity_Object = MibTableColumn
aepDIMMVpdMemoryCapacity = _AepDIMMVpdMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 10),
    _AepDIMMVpdMemoryCapacity_Type()
)
aepDIMMVpdMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdMemoryCapacity.setStatus("mandatory")
_AepDIMMVpdAppDirectCapacity_Type = DisplayString
_AepDIMMVpdAppDirectCapacity_Object = MibTableColumn
aepDIMMVpdAppDirectCapacity = _AepDIMMVpdAppDirectCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 11),
    _AepDIMMVpdAppDirectCapacity_Type()
)
aepDIMMVpdAppDirectCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdAppDirectCapacity.setStatus("mandatory")
_AepDIMMVpdUnconfiguredCapacity_Type = DisplayString
_AepDIMMVpdUnconfiguredCapacity_Object = MibTableColumn
aepDIMMVpdUnconfiguredCapacity = _AepDIMMVpdUnconfiguredCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 12),
    _AepDIMMVpdUnconfiguredCapacity_Type()
)
aepDIMMVpdUnconfiguredCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdUnconfiguredCapacity.setStatus("mandatory")
_AepDIMMVpdInaccessibleCapacity_Type = DisplayString
_AepDIMMVpdInaccessibleCapacity_Object = MibTableColumn
aepDIMMVpdInaccessibleCapacity = _AepDIMMVpdInaccessibleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 13),
    _AepDIMMVpdInaccessibleCapacity_Type()
)
aepDIMMVpdInaccessibleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdInaccessibleCapacity.setStatus("mandatory")
_AepDIMMVpdReservedCapacity_Type = DisplayString
_AepDIMMVpdReservedCapacity_Object = MibTableColumn
aepDIMMVpdReservedCapacity = _AepDIMMVpdReservedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 14),
    _AepDIMMVpdReservedCapacity_Type()
)
aepDIMMVpdReservedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdReservedCapacity.setStatus("mandatory")
_AepDIMMVpdClassification_Type = DisplayString
_AepDIMMVpdClassification_Object = MibTableColumn
aepDIMMVpdClassification = _AepDIMMVpdClassification_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 15),
    _AepDIMMVpdClassification_Type()
)
aepDIMMVpdClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdClassification.setStatus("mandatory")
_AepDIMMVpdFirmwareVersion_Type = DisplayString
_AepDIMMVpdFirmwareVersion_Object = MibTableColumn
aepDIMMVpdFirmwareVersion = _AepDIMMVpdFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 16),
    _AepDIMMVpdFirmwareVersion_Type()
)
aepDIMMVpdFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdFirmwareVersion.setStatus("mandatory")
_AepDIMMVpdSoftwareID_Type = DisplayString
_AepDIMMVpdSoftwareID_Object = MibTableColumn
aepDIMMVpdSoftwareID = _AepDIMMVpdSoftwareID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 5, 22, 1, 17),
    _AepDIMMVpdSoftwareID_Type()
)
aepDIMMVpdSoftwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aepDIMMVpdSoftwareID.setStatus("mandatory")
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 6)
)
_XccUsers_ObjectIdentity = ObjectIdentity
xccUsers = _XccUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 6, 1)
)
_CurrentlyLoggedInTable_Object = MibTable
currentlyLoggedInTable = _CurrentlyLoggedInTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    currentlyLoggedInTable.setStatus("mandatory")
_CurrentlyLoggedInEntry_Object = MibTableRow
currentlyLoggedInEntry = _CurrentlyLoggedInEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 6, 1, 1, 1)
)
currentlyLoggedInEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "currentlyLoggedInEntryIndex"),
)
if mibBuilder.loadTexts:
    currentlyLoggedInEntry.setStatus("mandatory")


class _CurrentlyLoggedInEntryIndex_Type(Integer32):
    """Custom type currentlyLoggedInEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CurrentlyLoggedInEntryIndex_Type.__name__ = "Integer32"
_CurrentlyLoggedInEntryIndex_Object = MibTableColumn
currentlyLoggedInEntryIndex = _CurrentlyLoggedInEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 6, 1, 1, 1, 1),
    _CurrentlyLoggedInEntryIndex_Type()
)
currentlyLoggedInEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyLoggedInEntryIndex.setStatus("mandatory")


class _CurrentlyLoggedInEntryUserId_Type(OctetString):
    """Custom type currentlyLoggedInEntryUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CurrentlyLoggedInEntryUserId_Type.__name__ = "OctetString"
_CurrentlyLoggedInEntryUserId_Object = MibTableColumn
currentlyLoggedInEntryUserId = _CurrentlyLoggedInEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 6, 1, 1, 1, 2),
    _CurrentlyLoggedInEntryUserId_Type()
)
currentlyLoggedInEntryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyLoggedInEntryUserId.setStatus("mandatory")


class _CurrentlyLoggedInEntryAccMethod_Type(OctetString):
    """Custom type currentlyLoggedInEntryAccMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CurrentlyLoggedInEntryAccMethod_Type.__name__ = "OctetString"
_CurrentlyLoggedInEntryAccMethod_Object = MibTableColumn
currentlyLoggedInEntryAccMethod = _CurrentlyLoggedInEntryAccMethod_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 6, 1, 1, 1, 3),
    _CurrentlyLoggedInEntryAccMethod_Type()
)
currentlyLoggedInEntryAccMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyLoggedInEntryAccMethod.setStatus("mandatory")
_Leds_ObjectIdentity = ObjectIdentity
leds = _Leds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8)
)


class _IdentityLED_Type(Integer32):
    """Custom type identityLED based on Integer32"""
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
        *(("off", 0),
          ("on", 1),
          ("blinking", 2),
          ("notAvailable", 3))
    )


_IdentityLED_Type.__name__ = "Integer32"
_IdentityLED_Object = MibScalar
identityLED = _IdentityLED_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 1),
    _IdentityLED_Type()
)
identityLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityLED.setStatus("mandatory")
_AllLEDsTable_Object = MibTable
allLEDsTable = _AllLEDsTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    allLEDsTable.setStatus("mandatory")
_AllLEDsEntry_Object = MibTableRow
allLEDsEntry = _AllLEDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 2, 1)
)
allLEDsEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "ledIndex"),
)
if mibBuilder.loadTexts:
    allLEDsEntry.setStatus("mandatory")


class _LedIndex_Type(Integer32):
    """Custom type ledIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_LedIndex_Type.__name__ = "Integer32"
_LedIndex_Object = MibTableColumn
ledIndex = _LedIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 2, 1, 1),
    _LedIndex_Type()
)
ledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledIndex.setStatus("mandatory")
_LedIdentifier_Type = Integer32
_LedIdentifier_Object = MibTableColumn
ledIdentifier = _LedIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 2, 1, 2),
    _LedIdentifier_Type()
)
ledIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledIdentifier.setStatus("mandatory")
_LedLabel_Type = DisplayString
_LedLabel_Object = MibTableColumn
ledLabel = _LedLabel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 2, 1, 4),
    _LedLabel_Type()
)
ledLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledLabel.setStatus("mandatory")


class _LedState_Type(Integer32):
    """Custom type ledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("blinking", 2))
    )


_LedState_Type.__name__ = "Integer32"
_LedState_Object = MibTableColumn
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 2, 1, 5),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("mandatory")
_LedColor_Type = DisplayString
_LedColor_Object = MibTableColumn
ledColor = _LedColor_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 2, 1, 6),
    _LedColor_Type()
)
ledColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledColor.setStatus("mandatory")


class _InformationLED_Type(Integer32):
    """Custom type informationLED based on Integer32"""
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
        *(("off", 0),
          ("on", 1),
          ("blinking", 2),
          ("notAvailable", 3))
    )


_InformationLED_Type.__name__ = "Integer32"
_InformationLED_Object = MibScalar
informationLED = _InformationLED_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 8, 3),
    _InformationLED_Type()
)
informationLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    informationLED.setStatus("mandatory")
_FuelGauge_ObjectIdentity = ObjectIdentity
fuelGauge = _FuelGauge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10)
)
_FuelGaugeInformation_ObjectIdentity = ObjectIdentity
fuelGaugeInformation = _FuelGaugeInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1)
)


class _FuelGaugePowerCappingPolicySetting_Type(Integer32):
    """Custom type fuelGaugePowerCappingPolicySetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerLimit", 0),
          ("staticPowerLimit", 1))
    )


_FuelGaugePowerCappingPolicySetting_Type.__name__ = "Integer32"
_FuelGaugePowerCappingPolicySetting_Object = MibScalar
fuelGaugePowerCappingPolicySetting = _FuelGaugePowerCappingPolicySetting_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 1),
    _FuelGaugePowerCappingPolicySetting_Type()
)
fuelGaugePowerCappingPolicySetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerCappingPolicySetting.setStatus("mandatory")
_FuelGaugeStaticPowerPcapSoftMin_Type = Integer32
_FuelGaugeStaticPowerPcapSoftMin_Object = MibScalar
fuelGaugeStaticPowerPcapSoftMin = _FuelGaugeStaticPowerPcapSoftMin_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 2),
    _FuelGaugeStaticPowerPcapSoftMin_Type()
)
fuelGaugeStaticPowerPcapSoftMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapSoftMin.setStatus("mandatory")
_FuelGaugeStaticPowerPcapMin_Type = Integer32
_FuelGaugeStaticPowerPcapMin_Object = MibScalar
fuelGaugeStaticPowerPcapMin = _FuelGaugeStaticPowerPcapMin_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 3),
    _FuelGaugeStaticPowerPcapMin_Type()
)
fuelGaugeStaticPowerPcapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapMin.setStatus("mandatory")
_FuelGaugeStaticPowerPcapCurrentSetting_Type = Integer32
_FuelGaugeStaticPowerPcapCurrentSetting_Object = MibScalar
fuelGaugeStaticPowerPcapCurrentSetting = _FuelGaugeStaticPowerPcapCurrentSetting_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 4),
    _FuelGaugeStaticPowerPcapCurrentSetting_Type()
)
fuelGaugeStaticPowerPcapCurrentSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapCurrentSetting.setStatus("mandatory")
_FuelGaugeStaticPowerPcapMax_Type = Integer32
_FuelGaugeStaticPowerPcapMax_Object = MibScalar
fuelGaugeStaticPowerPcapMax = _FuelGaugeStaticPowerPcapMax_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 5),
    _FuelGaugeStaticPowerPcapMax_Type()
)
fuelGaugeStaticPowerPcapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapMax.setStatus("mandatory")


class _FuelGaugeStaticPowerPcapMode_Type(Integer32):
    """Custom type fuelGaugeStaticPowerPcapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("output", 0),
          ("input", 1))
    )


_FuelGaugeStaticPowerPcapMode_Type.__name__ = "Integer32"
_FuelGaugeStaticPowerPcapMode_Object = MibScalar
fuelGaugeStaticPowerPcapMode = _FuelGaugeStaticPowerPcapMode_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 6),
    _FuelGaugeStaticPowerPcapMode_Type()
)
fuelGaugeStaticPowerPcapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapMode.setStatus("mandatory")
_FuelGaugeSystemMaxPower_Type = Integer32
_FuelGaugeSystemMaxPower_Object = MibScalar
fuelGaugeSystemMaxPower = _FuelGaugeSystemMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 7),
    _FuelGaugeSystemMaxPower_Type()
)
fuelGaugeSystemMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeSystemMaxPower.setStatus("mandatory")
_FuelGaugePowerRemaining_Type = Integer32
_FuelGaugePowerRemaining_Object = MibScalar
fuelGaugePowerRemaining = _FuelGaugePowerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 8),
    _FuelGaugePowerRemaining_Type()
)
fuelGaugePowerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerRemaining.setStatus("mandatory")
_FuelGaugeTotalPowerAvailable_Type = Integer32
_FuelGaugeTotalPowerAvailable_Object = MibScalar
fuelGaugeTotalPowerAvailable = _FuelGaugeTotalPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 9),
    _FuelGaugeTotalPowerAvailable_Type()
)
fuelGaugeTotalPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeTotalPowerAvailable.setStatus("mandatory")
_FuelGaugeTotalPowerInUse_Type = Integer32
_FuelGaugeTotalPowerInUse_Object = MibScalar
fuelGaugeTotalPowerInUse = _FuelGaugeTotalPowerInUse_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 10),
    _FuelGaugeTotalPowerInUse_Type()
)
fuelGaugeTotalPowerInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeTotalPowerInUse.setStatus("mandatory")
_FuelGaugePowerConsumptionCpu_Type = Integer32
_FuelGaugePowerConsumptionCpu_Object = MibScalar
fuelGaugePowerConsumptionCpu = _FuelGaugePowerConsumptionCpu_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 11),
    _FuelGaugePowerConsumptionCpu_Type()
)
fuelGaugePowerConsumptionCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerConsumptionCpu.setStatus("mandatory")
_FuelGaugePowerConsumptionMemory_Type = Integer32
_FuelGaugePowerConsumptionMemory_Object = MibScalar
fuelGaugePowerConsumptionMemory = _FuelGaugePowerConsumptionMemory_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 12),
    _FuelGaugePowerConsumptionMemory_Type()
)
fuelGaugePowerConsumptionMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerConsumptionMemory.setStatus("mandatory")
_FuelGaugePowerConsumptionOther_Type = Integer32
_FuelGaugePowerConsumptionOther_Object = MibScalar
fuelGaugePowerConsumptionOther = _FuelGaugePowerConsumptionOther_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 1, 13),
    _FuelGaugePowerConsumptionOther_Type()
)
fuelGaugePowerConsumptionOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerConsumptionOther.setStatus("mandatory")
_PowerPolicyInformation_ObjectIdentity = ObjectIdentity
powerPolicyInformation = _PowerPolicyInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2)
)
_PowerPolicyTable_Object = MibTable
powerPolicyTable = _PowerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    powerPolicyTable.setStatus("mandatory")
_PowerPolicyEntry_Object = MibTableRow
powerPolicyEntry = _PowerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1, 1)
)
powerPolicyEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "powerPolicyIndex"),
)
if mibBuilder.loadTexts:
    powerPolicyEntry.setStatus("mandatory")
_PowerPolicyIndex_Type = Integer32
_PowerPolicyIndex_Object = MibTableColumn
powerPolicyIndex = _PowerPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1, 1, 1),
    _PowerPolicyIndex_Type()
)
powerPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyIndex.setStatus("mandatory")
_PowerPolicyName_Type = OctetString
_PowerPolicyName_Object = MibTableColumn
powerPolicyName = _PowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1, 1, 2),
    _PowerPolicyName_Type()
)
powerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyName.setStatus("mandatory")
_PowerPolicyPwrSupplyFailureLimit_Type = Integer32
_PowerPolicyPwrSupplyFailureLimit_Object = MibTableColumn
powerPolicyPwrSupplyFailureLimit = _PowerPolicyPwrSupplyFailureLimit_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1, 1, 3),
    _PowerPolicyPwrSupplyFailureLimit_Type()
)
powerPolicyPwrSupplyFailureLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyPwrSupplyFailureLimit.setStatus("mandatory")
_PowerPolicyMaxPowerLimit_Type = Integer32
_PowerPolicyMaxPowerLimit_Object = MibTableColumn
powerPolicyMaxPowerLimit = _PowerPolicyMaxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1, 1, 4),
    _PowerPolicyMaxPowerLimit_Type()
)
powerPolicyMaxPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyMaxPowerLimit.setStatus("mandatory")
_PowerPolicyEstimatedUtilization_Type = Integer32
_PowerPolicyEstimatedUtilization_Object = MibTableColumn
powerPolicyEstimatedUtilization = _PowerPolicyEstimatedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1, 1, 5),
    _PowerPolicyEstimatedUtilization_Type()
)
powerPolicyEstimatedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyEstimatedUtilization.setStatus("mandatory")


class _PowerPolicyActivate_Type(Integer32):
    """Custom type powerPolicyActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PowerPolicyActivate_Type.__name__ = "Integer32"
_PowerPolicyActivate_Object = MibTableColumn
powerPolicyActivate = _PowerPolicyActivate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 1, 1, 6),
    _PowerPolicyActivate_Type()
)
powerPolicyActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyActivate.setStatus("mandatory")
_PowerRestorePolicyControl_ObjectIdentity = ObjectIdentity
powerRestorePolicyControl = _PowerRestorePolicyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 2)
)


class _PowerRestorePolicy_Type(Integer32):
    """Custom type powerRestorePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysoff", 0),
          ("restore", 1),
          ("alwayson", 2))
    )


_PowerRestorePolicy_Type.__name__ = "Integer32"
_PowerRestorePolicy_Object = MibScalar
powerRestorePolicy = _PowerRestorePolicy_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 2, 1),
    _PowerRestorePolicy_Type()
)
powerRestorePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestorePolicy.setStatus("mandatory")


class _PowerRestoreDelay_Type(Integer32):
    """Custom type powerRestoreDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("random", 1))
    )


_PowerRestoreDelay_Type.__name__ = "Integer32"
_PowerRestoreDelay_Object = MibScalar
powerRestoreDelay = _PowerRestoreDelay_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 2, 2, 2),
    _PowerRestoreDelay_Type()
)
powerRestoreDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerRestoreDelay.setStatus("mandatory")
_PowerPowerTrending_ObjectIdentity = ObjectIdentity
powerPowerTrending = _PowerPowerTrending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3)
)
_PowerTrendingSampleTable_Object = MibTable
powerTrendingSampleTable = _PowerTrendingSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    powerTrendingSampleTable.setStatus("mandatory")
_PowerTrendingSampleEntry_Object = MibTableRow
powerTrendingSampleEntry = _PowerTrendingSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1)
)
powerTrendingSampleEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "powerTrendingSampleIndex"),
)
if mibBuilder.loadTexts:
    powerTrendingSampleEntry.setStatus("mandatory")
_PowerTrendingSampleIndex_Type = Integer32
_PowerTrendingSampleIndex_Object = MibTableColumn
powerTrendingSampleIndex = _PowerTrendingSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 1),
    _PowerTrendingSampleIndex_Type()
)
powerTrendingSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleIndex.setStatus("mandatory")
_PowerTrendingSampleTimeStamp_Type = OctetString
_PowerTrendingSampleTimeStamp_Object = MibTableColumn
powerTrendingSampleTimeStamp = _PowerTrendingSampleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 2),
    _PowerTrendingSampleTimeStamp_Type()
)
powerTrendingSampleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleTimeStamp.setStatus("mandatory")
_PowerTrendingSampleInputAve_Type = Integer32
_PowerTrendingSampleInputAve_Object = MibTableColumn
powerTrendingSampleInputAve = _PowerTrendingSampleInputAve_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 3),
    _PowerTrendingSampleInputAve_Type()
)
powerTrendingSampleInputAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleInputAve.setStatus("mandatory")
_PowerTrendingSampleInputMin_Type = Integer32
_PowerTrendingSampleInputMin_Object = MibTableColumn
powerTrendingSampleInputMin = _PowerTrendingSampleInputMin_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 4),
    _PowerTrendingSampleInputMin_Type()
)
powerTrendingSampleInputMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleInputMin.setStatus("mandatory")
_PowerTrendingSampleInputMax_Type = Integer32
_PowerTrendingSampleInputMax_Object = MibTableColumn
powerTrendingSampleInputMax = _PowerTrendingSampleInputMax_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 5),
    _PowerTrendingSampleInputMax_Type()
)
powerTrendingSampleInputMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleInputMax.setStatus("mandatory")
_PowerTrendingSampleOutputAve_Type = Integer32
_PowerTrendingSampleOutputAve_Object = MibTableColumn
powerTrendingSampleOutputAve = _PowerTrendingSampleOutputAve_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 6),
    _PowerTrendingSampleOutputAve_Type()
)
powerTrendingSampleOutputAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleOutputAve.setStatus("mandatory")
_PowerTrendingSampleOutputMin_Type = Integer32
_PowerTrendingSampleOutputMin_Object = MibTableColumn
powerTrendingSampleOutputMin = _PowerTrendingSampleOutputMin_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 7),
    _PowerTrendingSampleOutputMin_Type()
)
powerTrendingSampleOutputMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleOutputMin.setStatus("mandatory")
_PowerTrendingSampleOutputMax_Type = Integer32
_PowerTrendingSampleOutputMax_Object = MibTableColumn
powerTrendingSampleOutputMax = _PowerTrendingSampleOutputMax_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 10, 3, 1, 1, 8),
    _PowerTrendingSampleOutputMax_Type()
)
powerTrendingSampleOutputMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleOutputMax.setStatus("mandatory")
_PowerModule_ObjectIdentity = ObjectIdentity
powerModule = _PowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11)
)
_PowerNumber_Type = Gauge32
_PowerNumber_Object = MibScalar
powerNumber = _PowerNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 1),
    _PowerNumber_Type()
)
powerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerNumber.setStatus("mandatory")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("mandatory")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2, 1)
)
powerEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("mandatory")


class _PowerIndex_Type(Integer32):
    """Custom type powerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PowerIndex_Type.__name__ = "Integer32"
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerIndex.setStatus("mandatory")


class _PowerFruName_Type(DisplayString):
    """Custom type powerFruName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerFruName_Type.__name__ = "DisplayString"
_PowerFruName_Object = MibTableColumn
powerFruName = _PowerFruName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2, 1, 2),
    _PowerFruName_Type()
)
powerFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFruName.setStatus("mandatory")


class _PowerPartNumber_Type(DisplayString):
    """Custom type powerPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerPartNumber_Type.__name__ = "DisplayString"
_PowerPartNumber_Object = MibTableColumn
powerPartNumber = _PowerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2, 1, 3),
    _PowerPartNumber_Type()
)
powerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPartNumber.setStatus("mandatory")


class _PowerFRUNumber_Type(DisplayString):
    """Custom type powerFRUNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerFRUNumber_Type.__name__ = "DisplayString"
_PowerFRUNumber_Object = MibTableColumn
powerFRUNumber = _PowerFRUNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2, 1, 4),
    _PowerFRUNumber_Type()
)
powerFRUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFRUNumber.setStatus("mandatory")


class _PowerFRUSerialNumber_Type(DisplayString):
    """Custom type powerFRUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerFRUSerialNumber_Type.__name__ = "DisplayString"
_PowerFRUSerialNumber_Object = MibTableColumn
powerFRUSerialNumber = _PowerFRUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2, 1, 5),
    _PowerFRUSerialNumber_Type()
)
powerFRUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFRUSerialNumber.setStatus("mandatory")


class _PowerHealthStatus_Type(DisplayString):
    """Custom type powerHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerHealthStatus_Type.__name__ = "DisplayString"
_PowerHealthStatus_Object = MibTableColumn
powerHealthStatus = _PowerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 11, 2, 1, 6),
    _PowerHealthStatus_Type()
)
powerHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerHealthStatus.setStatus("mandatory")
_Disks_ObjectIdentity = ObjectIdentity
disks = _Disks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 12)
)
_DiskNumber_Type = Gauge32
_DiskNumber_Object = MibScalar
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 12, 1),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("mandatory")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("mandatory")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 12, 2, 1)
)
diskEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("mandatory")


class _DiskIndex_Type(Integer32):
    """Custom type diskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskIndex_Type.__name__ = "Integer32"
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 12, 2, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIndex.setStatus("mandatory")


class _DiskFruName_Type(DisplayString):
    """Custom type diskFruName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DiskFruName_Type.__name__ = "DisplayString"
_DiskFruName_Object = MibTableColumn
diskFruName = _DiskFruName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 12, 2, 1, 2),
    _DiskFruName_Type()
)
diskFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFruName.setStatus("mandatory")


class _DiskHealthStatus_Type(DisplayString):
    """Custom type diskHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DiskHealthStatus_Type.__name__ = "DisplayString"
_DiskHealthStatus_Object = MibTableColumn
diskHealthStatus = _DiskHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 12, 2, 1, 3),
    _DiskHealthStatus_Type()
)
diskHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskHealthStatus.setStatus("mandatory")
_LocalStorage_ObjectIdentity = ObjectIdentity
localStorage = _LocalStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13)
)
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1)
)


class _RaidOOBCapable_Type(Integer32):
    """Custom type raidOOBCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RaidOOBCapable_Type.__name__ = "Integer32"
_RaidOOBCapable_Object = MibScalar
raidOOBCapable = _RaidOOBCapable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 1),
    _RaidOOBCapable_Type()
)
raidOOBCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidOOBCapable.setStatus("mandatory")
_RaidControllerTable_Object = MibTable
raidControllerTable = _RaidControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    raidControllerTable.setStatus("mandatory")
_RaidControllerEntry_Object = MibTableRow
raidControllerEntry = _RaidControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1)
)
raidControllerEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "raidCtrlIndex"),
)
if mibBuilder.loadTexts:
    raidControllerEntry.setStatus("mandatory")
_RaidCtrlIndex_Type = Integer32
_RaidCtrlIndex_Object = MibTableColumn
raidCtrlIndex = _RaidCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 1),
    _RaidCtrlIndex_Type()
)
raidCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlIndex.setStatus("mandatory")
_RaidCtrlName_Type = DisplayString
_RaidCtrlName_Object = MibTableColumn
raidCtrlName = _RaidCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 2),
    _RaidCtrlName_Type()
)
raidCtrlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlName.setStatus("mandatory")
_RaidCtrlVPDProdName_Type = DisplayString
_RaidCtrlVPDProdName_Object = MibTableColumn
raidCtrlVPDProdName = _RaidCtrlVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 3),
    _RaidCtrlVPDProdName_Type()
)
raidCtrlVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDProdName.setStatus("mandatory")
_RaidCtrlFWPkgVersion_Type = DisplayString
_RaidCtrlFWPkgVersion_Object = MibTableColumn
raidCtrlFWPkgVersion = _RaidCtrlFWPkgVersion_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 4),
    _RaidCtrlFWPkgVersion_Type()
)
raidCtrlFWPkgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlFWPkgVersion.setStatus("mandatory")


class _RaidCtrlBatBCK_Type(Integer32):
    """Custom type raidCtrlBatBCK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uninstalled", 0),
          ("installed", 1))
    )


_RaidCtrlBatBCK_Type.__name__ = "Integer32"
_RaidCtrlBatBCK_Object = MibTableColumn
raidCtrlBatBCK = _RaidCtrlBatBCK_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 5),
    _RaidCtrlBatBCK_Type()
)
raidCtrlBatBCK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCK.setStatus("mandatory")
_RaidCtrlVPDManufacture_Type = DisplayString
_RaidCtrlVPDManufacture_Object = MibTableColumn
raidCtrlVPDManufacture = _RaidCtrlVPDManufacture_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 6),
    _RaidCtrlVPDManufacture_Type()
)
raidCtrlVPDManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDManufacture.setStatus("mandatory")
_RaidCtrlVPDUUID_Type = DisplayString
_RaidCtrlVPDUUID_Object = MibTableColumn
raidCtrlVPDUUID = _RaidCtrlVPDUUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 7),
    _RaidCtrlVPDUUID_Type()
)
raidCtrlVPDUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDUUID.setStatus("mandatory")
_RaidCtrlVPDMachineType_Type = DisplayString
_RaidCtrlVPDMachineType_Object = MibTableColumn
raidCtrlVPDMachineType = _RaidCtrlVPDMachineType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 8),
    _RaidCtrlVPDMachineType_Type()
)
raidCtrlVPDMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDMachineType.setStatus("mandatory")
_RaidCtrlVPDModel_Type = DisplayString
_RaidCtrlVPDModel_Object = MibTableColumn
raidCtrlVPDModel = _RaidCtrlVPDModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 9),
    _RaidCtrlVPDModel_Type()
)
raidCtrlVPDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDModel.setStatus("mandatory")
_RaidCtrlVPDSerialNo_Type = DisplayString
_RaidCtrlVPDSerialNo_Object = MibTableColumn
raidCtrlVPDSerialNo = _RaidCtrlVPDSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 10),
    _RaidCtrlVPDSerialNo_Type()
)
raidCtrlVPDSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDSerialNo.setStatus("mandatory")
_RaidCtrlVPDFRUNo_Type = DisplayString
_RaidCtrlVPDFRUNo_Object = MibTableColumn
raidCtrlVPDFRUNo = _RaidCtrlVPDFRUNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 11),
    _RaidCtrlVPDFRUNo_Type()
)
raidCtrlVPDFRUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDFRUNo.setStatus("mandatory")
_RaidCtrlVPDPartNo_Type = DisplayString
_RaidCtrlVPDPartNo_Object = MibTableColumn
raidCtrlVPDPartNo = _RaidCtrlVPDPartNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 12),
    _RaidCtrlVPDPartNo_Type()
)
raidCtrlVPDPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlVPDPartNo.setStatus("mandatory")
_RaidCtrlCacheMdlStatus_Type = DisplayString
_RaidCtrlCacheMdlStatus_Object = MibTableColumn
raidCtrlCacheMdlStatus = _RaidCtrlCacheMdlStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 13),
    _RaidCtrlCacheMdlStatus_Type()
)
raidCtrlCacheMdlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlCacheMdlStatus.setStatus("mandatory")
_RaidCtrlCacheMdlMemSize_Type = DisplayString
_RaidCtrlCacheMdlMemSize_Object = MibTableColumn
raidCtrlCacheMdlMemSize = _RaidCtrlCacheMdlMemSize_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 14),
    _RaidCtrlCacheMdlMemSize_Type()
)
raidCtrlCacheMdlMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlCacheMdlMemSize.setStatus("mandatory")
_RaidCtrlCacheMdlSerialNo_Type = DisplayString
_RaidCtrlCacheMdlSerialNo_Object = MibTableColumn
raidCtrlCacheMdlSerialNo = _RaidCtrlCacheMdlSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 15),
    _RaidCtrlCacheMdlSerialNo_Type()
)
raidCtrlCacheMdlSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlCacheMdlSerialNo.setStatus("mandatory")
_RaidCtrlPCISlotNo_Type = Integer32
_RaidCtrlPCISlotNo_Object = MibTableColumn
raidCtrlPCISlotNo = _RaidCtrlPCISlotNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 16),
    _RaidCtrlPCISlotNo_Type()
)
raidCtrlPCISlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlPCISlotNo.setStatus("mandatory")
_RaidCtrlPCIBusNo_Type = Integer32
_RaidCtrlPCIBusNo_Object = MibTableColumn
raidCtrlPCIBusNo = _RaidCtrlPCIBusNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 17),
    _RaidCtrlPCIBusNo_Type()
)
raidCtrlPCIBusNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlPCIBusNo.setStatus("mandatory")
_RaidCtrlPCIDevNo_Type = Integer32
_RaidCtrlPCIDevNo_Object = MibTableColumn
raidCtrlPCIDevNo = _RaidCtrlPCIDevNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 18),
    _RaidCtrlPCIDevNo_Type()
)
raidCtrlPCIDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlPCIDevNo.setStatus("mandatory")
_RaidCtrlPCIFuncNo_Type = Integer32
_RaidCtrlPCIFuncNo_Object = MibTableColumn
raidCtrlPCIFuncNo = _RaidCtrlPCIFuncNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 19),
    _RaidCtrlPCIFuncNo_Type()
)
raidCtrlPCIFuncNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlPCIFuncNo.setStatus("mandatory")
_RaidCtrlPCIDevID_Type = DisplayString
_RaidCtrlPCIDevID_Object = MibTableColumn
raidCtrlPCIDevID = _RaidCtrlPCIDevID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 20),
    _RaidCtrlPCIDevID_Type()
)
raidCtrlPCIDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlPCIDevID.setStatus("mandatory")
_RaidCtrlPCISubDevID_Type = DisplayString
_RaidCtrlPCISubDevID_Object = MibTableColumn
raidCtrlPCISubDevID = _RaidCtrlPCISubDevID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 21),
    _RaidCtrlPCISubDevID_Type()
)
raidCtrlPCISubDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlPCISubDevID.setStatus("mandatory")
_RaidCtrlBatBCKProdName_Type = DisplayString
_RaidCtrlBatBCKProdName_Object = MibTableColumn
raidCtrlBatBCKProdName = _RaidCtrlBatBCKProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 22),
    _RaidCtrlBatBCKProdName_Type()
)
raidCtrlBatBCKProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKProdName.setStatus("mandatory")
_RaidCtrlBatBCKManufacture_Type = DisplayString
_RaidCtrlBatBCKManufacture_Object = MibTableColumn
raidCtrlBatBCKManufacture = _RaidCtrlBatBCKManufacture_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 23),
    _RaidCtrlBatBCKManufacture_Type()
)
raidCtrlBatBCKManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKManufacture.setStatus("mandatory")
_RaidCtrlBatBCKStatus_Type = DisplayString
_RaidCtrlBatBCKStatus_Object = MibTableColumn
raidCtrlBatBCKStatus = _RaidCtrlBatBCKStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 24),
    _RaidCtrlBatBCKStatus_Type()
)
raidCtrlBatBCKStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKStatus.setStatus("mandatory")
_RaidCtrlBatBCKType_Type = DisplayString
_RaidCtrlBatBCKType_Object = MibTableColumn
raidCtrlBatBCKType = _RaidCtrlBatBCKType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 25),
    _RaidCtrlBatBCKType_Type()
)
raidCtrlBatBCKType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKType.setStatus("mandatory")
_RaidCtrlBatBCKChem_Type = DisplayString
_RaidCtrlBatBCKChem_Object = MibTableColumn
raidCtrlBatBCKChem = _RaidCtrlBatBCKChem_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 26),
    _RaidCtrlBatBCKChem_Type()
)
raidCtrlBatBCKChem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKChem.setStatus("mandatory")
_RaidCtrlBatBCKSerialNo_Type = DisplayString
_RaidCtrlBatBCKSerialNo_Object = MibTableColumn
raidCtrlBatBCKSerialNo = _RaidCtrlBatBCKSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 27),
    _RaidCtrlBatBCKSerialNo_Type()
)
raidCtrlBatBCKSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKSerialNo.setStatus("mandatory")
_RaidCtrlBatBCKChgCap_Type = DisplayString
_RaidCtrlBatBCKChgCap_Object = MibTableColumn
raidCtrlBatBCKChgCap = _RaidCtrlBatBCKChgCap_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 28),
    _RaidCtrlBatBCKChgCap_Type()
)
raidCtrlBatBCKChgCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKChgCap.setStatus("mandatory")
_RaidCtrlBatBCKFirmware_Type = DisplayString
_RaidCtrlBatBCKFirmware_Object = MibTableColumn
raidCtrlBatBCKFirmware = _RaidCtrlBatBCKFirmware_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 29),
    _RaidCtrlBatBCKFirmware_Type()
)
raidCtrlBatBCKFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKFirmware.setStatus("mandatory")
_RaidCtrlBatBCKDgnVoltage_Type = DisplayString
_RaidCtrlBatBCKDgnVoltage_Object = MibTableColumn
raidCtrlBatBCKDgnVoltage = _RaidCtrlBatBCKDgnVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 30),
    _RaidCtrlBatBCKDgnVoltage_Type()
)
raidCtrlBatBCKDgnVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKDgnVoltage.setStatus("mandatory")
_RaidCtrlBatBCKVoltage_Type = DisplayString
_RaidCtrlBatBCKVoltage_Object = MibTableColumn
raidCtrlBatBCKVoltage = _RaidCtrlBatBCKVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 31),
    _RaidCtrlBatBCKVoltage_Type()
)
raidCtrlBatBCKVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKVoltage.setStatus("mandatory")
_RaidCtrlBatCurrent_Type = DisplayString
_RaidCtrlBatCurrent_Object = MibTableColumn
raidCtrlBatCurrent = _RaidCtrlBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 32),
    _RaidCtrlBatCurrent_Type()
)
raidCtrlBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatCurrent.setStatus("mandatory")
_RaidCtrlBatBCKDgnChgCap_Type = DisplayString
_RaidCtrlBatBCKDgnChgCap_Object = MibTableColumn
raidCtrlBatBCKDgnChgCap = _RaidCtrlBatBCKDgnChgCap_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 33),
    _RaidCtrlBatBCKDgnChgCap_Type()
)
raidCtrlBatBCKDgnChgCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKDgnChgCap.setStatus("mandatory")
_RaidCtrlBatBCKCrtTemp_Type = DisplayString
_RaidCtrlBatBCKCrtTemp_Object = MibTableColumn
raidCtrlBatBCKCrtTemp = _RaidCtrlBatBCKCrtTemp_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 34),
    _RaidCtrlBatBCKCrtTemp_Type()
)
raidCtrlBatBCKCrtTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlBatBCKCrtTemp.setStatus("mandatory")
_RaidCtrlFWNames_Type = DisplayString
_RaidCtrlFWNames_Object = MibTableColumn
raidCtrlFWNames = _RaidCtrlFWNames_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 35),
    _RaidCtrlFWNames_Type()
)
raidCtrlFWNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlFWNames.setStatus("mandatory")
_RaidCtrlPortDetails_Type = DisplayString
_RaidCtrlPortDetails_Object = MibTableColumn
raidCtrlPortDetails = _RaidCtrlPortDetails_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 36),
    _RaidCtrlPortDetails_Type()
)
raidCtrlPortDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlPortDetails.setStatus("mandatory")
_RaidCtrlStoragepools_Type = DisplayString
_RaidCtrlStoragepools_Object = MibTableColumn
raidCtrlStoragepools = _RaidCtrlStoragepools_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 37),
    _RaidCtrlStoragepools_Type()
)
raidCtrlStoragepools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlStoragepools.setStatus("mandatory")
_RaidCtrlDrives_Type = DisplayString
_RaidCtrlDrives_Object = MibTableColumn
raidCtrlDrives = _RaidCtrlDrives_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 2, 1, 38),
    _RaidCtrlDrives_Type()
)
raidCtrlDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCtrlDrives.setStatus("mandatory")
_RaidDriveTable_Object = MibTable
raidDriveTable = _RaidDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    raidDriveTable.setStatus("mandatory")
_RaidDriveEntry_Object = MibTableRow
raidDriveEntry = _RaidDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1)
)
raidDriveEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "raidDriveIndex"),
)
if mibBuilder.loadTexts:
    raidDriveEntry.setStatus("mandatory")
_RaidDriveIndex_Type = Integer32
_RaidDriveIndex_Object = MibTableColumn
raidDriveIndex = _RaidDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 1),
    _RaidDriveIndex_Type()
)
raidDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveIndex.setStatus("mandatory")
_RaidDriveName_Type = DisplayString
_RaidDriveName_Object = MibTableColumn
raidDriveName = _RaidDriveName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 2),
    _RaidDriveName_Type()
)
raidDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveName.setStatus("mandatory")
_RaidDriveVPDProdName_Type = DisplayString
_RaidDriveVPDProdName_Object = MibTableColumn
raidDriveVPDProdName = _RaidDriveVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 3),
    _RaidDriveVPDProdName_Type()
)
raidDriveVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveVPDProdName.setStatus("mandatory")
_RaidDriveState_Type = DisplayString
_RaidDriveState_Object = MibTableColumn
raidDriveState = _RaidDriveState_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 4),
    _RaidDriveState_Type()
)
raidDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveState.setStatus("mandatory")
_RaidDriveSlotNo_Type = Integer32
_RaidDriveSlotNo_Object = MibTableColumn
raidDriveSlotNo = _RaidDriveSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 5),
    _RaidDriveSlotNo_Type()
)
raidDriveSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveSlotNo.setStatus("mandatory")
_RaidDriveDeviceID_Type = DisplayString
_RaidDriveDeviceID_Object = MibTableColumn
raidDriveDeviceID = _RaidDriveDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 6),
    _RaidDriveDeviceID_Type()
)
raidDriveDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveDeviceID.setStatus("mandatory")
_RaidDriveDiskType_Type = DisplayString
_RaidDriveDiskType_Object = MibTableColumn
raidDriveDiskType = _RaidDriveDiskType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 7),
    _RaidDriveDiskType_Type()
)
raidDriveDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveDiskType.setStatus("mandatory")
_RaidDriveMediaType_Type = DisplayString
_RaidDriveMediaType_Object = MibTableColumn
raidDriveMediaType = _RaidDriveMediaType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 8),
    _RaidDriveMediaType_Type()
)
raidDriveMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveMediaType.setStatus("mandatory")
_RaidDriveSpeed_Type = DisplayString
_RaidDriveSpeed_Object = MibTableColumn
raidDriveSpeed = _RaidDriveSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 9),
    _RaidDriveSpeed_Type()
)
raidDriveSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveSpeed.setStatus("mandatory")
_RaidDriveCurTemp_Type = DisplayString
_RaidDriveCurTemp_Object = MibTableColumn
raidDriveCurTemp = _RaidDriveCurTemp_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 10),
    _RaidDriveCurTemp_Type()
)
raidDriveCurTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveCurTemp.setStatus("mandatory")
_RaidDriveHealthStataus_Type = DisplayString
_RaidDriveHealthStataus_Object = MibTableColumn
raidDriveHealthStataus = _RaidDriveHealthStataus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 11),
    _RaidDriveHealthStataus_Type()
)
raidDriveHealthStataus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveHealthStataus.setStatus("mandatory")
_RaidDriveCapacity_Type = DisplayString
_RaidDriveCapacity_Object = MibTableColumn
raidDriveCapacity = _RaidDriveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 12),
    _RaidDriveCapacity_Type()
)
raidDriveCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveCapacity.setStatus("mandatory")
_RaidDriveVPDManufacture_Type = DisplayString
_RaidDriveVPDManufacture_Object = MibTableColumn
raidDriveVPDManufacture = _RaidDriveVPDManufacture_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 13),
    _RaidDriveVPDManufacture_Type()
)
raidDriveVPDManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveVPDManufacture.setStatus("mandatory")
_RaidDriveEnclosureID_Type = DisplayString
_RaidDriveEnclosureID_Object = MibTableColumn
raidDriveEnclosureID = _RaidDriveEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 14),
    _RaidDriveEnclosureID_Type()
)
raidDriveEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveEnclosureID.setStatus("mandatory")
_RaidDriveVPDMachineType_Type = DisplayString
_RaidDriveVPDMachineType_Object = MibTableColumn
raidDriveVPDMachineType = _RaidDriveVPDMachineType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 15),
    _RaidDriveVPDMachineType_Type()
)
raidDriveVPDMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveVPDMachineType.setStatus("mandatory")
_RaidDriveVPDModel_Type = DisplayString
_RaidDriveVPDModel_Object = MibTableColumn
raidDriveVPDModel = _RaidDriveVPDModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 16),
    _RaidDriveVPDModel_Type()
)
raidDriveVPDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveVPDModel.setStatus("mandatory")
_RaidDriveVPDSerialNo_Type = DisplayString
_RaidDriveVPDSerialNo_Object = MibTableColumn
raidDriveVPDSerialNo = _RaidDriveVPDSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 17),
    _RaidDriveVPDSerialNo_Type()
)
raidDriveVPDSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveVPDSerialNo.setStatus("mandatory")
_RaidDriveVPDFRUNo_Type = DisplayString
_RaidDriveVPDFRUNo_Object = MibTableColumn
raidDriveVPDFRUNo = _RaidDriveVPDFRUNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 18),
    _RaidDriveVPDFRUNo_Type()
)
raidDriveVPDFRUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveVPDFRUNo.setStatus("mandatory")
_RaidDriveVPDPartNo_Type = DisplayString
_RaidDriveVPDPartNo_Object = MibTableColumn
raidDriveVPDPartNo = _RaidDriveVPDPartNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 19),
    _RaidDriveVPDPartNo_Type()
)
raidDriveVPDPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveVPDPartNo.setStatus("mandatory")
_RaidDriveFWNames_Type = DisplayString
_RaidDriveFWNames_Object = MibTableColumn
raidDriveFWNames = _RaidDriveFWNames_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 20),
    _RaidDriveFWNames_Type()
)
raidDriveFWNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFWNames.setStatus("mandatory")
_RaidDriveRotationRate_Type = DisplayString
_RaidDriveRotationRate_Object = MibTableColumn
raidDriveRotationRate = _RaidDriveRotationRate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 21),
    _RaidDriveRotationRate_Type()
)
raidDriveRotationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveRotationRate.setStatus("mandatory")
_RaidDriveMediaErrCnt_Type = Gauge32
_RaidDriveMediaErrCnt_Object = MibTableColumn
raidDriveMediaErrCnt = _RaidDriveMediaErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 22),
    _RaidDriveMediaErrCnt_Type()
)
raidDriveMediaErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveMediaErrCnt.setStatus("mandatory")
_RaidDriveOtherErrCnt_Type = Gauge32
_RaidDriveOtherErrCnt_Object = MibTableColumn
raidDriveOtherErrCnt = _RaidDriveOtherErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 23),
    _RaidDriveOtherErrCnt_Type()
)
raidDriveOtherErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveOtherErrCnt.setStatus("mandatory")
_RaidDrivePredFailCnt_Type = Gauge32
_RaidDrivePredFailCnt_Object = MibTableColumn
raidDrivePredFailCnt = _RaidDrivePredFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 24),
    _RaidDrivePredFailCnt_Type()
)
raidDrivePredFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDrivePredFailCnt.setStatus("mandatory")
_RaidDriveRemainingLife_Type = DisplayString
_RaidDriveRemainingLife_Object = MibTableColumn
raidDriveRemainingLife = _RaidDriveRemainingLife_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 25),
    _RaidDriveRemainingLife_Type()
)
raidDriveRemainingLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveRemainingLife.setStatus("mandatory")


class _RaidDriveFdeCapable_Type(Integer32):
    """Custom type raidDriveFdeCapable based on Integer32"""
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


_RaidDriveFdeCapable_Type.__name__ = "Integer32"
_RaidDriveFdeCapable_Object = MibTableColumn
raidDriveFdeCapable = _RaidDriveFdeCapable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 26),
    _RaidDriveFdeCapable_Type()
)
raidDriveFdeCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFdeCapable.setStatus("mandatory")


class _RaidDriveSecured_Type(Integer32):
    """Custom type raidDriveSecured based on Integer32"""
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


_RaidDriveSecured_Type.__name__ = "Integer32"
_RaidDriveSecured_Object = MibTableColumn
raidDriveSecured = _RaidDriveSecured_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 3, 1, 27),
    _RaidDriveSecured_Type()
)
raidDriveSecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveSecured.setStatus("mandatory")
_RaidControllerFirmwareTable_Object = MibTable
raidControllerFirmwareTable = _RaidControllerFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4)
)
if mibBuilder.loadTexts:
    raidControllerFirmwareTable.setStatus("mandatory")
_RaidControllerFirmwareEntry_Object = MibTableRow
raidControllerFirmwareEntry = _RaidControllerFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1)
)
raidControllerFirmwareEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "raidControllerFirmwareIndex"),
)
if mibBuilder.loadTexts:
    raidControllerFirmwareEntry.setStatus("mandatory")
_RaidControllerFirmwareIndex_Type = Integer32
_RaidControllerFirmwareIndex_Object = MibTableColumn
raidControllerFirmwareIndex = _RaidControllerFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1, 1),
    _RaidControllerFirmwareIndex_Type()
)
raidControllerFirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerFirmwareIndex.setStatus("mandatory")
_RaidControllerFirmwareName_Type = DisplayString
_RaidControllerFirmwareName_Object = MibTableColumn
raidControllerFirmwareName = _RaidControllerFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1, 2),
    _RaidControllerFirmwareName_Type()
)
raidControllerFirmwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerFirmwareName.setStatus("mandatory")
_RaidControllerFirmwareCtrlName_Type = DisplayString
_RaidControllerFirmwareCtrlName_Object = MibTableColumn
raidControllerFirmwareCtrlName = _RaidControllerFirmwareCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1, 3),
    _RaidControllerFirmwareCtrlName_Type()
)
raidControllerFirmwareCtrlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerFirmwareCtrlName.setStatus("mandatory")
_RaidControllerFirmwareDescription_Type = DisplayString
_RaidControllerFirmwareDescription_Object = MibTableColumn
raidControllerFirmwareDescription = _RaidControllerFirmwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1, 4),
    _RaidControllerFirmwareDescription_Type()
)
raidControllerFirmwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerFirmwareDescription.setStatus("mandatory")
_RaidControllerFirmwareManufacture_Type = DisplayString
_RaidControllerFirmwareManufacture_Object = MibTableColumn
raidControllerFirmwareManufacture = _RaidControllerFirmwareManufacture_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1, 5),
    _RaidControllerFirmwareManufacture_Type()
)
raidControllerFirmwareManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerFirmwareManufacture.setStatus("mandatory")
_RaidControllerFirmwareVersion_Type = DisplayString
_RaidControllerFirmwareVersion_Object = MibTableColumn
raidControllerFirmwareVersion = _RaidControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1, 6),
    _RaidControllerFirmwareVersion_Type()
)
raidControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerFirmwareVersion.setStatus("mandatory")
_RaidControllerFirmwareReleaseDate_Type = DisplayString
_RaidControllerFirmwareReleaseDate_Object = MibTableColumn
raidControllerFirmwareReleaseDate = _RaidControllerFirmwareReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 4, 1, 7),
    _RaidControllerFirmwareReleaseDate_Type()
)
raidControllerFirmwareReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidControllerFirmwareReleaseDate.setStatus("mandatory")
_RaidDriveFirmwareTable_Object = MibTable
raidDriveFirmwareTable = _RaidDriveFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5)
)
if mibBuilder.loadTexts:
    raidDriveFirmwareTable.setStatus("mandatory")
_RaidDriveFirmwareEntry_Object = MibTableRow
raidDriveFirmwareEntry = _RaidDriveFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1)
)
raidDriveFirmwareEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "raidDriveFirmwareIndex"),
)
if mibBuilder.loadTexts:
    raidDriveFirmwareEntry.setStatus("mandatory")
_RaidDriveFirmwareIndex_Type = Integer32
_RaidDriveFirmwareIndex_Object = MibTableColumn
raidDriveFirmwareIndex = _RaidDriveFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1, 1),
    _RaidDriveFirmwareIndex_Type()
)
raidDriveFirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFirmwareIndex.setStatus("mandatory")
_RaidDriveFirmwareName_Type = DisplayString
_RaidDriveFirmwareName_Object = MibTableColumn
raidDriveFirmwareName = _RaidDriveFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1, 2),
    _RaidDriveFirmwareName_Type()
)
raidDriveFirmwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFirmwareName.setStatus("mandatory")
_RaidDriveFirmwareDriveName_Type = DisplayString
_RaidDriveFirmwareDriveName_Object = MibTableColumn
raidDriveFirmwareDriveName = _RaidDriveFirmwareDriveName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1, 3),
    _RaidDriveFirmwareDriveName_Type()
)
raidDriveFirmwareDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFirmwareDriveName.setStatus("mandatory")
_RaidDriveFirmwareDescription_Type = DisplayString
_RaidDriveFirmwareDescription_Object = MibTableColumn
raidDriveFirmwareDescription = _RaidDriveFirmwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1, 4),
    _RaidDriveFirmwareDescription_Type()
)
raidDriveFirmwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFirmwareDescription.setStatus("mandatory")
_RaidDriveFirmwareManufacture_Type = DisplayString
_RaidDriveFirmwareManufacture_Object = MibTableColumn
raidDriveFirmwareManufacture = _RaidDriveFirmwareManufacture_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1, 5),
    _RaidDriveFirmwareManufacture_Type()
)
raidDriveFirmwareManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFirmwareManufacture.setStatus("mandatory")
_RaidDriveFirmwareVersion_Type = DisplayString
_RaidDriveFirmwareVersion_Object = MibTableColumn
raidDriveFirmwareVersion = _RaidDriveFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1, 6),
    _RaidDriveFirmwareVersion_Type()
)
raidDriveFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFirmwareVersion.setStatus("mandatory")
_RaidDriveFirmwareReleaseDate_Type = DisplayString
_RaidDriveFirmwareReleaseDate_Object = MibTableColumn
raidDriveFirmwareReleaseDate = _RaidDriveFirmwareReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 5, 1, 7),
    _RaidDriveFirmwareReleaseDate_Type()
)
raidDriveFirmwareReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDriveFirmwareReleaseDate.setStatus("mandatory")
_RaidStoragepoolTable_Object = MibTable
raidStoragepoolTable = _RaidStoragepoolTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6)
)
if mibBuilder.loadTexts:
    raidStoragepoolTable.setStatus("mandatory")
_RaidStoragepoolEntry_Object = MibTableRow
raidStoragepoolEntry = _RaidStoragepoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1)
)
raidStoragepoolEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "raidStoragepoolIndex"),
)
if mibBuilder.loadTexts:
    raidStoragepoolEntry.setStatus("mandatory")
_RaidStoragepoolIndex_Type = Integer32
_RaidStoragepoolIndex_Object = MibTableColumn
raidStoragepoolIndex = _RaidStoragepoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1, 1),
    _RaidStoragepoolIndex_Type()
)
raidStoragepoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStoragepoolIndex.setStatus("mandatory")
_RaidStoragepoolName_Type = DisplayString
_RaidStoragepoolName_Object = MibTableColumn
raidStoragepoolName = _RaidStoragepoolName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1, 2),
    _RaidStoragepoolName_Type()
)
raidStoragepoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStoragepoolName.setStatus("mandatory")
_RaidStoragepoolControllerName_Type = DisplayString
_RaidStoragepoolControllerName_Object = MibTableColumn
raidStoragepoolControllerName = _RaidStoragepoolControllerName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1, 3),
    _RaidStoragepoolControllerName_Type()
)
raidStoragepoolControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStoragepoolControllerName.setStatus("mandatory")
_RaidStoragepoolState_Type = DisplayString
_RaidStoragepoolState_Object = MibTableColumn
raidStoragepoolState = _RaidStoragepoolState_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1, 4),
    _RaidStoragepoolState_Type()
)
raidStoragepoolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStoragepoolState.setStatus("mandatory")
_RaidStoragepoolCapacity_Type = DisplayString
_RaidStoragepoolCapacity_Object = MibTableColumn
raidStoragepoolCapacity = _RaidStoragepoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1, 5),
    _RaidStoragepoolCapacity_Type()
)
raidStoragepoolCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStoragepoolCapacity.setStatus("mandatory")
_RaidStoragepoolVols_Type = DisplayString
_RaidStoragepoolVols_Object = MibTableColumn
raidStoragepoolVols = _RaidStoragepoolVols_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1, 6),
    _RaidStoragepoolVols_Type()
)
raidStoragepoolVols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStoragepoolVols.setStatus("mandatory")
_RaidStoragepoolDrives_Type = DisplayString
_RaidStoragepoolDrives_Object = MibTableColumn
raidStoragepoolDrives = _RaidStoragepoolDrives_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 6, 1, 7),
    _RaidStoragepoolDrives_Type()
)
raidStoragepoolDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStoragepoolDrives.setStatus("mandatory")
_RaidVolumeTable_Object = MibTable
raidVolumeTable = _RaidVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7)
)
if mibBuilder.loadTexts:
    raidVolumeTable.setStatus("mandatory")
_RaidVolumeEntry_Object = MibTableRow
raidVolumeEntry = _RaidVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1)
)
raidVolumeEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "raidVolumeIndex"),
)
if mibBuilder.loadTexts:
    raidVolumeEntry.setStatus("mandatory")
_RaidVolumeIndex_Type = Integer32
_RaidVolumeIndex_Object = MibTableColumn
raidVolumeIndex = _RaidVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1, 1),
    _RaidVolumeIndex_Type()
)
raidVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeIndex.setStatus("mandatory")
_RaidVolumeName_Type = DisplayString
_RaidVolumeName_Object = MibTableColumn
raidVolumeName = _RaidVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1, 2),
    _RaidVolumeName_Type()
)
raidVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeName.setStatus("mandatory")
_RaidVolumeControllerName_Type = DisplayString
_RaidVolumeControllerName_Object = MibTableColumn
raidVolumeControllerName = _RaidVolumeControllerName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1, 3),
    _RaidVolumeControllerName_Type()
)
raidVolumeControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeControllerName.setStatus("mandatory")
_RaidVolumeStatus_Type = DisplayString
_RaidVolumeStatus_Object = MibTableColumn
raidVolumeStatus = _RaidVolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1, 4),
    _RaidVolumeStatus_Type()
)
raidVolumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeStatus.setStatus("mandatory")
_RaidVolumeCapacity_Type = DisplayString
_RaidVolumeCapacity_Object = MibTableColumn
raidVolumeCapacity = _RaidVolumeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1, 5),
    _RaidVolumeCapacity_Type()
)
raidVolumeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeCapacity.setStatus("mandatory")
_RaidVolumeStripSize_Type = DisplayString
_RaidVolumeStripSize_Object = MibTableColumn
raidVolumeStripSize = _RaidVolumeStripSize_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1, 6),
    _RaidVolumeStripSize_Type()
)
raidVolumeStripSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeStripSize.setStatus("mandatory")
_RaidVolumeBootable_Type = DisplayString
_RaidVolumeBootable_Object = MibTableColumn
raidVolumeBootable = _RaidVolumeBootable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 13, 1, 7, 1, 7),
    _RaidVolumeBootable_Type()
)
raidVolumeBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeBootable.setStatus("mandatory")
_Adapters_ObjectIdentity = ObjectIdentity
adapters = _Adapters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14)
)


class _AdapterOOBCapable_Type(Integer32):
    """Custom type adapterOOBCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdapterOOBCapable_Type.__name__ = "Integer32"
_AdapterOOBCapable_Object = MibScalar
adapterOOBCapable = _AdapterOOBCapable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 1),
    _AdapterOOBCapable_Type()
)
adapterOOBCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterOOBCapable.setStatus("mandatory")
_AdapterGenericTable_Object = MibTable
adapterGenericTable = _AdapterGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    adapterGenericTable.setStatus("mandatory")
_AdapterGenericEntry_Object = MibTableRow
adapterGenericEntry = _AdapterGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 2, 1)
)
adapterGenericEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "adapterGenericIndex"),
)
if mibBuilder.loadTexts:
    adapterGenericEntry.setStatus("mandatory")
_AdapterGenericIndex_Type = Integer32
_AdapterGenericIndex_Object = MibTableColumn
adapterGenericIndex = _AdapterGenericIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 2, 1, 1),
    _AdapterGenericIndex_Type()
)
adapterGenericIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGenericIndex.setStatus("mandatory")
_AdapterGenericVPDProdName_Type = DisplayString
_AdapterGenericVPDProdName_Object = MibTableColumn
adapterGenericVPDProdName = _AdapterGenericVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 2, 1, 2),
    _AdapterGenericVPDProdName_Type()
)
adapterGenericVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGenericVPDProdName.setStatus("mandatory")
_AdapterGenericSlotNo_Type = Integer32
_AdapterGenericSlotNo_Object = MibTableColumn
adapterGenericSlotNo = _AdapterGenericSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 2, 1, 3),
    _AdapterGenericSlotNo_Type()
)
adapterGenericSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGenericSlotNo.setStatus("mandatory")
_AdapterGenericLocation_Type = DisplayString
_AdapterGenericLocation_Object = MibTableColumn
adapterGenericLocation = _AdapterGenericLocation_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 2, 1, 4),
    _AdapterGenericLocation_Type()
)
adapterGenericLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGenericLocation.setStatus("mandatory")
_AdapterGenericCardInterface_Type = DisplayString
_AdapterGenericCardInterface_Object = MibTableColumn
adapterGenericCardInterface = _AdapterGenericCardInterface_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 2, 1, 5),
    _AdapterGenericCardInterface_Type()
)
adapterGenericCardInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGenericCardInterface.setStatus("mandatory")
_AdapterNetworkFunctionTable_Object = MibTable
adapterNetworkFunctionTable = _AdapterNetworkFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3)
)
if mibBuilder.loadTexts:
    adapterNetworkFunctionTable.setStatus("mandatory")
_AdapterNetworkFunctionEntry_Object = MibTableRow
adapterNetworkFunctionEntry = _AdapterNetworkFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1)
)
adapterNetworkFunctionEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "adapterNetworkFunctionIndex"),
)
if mibBuilder.loadTexts:
    adapterNetworkFunctionEntry.setStatus("mandatory")
_AdapterNetworkFunctionIndex_Type = Integer32
_AdapterNetworkFunctionIndex_Object = MibTableColumn
adapterNetworkFunctionIndex = _AdapterNetworkFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 1),
    _AdapterNetworkFunctionIndex_Type()
)
adapterNetworkFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionIndex.setStatus("mandatory")
_AdapterNetworkFunctionNetworkVPDProdName_Type = DisplayString
_AdapterNetworkFunctionNetworkVPDProdName_Object = MibTableColumn
adapterNetworkFunctionNetworkVPDProdName = _AdapterNetworkFunctionNetworkVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 2),
    _AdapterNetworkFunctionNetworkVPDProdName_Type()
)
adapterNetworkFunctionNetworkVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionNetworkVPDProdName.setStatus("mandatory")
_AdapterNetworkFunctionAdapterVPDProdName_Type = DisplayString
_AdapterNetworkFunctionAdapterVPDProdName_Object = MibTableColumn
adapterNetworkFunctionAdapterVPDProdName = _AdapterNetworkFunctionAdapterVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 3),
    _AdapterNetworkFunctionAdapterVPDProdName_Type()
)
adapterNetworkFunctionAdapterVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionAdapterVPDProdName.setStatus("mandatory")
_AdapterNetworkFunctionNetworkVPDManufacturer_Type = DisplayString
_AdapterNetworkFunctionNetworkVPDManufacturer_Object = MibTableColumn
adapterNetworkFunctionNetworkVPDManufacturer = _AdapterNetworkFunctionNetworkVPDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 4),
    _AdapterNetworkFunctionNetworkVPDManufacturer_Type()
)
adapterNetworkFunctionNetworkVPDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionNetworkVPDManufacturer.setStatus("mandatory")
_AdapterNetworkFunctionNetworkVPDUUID_Type = DisplayString
_AdapterNetworkFunctionNetworkVPDUUID_Object = MibTableColumn
adapterNetworkFunctionNetworkVPDUUID = _AdapterNetworkFunctionNetworkVPDUUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 5),
    _AdapterNetworkFunctionNetworkVPDUUID_Type()
)
adapterNetworkFunctionNetworkVPDUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionNetworkVPDUUID.setStatus("mandatory")
_AdapterNetworkFunctionNetworkVPDModel_Type = DisplayString
_AdapterNetworkFunctionNetworkVPDModel_Object = MibTableColumn
adapterNetworkFunctionNetworkVPDModel = _AdapterNetworkFunctionNetworkVPDModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 6),
    _AdapterNetworkFunctionNetworkVPDModel_Type()
)
adapterNetworkFunctionNetworkVPDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionNetworkVPDModel.setStatus("mandatory")
_AdapterNetworkFunctionNetworkVPDSerialNo_Type = DisplayString
_AdapterNetworkFunctionNetworkVPDSerialNo_Object = MibTableColumn
adapterNetworkFunctionNetworkVPDSerialNo = _AdapterNetworkFunctionNetworkVPDSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 7),
    _AdapterNetworkFunctionNetworkVPDSerialNo_Type()
)
adapterNetworkFunctionNetworkVPDSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionNetworkVPDSerialNo.setStatus("mandatory")
_AdapterNetworkFunctionNetworkVPDFRUNo_Type = DisplayString
_AdapterNetworkFunctionNetworkVPDFRUNo_Object = MibTableColumn
adapterNetworkFunctionNetworkVPDFRUNo = _AdapterNetworkFunctionNetworkVPDFRUNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 8),
    _AdapterNetworkFunctionNetworkVPDFRUNo_Type()
)
adapterNetworkFunctionNetworkVPDFRUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionNetworkVPDFRUNo.setStatus("mandatory")
_AdapterNetworkFunctionNetworkVPDPartNo_Type = DisplayString
_AdapterNetworkFunctionNetworkVPDPartNo_Object = MibTableColumn
adapterNetworkFunctionNetworkVPDPartNo = _AdapterNetworkFunctionNetworkVPDPartNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 9),
    _AdapterNetworkFunctionNetworkVPDPartNo_Type()
)
adapterNetworkFunctionNetworkVPDPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionNetworkVPDPartNo.setStatus("mandatory")
_AdapterNetworkFunctionFoDUID_Type = DisplayString
_AdapterNetworkFunctionFoDUID_Object = MibTableColumn
adapterNetworkFunctionFoDUID = _AdapterNetworkFunctionFoDUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 10),
    _AdapterNetworkFunctionFoDUID_Type()
)
adapterNetworkFunctionFoDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionFoDUID.setStatus("mandatory")


class _AdapterNetworkFunctionSupportHotPlug_Type(Integer32):
    """Custom type adapterNetworkFunctionSupportHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AdapterNetworkFunctionSupportHotPlug_Type.__name__ = "Integer32"
_AdapterNetworkFunctionSupportHotPlug_Object = MibTableColumn
adapterNetworkFunctionSupportHotPlug = _AdapterNetworkFunctionSupportHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 11),
    _AdapterNetworkFunctionSupportHotPlug_Type()
)
adapterNetworkFunctionSupportHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionSupportHotPlug.setStatus("mandatory")
_AdapterNetworkFunctionPhysicalPortNumber_Type = Integer32
_AdapterNetworkFunctionPhysicalPortNumber_Object = MibTableColumn
adapterNetworkFunctionPhysicalPortNumber = _AdapterNetworkFunctionPhysicalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 12),
    _AdapterNetworkFunctionPhysicalPortNumber_Type()
)
adapterNetworkFunctionPhysicalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPhysicalPortNumber.setStatus("mandatory")
_AdapterNetworkFunctionMaxPortNumber_Type = Integer32
_AdapterNetworkFunctionMaxPortNumber_Object = MibTableColumn
adapterNetworkFunctionMaxPortNumber = _AdapterNetworkFunctionMaxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 13),
    _AdapterNetworkFunctionMaxPortNumber_Type()
)
adapterNetworkFunctionMaxPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionMaxPortNumber.setStatus("mandatory")
_AdapterNetworkFunctionPortNumber_Type = Integer32
_AdapterNetworkFunctionPortNumber_Object = MibTableColumn
adapterNetworkFunctionPortNumber = _AdapterNetworkFunctionPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 14),
    _AdapterNetworkFunctionPortNumber_Type()
)
adapterNetworkFunctionPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPortNumber.setStatus("mandatory")
_AdapterNetworkFunctionMaxDataWidth_Type = Integer32
_AdapterNetworkFunctionMaxDataWidth_Object = MibTableColumn
adapterNetworkFunctionMaxDataWidth = _AdapterNetworkFunctionMaxDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 15),
    _AdapterNetworkFunctionMaxDataWidth_Type()
)
adapterNetworkFunctionMaxDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionMaxDataWidth.setStatus("mandatory")
_AdapterNetworkFunctionPackageType_Type = DisplayString
_AdapterNetworkFunctionPackageType_Object = MibTableColumn
adapterNetworkFunctionPackageType = _AdapterNetworkFunctionPackageType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 16),
    _AdapterNetworkFunctionPackageType_Type()
)
adapterNetworkFunctionPackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPackageType.setStatus("mandatory")
_AdapterNetworkFunctionPCIBusNo_Type = Integer32
_AdapterNetworkFunctionPCIBusNo_Object = MibTableColumn
adapterNetworkFunctionPCIBusNo = _AdapterNetworkFunctionPCIBusNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 17),
    _AdapterNetworkFunctionPCIBusNo_Type()
)
adapterNetworkFunctionPCIBusNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCIBusNo.setStatus("mandatory")
_AdapterNetworkFunctionPCIDevNo_Type = Integer32
_AdapterNetworkFunctionPCIDevNo_Object = MibTableColumn
adapterNetworkFunctionPCIDevNo = _AdapterNetworkFunctionPCIDevNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 18),
    _AdapterNetworkFunctionPCIDevNo_Type()
)
adapterNetworkFunctionPCIDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCIDevNo.setStatus("mandatory")
_AdapterNetworkFunctionPCIFuncNo_Type = Integer32
_AdapterNetworkFunctionPCIFuncNo_Object = MibTableColumn
adapterNetworkFunctionPCIFuncNo = _AdapterNetworkFunctionPCIFuncNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 19),
    _AdapterNetworkFunctionPCIFuncNo_Type()
)
adapterNetworkFunctionPCIFuncNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCIFuncNo.setStatus("mandatory")
_AdapterNetworkFunctionPCIVendorId_Type = DisplayString
_AdapterNetworkFunctionPCIVendorId_Object = MibTableColumn
adapterNetworkFunctionPCIVendorId = _AdapterNetworkFunctionPCIVendorId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 20),
    _AdapterNetworkFunctionPCIVendorId_Type()
)
adapterNetworkFunctionPCIVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCIVendorId.setStatus("mandatory")
_AdapterNetworkFunctionPCIDevId_Type = DisplayString
_AdapterNetworkFunctionPCIDevId_Object = MibTableColumn
adapterNetworkFunctionPCIDevId = _AdapterNetworkFunctionPCIDevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 21),
    _AdapterNetworkFunctionPCIDevId_Type()
)
adapterNetworkFunctionPCIDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCIDevId.setStatus("mandatory")
_AdapterNetworkFunctionPCIDevType_Type = DisplayString
_AdapterNetworkFunctionPCIDevType_Object = MibTableColumn
adapterNetworkFunctionPCIDevType = _AdapterNetworkFunctionPCIDevType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 22),
    _AdapterNetworkFunctionPCIDevType_Type()
)
adapterNetworkFunctionPCIDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCIDevType.setStatus("mandatory")
_AdapterNetworkFunctionPCIRevId_Type = DisplayString
_AdapterNetworkFunctionPCIRevId_Object = MibTableColumn
adapterNetworkFunctionPCIRevId = _AdapterNetworkFunctionPCIRevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 23),
    _AdapterNetworkFunctionPCIRevId_Type()
)
adapterNetworkFunctionPCIRevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCIRevId.setStatus("mandatory")
_AdapterNetworkFunctionPCISubVendorId_Type = DisplayString
_AdapterNetworkFunctionPCISubVendorId_Object = MibTableColumn
adapterNetworkFunctionPCISubVendorId = _AdapterNetworkFunctionPCISubVendorId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 24),
    _AdapterNetworkFunctionPCISubVendorId_Type()
)
adapterNetworkFunctionPCISubVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCISubVendorId.setStatus("mandatory")
_AdapterNetworkFunctionPCISubDevId_Type = DisplayString
_AdapterNetworkFunctionPCISubDevId_Object = MibTableColumn
adapterNetworkFunctionPCISubDevId = _AdapterNetworkFunctionPCISubDevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 25),
    _AdapterNetworkFunctionPCISubDevId_Type()
)
adapterNetworkFunctionPCISubDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCISubDevId.setStatus("mandatory")
_AdapterNetworkFunctionPCISlotDesignation_Type = DisplayString
_AdapterNetworkFunctionPCISlotDesignation_Object = MibTableColumn
adapterNetworkFunctionPCISlotDesignation = _AdapterNetworkFunctionPCISlotDesignation_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 3, 1, 26),
    _AdapterNetworkFunctionPCISlotDesignation_Type()
)
adapterNetworkFunctionPCISlotDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkFunctionPCISlotDesignation.setStatus("mandatory")
_AdapterNetworkPortTable_Object = MibTable
adapterNetworkPortTable = _AdapterNetworkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4)
)
if mibBuilder.loadTexts:
    adapterNetworkPortTable.setStatus("mandatory")
_AdapterNetworkPortEntry_Object = MibTableRow
adapterNetworkPortEntry = _AdapterNetworkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1)
)
adapterNetworkPortEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "adapterNetworkPortIndex"),
)
if mibBuilder.loadTexts:
    adapterNetworkPortEntry.setStatus("mandatory")
_AdapterNetworkPortIndex_Type = Integer32
_AdapterNetworkPortIndex_Object = MibTableColumn
adapterNetworkPortIndex = _AdapterNetworkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 1),
    _AdapterNetworkPortIndex_Type()
)
adapterNetworkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortIndex.setStatus("mandatory")
_AdapterNetworkPortNetworkVPDProdName_Type = DisplayString
_AdapterNetworkPortNetworkVPDProdName_Object = MibTableColumn
adapterNetworkPortNetworkVPDProdName = _AdapterNetworkPortNetworkVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 2),
    _AdapterNetworkPortNetworkVPDProdName_Type()
)
adapterNetworkPortNetworkVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortNetworkVPDProdName.setStatus("mandatory")
_AdapterNetworkPortPhyPortNo_Type = Integer32
_AdapterNetworkPortPhyPortNo_Object = MibTableColumn
adapterNetworkPortPhyPortNo = _AdapterNetworkPortPhyPortNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 3),
    _AdapterNetworkPortPhyPortNo_Type()
)
adapterNetworkPortPhyPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortPhyPortNo.setStatus("mandatory")
_AdapterNetworkPortPhyPortConnector_Type = DisplayString
_AdapterNetworkPortPhyPortConnector_Object = MibTableColumn
adapterNetworkPortPhyPortConnector = _AdapterNetworkPortPhyPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 4),
    _AdapterNetworkPortPhyPortConnector_Type()
)
adapterNetworkPortPhyPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortPhyPortConnector.setStatus("mandatory")
_AdapterNetworkPortPhyPortBurnedinAddress_Type = DisplayString
_AdapterNetworkPortPhyPortBurnedinAddress_Object = MibTableColumn
adapterNetworkPortPhyPortBurnedinAddress = _AdapterNetworkPortPhyPortBurnedinAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 5),
    _AdapterNetworkPortPhyPortBurnedinAddress_Type()
)
adapterNetworkPortPhyPortBurnedinAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortPhyPortBurnedinAddress.setStatus("mandatory")
_AdapterNetworkPortNo_Type = Integer32
_AdapterNetworkPortNo_Object = MibTableColumn
adapterNetworkPortNo = _AdapterNetworkPortNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 6),
    _AdapterNetworkPortNo_Type()
)
adapterNetworkPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortNo.setStatus("mandatory")
_AdapterNetworkPortMaxDataSize_Type = Gauge32
_AdapterNetworkPortMaxDataSize_Object = MibTableColumn
adapterNetworkPortMaxDataSize = _AdapterNetworkPortMaxDataSize_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 7),
    _AdapterNetworkPortMaxDataSize_Type()
)
adapterNetworkPortMaxDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortMaxDataSize.setStatus("mandatory")
_AdapterNetworkPortPermanentAddress_Type = DisplayString
_AdapterNetworkPortPermanentAddress_Object = MibTableColumn
adapterNetworkPortPermanentAddress = _AdapterNetworkPortPermanentAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 8),
    _AdapterNetworkPortPermanentAddress_Type()
)
adapterNetworkPortPermanentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortPermanentAddress.setStatus("mandatory")
_AdapterNetworkPortNetworkAddress_Type = DisplayString
_AdapterNetworkPortNetworkAddress_Object = MibTableColumn
adapterNetworkPortNetworkAddress = _AdapterNetworkPortNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 9),
    _AdapterNetworkPortNetworkAddress_Type()
)
adapterNetworkPortNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortNetworkAddress.setStatus("mandatory")
_AdapterNetworkPortLinkTechnology_Type = DisplayString
_AdapterNetworkPortLinkTechnology_Object = MibTableColumn
adapterNetworkPortLinkTechnology = _AdapterNetworkPortLinkTechnology_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 10),
    _AdapterNetworkPortLinkTechnology_Type()
)
adapterNetworkPortLinkTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortLinkTechnology.setStatus("mandatory")
_AdapterNetworkPortvNICMode_Type = DisplayString
_AdapterNetworkPortvNICMode_Object = MibTableColumn
adapterNetworkPortvNICMode = _AdapterNetworkPortvNICMode_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 11),
    _AdapterNetworkPortvNICMode_Type()
)
adapterNetworkPortvNICMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortvNICMode.setStatus("mandatory")
_AdapterNetworkPortMaxSpeed_Type = DisplayString
_AdapterNetworkPortMaxSpeed_Object = MibTableColumn
adapterNetworkPortMaxSpeed = _AdapterNetworkPortMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 12),
    _AdapterNetworkPortMaxSpeed_Type()
)
adapterNetworkPortMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortMaxSpeed.setStatus("mandatory")
_AdapterNetworkPortProtocolType_Type = DisplayString
_AdapterNetworkPortProtocolType_Object = MibTableColumn
adapterNetworkPortProtocolType = _AdapterNetworkPortProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 13),
    _AdapterNetworkPortProtocolType_Type()
)
adapterNetworkPortProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortProtocolType.setStatus("mandatory")
_AdapterNetworkPortCurrentProtocol_Type = DisplayString
_AdapterNetworkPortCurrentProtocol_Object = MibTableColumn
adapterNetworkPortCurrentProtocol = _AdapterNetworkPortCurrentProtocol_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 14),
    _AdapterNetworkPortCurrentProtocol_Type()
)
adapterNetworkPortCurrentProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortCurrentProtocol.setStatus("mandatory")
_AdapterNetworkPortFCoEPermanentAddress_Type = DisplayString
_AdapterNetworkPortFCoEPermanentAddress_Object = MibTableColumn
adapterNetworkPortFCoEPermanentAddress = _AdapterNetworkPortFCoEPermanentAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 15),
    _AdapterNetworkPortFCoEPermanentAddress_Type()
)
adapterNetworkPortFCoEPermanentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortFCoEPermanentAddress.setStatus("mandatory")
_AdapterNetworkPortFCoENetworkAddress_Type = DisplayString
_AdapterNetworkPortFCoENetworkAddress_Object = MibTableColumn
adapterNetworkPortFCoENetworkAddress = _AdapterNetworkPortFCoENetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 16),
    _AdapterNetworkPortFCoENetworkAddress_Type()
)
adapterNetworkPortFCoENetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortFCoENetworkAddress.setStatus("mandatory")
_AdapterNetworkPortConnectionType_Type = DisplayString
_AdapterNetworkPortConnectionType_Object = MibTableColumn
adapterNetworkPortConnectionType = _AdapterNetworkPortConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 17),
    _AdapterNetworkPortConnectionType_Type()
)
adapterNetworkPortConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortConnectionType.setStatus("mandatory")
_AdapterNetworkPortRole_Type = DisplayString
_AdapterNetworkPortRole_Object = MibTableColumn
adapterNetworkPortRole = _AdapterNetworkPortRole_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 18),
    _AdapterNetworkPortRole_Type()
)
adapterNetworkPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortRole.setStatus("mandatory")
_AdapterNetworkPortTargetRelativePortNo_Type = Gauge32
_AdapterNetworkPortTargetRelativePortNo_Object = MibTableColumn
adapterNetworkPortTargetRelativePortNo = _AdapterNetworkPortTargetRelativePortNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 19),
    _AdapterNetworkPortTargetRelativePortNo_Type()
)
adapterNetworkPortTargetRelativePortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortTargetRelativePortNo.setStatus("mandatory")
_AdapterNetworkPortPhyPortLinkStatus_Type = DisplayString
_AdapterNetworkPortPhyPortLinkStatus_Object = MibTableColumn
adapterNetworkPortPhyPortLinkStatus = _AdapterNetworkPortPhyPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 20),
    _AdapterNetworkPortPhyPortLinkStatus_Type()
)
adapterNetworkPortPhyPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortPhyPortLinkStatus.setStatus("mandatory")
_AdapterNetworkPortPhyPortLinkSpeed_Type = DisplayString
_AdapterNetworkPortPhyPortLinkSpeed_Object = MibTableColumn
adapterNetworkPortPhyPortLinkSpeed = _AdapterNetworkPortPhyPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 4, 1, 21),
    _AdapterNetworkPortPhyPortLinkSpeed_Type()
)
adapterNetworkPortPhyPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterNetworkPortPhyPortLinkSpeed.setStatus("mandatory")
_AdapterGPUFunctionTable_Object = MibTable
adapterGPUFunctionTable = _AdapterGPUFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5)
)
if mibBuilder.loadTexts:
    adapterGPUFunctionTable.setStatus("mandatory")
_AdapterGPUFunctionEntry_Object = MibTableRow
adapterGPUFunctionEntry = _AdapterGPUFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1)
)
adapterGPUFunctionEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "adapterGPUFunctionIndex"),
)
if mibBuilder.loadTexts:
    adapterGPUFunctionEntry.setStatus("mandatory")
_AdapterGPUFunctionIndex_Type = Integer32
_AdapterGPUFunctionIndex_Object = MibTableColumn
adapterGPUFunctionIndex = _AdapterGPUFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 1),
    _AdapterGPUFunctionIndex_Type()
)
adapterGPUFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionIndex.setStatus("mandatory")
_AdapterGPUFunctionGpuVPDProdName_Type = DisplayString
_AdapterGPUFunctionGpuVPDProdName_Object = MibTableColumn
adapterGPUFunctionGpuVPDProdName = _AdapterGPUFunctionGpuVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 2),
    _AdapterGPUFunctionGpuVPDProdName_Type()
)
adapterGPUFunctionGpuVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionGpuVPDProdName.setStatus("mandatory")
_AdapterGPUFunctionAdapterVPDProdName_Type = DisplayString
_AdapterGPUFunctionAdapterVPDProdName_Object = MibTableColumn
adapterGPUFunctionAdapterVPDProdName = _AdapterGPUFunctionAdapterVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 3),
    _AdapterGPUFunctionAdapterVPDProdName_Type()
)
adapterGPUFunctionAdapterVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionAdapterVPDProdName.setStatus("mandatory")
_AdapterGPUFunctionGpuVPDManufacturer_Type = DisplayString
_AdapterGPUFunctionGpuVPDManufacturer_Object = MibTableColumn
adapterGPUFunctionGpuVPDManufacturer = _AdapterGPUFunctionGpuVPDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 4),
    _AdapterGPUFunctionGpuVPDManufacturer_Type()
)
adapterGPUFunctionGpuVPDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionGpuVPDManufacturer.setStatus("mandatory")
_AdapterGPUFunctionGpuVPDUUID_Type = DisplayString
_AdapterGPUFunctionGpuVPDUUID_Object = MibTableColumn
adapterGPUFunctionGpuVPDUUID = _AdapterGPUFunctionGpuVPDUUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 5),
    _AdapterGPUFunctionGpuVPDUUID_Type()
)
adapterGPUFunctionGpuVPDUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionGpuVPDUUID.setStatus("mandatory")
_AdapterGPUFunctionGpuVPDModel_Type = DisplayString
_AdapterGPUFunctionGpuVPDModel_Object = MibTableColumn
adapterGPUFunctionGpuVPDModel = _AdapterGPUFunctionGpuVPDModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 6),
    _AdapterGPUFunctionGpuVPDModel_Type()
)
adapterGPUFunctionGpuVPDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionGpuVPDModel.setStatus("mandatory")
_AdapterGPUFunctionGpuVPDSerialNo_Type = DisplayString
_AdapterGPUFunctionGpuVPDSerialNo_Object = MibTableColumn
adapterGPUFunctionGpuVPDSerialNo = _AdapterGPUFunctionGpuVPDSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 7),
    _AdapterGPUFunctionGpuVPDSerialNo_Type()
)
adapterGPUFunctionGpuVPDSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionGpuVPDSerialNo.setStatus("mandatory")
_AdapterGPUFunctionGpuVPDFRUNo_Type = DisplayString
_AdapterGPUFunctionGpuVPDFRUNo_Object = MibTableColumn
adapterGPUFunctionGpuVPDFRUNo = _AdapterGPUFunctionGpuVPDFRUNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 8),
    _AdapterGPUFunctionGpuVPDFRUNo_Type()
)
adapterGPUFunctionGpuVPDFRUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionGpuVPDFRUNo.setStatus("mandatory")
_AdapterGPUFunctionGpuVPDPartNo_Type = DisplayString
_AdapterGPUFunctionGpuVPDPartNo_Object = MibTableColumn
adapterGPUFunctionGpuVPDPartNo = _AdapterGPUFunctionGpuVPDPartNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 9),
    _AdapterGPUFunctionGpuVPDPartNo_Type()
)
adapterGPUFunctionGpuVPDPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionGpuVPDPartNo.setStatus("mandatory")
_AdapterGPUFunctionFoDUID_Type = DisplayString
_AdapterGPUFunctionFoDUID_Object = MibTableColumn
adapterGPUFunctionFoDUID = _AdapterGPUFunctionFoDUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 10),
    _AdapterGPUFunctionFoDUID_Type()
)
adapterGPUFunctionFoDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionFoDUID.setStatus("mandatory")


class _AdapterGPUFunctionSupportHotPlug_Type(Integer32):
    """Custom type adapterGPUFunctionSupportHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AdapterGPUFunctionSupportHotPlug_Type.__name__ = "Integer32"
_AdapterGPUFunctionSupportHotPlug_Object = MibTableColumn
adapterGPUFunctionSupportHotPlug = _AdapterGPUFunctionSupportHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 11),
    _AdapterGPUFunctionSupportHotPlug_Type()
)
adapterGPUFunctionSupportHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionSupportHotPlug.setStatus("mandatory")
_AdapterGPUFunctionVideoMemorySize_Type = DisplayString
_AdapterGPUFunctionVideoMemorySize_Object = MibTableColumn
adapterGPUFunctionVideoMemorySize = _AdapterGPUFunctionVideoMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 12),
    _AdapterGPUFunctionVideoMemorySize_Type()
)
adapterGPUFunctionVideoMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionVideoMemorySize.setStatus("mandatory")
_AdapterGPUFunctionVideoMemoryType_Type = DisplayString
_AdapterGPUFunctionVideoMemoryType_Object = MibTableColumn
adapterGPUFunctionVideoMemoryType = _AdapterGPUFunctionVideoMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 13),
    _AdapterGPUFunctionVideoMemoryType_Type()
)
adapterGPUFunctionVideoMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionVideoMemoryType.setStatus("mandatory")
_AdapterGPUFunctionChipNumber_Type = Integer32
_AdapterGPUFunctionChipNumber_Object = MibTableColumn
adapterGPUFunctionChipNumber = _AdapterGPUFunctionChipNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 14),
    _AdapterGPUFunctionChipNumber_Type()
)
adapterGPUFunctionChipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionChipNumber.setStatus("mandatory")
_AdapterGPUFunctionMaxDataWidth_Type = Integer32
_AdapterGPUFunctionMaxDataWidth_Object = MibTableColumn
adapterGPUFunctionMaxDataWidth = _AdapterGPUFunctionMaxDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 15),
    _AdapterGPUFunctionMaxDataWidth_Type()
)
adapterGPUFunctionMaxDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionMaxDataWidth.setStatus("mandatory")
_AdapterGPUFunctionPackageType_Type = DisplayString
_AdapterGPUFunctionPackageType_Object = MibTableColumn
adapterGPUFunctionPackageType = _AdapterGPUFunctionPackageType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 16),
    _AdapterGPUFunctionPackageType_Type()
)
adapterGPUFunctionPackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPackageType.setStatus("mandatory")
_AdapterGPUFunctionPCIBusNo_Type = Integer32
_AdapterGPUFunctionPCIBusNo_Object = MibTableColumn
adapterGPUFunctionPCIBusNo = _AdapterGPUFunctionPCIBusNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 17),
    _AdapterGPUFunctionPCIBusNo_Type()
)
adapterGPUFunctionPCIBusNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCIBusNo.setStatus("mandatory")
_AdapterGPUFunctionPCIDevNo_Type = Integer32
_AdapterGPUFunctionPCIDevNo_Object = MibTableColumn
adapterGPUFunctionPCIDevNo = _AdapterGPUFunctionPCIDevNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 18),
    _AdapterGPUFunctionPCIDevNo_Type()
)
adapterGPUFunctionPCIDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCIDevNo.setStatus("mandatory")
_AdapterGPUFunctionPCIFuncNo_Type = Integer32
_AdapterGPUFunctionPCIFuncNo_Object = MibTableColumn
adapterGPUFunctionPCIFuncNo = _AdapterGPUFunctionPCIFuncNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 19),
    _AdapterGPUFunctionPCIFuncNo_Type()
)
adapterGPUFunctionPCIFuncNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCIFuncNo.setStatus("mandatory")
_AdapterGPUFunctionPCIVendorId_Type = DisplayString
_AdapterGPUFunctionPCIVendorId_Object = MibTableColumn
adapterGPUFunctionPCIVendorId = _AdapterGPUFunctionPCIVendorId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 20),
    _AdapterGPUFunctionPCIVendorId_Type()
)
adapterGPUFunctionPCIVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCIVendorId.setStatus("mandatory")
_AdapterGPUFunctionPCIDevId_Type = DisplayString
_AdapterGPUFunctionPCIDevId_Object = MibTableColumn
adapterGPUFunctionPCIDevId = _AdapterGPUFunctionPCIDevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 21),
    _AdapterGPUFunctionPCIDevId_Type()
)
adapterGPUFunctionPCIDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCIDevId.setStatus("mandatory")
_AdapterGPUFunctionPCIDevType_Type = DisplayString
_AdapterGPUFunctionPCIDevType_Object = MibTableColumn
adapterGPUFunctionPCIDevType = _AdapterGPUFunctionPCIDevType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 22),
    _AdapterGPUFunctionPCIDevType_Type()
)
adapterGPUFunctionPCIDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCIDevType.setStatus("mandatory")
_AdapterGPUFunctionPCIRevId_Type = DisplayString
_AdapterGPUFunctionPCIRevId_Object = MibTableColumn
adapterGPUFunctionPCIRevId = _AdapterGPUFunctionPCIRevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 23),
    _AdapterGPUFunctionPCIRevId_Type()
)
adapterGPUFunctionPCIRevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCIRevId.setStatus("mandatory")
_AdapterGPUFunctionPCISubVendorId_Type = DisplayString
_AdapterGPUFunctionPCISubVendorId_Object = MibTableColumn
adapterGPUFunctionPCISubVendorId = _AdapterGPUFunctionPCISubVendorId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 24),
    _AdapterGPUFunctionPCISubVendorId_Type()
)
adapterGPUFunctionPCISubVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCISubVendorId.setStatus("mandatory")
_AdapterGPUFunctionPCISubDevId_Type = DisplayString
_AdapterGPUFunctionPCISubDevId_Object = MibTableColumn
adapterGPUFunctionPCISubDevId = _AdapterGPUFunctionPCISubDevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 25),
    _AdapterGPUFunctionPCISubDevId_Type()
)
adapterGPUFunctionPCISubDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCISubDevId.setStatus("mandatory")
_AdapterGPUFunctionPCISlotDesignation_Type = DisplayString
_AdapterGPUFunctionPCISlotDesignation_Object = MibTableColumn
adapterGPUFunctionPCISlotDesignation = _AdapterGPUFunctionPCISlotDesignation_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 5, 1, 26),
    _AdapterGPUFunctionPCISlotDesignation_Type()
)
adapterGPUFunctionPCISlotDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUFunctionPCISlotDesignation.setStatus("mandatory")
_AdapterGPUChipTable_Object = MibTable
adapterGPUChipTable = _AdapterGPUChipTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6)
)
if mibBuilder.loadTexts:
    adapterGPUChipTable.setStatus("mandatory")
_AdapterGPUChipEntry_Object = MibTableRow
adapterGPUChipEntry = _AdapterGPUChipEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1)
)
adapterGPUChipEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "adapterGPUChipIndex"),
)
if mibBuilder.loadTexts:
    adapterGPUChipEntry.setStatus("mandatory")
_AdapterGPUChipIndex_Type = Integer32
_AdapterGPUChipIndex_Object = MibTableColumn
adapterGPUChipIndex = _AdapterGPUChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 1),
    _AdapterGPUChipIndex_Type()
)
adapterGPUChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipIndex.setStatus("mandatory")
_AdapterGPUChipGpuVPDProdName_Type = DisplayString
_AdapterGPUChipGpuVPDProdName_Object = MibTableColumn
adapterGPUChipGpuVPDProdName = _AdapterGPUChipGpuVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 2),
    _AdapterGPUChipGpuVPDProdName_Type()
)
adapterGPUChipGpuVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipGpuVPDProdName.setStatus("mandatory")
_AdapterGPUChipNo_Type = Integer32
_AdapterGPUChipNo_Object = MibTableColumn
adapterGPUChipNo = _AdapterGPUChipNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 3),
    _AdapterGPUChipNo_Type()
)
adapterGPUChipNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipNo.setStatus("mandatory")
_AdapterGPUChipName_Type = DisplayString
_AdapterGPUChipName_Object = MibTableColumn
adapterGPUChipName = _AdapterGPUChipName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 4),
    _AdapterGPUChipName_Type()
)
adapterGPUChipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipName.setStatus("mandatory")
_AdapterGPUChipFamily_Type = DisplayString
_AdapterGPUChipFamily_Object = MibTableColumn
adapterGPUChipFamily = _AdapterGPUChipFamily_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 5),
    _AdapterGPUChipFamily_Type()
)
adapterGPUChipFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipFamily.setStatus("mandatory")
_AdapterGPUChipManufacturer_Type = DisplayString
_AdapterGPUChipManufacturer_Object = MibTableColumn
adapterGPUChipManufacturer = _AdapterGPUChipManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 6),
    _AdapterGPUChipManufacturer_Type()
)
adapterGPUChipManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipManufacturer.setStatus("mandatory")
_AdapterGPUChipCoresEnabled_Type = Integer32
_AdapterGPUChipCoresEnabled_Object = MibTableColumn
adapterGPUChipCoresEnabled = _AdapterGPUChipCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 7),
    _AdapterGPUChipCoresEnabled_Type()
)
adapterGPUChipCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipCoresEnabled.setStatus("mandatory")
_AdapterGPUChipMaxClockSpeed_Type = Gauge32
_AdapterGPUChipMaxClockSpeed_Object = MibTableColumn
adapterGPUChipMaxClockSpeed = _AdapterGPUChipMaxClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 8),
    _AdapterGPUChipMaxClockSpeed_Type()
)
adapterGPUChipMaxClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipMaxClockSpeed.setStatus("mandatory")
_AdapterGPUChipExtBusClockSpeed_Type = Gauge32
_AdapterGPUChipExtBusClockSpeed_Object = MibTableColumn
adapterGPUChipExtBusClockSpeed = _AdapterGPUChipExtBusClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 9),
    _AdapterGPUChipExtBusClockSpeed_Type()
)
adapterGPUChipExtBusClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipExtBusClockSpeed.setStatus("mandatory")
_AdapterGPUChipAddressWidth_Type = Integer32
_AdapterGPUChipAddressWidth_Object = MibTableColumn
adapterGPUChipAddressWidth = _AdapterGPUChipAddressWidth_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 10),
    _AdapterGPUChipAddressWidth_Type()
)
adapterGPUChipAddressWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipAddressWidth.setStatus("mandatory")
_AdapterGPUChipDataWidth_Type = Integer32
_AdapterGPUChipDataWidth_Object = MibTableColumn
adapterGPUChipDataWidth = _AdapterGPUChipDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 11),
    _AdapterGPUChipDataWidth_Type()
)
adapterGPUChipDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipDataWidth.setStatus("mandatory")
_AdapterGPUChipFormFactor_Type = DisplayString
_AdapterGPUChipFormFactor_Object = MibTableColumn
adapterGPUChipFormFactor = _AdapterGPUChipFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 12),
    _AdapterGPUChipFormFactor_Type()
)
adapterGPUChipFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipFormFactor.setStatus("mandatory")
_AdapterGPUChipModel_Type = DisplayString
_AdapterGPUChipModel_Object = MibTableColumn
adapterGPUChipModel = _AdapterGPUChipModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 13),
    _AdapterGPUChipModel_Type()
)
adapterGPUChipModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipModel.setStatus("mandatory")
_AdapterGPUChipSerialNo_Type = DisplayString
_AdapterGPUChipSerialNo_Object = MibTableColumn
adapterGPUChipSerialNo = _AdapterGPUChipSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 14),
    _AdapterGPUChipSerialNo_Type()
)
adapterGPUChipSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipSerialNo.setStatus("mandatory")
_AdapterGPUChipFRUNo_Type = DisplayString
_AdapterGPUChipFRUNo_Object = MibTableColumn
adapterGPUChipFRUNo = _AdapterGPUChipFRUNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 15),
    _AdapterGPUChipFRUNo_Type()
)
adapterGPUChipFRUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipFRUNo.setStatus("mandatory")
_AdapterGPUChipPartNo_Type = DisplayString
_AdapterGPUChipPartNo_Object = MibTableColumn
adapterGPUChipPartNo = _AdapterGPUChipPartNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 16),
    _AdapterGPUChipPartNo_Type()
)
adapterGPUChipPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipPartNo.setStatus("mandatory")
_AdapterGPUChipUniqueID_Type = DisplayString
_AdapterGPUChipUniqueID_Object = MibTableColumn
adapterGPUChipUniqueID = _AdapterGPUChipUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 6, 1, 17),
    _AdapterGPUChipUniqueID_Type()
)
adapterGPUChipUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterGPUChipUniqueID.setStatus("mandatory")
_AdapterRAIDFunctionTable_Object = MibTable
adapterRAIDFunctionTable = _AdapterRAIDFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7)
)
if mibBuilder.loadTexts:
    adapterRAIDFunctionTable.setStatus("mandatory")
_AdapterRAIDFunctionEntry_Object = MibTableRow
adapterRAIDFunctionEntry = _AdapterRAIDFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1)
)
adapterRAIDFunctionEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "adapterRAIDFunctionIndex"),
)
if mibBuilder.loadTexts:
    adapterRAIDFunctionEntry.setStatus("mandatory")
_AdapterRAIDFunctionIndex_Type = Integer32
_AdapterRAIDFunctionIndex_Object = MibTableColumn
adapterRAIDFunctionIndex = _AdapterRAIDFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 1),
    _AdapterRAIDFunctionIndex_Type()
)
adapterRAIDFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionIndex.setStatus("mandatory")
_AdapterRAIDFunctionRaidVPDProdName_Type = DisplayString
_AdapterRAIDFunctionRaidVPDProdName_Object = MibTableColumn
adapterRAIDFunctionRaidVPDProdName = _AdapterRAIDFunctionRaidVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 2),
    _AdapterRAIDFunctionRaidVPDProdName_Type()
)
adapterRAIDFunctionRaidVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionRaidVPDProdName.setStatus("mandatory")
_AdapterRAIDFunctionAdapterVPDProdName_Type = DisplayString
_AdapterRAIDFunctionAdapterVPDProdName_Object = MibTableColumn
adapterRAIDFunctionAdapterVPDProdName = _AdapterRAIDFunctionAdapterVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 3),
    _AdapterRAIDFunctionAdapterVPDProdName_Type()
)
adapterRAIDFunctionAdapterVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionAdapterVPDProdName.setStatus("mandatory")
_AdapterRAIDFunctionRaidVPDManufacturer_Type = DisplayString
_AdapterRAIDFunctionRaidVPDManufacturer_Object = MibTableColumn
adapterRAIDFunctionRaidVPDManufacturer = _AdapterRAIDFunctionRaidVPDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 4),
    _AdapterRAIDFunctionRaidVPDManufacturer_Type()
)
adapterRAIDFunctionRaidVPDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionRaidVPDManufacturer.setStatus("mandatory")
_AdapterRAIDFunctionRaidVPDUUID_Type = DisplayString
_AdapterRAIDFunctionRaidVPDUUID_Object = MibTableColumn
adapterRAIDFunctionRaidVPDUUID = _AdapterRAIDFunctionRaidVPDUUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 5),
    _AdapterRAIDFunctionRaidVPDUUID_Type()
)
adapterRAIDFunctionRaidVPDUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionRaidVPDUUID.setStatus("mandatory")
_AdapterRAIDFunctionRaidVPDModel_Type = DisplayString
_AdapterRAIDFunctionRaidVPDModel_Object = MibTableColumn
adapterRAIDFunctionRaidVPDModel = _AdapterRAIDFunctionRaidVPDModel_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 6),
    _AdapterRAIDFunctionRaidVPDModel_Type()
)
adapterRAIDFunctionRaidVPDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionRaidVPDModel.setStatus("mandatory")
_AdapterRAIDFunctionRaidVPDSerialNo_Type = DisplayString
_AdapterRAIDFunctionRaidVPDSerialNo_Object = MibTableColumn
adapterRAIDFunctionRaidVPDSerialNo = _AdapterRAIDFunctionRaidVPDSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 7),
    _AdapterRAIDFunctionRaidVPDSerialNo_Type()
)
adapterRAIDFunctionRaidVPDSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionRaidVPDSerialNo.setStatus("mandatory")
_AdapterRAIDFunctionRaidVPDFRUNo_Type = DisplayString
_AdapterRAIDFunctionRaidVPDFRUNo_Object = MibTableColumn
adapterRAIDFunctionRaidVPDFRUNo = _AdapterRAIDFunctionRaidVPDFRUNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 8),
    _AdapterRAIDFunctionRaidVPDFRUNo_Type()
)
adapterRAIDFunctionRaidVPDFRUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionRaidVPDFRUNo.setStatus("mandatory")
_AdapterRAIDFunctionRaidVPDPartNo_Type = DisplayString
_AdapterRAIDFunctionRaidVPDPartNo_Object = MibTableColumn
adapterRAIDFunctionRaidVPDPartNo = _AdapterRAIDFunctionRaidVPDPartNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 9),
    _AdapterRAIDFunctionRaidVPDPartNo_Type()
)
adapterRAIDFunctionRaidVPDPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionRaidVPDPartNo.setStatus("mandatory")
_AdapterRAIDFunctionFoDUID_Type = DisplayString
_AdapterRAIDFunctionFoDUID_Object = MibTableColumn
adapterRAIDFunctionFoDUID = _AdapterRAIDFunctionFoDUID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 10),
    _AdapterRAIDFunctionFoDUID_Type()
)
adapterRAIDFunctionFoDUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionFoDUID.setStatus("mandatory")


class _AdapterRAIDFunctionSupportHotPlug_Type(Integer32):
    """Custom type adapterRAIDFunctionSupportHotPlug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AdapterRAIDFunctionSupportHotPlug_Type.__name__ = "Integer32"
_AdapterRAIDFunctionSupportHotPlug_Object = MibTableColumn
adapterRAIDFunctionSupportHotPlug = _AdapterRAIDFunctionSupportHotPlug_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 11),
    _AdapterRAIDFunctionSupportHotPlug_Type()
)
adapterRAIDFunctionSupportHotPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionSupportHotPlug.setStatus("mandatory")
_AdapterRAIDFunctionMaxDataWidth_Type = Integer32
_AdapterRAIDFunctionMaxDataWidth_Object = MibTableColumn
adapterRAIDFunctionMaxDataWidth = _AdapterRAIDFunctionMaxDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 12),
    _AdapterRAIDFunctionMaxDataWidth_Type()
)
adapterRAIDFunctionMaxDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionMaxDataWidth.setStatus("mandatory")
_AdapterRAIDFunctionPackageType_Type = DisplayString
_AdapterRAIDFunctionPackageType_Object = MibTableColumn
adapterRAIDFunctionPackageType = _AdapterRAIDFunctionPackageType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 13),
    _AdapterRAIDFunctionPackageType_Type()
)
adapterRAIDFunctionPackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPackageType.setStatus("mandatory")
_AdapterRAIDFunctionPCIBusNo_Type = Integer32
_AdapterRAIDFunctionPCIBusNo_Object = MibTableColumn
adapterRAIDFunctionPCIBusNo = _AdapterRAIDFunctionPCIBusNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 14),
    _AdapterRAIDFunctionPCIBusNo_Type()
)
adapterRAIDFunctionPCIBusNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCIBusNo.setStatus("mandatory")
_AdapterRAIDFunctionPCIDevNo_Type = Integer32
_AdapterRAIDFunctionPCIDevNo_Object = MibTableColumn
adapterRAIDFunctionPCIDevNo = _AdapterRAIDFunctionPCIDevNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 15),
    _AdapterRAIDFunctionPCIDevNo_Type()
)
adapterRAIDFunctionPCIDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCIDevNo.setStatus("mandatory")
_AdapterRAIDFunctionPCIFuncNo_Type = Integer32
_AdapterRAIDFunctionPCIFuncNo_Object = MibTableColumn
adapterRAIDFunctionPCIFuncNo = _AdapterRAIDFunctionPCIFuncNo_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 16),
    _AdapterRAIDFunctionPCIFuncNo_Type()
)
adapterRAIDFunctionPCIFuncNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCIFuncNo.setStatus("mandatory")
_AdapterRAIDFunctionPCIVendorId_Type = DisplayString
_AdapterRAIDFunctionPCIVendorId_Object = MibTableColumn
adapterRAIDFunctionPCIVendorId = _AdapterRAIDFunctionPCIVendorId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 17),
    _AdapterRAIDFunctionPCIVendorId_Type()
)
adapterRAIDFunctionPCIVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCIVendorId.setStatus("mandatory")
_AdapterRAIDFunctionPCIDevId_Type = DisplayString
_AdapterRAIDFunctionPCIDevId_Object = MibTableColumn
adapterRAIDFunctionPCIDevId = _AdapterRAIDFunctionPCIDevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 18),
    _AdapterRAIDFunctionPCIDevId_Type()
)
adapterRAIDFunctionPCIDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCIDevId.setStatus("mandatory")
_AdapterRAIDFunctionPCIDevType_Type = DisplayString
_AdapterRAIDFunctionPCIDevType_Object = MibTableColumn
adapterRAIDFunctionPCIDevType = _AdapterRAIDFunctionPCIDevType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 19),
    _AdapterRAIDFunctionPCIDevType_Type()
)
adapterRAIDFunctionPCIDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCIDevType.setStatus("mandatory")
_AdapterRAIDFunctionPCIRevId_Type = DisplayString
_AdapterRAIDFunctionPCIRevId_Object = MibTableColumn
adapterRAIDFunctionPCIRevId = _AdapterRAIDFunctionPCIRevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 20),
    _AdapterRAIDFunctionPCIRevId_Type()
)
adapterRAIDFunctionPCIRevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCIRevId.setStatus("mandatory")
_AdapterRAIDFunctionPCISubVendorId_Type = DisplayString
_AdapterRAIDFunctionPCISubVendorId_Object = MibTableColumn
adapterRAIDFunctionPCISubVendorId = _AdapterRAIDFunctionPCISubVendorId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 21),
    _AdapterRAIDFunctionPCISubVendorId_Type()
)
adapterRAIDFunctionPCISubVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCISubVendorId.setStatus("mandatory")
_AdapterRAIDFunctionPCISubDevId_Type = DisplayString
_AdapterRAIDFunctionPCISubDevId_Object = MibTableColumn
adapterRAIDFunctionPCISubDevId = _AdapterRAIDFunctionPCISubDevId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 22),
    _AdapterRAIDFunctionPCISubDevId_Type()
)
adapterRAIDFunctionPCISubDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCISubDevId.setStatus("mandatory")
_AdapterRAIDFunctionPCISlotDesignation_Type = DisplayString
_AdapterRAIDFunctionPCISlotDesignation_Object = MibTableColumn
adapterRAIDFunctionPCISlotDesignation = _AdapterRAIDFunctionPCISlotDesignation_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 7, 1, 23),
    _AdapterRAIDFunctionPCISlotDesignation_Type()
)
adapterRAIDFunctionPCISlotDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterRAIDFunctionPCISlotDesignation.setStatus("mandatory")
_AdapterFirmwareTable_Object = MibTable
adapterFirmwareTable = _AdapterFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8)
)
if mibBuilder.loadTexts:
    adapterFirmwareTable.setStatus("mandatory")
_AdapterFirmwareEntry_Object = MibTableRow
adapterFirmwareEntry = _AdapterFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1)
)
adapterFirmwareEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "adapterFwIndex"),
)
if mibBuilder.loadTexts:
    adapterFirmwareEntry.setStatus("mandatory")
_AdapterFwIndex_Type = Integer32
_AdapterFwIndex_Object = MibTableColumn
adapterFwIndex = _AdapterFwIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 1),
    _AdapterFwIndex_Type()
)
adapterFwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwIndex.setStatus("mandatory")
_AdapterFwFunctionVPDProdName_Type = DisplayString
_AdapterFwFunctionVPDProdName_Object = MibTableColumn
adapterFwFunctionVPDProdName = _AdapterFwFunctionVPDProdName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 2),
    _AdapterFwFunctionVPDProdName_Type()
)
adapterFwFunctionVPDProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwFunctionVPDProdName.setStatus("mandatory")
_AdapterFwName_Type = DisplayString
_AdapterFwName_Object = MibTableColumn
adapterFwName = _AdapterFwName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 3),
    _AdapterFwName_Type()
)
adapterFwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwName.setStatus("mandatory")
_AdapterFwClassification_Type = DisplayString
_AdapterFwClassification_Object = MibTableColumn
adapterFwClassification = _AdapterFwClassification_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 4),
    _AdapterFwClassification_Type()
)
adapterFwClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwClassification.setStatus("mandatory")
_AdapterFwDescription_Type = DisplayString
_AdapterFwDescription_Object = MibTableColumn
adapterFwDescription = _AdapterFwDescription_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 5),
    _AdapterFwDescription_Type()
)
adapterFwDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwDescription.setStatus("mandatory")
_AdapterFwManufacture_Type = DisplayString
_AdapterFwManufacture_Object = MibTableColumn
adapterFwManufacture = _AdapterFwManufacture_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 6),
    _AdapterFwManufacture_Type()
)
adapterFwManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwManufacture.setStatus("mandatory")
_AdapterFwVersion_Type = DisplayString
_AdapterFwVersion_Object = MibTableColumn
adapterFwVersion = _AdapterFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 7),
    _AdapterFwVersion_Type()
)
adapterFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwVersion.setStatus("mandatory")
_AdapterFwReleaseDate_Type = DisplayString
_AdapterFwReleaseDate_Object = MibTableColumn
adapterFwReleaseDate = _AdapterFwReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 8),
    _AdapterFwReleaseDate_Type()
)
adapterFwReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwReleaseDate.setStatus("mandatory")
_AdapterFwSoftwareID_Type = DisplayString
_AdapterFwSoftwareID_Object = MibTableColumn
adapterFwSoftwareID = _AdapterFwSoftwareID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 1, 14, 8, 1, 9),
    _AdapterFwSoftwareID_Type()
)
adapterFwSoftwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterFwSoftwareID.setStatus("mandatory")
_ErrorLogs_ObjectIdentity = ObjectIdentity
errorLogs = _ErrorLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2)
)
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1)
)
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1, 1, 1)
)
eventLogEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("mandatory")


class _EventLogIndex_Type(Integer32):
    """Custom type eventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_EventLogIndex_Type.__name__ = "Integer32"
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1, 1, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("mandatory")
_EventLogString_Type = OctetString
_EventLogString_Object = MibTableColumn
eventLogString = _EventLogString_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1, 1, 1, 2),
    _EventLogString_Type()
)
eventLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogString.setStatus("mandatory")


class _EventLogSeverity_Type(Integer32):
    """Custom type eventLogSeverity based on Integer32"""
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
        *(("error", 0),
          ("warning", 1),
          ("information", 2),
          ("other", 3))
    )


_EventLogSeverity_Type.__name__ = "Integer32"
_EventLogSeverity_Object = MibTableColumn
eventLogSeverity = _EventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1, 1, 1, 3),
    _EventLogSeverity_Type()
)
eventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSeverity.setStatus("mandatory")
_EventLogDate_Type = OctetString
_EventLogDate_Object = MibTableColumn
eventLogDate = _EventLogDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1, 1, 1, 4),
    _EventLogDate_Type()
)
eventLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDate.setStatus("mandatory")
_EventLogTime_Type = OctetString
_EventLogTime_Object = MibTableColumn
eventLogTime = _EventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 2, 1, 1, 1, 5),
    _EventLogTime_Type()
)
eventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTime.setStatus("mandatory")
_ConfigureSP_ObjectIdentity = ObjectIdentity
configureSP = _ConfigureSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3)
)
_RemoteAccessConfig_ObjectIdentity = ObjectIdentity
remoteAccessConfig = _RemoteAccessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1)
)
_GeneralRemoteCfg_ObjectIdentity = ObjectIdentity
generalRemoteCfg = _GeneralRemoteCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1)
)


class _RemoteAlertRetryDelay_Type(Integer32):
    """Custom type remoteAlertRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              90,
              120,
              150,
              180,
              210,
              240)
        )
    )
    namedValues = NamedValues(
        *(("noDelay", 0),
          ("oneHalfMinute", 30),
          ("oneMinute", 60),
          ("oneAndHalfMinutes", 90),
          ("twoMinutes", 120),
          ("twoAndHalfMinutes", 150),
          ("threeMinutes", 180),
          ("threeAndHalfMinutes", 210),
          ("fourMinutes", 240))
    )


_RemoteAlertRetryDelay_Type.__name__ = "Integer32"
_RemoteAlertRetryDelay_Object = MibScalar
remoteAlertRetryDelay = _RemoteAlertRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 1),
    _RemoteAlertRetryDelay_Type()
)
remoteAlertRetryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertRetryDelay.setStatus("mandatory")


class _RemoteAlertRetryCount_Type(Integer32):
    """Custom type remoteAlertRetryCount based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noretry", 0),
          ("retry1", 1),
          ("retry2", 2),
          ("retry3", 3),
          ("retry4", 4),
          ("retry5", 5),
          ("retry6", 6),
          ("retry7", 7),
          ("retry8", 8))
    )


_RemoteAlertRetryCount_Type.__name__ = "Integer32"
_RemoteAlertRetryCount_Object = MibScalar
remoteAlertRetryCount = _RemoteAlertRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 2),
    _RemoteAlertRetryCount_Type()
)
remoteAlertRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertRetryCount.setStatus("mandatory")


class _RemoteAlertEntryDelay_Type(Integer32):
    """Custom type remoteAlertEntryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              90,
              120,
              150,
              180,
              210,
              240)
        )
    )
    namedValues = NamedValues(
        *(("noDelay", 0),
          ("oneHalfMinute", 30),
          ("oneMinute", 60),
          ("oneAndHalfMinutes", 90),
          ("twoMinutes", 120),
          ("twoAndHalfMinutes", 150),
          ("threeMinutes", 180),
          ("threeAndHalfMinutes", 210),
          ("fourMinutes", 240))
    )


_RemoteAlertEntryDelay_Type.__name__ = "Integer32"
_RemoteAlertEntryDelay_Object = MibScalar
remoteAlertEntryDelay = _RemoteAlertEntryDelay_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 3),
    _RemoteAlertEntryDelay_Type()
)
remoteAlertEntryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertEntryDelay.setStatus("mandatory")


class _SnmpCriticalAlerts_Type(Integer32):
    """Custom type snmpCriticalAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpCriticalAlerts_Type.__name__ = "Integer32"
_SnmpCriticalAlerts_Object = MibScalar
snmpCriticalAlerts = _SnmpCriticalAlerts_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 4),
    _SnmpCriticalAlerts_Type()
)
snmpCriticalAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCriticalAlerts.setStatus("mandatory")


class _SnmpWarningAlerts_Type(Integer32):
    """Custom type snmpWarningAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpWarningAlerts_Type.__name__ = "Integer32"
_SnmpWarningAlerts_Object = MibScalar
snmpWarningAlerts = _SnmpWarningAlerts_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 5),
    _SnmpWarningAlerts_Type()
)
snmpWarningAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpWarningAlerts.setStatus("mandatory")


class _SnmpSystemAlerts_Type(Integer32):
    """Custom type snmpSystemAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpSystemAlerts_Type.__name__ = "Integer32"
_SnmpSystemAlerts_Object = MibScalar
snmpSystemAlerts = _SnmpSystemAlerts_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 6),
    _SnmpSystemAlerts_Type()
)
snmpSystemAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSystemAlerts.setStatus("mandatory")
_RemoteAccessTamperDelay_Type = Integer32
_RemoteAccessTamperDelay_Object = MibScalar
remoteAccessTamperDelay = _RemoteAccessTamperDelay_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 7),
    _RemoteAccessTamperDelay_Type()
)
remoteAccessTamperDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessTamperDelay.setStatus("mandatory")


class _UserAuthenticationMethod_Type(Integer32):
    """Custom type userAuthenticationMethod based on Integer32"""
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
        *(("localOnly", 0),
          ("ldapOnly", 1),
          ("localFirstThenLdap", 2),
          ("ldapFirstThenLocal", 3))
    )


_UserAuthenticationMethod_Type.__name__ = "Integer32"
_UserAuthenticationMethod_Object = MibScalar
userAuthenticationMethod = _UserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 8),
    _UserAuthenticationMethod_Type()
)
userAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthenticationMethod.setStatus("mandatory")
_WebInactivityTimeout_Type = Integer32
_WebInactivityTimeout_Object = MibScalar
webInactivityTimeout = _WebInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 9),
    _WebInactivityTimeout_Type()
)
webInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webInactivityTimeout.setStatus("mandatory")
_SnmpAlertFilters_ObjectIdentity = ObjectIdentity
snmpAlertFilters = _SnmpAlertFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10)
)


class _SafSpTrapTempC_Type(Integer32):
    """Custom type safSpTrapTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapTempC_Type.__name__ = "Integer32"
_SafSpTrapTempC_Object = MibScalar
safSpTrapTempC = _SafSpTrapTempC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 2),
    _SafSpTrapTempC_Type()
)
safSpTrapTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapTempC.setStatus("mandatory")


class _SafSpTrapVoltC_Type(Integer32):
    """Custom type safSpTrapVoltC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapVoltC_Type.__name__ = "Integer32"
_SafSpTrapVoltC_Object = MibScalar
safSpTrapVoltC = _SafSpTrapVoltC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 3),
    _SafSpTrapVoltC_Type()
)
safSpTrapVoltC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapVoltC.setStatus("mandatory")


class _SafSpTrapPowerC_Type(Integer32):
    """Custom type safSpTrapPowerC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPowerC_Type.__name__ = "Integer32"
_SafSpTrapPowerC_Object = MibScalar
safSpTrapPowerC = _SafSpTrapPowerC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 4),
    _SafSpTrapPowerC_Type()
)
safSpTrapPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapPowerC.setStatus("mandatory")


class _SafSpTrapHdC_Type(Integer32):
    """Custom type safSpTrapHdC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapHdC_Type.__name__ = "Integer32"
_SafSpTrapHdC_Object = MibScalar
safSpTrapHdC = _SafSpTrapHdC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 5),
    _SafSpTrapHdC_Type()
)
safSpTrapHdC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapHdC.setStatus("mandatory")


class _SafSpTrapFanC_Type(Integer32):
    """Custom type safSpTrapFanC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapFanC_Type.__name__ = "Integer32"
_SafSpTrapFanC_Object = MibScalar
safSpTrapFanC = _SafSpTrapFanC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 6),
    _SafSpTrapFanC_Type()
)
safSpTrapFanC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapFanC.setStatus("mandatory")


class _SafSpTrapIhcC_Type(Integer32):
    """Custom type safSpTrapIhcC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapIhcC_Type.__name__ = "Integer32"
_SafSpTrapIhcC_Object = MibScalar
safSpTrapIhcC = _SafSpTrapIhcC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 7),
    _SafSpTrapIhcC_Type()
)
safSpTrapIhcC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapIhcC.setStatus("mandatory")


class _SafSpTrapCPUC_Type(Integer32):
    """Custom type safSpTrapCPUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapCPUC_Type.__name__ = "Integer32"
_SafSpTrapCPUC_Object = MibScalar
safSpTrapCPUC = _SafSpTrapCPUC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 8),
    _SafSpTrapCPUC_Type()
)
safSpTrapCPUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapCPUC.setStatus("mandatory")


class _SafSpTrapMemoryC_Type(Integer32):
    """Custom type safSpTrapMemoryC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapMemoryC_Type.__name__ = "Integer32"
_SafSpTrapMemoryC_Object = MibScalar
safSpTrapMemoryC = _SafSpTrapMemoryC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 9),
    _SafSpTrapMemoryC_Type()
)
safSpTrapMemoryC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapMemoryC.setStatus("mandatory")


class _SafSpTrapRdpsC_Type(Integer32):
    """Custom type safSpTrapRdpsC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapRdpsC_Type.__name__ = "Integer32"
_SafSpTrapRdpsC_Object = MibScalar
safSpTrapRdpsC = _SafSpTrapRdpsC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 10),
    _SafSpTrapRdpsC_Type()
)
safSpTrapRdpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapRdpsC.setStatus("mandatory")


class _SafSpTrapHardwareC_Type(Integer32):
    """Custom type safSpTrapHardwareC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapHardwareC_Type.__name__ = "Integer32"
_SafSpTrapHardwareC_Object = MibScalar
safSpTrapHardwareC = _SafSpTrapHardwareC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 11),
    _SafSpTrapHardwareC_Type()
)
safSpTrapHardwareC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapHardwareC.setStatus("mandatory")


class _SafSpTrapRdpsN_Type(Integer32):
    """Custom type safSpTrapRdpsN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapRdpsN_Type.__name__ = "Integer32"
_SafSpTrapRdpsN_Object = MibScalar
safSpTrapRdpsN = _SafSpTrapRdpsN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 12),
    _SafSpTrapRdpsN_Type()
)
safSpTrapRdpsN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapRdpsN.setStatus("mandatory")


class _SafSpTrapTempN_Type(Integer32):
    """Custom type safSpTrapTempN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapTempN_Type.__name__ = "Integer32"
_SafSpTrapTempN_Object = MibScalar
safSpTrapTempN = _SafSpTrapTempN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 13),
    _SafSpTrapTempN_Type()
)
safSpTrapTempN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapTempN.setStatus("mandatory")


class _SafSpTrapVoltN_Type(Integer32):
    """Custom type safSpTrapVoltN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapVoltN_Type.__name__ = "Integer32"
_SafSpTrapVoltN_Object = MibScalar
safSpTrapVoltN = _SafSpTrapVoltN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 14),
    _SafSpTrapVoltN_Type()
)
safSpTrapVoltN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapVoltN.setStatus("mandatory")


class _SafSpTrapPowerN_Type(Integer32):
    """Custom type safSpTrapPowerN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPowerN_Type.__name__ = "Integer32"
_SafSpTrapPowerN_Object = MibScalar
safSpTrapPowerN = _SafSpTrapPowerN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 15),
    _SafSpTrapPowerN_Type()
)
safSpTrapPowerN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapPowerN.setStatus("mandatory")


class _SafSpTrapFanN_Type(Integer32):
    """Custom type safSpTrapFanN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapFanN_Type.__name__ = "Integer32"
_SafSpTrapFanN_Object = MibScalar
safSpTrapFanN = _SafSpTrapFanN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 16),
    _SafSpTrapFanN_Type()
)
safSpTrapFanN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapFanN.setStatus("mandatory")


class _SafSpTrapCPUN_Type(Integer32):
    """Custom type safSpTrapCPUN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapCPUN_Type.__name__ = "Integer32"
_SafSpTrapCPUN_Object = MibScalar
safSpTrapCPUN = _SafSpTrapCPUN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 17),
    _SafSpTrapCPUN_Type()
)
safSpTrapCPUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapCPUN.setStatus("mandatory")


class _SafSpTrapMemoryN_Type(Integer32):
    """Custom type safSpTrapMemoryN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapMemoryN_Type.__name__ = "Integer32"
_SafSpTrapMemoryN_Object = MibScalar
safSpTrapMemoryN = _SafSpTrapMemoryN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 18),
    _SafSpTrapMemoryN_Type()
)
safSpTrapMemoryN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapMemoryN.setStatus("mandatory")


class _SafSpTrapHardwareN_Type(Integer32):
    """Custom type safSpTrapHardwareN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapHardwareN_Type.__name__ = "Integer32"
_SafSpTrapHardwareN_Object = MibScalar
safSpTrapHardwareN = _SafSpTrapHardwareN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 19),
    _SafSpTrapHardwareN_Type()
)
safSpTrapHardwareN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapHardwareN.setStatus("mandatory")


class _SafSpTrapRLogin_Type(Integer32):
    """Custom type safSpTrapRLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapRLogin_Type.__name__ = "Integer32"
_SafSpTrapRLogin_Object = MibScalar
safSpTrapRLogin = _SafSpTrapRLogin_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 20),
    _SafSpTrapRLogin_Type()
)
safSpTrapRLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapRLogin.setStatus("mandatory")


class _SafSpTrapOsToS_Type(Integer32):
    """Custom type safSpTrapOsToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapOsToS_Type.__name__ = "Integer32"
_SafSpTrapOsToS_Object = MibScalar
safSpTrapOsToS = _SafSpTrapOsToS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 21),
    _SafSpTrapOsToS_Type()
)
safSpTrapOsToS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapOsToS.setStatus("mandatory")


class _SafSpTrapAppS_Type(Integer32):
    """Custom type safSpTrapAppS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapAppS_Type.__name__ = "Integer32"
_SafSpTrapAppS_Object = MibScalar
safSpTrapAppS = _SafSpTrapAppS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 22),
    _SafSpTrapAppS_Type()
)
safSpTrapAppS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapAppS.setStatus("mandatory")


class _SafSpTrapPowerS_Type(Integer32):
    """Custom type safSpTrapPowerS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPowerS_Type.__name__ = "Integer32"
_SafSpTrapPowerS_Object = MibScalar
safSpTrapPowerS = _SafSpTrapPowerS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 23),
    _SafSpTrapPowerS_Type()
)
safSpTrapPowerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapPowerS.setStatus("mandatory")


class _SafSpTrapBootS_Type(Integer32):
    """Custom type safSpTrapBootS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapBootS_Type.__name__ = "Integer32"
_SafSpTrapBootS_Object = MibScalar
safSpTrapBootS = _SafSpTrapBootS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 24),
    _SafSpTrapBootS_Type()
)
safSpTrapBootS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapBootS.setStatus("mandatory")


class _SafSpTrapLdrToS_Type(Integer32):
    """Custom type safSpTrapLdrToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapLdrToS_Type.__name__ = "Integer32"
_SafSpTrapLdrToS_Object = MibScalar
safSpTrapLdrToS = _SafSpTrapLdrToS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 25),
    _SafSpTrapLdrToS_Type()
)
safSpTrapLdrToS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapLdrToS.setStatus("mandatory")


class _SafSpTrapPFAS_Type(Integer32):
    """Custom type safSpTrapPFAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPFAS_Type.__name__ = "Integer32"
_SafSpTrapPFAS_Object = MibScalar
safSpTrapPFAS = _SafSpTrapPFAS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 26),
    _SafSpTrapPFAS_Type()
)
safSpTrapPFAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapPFAS.setStatus("mandatory")


class _SafSpTrapSysLogS_Type(Integer32):
    """Custom type safSpTrapSysLogS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapSysLogS_Type.__name__ = "Integer32"
_SafSpTrapSysLogS_Object = MibScalar
safSpTrapSysLogS = _SafSpTrapSysLogS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 27),
    _SafSpTrapSysLogS_Type()
)
safSpTrapSysLogS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapSysLogS.setStatus("mandatory")


class _SafSpTrapNwChangeS_Type(Integer32):
    """Custom type safSpTrapNwChangeS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapNwChangeS_Type.__name__ = "Integer32"
_SafSpTrapNwChangeS_Object = MibScalar
safSpTrapNwChangeS = _SafSpTrapNwChangeS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 10, 28),
    _SafSpTrapNwChangeS_Type()
)
safSpTrapNwChangeS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safSpTrapNwChangeS.setStatus("mandatory")
_CustomSecuritySettings_ObjectIdentity = ObjectIdentity
customSecuritySettings = _CustomSecuritySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20)
)
_PasswordExpirationWarningPeriod_Type = Integer32
_PasswordExpirationWarningPeriod_Object = MibScalar
passwordExpirationWarningPeriod = _PasswordExpirationWarningPeriod_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 1),
    _PasswordExpirationWarningPeriod_Type()
)
passwordExpirationWarningPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passwordExpirationWarningPeriod.setStatus("mandatory")
_PasswordExpirationPeriod_Type = Integer32
_PasswordExpirationPeriod_Object = MibScalar
passwordExpirationPeriod = _PasswordExpirationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 2),
    _PasswordExpirationPeriod_Type()
)
passwordExpirationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passwordExpirationPeriod.setStatus("mandatory")
_MinimumPasswordReuseCycle_Type = Integer32
_MinimumPasswordReuseCycle_Object = MibScalar
minimumPasswordReuseCycle = _MinimumPasswordReuseCycle_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 3),
    _MinimumPasswordReuseCycle_Type()
)
minimumPasswordReuseCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minimumPasswordReuseCycle.setStatus("mandatory")
_MinimumPasswordLength_Type = Integer32
_MinimumPasswordLength_Object = MibScalar
minimumPasswordLength = _MinimumPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 5),
    _MinimumPasswordLength_Type()
)
minimumPasswordLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minimumPasswordLength.setStatus("mandatory")
_DefaultAdminPasswordExpired_Type = Integer32
_DefaultAdminPasswordExpired_Object = MibScalar
defaultAdminPasswordExpired = _DefaultAdminPasswordExpired_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 6),
    _DefaultAdminPasswordExpired_Type()
)
defaultAdminPasswordExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultAdminPasswordExpired.setStatus("mandatory")
_ChangePasswordFirstAccess_Type = Integer32
_ChangePasswordFirstAccess_Object = MibScalar
changePasswordFirstAccess = _ChangePasswordFirstAccess_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 8),
    _ChangePasswordFirstAccess_Type()
)
changePasswordFirstAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changePasswordFirstAccess.setStatus("mandatory")
_AccountLockoutPeriod_Type = Integer32
_AccountLockoutPeriod_Object = MibScalar
accountLockoutPeriod = _AccountLockoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 9),
    _AccountLockoutPeriod_Type()
)
accountLockoutPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountLockoutPeriod.setStatus("mandatory")
_MaxLoginFailures_Type = Integer32
_MaxLoginFailures_Object = MibScalar
maxLoginFailures = _MaxLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 10),
    _MaxLoginFailures_Type()
)
maxLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLoginFailures.setStatus("mandatory")
_PasswordChangeInterval_Type = Integer32
_PasswordChangeInterval_Object = MibScalar
passwordChangeInterval = _PasswordChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 1, 20, 11),
    _PasswordChangeInterval_Type()
)
passwordChangeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passwordChangeInterval.setStatus("mandatory")
_SerialPortCfg_ObjectIdentity = ObjectIdentity
serialPortCfg = _SerialPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 2)
)


class _PortBaud_Type(Integer32):
    """Custom type portBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 3),
          ("baud19200", 4),
          ("baud38400", 5),
          ("baud57600", 6),
          ("baud115200", 7))
    )


_PortBaud_Type.__name__ = "Integer32"
_PortBaud_Object = MibScalar
portBaud = _PortBaud_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 2, 1),
    _PortBaud_Type()
)
portBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBaud.setStatus("mandatory")


class _PortParity_Type(Integer32):
    """Custom type portParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("odd", 1),
          ("even", 3))
    )


_PortParity_Type.__name__ = "Integer32"
_PortParity_Object = MibScalar
portParity = _PortParity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 2, 2),
    _PortParity_Type()
)
portParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portParity.setStatus("mandatory")
_SerialRedirect_ObjectIdentity = ObjectIdentity
serialRedirect = _SerialRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 2, 3)
)


class _EnterCLIkeySeq_Type(OctetString):
    """Custom type enterCLIkeySeq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EnterCLIkeySeq_Type.__name__ = "OctetString"
_EnterCLIkeySeq_Object = MibScalar
enterCLIkeySeq = _EnterCLIkeySeq_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 2, 3, 1),
    _EnterCLIkeySeq_Type()
)
enterCLIkeySeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enterCLIkeySeq.setStatus("mandatory")


class _PortStopBits_Type(Integer32):
    """Custom type portStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oneStopbit", 0),
          ("twoOrOnePtFive", 1))
    )


_PortStopBits_Type.__name__ = "Integer32"
_PortStopBits_Object = MibScalar
portStopBits = _PortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 2, 4),
    _PortStopBits_Type()
)
portStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStopBits.setStatus("mandatory")


class _PortCLImode_Type(Integer32):
    """Custom type portCLImode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cliDisable", 0),
          ("cliWithEMScompatibleKeystrokeSeq", 1),
          ("cliWithUserDefinedKeystrokeSeq", 2))
    )


_PortCLImode_Type.__name__ = "Integer32"
_PortCLImode_Object = MibScalar
portCLImode = _PortCLImode_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 2, 18),
    _PortCLImode_Type()
)
portCLImode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCLImode.setStatus("mandatory")
_RemoteAlertIds_ObjectIdentity = ObjectIdentity
remoteAlertIds = _RemoteAlertIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3)
)
_RemoteAlertIdsTable_Object = MibTable
remoteAlertIdsTable = _RemoteAlertIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    remoteAlertIdsTable.setStatus("mandatory")
_RemoteAlertIdsEntry_Object = MibTableRow
remoteAlertIdsEntry = _RemoteAlertIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1)
)
remoteAlertIdsEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "remoteAlertIdEntryIndex"),
)
if mibBuilder.loadTexts:
    remoteAlertIdsEntry.setStatus("mandatory")


class _RemoteAlertIdEntryIndex_Type(Integer32):
    """Custom type remoteAlertIdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RemoteAlertIdEntryIndex_Type.__name__ = "Integer32"
_RemoteAlertIdEntryIndex_Object = MibTableColumn
remoteAlertIdEntryIndex = _RemoteAlertIdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 1),
    _RemoteAlertIdEntryIndex_Type()
)
remoteAlertIdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryIndex.setStatus("mandatory")


class _RemoteAlertIdEntryStatus_Type(Integer32):
    """Custom type remoteAlertIdEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RemoteAlertIdEntryStatus_Type.__name__ = "Integer32"
_RemoteAlertIdEntryStatus_Object = MibTableColumn
remoteAlertIdEntryStatus = _RemoteAlertIdEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 2),
    _RemoteAlertIdEntryStatus_Type()
)
remoteAlertIdEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryStatus.setStatus("mandatory")


class _RemoteAlertIdEntryName_Type(OctetString):
    """Custom type remoteAlertIdEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RemoteAlertIdEntryName_Type.__name__ = "OctetString"
_RemoteAlertIdEntryName_Object = MibTableColumn
remoteAlertIdEntryName = _RemoteAlertIdEntryName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 3),
    _RemoteAlertIdEntryName_Type()
)
remoteAlertIdEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryName.setStatus("mandatory")


class _RemoteAlertIdEmailAddr_Type(OctetString):
    """Custom type remoteAlertIdEmailAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 320),
    )


_RemoteAlertIdEmailAddr_Type.__name__ = "OctetString"
_RemoteAlertIdEmailAddr_Object = MibTableColumn
remoteAlertIdEmailAddr = _RemoteAlertIdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 4),
    _RemoteAlertIdEmailAddr_Type()
)
remoteAlertIdEmailAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEmailAddr.setStatus("mandatory")


class _RemoteAlertIdEntryCriticalAlert_Type(Integer32):
    """Custom type remoteAlertIdEntryCriticalAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteAlertIdEntryCriticalAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntryCriticalAlert_Object = MibTableColumn
remoteAlertIdEntryCriticalAlert = _RemoteAlertIdEntryCriticalAlert_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 5),
    _RemoteAlertIdEntryCriticalAlert_Type()
)
remoteAlertIdEntryCriticalAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryCriticalAlert.setStatus("mandatory")


class _RemoteAlertIdEntryWarningAlert_Type(Integer32):
    """Custom type remoteAlertIdEntryWarningAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteAlertIdEntryWarningAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntryWarningAlert_Object = MibTableColumn
remoteAlertIdEntryWarningAlert = _RemoteAlertIdEntryWarningAlert_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 6),
    _RemoteAlertIdEntryWarningAlert_Type()
)
remoteAlertIdEntryWarningAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryWarningAlert.setStatus("mandatory")


class _RemoteAlertIdEntrySystemAlert_Type(Integer32):
    """Custom type remoteAlertIdEntrySystemAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteAlertIdEntrySystemAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntrySystemAlert_Object = MibTableColumn
remoteAlertIdEntrySystemAlert = _RemoteAlertIdEntrySystemAlert_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 7),
    _RemoteAlertIdEntrySystemAlert_Type()
)
remoteAlertIdEntrySystemAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntrySystemAlert.setStatus("mandatory")


class _RemoteAlertIdEntryAuditAlert_Type(Integer32):
    """Custom type remoteAlertIdEntryAuditAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteAlertIdEntryAuditAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntryAuditAlert_Object = MibTableColumn
remoteAlertIdEntryAuditAlert = _RemoteAlertIdEntryAuditAlert_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 8),
    _RemoteAlertIdEntryAuditAlert_Type()
)
remoteAlertIdEntryAuditAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryAuditAlert.setStatus("mandatory")


class _RemoteAlertIdEntryAttachmentsToEmailAlerts_Type(Integer32):
    """Custom type remoteAlertIdEntryAttachmentsToEmailAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAttachments", 0),
          ("attachEventLog", 1))
    )


_RemoteAlertIdEntryAttachmentsToEmailAlerts_Type.__name__ = "Integer32"
_RemoteAlertIdEntryAttachmentsToEmailAlerts_Object = MibTableColumn
remoteAlertIdEntryAttachmentsToEmailAlerts = _RemoteAlertIdEntryAttachmentsToEmailAlerts_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 9),
    _RemoteAlertIdEntryAttachmentsToEmailAlerts_Type()
)
remoteAlertIdEntryAttachmentsToEmailAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryAttachmentsToEmailAlerts.setStatus("mandatory")
_RemoteAlertIdEntrySyslogPortAssignment_Type = Integer32
_RemoteAlertIdEntrySyslogPortAssignment_Object = MibTableColumn
remoteAlertIdEntrySyslogPortAssignment = _RemoteAlertIdEntrySyslogPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 10),
    _RemoteAlertIdEntrySyslogPortAssignment_Type()
)
remoteAlertIdEntrySyslogPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntrySyslogPortAssignment.setStatus("mandatory")


class _RemoteAlertIdEntrySyslogHostname_Type(OctetString):
    """Custom type remoteAlertIdEntrySyslogHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAlertIdEntrySyslogHostname_Type.__name__ = "OctetString"
_RemoteAlertIdEntrySyslogHostname_Object = MibTableColumn
remoteAlertIdEntrySyslogHostname = _RemoteAlertIdEntrySyslogHostname_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 11),
    _RemoteAlertIdEntrySyslogHostname_Type()
)
remoteAlertIdEntrySyslogHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntrySyslogHostname.setStatus("mandatory")


class _RemoteAlertIdEntryType_Type(Integer32):
    """Custom type remoteAlertIdEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("email", 1),
          ("syslog", 2))
    )


_RemoteAlertIdEntryType_Type.__name__ = "Integer32"
_RemoteAlertIdEntryType_Object = MibTableColumn
remoteAlertIdEntryType = _RemoteAlertIdEntryType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 1, 1, 12),
    _RemoteAlertIdEntryType_Type()
)
remoteAlertIdEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryType.setStatus("mandatory")
_RemoteAlertFiltersTable_Object = MibTable
remoteAlertFiltersTable = _RemoteAlertFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    remoteAlertFiltersTable.setStatus("mandatory")
_RemoteAlertFiltersEntry_Object = MibTableRow
remoteAlertFiltersEntry = _RemoteAlertFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1)
)
remoteAlertFiltersEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "rafIndex"),
)
if mibBuilder.loadTexts:
    remoteAlertFiltersEntry.setStatus("mandatory")


class _RafIndex_Type(Integer32):
    """Custom type rafIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RafIndex_Type.__name__ = "Integer32"
_RafIndex_Object = MibTableColumn
rafIndex = _RafIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 1),
    _RafIndex_Type()
)
rafIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafIndex.setStatus("mandatory")


class _RafSpTrapTempC_Type(Integer32):
    """Custom type rafSpTrapTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapTempC_Type.__name__ = "Integer32"
_RafSpTrapTempC_Object = MibTableColumn
rafSpTrapTempC = _RafSpTrapTempC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 2),
    _RafSpTrapTempC_Type()
)
rafSpTrapTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapTempC.setStatus("mandatory")


class _RafSpTrapVoltC_Type(Integer32):
    """Custom type rafSpTrapVoltC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapVoltC_Type.__name__ = "Integer32"
_RafSpTrapVoltC_Object = MibTableColumn
rafSpTrapVoltC = _RafSpTrapVoltC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 3),
    _RafSpTrapVoltC_Type()
)
rafSpTrapVoltC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapVoltC.setStatus("mandatory")


class _RafSpTrapPowerC_Type(Integer32):
    """Custom type rafSpTrapPowerC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPowerC_Type.__name__ = "Integer32"
_RafSpTrapPowerC_Object = MibTableColumn
rafSpTrapPowerC = _RafSpTrapPowerC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 4),
    _RafSpTrapPowerC_Type()
)
rafSpTrapPowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapPowerC.setStatus("mandatory")


class _RafSpTrapHdC_Type(Integer32):
    """Custom type rafSpTrapHdC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapHdC_Type.__name__ = "Integer32"
_RafSpTrapHdC_Object = MibTableColumn
rafSpTrapHdC = _RafSpTrapHdC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 5),
    _RafSpTrapHdC_Type()
)
rafSpTrapHdC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapHdC.setStatus("mandatory")


class _RafSpTrapFanC_Type(Integer32):
    """Custom type rafSpTrapFanC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapFanC_Type.__name__ = "Integer32"
_RafSpTrapFanC_Object = MibTableColumn
rafSpTrapFanC = _RafSpTrapFanC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 6),
    _RafSpTrapFanC_Type()
)
rafSpTrapFanC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapFanC.setStatus("mandatory")


class _RafSpTrapIhcC_Type(Integer32):
    """Custom type rafSpTrapIhcC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapIhcC_Type.__name__ = "Integer32"
_RafSpTrapIhcC_Object = MibTableColumn
rafSpTrapIhcC = _RafSpTrapIhcC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 7),
    _RafSpTrapIhcC_Type()
)
rafSpTrapIhcC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapIhcC.setStatus("mandatory")


class _RafSpTrapCPUC_Type(Integer32):
    """Custom type rafSpTrapCPUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapCPUC_Type.__name__ = "Integer32"
_RafSpTrapCPUC_Object = MibTableColumn
rafSpTrapCPUC = _RafSpTrapCPUC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 8),
    _RafSpTrapCPUC_Type()
)
rafSpTrapCPUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapCPUC.setStatus("mandatory")


class _RafSpTrapMemoryC_Type(Integer32):
    """Custom type rafSpTrapMemoryC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapMemoryC_Type.__name__ = "Integer32"
_RafSpTrapMemoryC_Object = MibTableColumn
rafSpTrapMemoryC = _RafSpTrapMemoryC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 9),
    _RafSpTrapMemoryC_Type()
)
rafSpTrapMemoryC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapMemoryC.setStatus("mandatory")


class _RafSpTrapRdpsC_Type(Integer32):
    """Custom type rafSpTrapRdpsC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapRdpsC_Type.__name__ = "Integer32"
_RafSpTrapRdpsC_Object = MibTableColumn
rafSpTrapRdpsC = _RafSpTrapRdpsC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 10),
    _RafSpTrapRdpsC_Type()
)
rafSpTrapRdpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapRdpsC.setStatus("mandatory")


class _RafSpTrapHardwareC_Type(Integer32):
    """Custom type rafSpTrapHardwareC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapHardwareC_Type.__name__ = "Integer32"
_RafSpTrapHardwareC_Object = MibTableColumn
rafSpTrapHardwareC = _RafSpTrapHardwareC_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 11),
    _RafSpTrapHardwareC_Type()
)
rafSpTrapHardwareC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapHardwareC.setStatus("mandatory")


class _RafSpTrapRdpsN_Type(Integer32):
    """Custom type rafSpTrapRdpsN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapRdpsN_Type.__name__ = "Integer32"
_RafSpTrapRdpsN_Object = MibTableColumn
rafSpTrapRdpsN = _RafSpTrapRdpsN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 12),
    _RafSpTrapRdpsN_Type()
)
rafSpTrapRdpsN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapRdpsN.setStatus("mandatory")


class _RafSpTrapTempN_Type(Integer32):
    """Custom type rafSpTrapTempN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapTempN_Type.__name__ = "Integer32"
_RafSpTrapTempN_Object = MibTableColumn
rafSpTrapTempN = _RafSpTrapTempN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 13),
    _RafSpTrapTempN_Type()
)
rafSpTrapTempN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapTempN.setStatus("mandatory")


class _RafSpTrapVoltN_Type(Integer32):
    """Custom type rafSpTrapVoltN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapVoltN_Type.__name__ = "Integer32"
_RafSpTrapVoltN_Object = MibTableColumn
rafSpTrapVoltN = _RafSpTrapVoltN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 14),
    _RafSpTrapVoltN_Type()
)
rafSpTrapVoltN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapVoltN.setStatus("mandatory")


class _RafSpTrapPowerN_Type(Integer32):
    """Custom type rafSpTrapPowerN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPowerN_Type.__name__ = "Integer32"
_RafSpTrapPowerN_Object = MibTableColumn
rafSpTrapPowerN = _RafSpTrapPowerN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 15),
    _RafSpTrapPowerN_Type()
)
rafSpTrapPowerN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapPowerN.setStatus("mandatory")


class _RafSpTrapFanN_Type(Integer32):
    """Custom type rafSpTrapFanN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapFanN_Type.__name__ = "Integer32"
_RafSpTrapFanN_Object = MibTableColumn
rafSpTrapFanN = _RafSpTrapFanN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 16),
    _RafSpTrapFanN_Type()
)
rafSpTrapFanN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapFanN.setStatus("mandatory")


class _RafSpTrapCPUN_Type(Integer32):
    """Custom type rafSpTrapCPUN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapCPUN_Type.__name__ = "Integer32"
_RafSpTrapCPUN_Object = MibTableColumn
rafSpTrapCPUN = _RafSpTrapCPUN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 17),
    _RafSpTrapCPUN_Type()
)
rafSpTrapCPUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapCPUN.setStatus("mandatory")


class _RafSpTrapMemoryN_Type(Integer32):
    """Custom type rafSpTrapMemoryN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapMemoryN_Type.__name__ = "Integer32"
_RafSpTrapMemoryN_Object = MibTableColumn
rafSpTrapMemoryN = _RafSpTrapMemoryN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 18),
    _RafSpTrapMemoryN_Type()
)
rafSpTrapMemoryN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapMemoryN.setStatus("mandatory")


class _RafSpTrapHardwareN_Type(Integer32):
    """Custom type rafSpTrapHardwareN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapHardwareN_Type.__name__ = "Integer32"
_RafSpTrapHardwareN_Object = MibTableColumn
rafSpTrapHardwareN = _RafSpTrapHardwareN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 19),
    _RafSpTrapHardwareN_Type()
)
rafSpTrapHardwareN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapHardwareN.setStatus("mandatory")


class _RafSpTrapRLogin_Type(Integer32):
    """Custom type rafSpTrapRLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapRLogin_Type.__name__ = "Integer32"
_RafSpTrapRLogin_Object = MibTableColumn
rafSpTrapRLogin = _RafSpTrapRLogin_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 20),
    _RafSpTrapRLogin_Type()
)
rafSpTrapRLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapRLogin.setStatus("mandatory")


class _RafSpTrapOsToS_Type(Integer32):
    """Custom type rafSpTrapOsToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapOsToS_Type.__name__ = "Integer32"
_RafSpTrapOsToS_Object = MibTableColumn
rafSpTrapOsToS = _RafSpTrapOsToS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 21),
    _RafSpTrapOsToS_Type()
)
rafSpTrapOsToS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapOsToS.setStatus("mandatory")


class _RafSpTrapAppS_Type(Integer32):
    """Custom type rafSpTrapAppS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapAppS_Type.__name__ = "Integer32"
_RafSpTrapAppS_Object = MibTableColumn
rafSpTrapAppS = _RafSpTrapAppS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 22),
    _RafSpTrapAppS_Type()
)
rafSpTrapAppS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapAppS.setStatus("mandatory")


class _RafSpTrapPowerS_Type(Integer32):
    """Custom type rafSpTrapPowerS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPowerS_Type.__name__ = "Integer32"
_RafSpTrapPowerS_Object = MibTableColumn
rafSpTrapPowerS = _RafSpTrapPowerS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 23),
    _RafSpTrapPowerS_Type()
)
rafSpTrapPowerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapPowerS.setStatus("mandatory")


class _RafSpTrapBootS_Type(Integer32):
    """Custom type rafSpTrapBootS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapBootS_Type.__name__ = "Integer32"
_RafSpTrapBootS_Object = MibTableColumn
rafSpTrapBootS = _RafSpTrapBootS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 24),
    _RafSpTrapBootS_Type()
)
rafSpTrapBootS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapBootS.setStatus("mandatory")


class _RafSpTrapLdrToS_Type(Integer32):
    """Custom type rafSpTrapLdrToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapLdrToS_Type.__name__ = "Integer32"
_RafSpTrapLdrToS_Object = MibTableColumn
rafSpTrapLdrToS = _RafSpTrapLdrToS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 25),
    _RafSpTrapLdrToS_Type()
)
rafSpTrapLdrToS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapLdrToS.setStatus("mandatory")


class _RafSpTrapPFAS_Type(Integer32):
    """Custom type rafSpTrapPFAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPFAS_Type.__name__ = "Integer32"
_RafSpTrapPFAS_Object = MibTableColumn
rafSpTrapPFAS = _RafSpTrapPFAS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 26),
    _RafSpTrapPFAS_Type()
)
rafSpTrapPFAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapPFAS.setStatus("mandatory")


class _RafSpTrapSysLogS_Type(Integer32):
    """Custom type rafSpTrapSysLogS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapSysLogS_Type.__name__ = "Integer32"
_RafSpTrapSysLogS_Object = MibTableColumn
rafSpTrapSysLogS = _RafSpTrapSysLogS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 27),
    _RafSpTrapSysLogS_Type()
)
rafSpTrapSysLogS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapSysLogS.setStatus("mandatory")


class _RafSpTrapNwChangeS_Type(Integer32):
    """Custom type rafSpTrapNwChangeS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapNwChangeS_Type.__name__ = "Integer32"
_RafSpTrapNwChangeS_Object = MibTableColumn
rafSpTrapNwChangeS = _RafSpTrapNwChangeS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 28),
    _RafSpTrapNwChangeS_Type()
)
rafSpTrapNwChangeS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapNwChangeS.setStatus("mandatory")


class _RafSpTrapAllAuditS_Type(Integer32):
    """Custom type rafSpTrapAllAuditS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapAllAuditS_Type.__name__ = "Integer32"
_RafSpTrapAllAuditS_Object = MibTableColumn
rafSpTrapAllAuditS = _RafSpTrapAllAuditS_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 3, 2, 1, 29),
    _RafSpTrapAllAuditS_Type()
)
rafSpTrapAllAuditS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafSpTrapAllAuditS.setStatus("mandatory")
_RemoteAccessIds_ObjectIdentity = ObjectIdentity
remoteAccessIds = _RemoteAccessIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4)
)
_RemoteAccessIdsTable_Object = MibTable
remoteAccessIdsTable = _RemoteAccessIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    remoteAccessIdsTable.setStatus("mandatory")
_RemoteAccessIdsEntry_Object = MibTableRow
remoteAccessIdsEntry = _RemoteAccessIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 1, 1)
)
remoteAccessIdsEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "remoteAccessIdEntryIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessIdsEntry.setStatus("mandatory")


class _RemoteAccessIdEntryIndex_Type(Integer32):
    """Custom type remoteAccessIdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemoteAccessIdEntryIndex_Type.__name__ = "Integer32"
_RemoteAccessIdEntryIndex_Object = MibTableColumn
remoteAccessIdEntryIndex = _RemoteAccessIdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 1, 1, 1),
    _RemoteAccessIdEntryIndex_Type()
)
remoteAccessIdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessIdEntryIndex.setStatus("mandatory")


class _RemoteAccessIdEntryUserId_Type(OctetString):
    """Custom type remoteAccessIdEntryUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RemoteAccessIdEntryUserId_Type.__name__ = "OctetString"
_RemoteAccessIdEntryUserId_Object = MibTableColumn
remoteAccessIdEntryUserId = _RemoteAccessIdEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 1, 1, 2),
    _RemoteAccessIdEntryUserId_Type()
)
remoteAccessIdEntryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessIdEntryUserId.setStatus("mandatory")


class _RemoteAccessIdEntryUserPwdLeftDays_Type(Integer32):
    """Custom type remoteAccessIdEntryUserPwdLeftDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_RemoteAccessIdEntryUserPwdLeftDays_Type.__name__ = "Integer32"
_RemoteAccessIdEntryUserPwdLeftDays_Object = MibTableColumn
remoteAccessIdEntryUserPwdLeftDays = _RemoteAccessIdEntryUserPwdLeftDays_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 1, 1, 3),
    _RemoteAccessIdEntryUserPwdLeftDays_Type()
)
remoteAccessIdEntryUserPwdLeftDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessIdEntryUserPwdLeftDays.setStatus("mandatory")
_RemoteAccessUserAuthorityLevelTable_Object = MibTable
remoteAccessUserAuthorityLevelTable = _RemoteAccessUserAuthorityLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    remoteAccessUserAuthorityLevelTable.setStatus("mandatory")
_RemoteAccessUserAuthorityLevelEntry_Object = MibTableRow
remoteAccessUserAuthorityLevelEntry = _RemoteAccessUserAuthorityLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1)
)
remoteAccessUserAuthorityLevelEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "ualIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessUserAuthorityLevelEntry.setStatus("mandatory")


class _UalIndex_Type(Integer32):
    """Custom type ualIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UalIndex_Type.__name__ = "Integer32"
_UalIndex_Object = MibTableColumn
ualIndex = _UalIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 1),
    _UalIndex_Type()
)
ualIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualIndex.setStatus("mandatory")


class _UalId_Type(OctetString):
    """Custom type ualId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UalId_Type.__name__ = "OctetString"
_UalId_Object = MibTableColumn
ualId = _UalId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 2),
    _UalId_Type()
)
ualId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualId.setStatus("mandatory")


class _UalSupervisor_Type(Integer32):
    """Custom type ualSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalSupervisor_Type.__name__ = "Integer32"
_UalSupervisor_Object = MibTableColumn
ualSupervisor = _UalSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 3),
    _UalSupervisor_Type()
)
ualSupervisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualSupervisor.setStatus("mandatory")


class _UalReadOnly_Type(Integer32):
    """Custom type ualReadOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalReadOnly_Type.__name__ = "Integer32"
_UalReadOnly_Object = MibTableColumn
ualReadOnly = _UalReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 4),
    _UalReadOnly_Type()
)
ualReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualReadOnly.setStatus("mandatory")


class _UalAccountManagement_Type(Integer32):
    """Custom type ualAccountManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAccountManagement_Type.__name__ = "Integer32"
_UalAccountManagement_Object = MibTableColumn
ualAccountManagement = _UalAccountManagement_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 5),
    _UalAccountManagement_Type()
)
ualAccountManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualAccountManagement.setStatus("mandatory")


class _UalConsoleAccess_Type(Integer32):
    """Custom type ualConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalConsoleAccess_Type.__name__ = "Integer32"
_UalConsoleAccess_Object = MibTableColumn
ualConsoleAccess = _UalConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 6),
    _UalConsoleAccess_Type()
)
ualConsoleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualConsoleAccess.setStatus("mandatory")


class _UalConsoleAndVirtualMediaAccess_Type(Integer32):
    """Custom type ualConsoleAndVirtualMediaAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalConsoleAndVirtualMediaAccess_Type.__name__ = "Integer32"
_UalConsoleAndVirtualMediaAccess_Object = MibTableColumn
ualConsoleAndVirtualMediaAccess = _UalConsoleAndVirtualMediaAccess_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 7),
    _UalConsoleAndVirtualMediaAccess_Type()
)
ualConsoleAndVirtualMediaAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualConsoleAndVirtualMediaAccess.setStatus("mandatory")


class _UalServerPowerAccess_Type(Integer32):
    """Custom type ualServerPowerAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalServerPowerAccess_Type.__name__ = "Integer32"
_UalServerPowerAccess_Object = MibTableColumn
ualServerPowerAccess = _UalServerPowerAccess_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 8),
    _UalServerPowerAccess_Type()
)
ualServerPowerAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualServerPowerAccess.setStatus("mandatory")


class _UalAllowClearLog_Type(Integer32):
    """Custom type ualAllowClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAllowClearLog_Type.__name__ = "Integer32"
_UalAllowClearLog_Object = MibTableColumn
ualAllowClearLog = _UalAllowClearLog_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 9),
    _UalAllowClearLog_Type()
)
ualAllowClearLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualAllowClearLog.setStatus("mandatory")


class _UalAdapterBasicConfig_Type(Integer32):
    """Custom type ualAdapterBasicConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterBasicConfig_Type.__name__ = "Integer32"
_UalAdapterBasicConfig_Object = MibTableColumn
ualAdapterBasicConfig = _UalAdapterBasicConfig_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 10),
    _UalAdapterBasicConfig_Type()
)
ualAdapterBasicConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualAdapterBasicConfig.setStatus("mandatory")


class _UalAdapterNetworkAndSecurityConfig_Type(Integer32):
    """Custom type ualAdapterNetworkAndSecurityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterNetworkAndSecurityConfig_Type.__name__ = "Integer32"
_UalAdapterNetworkAndSecurityConfig_Object = MibTableColumn
ualAdapterNetworkAndSecurityConfig = _UalAdapterNetworkAndSecurityConfig_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 11),
    _UalAdapterNetworkAndSecurityConfig_Type()
)
ualAdapterNetworkAndSecurityConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualAdapterNetworkAndSecurityConfig.setStatus("mandatory")


class _UalAdapterAdvancedConfig_Type(Integer32):
    """Custom type ualAdapterAdvancedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterAdvancedConfig_Type.__name__ = "Integer32"
_UalAdapterAdvancedConfig_Object = MibTableColumn
ualAdapterAdvancedConfig = _UalAdapterAdvancedConfig_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 4, 2, 1, 12),
    _UalAdapterAdvancedConfig_Type()
)
ualAdapterAdvancedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualAdapterAdvancedConfig.setStatus("mandatory")
_GroupProfiles_ObjectIdentity = ObjectIdentity
groupProfiles = _GroupProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5)
)
_GroupIdsTable_Object = MibTable
groupIdsTable = _GroupIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    groupIdsTable.setStatus("mandatory")
_GroupIdsEntry_Object = MibTableRow
groupIdsEntry = _GroupIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 1, 1)
)
groupIdsEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupIdsEntry.setStatus("mandatory")


class _GroupIndex_Type(Integer32):
    """Custom type groupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GroupIndex_Type.__name__ = "Integer32"
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 1, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupIndex.setStatus("mandatory")


class _GroupId_Type(OctetString):
    """Custom type groupId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GroupId_Type.__name__ = "OctetString"
_GroupId_Object = MibTableColumn
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 1, 1, 2),
    _GroupId_Type()
)
groupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupId.setStatus("mandatory")
_GroupRole_Type = OctetString
_GroupRole_Object = MibTableColumn
groupRole = _GroupRole_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 1, 1, 3),
    _GroupRole_Type()
)
groupRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRole.setStatus("mandatory")
_GroupRBSroleTable_Object = MibTable
groupRBSroleTable = _GroupRBSroleTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    groupRBSroleTable.setStatus("mandatory")
_GroupRBSroleEntry_Object = MibTableRow
groupRBSroleEntry = _GroupRBSroleEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1)
)
groupRBSroleEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "groupRBSroleIndex"),
)
if mibBuilder.loadTexts:
    groupRBSroleEntry.setStatus("mandatory")


class _GroupRBSroleIndex_Type(Integer32):
    """Custom type groupRBSroleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GroupRBSroleIndex_Type.__name__ = "Integer32"
_GroupRBSroleIndex_Object = MibTableColumn
groupRBSroleIndex = _GroupRBSroleIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 1),
    _GroupRBSroleIndex_Type()
)
groupRBSroleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSroleIndex.setStatus("mandatory")


class _GroupRBSroleId_Type(OctetString):
    """Custom type groupRBSroleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GroupRBSroleId_Type.__name__ = "OctetString"
_GroupRBSroleId_Object = MibTableColumn
groupRBSroleId = _GroupRBSroleId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 2),
    _GroupRBSroleId_Type()
)
groupRBSroleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSroleId.setStatus("mandatory")


class _GroupRBSSupervisor_Type(Integer32):
    """Custom type groupRBSSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSSupervisor_Type.__name__ = "Integer32"
_GroupRBSSupervisor_Object = MibTableColumn
groupRBSSupervisor = _GroupRBSSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 3),
    _GroupRBSSupervisor_Type()
)
groupRBSSupervisor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSSupervisor.setStatus("mandatory")


class _GroupRBSOperator_Type(Integer32):
    """Custom type groupRBSOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSOperator_Type.__name__ = "Integer32"
_GroupRBSOperator_Object = MibTableColumn
groupRBSOperator = _GroupRBSOperator_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 4),
    _GroupRBSOperator_Type()
)
groupRBSOperator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSOperator.setStatus("mandatory")


class _GroupRBSNetworkSecurity_Type(Integer32):
    """Custom type groupRBSNetworkSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSNetworkSecurity_Type.__name__ = "Integer32"
_GroupRBSNetworkSecurity_Object = MibTableColumn
groupRBSNetworkSecurity = _GroupRBSNetworkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 5),
    _GroupRBSNetworkSecurity_Type()
)
groupRBSNetworkSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSNetworkSecurity.setStatus("mandatory")


class _GroupRBSUserAccountManagement_Type(Integer32):
    """Custom type groupRBSUserAccountManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSUserAccountManagement_Type.__name__ = "Integer32"
_GroupRBSUserAccountManagement_Object = MibTableColumn
groupRBSUserAccountManagement = _GroupRBSUserAccountManagement_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 6),
    _GroupRBSUserAccountManagement_Type()
)
groupRBSUserAccountManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSUserAccountManagement.setStatus("mandatory")


class _GroupRBSRemoteConsoleAccess_Type(Integer32):
    """Custom type groupRBSRemoteConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSRemoteConsoleAccess_Type.__name__ = "Integer32"
_GroupRBSRemoteConsoleAccess_Object = MibTableColumn
groupRBSRemoteConsoleAccess = _GroupRBSRemoteConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 7),
    _GroupRBSRemoteConsoleAccess_Type()
)
groupRBSRemoteConsoleAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSRemoteConsoleAccess.setStatus("mandatory")


class _GroupRBSRemoteConsoleRemoteDiskAccess_Type(Integer32):
    """Custom type groupRBSRemoteConsoleRemoteDiskAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSRemoteConsoleRemoteDiskAccess_Type.__name__ = "Integer32"
_GroupRBSRemoteConsoleRemoteDiskAccess_Object = MibTableColumn
groupRBSRemoteConsoleRemoteDiskAccess = _GroupRBSRemoteConsoleRemoteDiskAccess_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 8),
    _GroupRBSRemoteConsoleRemoteDiskAccess_Type()
)
groupRBSRemoteConsoleRemoteDiskAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSRemoteConsoleRemoteDiskAccess.setStatus("mandatory")


class _GroupRBSServerPowerRestartAccess_Type(Integer32):
    """Custom type groupRBSServerPowerRestartAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSServerPowerRestartAccess_Type.__name__ = "Integer32"
_GroupRBSServerPowerRestartAccess_Object = MibTableColumn
groupRBSServerPowerRestartAccess = _GroupRBSServerPowerRestartAccess_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 9),
    _GroupRBSServerPowerRestartAccess_Type()
)
groupRBSServerPowerRestartAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSServerPowerRestartAccess.setStatus("mandatory")


class _GroupRBSBasicAdapterConfiguration_Type(Integer32):
    """Custom type groupRBSBasicAdapterConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSBasicAdapterConfiguration_Type.__name__ = "Integer32"
_GroupRBSBasicAdapterConfiguration_Object = MibTableColumn
groupRBSBasicAdapterConfiguration = _GroupRBSBasicAdapterConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 10),
    _GroupRBSBasicAdapterConfiguration_Type()
)
groupRBSBasicAdapterConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSBasicAdapterConfiguration.setStatus("mandatory")


class _GroupRBSClearEventLog_Type(Integer32):
    """Custom type groupRBSClearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSClearEventLog_Type.__name__ = "Integer32"
_GroupRBSClearEventLog_Object = MibTableColumn
groupRBSClearEventLog = _GroupRBSClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 11),
    _GroupRBSClearEventLog_Type()
)
groupRBSClearEventLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSClearEventLog.setStatus("mandatory")


class _GroupRBSAdvancedAdapterConfiguration_Type(Integer32):
    """Custom type groupRBSAdvancedAdapterConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSAdvancedAdapterConfiguration_Type.__name__ = "Integer32"
_GroupRBSAdvancedAdapterConfiguration_Object = MibTableColumn
groupRBSAdvancedAdapterConfiguration = _GroupRBSAdvancedAdapterConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 5, 2, 1, 12),
    _GroupRBSAdvancedAdapterConfiguration_Type()
)
groupRBSAdvancedAdapterConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSAdvancedAdapterConfiguration.setStatus("mandatory")
_SshClientAuth_ObjectIdentity = ObjectIdentity
sshClientAuth = _SshClientAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6)
)
_SshClientAuthPubKeyTable_Object = MibTable
sshClientAuthPubKeyTable = _SshClientAuthPubKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sshClientAuthPubKeyTable.setStatus("mandatory")
_SshClientAuthPubKeyEntry_Object = MibTableRow
sshClientAuthPubKeyEntry = _SshClientAuthPubKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1, 1)
)
sshClientAuthPubKeyEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "sshClientAuthRemoteAccessIdIndex"),
    (0, "LENOVO-XCC-MIB", "sshClientAuthPubKeyIndex"),
)
if mibBuilder.loadTexts:
    sshClientAuthPubKeyEntry.setStatus("mandatory")


class _SshClientAuthRemoteAccessIdIndex_Type(Integer32):
    """Custom type sshClientAuthRemoteAccessIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SshClientAuthRemoteAccessIdIndex_Type.__name__ = "Integer32"
_SshClientAuthRemoteAccessIdIndex_Object = MibTableColumn
sshClientAuthRemoteAccessIdIndex = _SshClientAuthRemoteAccessIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1, 1, 1),
    _SshClientAuthRemoteAccessIdIndex_Type()
)
sshClientAuthRemoteAccessIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshClientAuthRemoteAccessIdIndex.setStatus("mandatory")


class _SshClientAuthPubKeyIndex_Type(Integer32):
    """Custom type sshClientAuthPubKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SshClientAuthPubKeyIndex_Type.__name__ = "Integer32"
_SshClientAuthPubKeyIndex_Object = MibTableColumn
sshClientAuthPubKeyIndex = _SshClientAuthPubKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1, 1, 2),
    _SshClientAuthPubKeyIndex_Type()
)
sshClientAuthPubKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyIndex.setStatus("mandatory")


class _SshClientAuthPubKeyType_Type(Integer32):
    """Custom type sshClientAuthPubKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sshDss", 1),
          ("sshRsa", 2))
    )


_SshClientAuthPubKeyType_Type.__name__ = "Integer32"
_SshClientAuthPubKeyType_Object = MibTableColumn
sshClientAuthPubKeyType = _SshClientAuthPubKeyType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1, 1, 3),
    _SshClientAuthPubKeyType_Type()
)
sshClientAuthPubKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyType.setStatus("mandatory")


class _SshClientAuthPubKeySize_Type(Integer32):
    """Custom type sshClientAuthPubKeySize based on Integer32"""
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
        *(("bits512", 1),
          ("bits768", 2),
          ("bits1024", 3),
          ("bits2048", 4),
          ("bits4096", 5))
    )


_SshClientAuthPubKeySize_Type.__name__ = "Integer32"
_SshClientAuthPubKeySize_Object = MibTableColumn
sshClientAuthPubKeySize = _SshClientAuthPubKeySize_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1, 1, 4),
    _SshClientAuthPubKeySize_Type()
)
sshClientAuthPubKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeySize.setStatus("mandatory")
_SshClientAuthPubKeyFingerprint_Type = OctetString
_SshClientAuthPubKeyFingerprint_Object = MibTableColumn
sshClientAuthPubKeyFingerprint = _SshClientAuthPubKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1, 1, 5),
    _SshClientAuthPubKeyFingerprint_Type()
)
sshClientAuthPubKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyFingerprint.setStatus("mandatory")
_SshClientAuthPubKeyAcceptFrom_Type = OctetString
_SshClientAuthPubKeyAcceptFrom_Object = MibTableColumn
sshClientAuthPubKeyAcceptFrom = _SshClientAuthPubKeyAcceptFrom_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 1, 1, 6),
    _SshClientAuthPubKeyAcceptFrom_Type()
)
sshClientAuthPubKeyAcceptFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyAcceptFrom.setStatus("mandatory")
_SshClientAuthPubKeyUnused_Type = Integer32
_SshClientAuthPubKeyUnused_Object = MibScalar
sshClientAuthPubKeyUnused = _SshClientAuthPubKeyUnused_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 1, 6, 2),
    _SshClientAuthPubKeyUnused_Type()
)
sshClientAuthPubKeyUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyUnused.setStatus("mandatory")
_SpClock_ObjectIdentity = ObjectIdentity
spClock = _SpClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 2)
)
_SpClockDateAndTimeSetting_Type = OctetString
_SpClockDateAndTimeSetting_Object = MibScalar
spClockDateAndTimeSetting = _SpClockDateAndTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 2, 1),
    _SpClockDateAndTimeSetting_Type()
)
spClockDateAndTimeSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spClockDateAndTimeSetting.setStatus("mandatory")
_SpClockTimezoneSetting_Type = OctetString
_SpClockTimezoneSetting_Object = MibScalar
spClockTimezoneSetting = _SpClockTimezoneSetting_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 2, 2),
    _SpClockTimezoneSetting_Type()
)
spClockTimezoneSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spClockTimezoneSetting.setStatus("mandatory")
_SpIdentification_ObjectIdentity = ObjectIdentity
spIdentification = _SpIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3)
)


class _SpTxtId_Type(OctetString):
    """Custom type spTxtId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SpTxtId_Type.__name__ = "OctetString"
_SpTxtId_Object = MibScalar
spTxtId = _SpTxtId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3, 1),
    _SpTxtId_Type()
)
spTxtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTxtId.setStatus("mandatory")
_SpRoomID_Type = DisplayString
_SpRoomID_Object = MibScalar
spRoomID = _SpRoomID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3, 2),
    _SpRoomID_Type()
)
spRoomID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRoomID.setStatus("mandatory")
_SpRackID_Type = DisplayString
_SpRackID_Object = MibScalar
spRackID = _SpRackID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3, 3),
    _SpRackID_Type()
)
spRackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRackID.setStatus("mandatory")
_SpRackUnitPosition_Type = DisplayString
_SpRackUnitPosition_Object = MibScalar
spRackUnitPosition = _SpRackUnitPosition_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3, 4),
    _SpRackUnitPosition_Type()
)
spRackUnitPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRackUnitPosition.setStatus("mandatory")
_SpRackUnitHeight_Type = DisplayString
_SpRackUnitHeight_Object = MibScalar
spRackUnitHeight = _SpRackUnitHeight_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3, 5),
    _SpRackUnitHeight_Type()
)
spRackUnitHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRackUnitHeight.setStatus("mandatory")
_SpRackBladeBay_Type = DisplayString
_SpRackBladeBay_Object = MibScalar
spRackBladeBay = _SpRackBladeBay_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3, 6),
    _SpRackBladeBay_Type()
)
spRackBladeBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRackBladeBay.setStatus("mandatory")
_SpFullPostalAddress_Type = DisplayString
_SpFullPostalAddress_Object = MibScalar
spFullPostalAddress = _SpFullPostalAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 3, 7),
    _SpFullPostalAddress_Type()
)
spFullPostalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spFullPostalAddress.setStatus("mandatory")
_NetworkConfiguration_ObjectIdentity = ObjectIdentity
networkConfiguration = _NetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4)
)
_NetworkInterfaces_ObjectIdentity = ObjectIdentity
networkInterfaces = _NetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1)
)
_EthernetInterface_ObjectIdentity = ObjectIdentity
ethernetInterface = _EthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1)
)


class _EthernetInterfaceType_Type(OctetString):
    """Custom type ethernetInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EthernetInterfaceType_Type.__name__ = "OctetString"
_EthernetInterfaceType_Object = MibScalar
ethernetInterfaceType = _EthernetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 1),
    _EthernetInterfaceType_Type()
)
ethernetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceType.setStatus("mandatory")


class _EthernetInterfaceEnabled_Type(Integer32):
    """Custom type ethernetInterfaceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDisabled", 0),
          ("interfaceEnabled", 1))
    )


_EthernetInterfaceEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceEnabled_Object = MibScalar
ethernetInterfaceEnabled = _EthernetInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 2),
    _EthernetInterfaceEnabled_Type()
)
ethernetInterfaceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceEnabled.setStatus("mandatory")


class _EthernetInterfaceHostName_Type(OctetString):
    """Custom type ethernetInterfaceHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthernetInterfaceHostName_Type.__name__ = "OctetString"
_EthernetInterfaceHostName_Object = MibScalar
ethernetInterfaceHostName = _EthernetInterfaceHostName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 3),
    _EthernetInterfaceHostName_Type()
)
ethernetInterfaceHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceHostName.setStatus("mandatory")
_EthernetInterfaceIPAddress_Type = IpAddress
_EthernetInterfaceIPAddress_Object = MibScalar
ethernetInterfaceIPAddress = _EthernetInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 4),
    _EthernetInterfaceIPAddress_Type()
)
ethernetInterfaceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPAddress.setStatus("mandatory")


class _EthernetInterfaceAutoNegotiate_Type(Integer32):
    """Custom type ethernetInterfaceAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("disabled", 1))
    )


_EthernetInterfaceAutoNegotiate_Type.__name__ = "Integer32"
_EthernetInterfaceAutoNegotiate_Object = MibScalar
ethernetInterfaceAutoNegotiate = _EthernetInterfaceAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 5),
    _EthernetInterfaceAutoNegotiate_Type()
)
ethernetInterfaceAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceAutoNegotiate.setStatus("mandatory")


class _EthernetInterfaceDataRate_Type(Integer32):
    """Custom type ethernetInterfaceDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enet10Megabit", 3),
          ("enet100Megabit", 4))
    )


_EthernetInterfaceDataRate_Type.__name__ = "Integer32"
_EthernetInterfaceDataRate_Object = MibScalar
ethernetInterfaceDataRate = _EthernetInterfaceDataRate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 6),
    _EthernetInterfaceDataRate_Type()
)
ethernetInterfaceDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDataRate.setStatus("mandatory")


class _EthernetInterfaceDuplexSetting_Type(Integer32):
    """Custom type ethernetInterfaceDuplexSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_EthernetInterfaceDuplexSetting_Type.__name__ = "Integer32"
_EthernetInterfaceDuplexSetting_Object = MibScalar
ethernetInterfaceDuplexSetting = _EthernetInterfaceDuplexSetting_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 7),
    _EthernetInterfaceDuplexSetting_Type()
)
ethernetInterfaceDuplexSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDuplexSetting.setStatus("mandatory")


class _EthernetInterfaceLAA_Type(OctetString):
    """Custom type ethernetInterfaceLAA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_EthernetInterfaceLAA_Type.__name__ = "OctetString"
_EthernetInterfaceLAA_Object = MibScalar
ethernetInterfaceLAA = _EthernetInterfaceLAA_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 8),
    _EthernetInterfaceLAA_Type()
)
ethernetInterfaceLAA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceLAA.setStatus("mandatory")


class _EthernetInterfaceDhcpEnabled_Type(Integer32):
    """Custom type ethernetInterfaceDhcpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpDisabled", 0),
          ("dhcpEnabled", 1),
          ("dhcpTry", 2))
    )


_EthernetInterfaceDhcpEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceDhcpEnabled_Object = MibScalar
ethernetInterfaceDhcpEnabled = _EthernetInterfaceDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 9),
    _EthernetInterfaceDhcpEnabled_Type()
)
ethernetInterfaceDhcpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDhcpEnabled.setStatus("mandatory")
_EthernetInterfaceGatewayIPAddress_Type = IpAddress
_EthernetInterfaceGatewayIPAddress_Object = MibScalar
ethernetInterfaceGatewayIPAddress = _EthernetInterfaceGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 10),
    _EthernetInterfaceGatewayIPAddress_Type()
)
ethernetInterfaceGatewayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceGatewayIPAddress.setStatus("mandatory")


class _EthernetInterfaceBIA_Type(OctetString):
    """Custom type ethernetInterfaceBIA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_EthernetInterfaceBIA_Type.__name__ = "OctetString"
_EthernetInterfaceBIA_Object = MibScalar
ethernetInterfaceBIA = _EthernetInterfaceBIA_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 11),
    _EthernetInterfaceBIA_Type()
)
ethernetInterfaceBIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceBIA.setStatus("mandatory")
_EthernetInterfaceMTU_Type = Integer32
_EthernetInterfaceMTU_Object = MibScalar
ethernetInterfaceMTU = _EthernetInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 12),
    _EthernetInterfaceMTU_Type()
)
ethernetInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceMTU.setStatus("mandatory")
_EthernetInterfaceSubnetMask_Type = IpAddress
_EthernetInterfaceSubnetMask_Object = MibScalar
ethernetInterfaceSubnetMask = _EthernetInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 13),
    _EthernetInterfaceSubnetMask_Type()
)
ethernetInterfaceSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceSubnetMask.setStatus("mandatory")
_DhcpEthernetInterface_ObjectIdentity = ObjectIdentity
dhcpEthernetInterface = _DhcpEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14)
)


class _DhcpHostName_Type(OctetString):
    """Custom type dhcpHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpHostName_Type.__name__ = "OctetString"
_DhcpHostName_Object = MibScalar
dhcpHostName = _DhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 1),
    _DhcpHostName_Type()
)
dhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpHostName.setStatus("mandatory")
_DhcpIPAddress_Type = IpAddress
_DhcpIPAddress_Object = MibScalar
dhcpIPAddress = _DhcpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 2),
    _DhcpIPAddress_Type()
)
dhcpIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIPAddress.setStatus("mandatory")
_DhcpGatewayIPAddress_Type = IpAddress
_DhcpGatewayIPAddress_Object = MibScalar
dhcpGatewayIPAddress = _DhcpGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 3),
    _DhcpGatewayIPAddress_Type()
)
dhcpGatewayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpGatewayIPAddress.setStatus("mandatory")
_DhcpSubnetMask_Type = IpAddress
_DhcpSubnetMask_Object = MibScalar
dhcpSubnetMask = _DhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 4),
    _DhcpSubnetMask_Type()
)
dhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetMask.setStatus("mandatory")


class _DhcpDomainName_Type(OctetString):
    """Custom type dhcpDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpDomainName_Type.__name__ = "OctetString"
_DhcpDomainName_Object = MibScalar
dhcpDomainName = _DhcpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 5),
    _DhcpDomainName_Type()
)
dhcpDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDomainName.setStatus("mandatory")
_DhcpPrimaryDNSServer_Type = IpAddress
_DhcpPrimaryDNSServer_Object = MibScalar
dhcpPrimaryDNSServer = _DhcpPrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 6),
    _DhcpPrimaryDNSServer_Type()
)
dhcpPrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPrimaryDNSServer.setStatus("mandatory")
_DhcpSecondaryDNSServer_Type = IpAddress
_DhcpSecondaryDNSServer_Object = MibScalar
dhcpSecondaryDNSServer = _DhcpSecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 7),
    _DhcpSecondaryDNSServer_Type()
)
dhcpSecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSecondaryDNSServer.setStatus("mandatory")
_DhcpTertiaryDNSServer_Type = IpAddress
_DhcpTertiaryDNSServer_Object = MibScalar
dhcpTertiaryDNSServer = _DhcpTertiaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 14, 8),
    _DhcpTertiaryDNSServer_Type()
)
dhcpTertiaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpTertiaryDNSServer.setStatus("mandatory")


class _EthernetInterfaceVlan_Type(Integer32):
    """Custom type ethernetInterfaceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("disabled", 1))
    )


_EthernetInterfaceVlan_Type.__name__ = "Integer32"
_EthernetInterfaceVlan_Object = MibScalar
ethernetInterfaceVlan = _EthernetInterfaceVlan_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 15),
    _EthernetInterfaceVlan_Type()
)
ethernetInterfaceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceVlan.setStatus("mandatory")


class _EthernetInterfaceVlanID_Type(Integer32):
    """Custom type ethernetInterfaceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EthernetInterfaceVlanID_Type.__name__ = "Integer32"
_EthernetInterfaceVlanID_Object = MibScalar
ethernetInterfaceVlanID = _EthernetInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 1, 16),
    _EthernetInterfaceVlanID_Type()
)
ethernetInterfaceVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceVlanID.setStatus("mandatory")
_EthernetInterfaceIPv6_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6 = _EthernetInterfaceIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4)
)


class _EthernetInterfaceIPv6Enabled_Type(Integer32):
    """Custom type ethernetInterfaceIPv6Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceIPv6Enabled_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6Enabled_Object = MibScalar
ethernetInterfaceIPv6Enabled = _EthernetInterfaceIPv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 2),
    _EthernetInterfaceIPv6Enabled_Type()
)
ethernetInterfaceIPv6Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6Enabled.setStatus("mandatory")
_EthernetInterfaceIPv6Config_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6Config = _EthernetInterfaceIPv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5)
)
_EthernetInterfaceIPv6LocalAddress_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6LocalAddress = _EthernetInterfaceIPv6LocalAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 1)
)
_EthernetInterfaceIPv6LinkLocalAddress_Type = InetAddressIPv6
_EthernetInterfaceIPv6LinkLocalAddress_Object = MibScalar
ethernetInterfaceIPv6LinkLocalAddress = _EthernetInterfaceIPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 1, 1),
    _EthernetInterfaceIPv6LinkLocalAddress_Type()
)
ethernetInterfaceIPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6LinkLocalAddress.setStatus("mandatory")
_EthernetInterfaceIPv6StaticIPConfig_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6StaticIPConfig = _EthernetInterfaceIPv6StaticIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 2)
)


class _EthernetInterfaceIPv6StaticIPConfigEnabled_Type(Integer32):
    """Custom type ethernetInterfaceIPv6StaticIPConfigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceIPv6StaticIPConfigEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6StaticIPConfigEnabled_Object = MibScalar
ethernetInterfaceIPv6StaticIPConfigEnabled = _EthernetInterfaceIPv6StaticIPConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 2, 1),
    _EthernetInterfaceIPv6StaticIPConfigEnabled_Type()
)
ethernetInterfaceIPv6StaticIPConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPConfigEnabled.setStatus("mandatory")
_EthernetInterfaceIPv6StaticIPAddress_Type = InetAddressIPv6
_EthernetInterfaceIPv6StaticIPAddress_Object = MibScalar
ethernetInterfaceIPv6StaticIPAddress = _EthernetInterfaceIPv6StaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 2, 2),
    _EthernetInterfaceIPv6StaticIPAddress_Type()
)
ethernetInterfaceIPv6StaticIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPAddress.setStatus("mandatory")


class _EthernetInterfaceIPv6StaticIPAddressPrefixLen_Type(Integer32):
    """Custom type ethernetInterfaceIPv6StaticIPAddressPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_EthernetInterfaceIPv6StaticIPAddressPrefixLen_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6StaticIPAddressPrefixLen_Object = MibScalar
ethernetInterfaceIPv6StaticIPAddressPrefixLen = _EthernetInterfaceIPv6StaticIPAddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 2, 3),
    _EthernetInterfaceIPv6StaticIPAddressPrefixLen_Type()
)
ethernetInterfaceIPv6StaticIPAddressPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPAddressPrefixLen.setStatus("mandatory")
_EthernetInterfaceIPv6StaticIPDefaultRoute_Type = InetAddressIPv6
_EthernetInterfaceIPv6StaticIPDefaultRoute_Object = MibScalar
ethernetInterfaceIPv6StaticIPDefaultRoute = _EthernetInterfaceIPv6StaticIPDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 2, 4),
    _EthernetInterfaceIPv6StaticIPDefaultRoute_Type()
)
ethernetInterfaceIPv6StaticIPDefaultRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPDefaultRoute.setStatus("mandatory")
_EthernetInterfaceIPv6AutoIPConfig_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6AutoIPConfig = _EthernetInterfaceIPv6AutoIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3)
)
_EthernetInterfaceDHCPv6Config_ObjectIdentity = ObjectIdentity
ethernetInterfaceDHCPv6Config = _EthernetInterfaceDHCPv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2)
)


class _EthernetInterfaceDHCPv6Enabled_Type(Integer32):
    """Custom type ethernetInterfaceDHCPv6Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceDHCPv6Enabled_Type.__name__ = "Integer32"
_EthernetInterfaceDHCPv6Enabled_Object = MibScalar
ethernetInterfaceDHCPv6Enabled = _EthernetInterfaceDHCPv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2, 1),
    _EthernetInterfaceDHCPv6Enabled_Type()
)
ethernetInterfaceDHCPv6Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6Enabled.setStatus("mandatory")
_EthernetInterfaceDHCPv6IPAddress_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6IPAddress_Object = MibScalar
ethernetInterfaceDHCPv6IPAddress = _EthernetInterfaceDHCPv6IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2, 2),
    _EthernetInterfaceDHCPv6IPAddress_Type()
)
ethernetInterfaceDHCPv6IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6IPAddress.setStatus("mandatory")


class _EthernetInterfaceDHCPv6DomainName_Type(OctetString):
    """Custom type ethernetInterfaceDHCPv6DomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthernetInterfaceDHCPv6DomainName_Type.__name__ = "OctetString"
_EthernetInterfaceDHCPv6DomainName_Object = MibScalar
ethernetInterfaceDHCPv6DomainName = _EthernetInterfaceDHCPv6DomainName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2, 4),
    _EthernetInterfaceDHCPv6DomainName_Type()
)
ethernetInterfaceDHCPv6DomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6DomainName.setStatus("mandatory")
_EthernetInterfaceDHCPv6PrimaryDNSServer_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6PrimaryDNSServer_Object = MibScalar
ethernetInterfaceDHCPv6PrimaryDNSServer = _EthernetInterfaceDHCPv6PrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2, 5),
    _EthernetInterfaceDHCPv6PrimaryDNSServer_Type()
)
ethernetInterfaceDHCPv6PrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6PrimaryDNSServer.setStatus("mandatory")
_EthernetInterfaceDHCPv6SecondaryDNSServer_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6SecondaryDNSServer_Object = MibScalar
ethernetInterfaceDHCPv6SecondaryDNSServer = _EthernetInterfaceDHCPv6SecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2, 6),
    _EthernetInterfaceDHCPv6SecondaryDNSServer_Type()
)
ethernetInterfaceDHCPv6SecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6SecondaryDNSServer.setStatus("mandatory")
_EthernetInterfaceDHCPv6TertiaryDNSServer_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6TertiaryDNSServer_Object = MibScalar
ethernetInterfaceDHCPv6TertiaryDNSServer = _EthernetInterfaceDHCPv6TertiaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2, 7),
    _EthernetInterfaceDHCPv6TertiaryDNSServer_Type()
)
ethernetInterfaceDHCPv6TertiaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6TertiaryDNSServer.setStatus("mandatory")
_EthernetInterfaceDHCPv6Server_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6Server_Object = MibScalar
ethernetInterfaceDHCPv6Server = _EthernetInterfaceDHCPv6Server_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 2, 8),
    _EthernetInterfaceDHCPv6Server_Type()
)
ethernetInterfaceDHCPv6Server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6Server.setStatus("mandatory")
_EthernetInterfaceIPv6StatelessAutoConfig_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6StatelessAutoConfig = _EthernetInterfaceIPv6StatelessAutoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 3)
)


class _EthernetInterfaceIPv6StatelessAutoConfigEnabled_Type(Integer32):
    """Custom type ethernetInterfaceIPv6StatelessAutoConfigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceIPv6StatelessAutoConfigEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6StatelessAutoConfigEnabled_Object = MibScalar
ethernetInterfaceIPv6StatelessAutoConfigEnabled = _EthernetInterfaceIPv6StatelessAutoConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 3, 1),
    _EthernetInterfaceIPv6StatelessAutoConfigEnabled_Type()
)
ethernetInterfaceIPv6StatelessAutoConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StatelessAutoConfigEnabled.setStatus("mandatory")
_EthernetInterfaceStatelessAutoConfigAddressesTable_Object = MibTable
ethernetInterfaceStatelessAutoConfigAddressesTable = _EthernetInterfaceStatelessAutoConfigAddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesTable.setStatus("mandatory")
_EthernetInterfaceStatelessAutoConfigAddressesEntry_Object = MibTableRow
ethernetInterfaceStatelessAutoConfigAddressesEntry = _EthernetInterfaceStatelessAutoConfigAddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 3, 2, 1)
)
ethernetInterfaceStatelessAutoConfigAddressesEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "ethernetInterfaceStatelessAutoConfigAddressesIndex"),
)
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesEntry.setStatus("mandatory")


class _EthernetInterfaceStatelessAutoConfigAddressesIndex_Type(Integer32):
    """Custom type ethernetInterfaceStatelessAutoConfigAddressesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EthernetInterfaceStatelessAutoConfigAddressesIndex_Type.__name__ = "Integer32"
_EthernetInterfaceStatelessAutoConfigAddressesIndex_Object = MibTableColumn
ethernetInterfaceStatelessAutoConfigAddressesIndex = _EthernetInterfaceStatelessAutoConfigAddressesIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 3, 2, 1, 1),
    _EthernetInterfaceStatelessAutoConfigAddressesIndex_Type()
)
ethernetInterfaceStatelessAutoConfigAddressesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesIndex.setStatus("mandatory")
_EthernetInterfaceStatelessAutoConfigAddresses_Type = InetAddressIPv6
_EthernetInterfaceStatelessAutoConfigAddresses_Object = MibTableColumn
ethernetInterfaceStatelessAutoConfigAddresses = _EthernetInterfaceStatelessAutoConfigAddresses_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 3, 2, 1, 2),
    _EthernetInterfaceStatelessAutoConfigAddresses_Type()
)
ethernetInterfaceStatelessAutoConfigAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddresses.setStatus("mandatory")


class _EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Type(Integer32):
    """Custom type ethernetInterfaceStatelessAutoConfigAddressesPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Type.__name__ = "Integer32"
_EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Object = MibTableColumn
ethernetInterfaceStatelessAutoConfigAddressesPrefixLen = _EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 4, 5, 3, 3, 2, 1, 3),
    _EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Type()
)
ethernetInterfaceStatelessAutoConfigAddressesPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesPrefixLen.setStatus("mandatory")
_VlansSM_ObjectIdentity = ObjectIdentity
vlansSM = _VlansSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5)
)
_VlansSMvlan1config_ObjectIdentity = ObjectIdentity
vlansSMvlan1config = _VlansSMvlan1config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 1)
)
_VlansSMvlan1Name_Type = OctetString
_VlansSMvlan1Name_Object = MibScalar
vlansSMvlan1Name = _VlansSMvlan1Name_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 1, 1),
    _VlansSMvlan1Name_Type()
)
vlansSMvlan1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan1Name.setStatus("mandatory")


class _VlansSMvlan1vlanId_Type(Integer32):
    """Custom type vlansSMvlan1vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlansSMvlan1vlanId_Type.__name__ = "Integer32"
_VlansSMvlan1vlanId_Object = MibScalar
vlansSMvlan1vlanId = _VlansSMvlan1vlanId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 1, 2),
    _VlansSMvlan1vlanId_Type()
)
vlansSMvlan1vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan1vlanId.setStatus("mandatory")


class _VlansSMvlan1State_Type(Integer32):
    """Custom type vlansSMvlan1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VlansSMvlan1State_Type.__name__ = "Integer32"
_VlansSMvlan1State_Object = MibScalar
vlansSMvlan1State = _VlansSMvlan1State_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 1, 3),
    _VlansSMvlan1State_Type()
)
vlansSMvlan1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan1State.setStatus("mandatory")


class _VlansSMvlan1RemoteControl_Type(Integer32):
    """Custom type vlansSMvlan1RemoteControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VlansSMvlan1RemoteControl_Type.__name__ = "Integer32"
_VlansSMvlan1RemoteControl_Object = MibScalar
vlansSMvlan1RemoteControl = _VlansSMvlan1RemoteControl_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 1, 4),
    _VlansSMvlan1RemoteControl_Type()
)
vlansSMvlan1RemoteControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan1RemoteControl.setStatus("mandatory")


class _VlansSMvlan1SSerialOverLan_Type(Integer32):
    """Custom type vlansSMvlan1SSerialOverLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VlansSMvlan1SSerialOverLan_Type.__name__ = "Integer32"
_VlansSMvlan1SSerialOverLan_Object = MibScalar
vlansSMvlan1SSerialOverLan = _VlansSMvlan1SSerialOverLan_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 1, 5),
    _VlansSMvlan1SSerialOverLan_Type()
)
vlansSMvlan1SSerialOverLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan1SSerialOverLan.setStatus("mandatory")
_VlansSMvlan2config_ObjectIdentity = ObjectIdentity
vlansSMvlan2config = _VlansSMvlan2config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2)
)
_VlansSMvlan2Name_Type = OctetString
_VlansSMvlan2Name_Object = MibScalar
vlansSMvlan2Name = _VlansSMvlan2Name_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 1),
    _VlansSMvlan2Name_Type()
)
vlansSMvlan2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2Name.setStatus("mandatory")


class _VlansSMvlan2vlanId_Type(Integer32):
    """Custom type vlansSMvlan2vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlansSMvlan2vlanId_Type.__name__ = "Integer32"
_VlansSMvlan2vlanId_Object = MibScalar
vlansSMvlan2vlanId = _VlansSMvlan2vlanId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 2),
    _VlansSMvlan2vlanId_Type()
)
vlansSMvlan2vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2vlanId.setStatus("mandatory")


class _VlansSMvlan2State_Type(Integer32):
    """Custom type vlansSMvlan2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VlansSMvlan2State_Type.__name__ = "Integer32"
_VlansSMvlan2State_Object = MibScalar
vlansSMvlan2State = _VlansSMvlan2State_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 3),
    _VlansSMvlan2State_Type()
)
vlansSMvlan2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2State.setStatus("mandatory")


class _VlansSMvlan2RemoteControl_Type(Integer32):
    """Custom type vlansSMvlan2RemoteControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VlansSMvlan2RemoteControl_Type.__name__ = "Integer32"
_VlansSMvlan2RemoteControl_Object = MibScalar
vlansSMvlan2RemoteControl = _VlansSMvlan2RemoteControl_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 4),
    _VlansSMvlan2RemoteControl_Type()
)
vlansSMvlan2RemoteControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2RemoteControl.setStatus("mandatory")


class _VlansSMvlan2SerialOverLan_Type(Integer32):
    """Custom type vlansSMvlan2SerialOverLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VlansSMvlan2SerialOverLan_Type.__name__ = "Integer32"
_VlansSMvlan2SerialOverLan_Object = MibScalar
vlansSMvlan2SerialOverLan = _VlansSMvlan2SerialOverLan_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 5),
    _VlansSMvlan2SerialOverLan_Type()
)
vlansSMvlan2SerialOverLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2SerialOverLan.setStatus("mandatory")
_VlansSMvlan2ipv4Config_ObjectIdentity = ObjectIdentity
vlansSMvlan2ipv4Config = _VlansSMvlan2ipv4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 6)
)
_VlansSMvlan2IPv4Address_Type = IpAddress
_VlansSMvlan2IPv4Address_Object = MibScalar
vlansSMvlan2IPv4Address = _VlansSMvlan2IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 6, 1),
    _VlansSMvlan2IPv4Address_Type()
)
vlansSMvlan2IPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4Address.setStatus("mandatory")
_VlansSMvlan2IPv4Gateway_Type = IpAddress
_VlansSMvlan2IPv4Gateway_Object = MibScalar
vlansSMvlan2IPv4Gateway = _VlansSMvlan2IPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 6, 2),
    _VlansSMvlan2IPv4Gateway_Type()
)
vlansSMvlan2IPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4Gateway.setStatus("mandatory")
_VlansSMvlan2IPv4SubnetMask_Type = IpAddress
_VlansSMvlan2IPv4SubnetMask_Object = MibScalar
vlansSMvlan2IPv4SubnetMask = _VlansSMvlan2IPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 6, 3),
    _VlansSMvlan2IPv4SubnetMask_Type()
)
vlansSMvlan2IPv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4SubnetMask.setStatus("mandatory")
_VlansSMvlan2ipv6Config_ObjectIdentity = ObjectIdentity
vlansSMvlan2ipv6Config = _VlansSMvlan2ipv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 7)
)
_VlansSMvlan2IPv6Address_Type = InetAddressIPv6
_VlansSMvlan2IPv6Address_Object = MibScalar
vlansSMvlan2IPv6Address = _VlansSMvlan2IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 7, 1),
    _VlansSMvlan2IPv6Address_Type()
)
vlansSMvlan2IPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6Address.setStatus("mandatory")
_VlansSMvlan2IPv6Gateway_Type = InetAddressIPv6
_VlansSMvlan2IPv6Gateway_Object = MibScalar
vlansSMvlan2IPv6Gateway = _VlansSMvlan2IPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 7, 2),
    _VlansSMvlan2IPv6Gateway_Type()
)
vlansSMvlan2IPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6Gateway.setStatus("mandatory")


class _VlansSMvlan2IPv6PrefixLength_Type(Integer32):
    """Custom type vlansSMvlan2IPv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VlansSMvlan2IPv6PrefixLength_Type.__name__ = "Integer32"
_VlansSMvlan2IPv6PrefixLength_Object = MibScalar
vlansSMvlan2IPv6PrefixLength = _VlansSMvlan2IPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 7, 3),
    _VlansSMvlan2IPv6PrefixLength_Type()
)
vlansSMvlan2IPv6PrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6PrefixLength.setStatus("mandatory")
_VlansSMvlan2ipv4StatusRoutes_ObjectIdentity = ObjectIdentity
vlansSMvlan2ipv4StatusRoutes = _VlansSMvlan2ipv4StatusRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 8)
)
_VlansSMvlan2IPv4StaticRouteIP1_Type = IpAddress
_VlansSMvlan2IPv4StaticRouteIP1_Object = MibScalar
vlansSMvlan2IPv4StaticRouteIP1 = _VlansSMvlan2IPv4StaticRouteIP1_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 8, 1),
    _VlansSMvlan2IPv4StaticRouteIP1_Type()
)
vlansSMvlan2IPv4StaticRouteIP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4StaticRouteIP1.setStatus("mandatory")
_VlansSMvlan2IPv4StaticRouteSM1_Type = IpAddress
_VlansSMvlan2IPv4StaticRouteSM1_Object = MibScalar
vlansSMvlan2IPv4StaticRouteSM1 = _VlansSMvlan2IPv4StaticRouteSM1_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 8, 2),
    _VlansSMvlan2IPv4StaticRouteSM1_Type()
)
vlansSMvlan2IPv4StaticRouteSM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4StaticRouteSM1.setStatus("mandatory")
_VlansSMvlan2IPv4StaticRouteIP2_Type = IpAddress
_VlansSMvlan2IPv4StaticRouteIP2_Object = MibScalar
vlansSMvlan2IPv4StaticRouteIP2 = _VlansSMvlan2IPv4StaticRouteIP2_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 8, 3),
    _VlansSMvlan2IPv4StaticRouteIP2_Type()
)
vlansSMvlan2IPv4StaticRouteIP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4StaticRouteIP2.setStatus("mandatory")
_VlansSMvlan2IPv4StaticRouteSM2_Type = IpAddress
_VlansSMvlan2IPv4StaticRouteSM2_Object = MibScalar
vlansSMvlan2IPv4StaticRouteSM2 = _VlansSMvlan2IPv4StaticRouteSM2_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 8, 4),
    _VlansSMvlan2IPv4StaticRouteSM2_Type()
)
vlansSMvlan2IPv4StaticRouteSM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4StaticRouteSM2.setStatus("mandatory")
_VlansSMvlan2IPv4StaticRouteIP3_Type = IpAddress
_VlansSMvlan2IPv4StaticRouteIP3_Object = MibScalar
vlansSMvlan2IPv4StaticRouteIP3 = _VlansSMvlan2IPv4StaticRouteIP3_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 8, 5),
    _VlansSMvlan2IPv4StaticRouteIP3_Type()
)
vlansSMvlan2IPv4StaticRouteIP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4StaticRouteIP3.setStatus("mandatory")
_VlansSMvlan2IPv4StaticRouteSM3_Type = IpAddress
_VlansSMvlan2IPv4StaticRouteSM3_Object = MibScalar
vlansSMvlan2IPv4StaticRouteSM3 = _VlansSMvlan2IPv4StaticRouteSM3_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 8, 6),
    _VlansSMvlan2IPv4StaticRouteSM3_Type()
)
vlansSMvlan2IPv4StaticRouteSM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv4StaticRouteSM3.setStatus("mandatory")
_VlansSMvlan2ipv6StatusRoutes_ObjectIdentity = ObjectIdentity
vlansSMvlan2ipv6StatusRoutes = _VlansSMvlan2ipv6StatusRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 9)
)
_VlansSMvlan2IPv6StaticRouteIP1_Type = InetAddressIPv6
_VlansSMvlan2IPv6StaticRouteIP1_Object = MibScalar
vlansSMvlan2IPv6StaticRouteIP1 = _VlansSMvlan2IPv6StaticRouteIP1_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 9, 1),
    _VlansSMvlan2IPv6StaticRouteIP1_Type()
)
vlansSMvlan2IPv6StaticRouteIP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6StaticRouteIP1.setStatus("mandatory")


class _VlansSMvlan2IPv6StaticRoutePL1_Type(Integer32):
    """Custom type vlansSMvlan2IPv6StaticRoutePL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VlansSMvlan2IPv6StaticRoutePL1_Type.__name__ = "Integer32"
_VlansSMvlan2IPv6StaticRoutePL1_Object = MibScalar
vlansSMvlan2IPv6StaticRoutePL1 = _VlansSMvlan2IPv6StaticRoutePL1_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 9, 2),
    _VlansSMvlan2IPv6StaticRoutePL1_Type()
)
vlansSMvlan2IPv6StaticRoutePL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6StaticRoutePL1.setStatus("mandatory")
_VlansSMvlan2IPv6StaticRouteIP2_Type = InetAddressIPv6
_VlansSMvlan2IPv6StaticRouteIP2_Object = MibScalar
vlansSMvlan2IPv6StaticRouteIP2 = _VlansSMvlan2IPv6StaticRouteIP2_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 9, 3),
    _VlansSMvlan2IPv6StaticRouteIP2_Type()
)
vlansSMvlan2IPv6StaticRouteIP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6StaticRouteIP2.setStatus("mandatory")


class _VlansSMvlan2IPv6StaticRoutePL2_Type(Integer32):
    """Custom type vlansSMvlan2IPv6StaticRoutePL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VlansSMvlan2IPv6StaticRoutePL2_Type.__name__ = "Integer32"
_VlansSMvlan2IPv6StaticRoutePL2_Object = MibScalar
vlansSMvlan2IPv6StaticRoutePL2 = _VlansSMvlan2IPv6StaticRoutePL2_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 9, 4),
    _VlansSMvlan2IPv6StaticRoutePL2_Type()
)
vlansSMvlan2IPv6StaticRoutePL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6StaticRoutePL2.setStatus("mandatory")
_VlansSMvlan2IPv6StaticRouteIP3_Type = InetAddressIPv6
_VlansSMvlan2IPv6StaticRouteIP3_Object = MibScalar
vlansSMvlan2IPv6StaticRouteIP3 = _VlansSMvlan2IPv6StaticRouteIP3_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 9, 5),
    _VlansSMvlan2IPv6StaticRouteIP3_Type()
)
vlansSMvlan2IPv6StaticRouteIP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6StaticRouteIP3.setStatus("mandatory")


class _VlansSMvlan2IPv6StaticRoutePL3_Type(Integer32):
    """Custom type vlansSMvlan2IPv6StaticRoutePL3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VlansSMvlan2IPv6StaticRoutePL3_Type.__name__ = "Integer32"
_VlansSMvlan2IPv6StaticRoutePL3_Object = MibScalar
vlansSMvlan2IPv6StaticRoutePL3 = _VlansSMvlan2IPv6StaticRoutePL3_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 2, 9, 6),
    _VlansSMvlan2IPv6StaticRoutePL3_Type()
)
vlansSMvlan2IPv6StaticRoutePL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlan2IPv6StaticRoutePL3.setStatus("mandatory")
_VlansSMvlanControl_ObjectIdentity = ObjectIdentity
vlansSMvlanControl = _VlansSMvlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 3)
)


class _VlansSMvlanConfigRevertTimout_Type(Integer32):
    """Custom type vlansSMvlanConfigRevertTimout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VlansSMvlanConfigRevertTimout_Type.__name__ = "Integer32"
_VlansSMvlanConfigRevertTimout_Object = MibScalar
vlansSMvlanConfigRevertTimout = _VlansSMvlanConfigRevertTimout_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 5, 3, 1),
    _VlansSMvlanConfigRevertTimout_Type()
)
vlansSMvlanConfigRevertTimout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlansSMvlanConfigRevertTimout.setStatus("mandatory")


class _DdnsStatus_Type(Integer32):
    """Custom type ddnsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DdnsStatus_Type.__name__ = "Integer32"
_DdnsStatus_Object = MibScalar
ddnsStatus = _DdnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 10),
    _DdnsStatus_Type()
)
ddnsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddnsStatus.setStatus("mandatory")


class _HostName_Type(OctetString):
    """Custom type hostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HostName_Type.__name__ = "OctetString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 11),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")


class _DdnsDomainToUse_Type(Integer32):
    """Custom type ddnsDomainToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("manual", 2))
    )


_DdnsDomainToUse_Type.__name__ = "Integer32"
_DdnsDomainToUse_Object = MibScalar
ddnsDomainToUse = _DdnsDomainToUse_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 12),
    _DdnsDomainToUse_Type()
)
ddnsDomainToUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddnsDomainToUse.setStatus("mandatory")
_DomainName_Type = OctetString
_DomainName_Object = MibScalar
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 13),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("mandatory")
_LanOverUSBInterface_ObjectIdentity = ObjectIdentity
lanOverUSBInterface = _LanOverUSBInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 14)
)
_XccUSBIPAddress_Type = IpAddress
_XccUSBIPAddress_Object = MibScalar
xccUSBIPAddress = _XccUSBIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 14, 1),
    _XccUSBIPAddress_Type()
)
xccUSBIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccUSBIPAddress.setStatus("mandatory")
_XccUSBSubnetMask_Type = IpAddress
_XccUSBSubnetMask_Object = MibScalar
xccUSBSubnetMask = _XccUSBSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 14, 2),
    _XccUSBSubnetMask_Type()
)
xccUSBSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccUSBSubnetMask.setStatus("mandatory")
_OsUSBIPAddress_Type = IpAddress
_OsUSBIPAddress_Object = MibScalar
osUSBIPAddress = _OsUSBIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 1, 14, 3),
    _OsUSBIPAddress_Type()
)
osUSBIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osUSBIPAddress.setStatus("mandatory")
_TcpProtocols_ObjectIdentity = ObjectIdentity
tcpProtocols = _TcpProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2)
)
_SnmpAgentConfig_ObjectIdentity = ObjectIdentity
snmpAgentConfig = _SnmpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1)
)


class _SnmpSystemName_Type(OctetString):
    """Custom type snmpSystemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemName_Type.__name__ = "OctetString"
_SnmpSystemName_Object = MibScalar
snmpSystemName = _SnmpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 1),
    _SnmpSystemName_Type()
)
snmpSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSystemName.setStatus("mandatory")


class _SnmpSystemContact_Type(OctetString):
    """Custom type snmpSystemContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemContact_Type.__name__ = "OctetString"
_SnmpSystemContact_Object = MibScalar
snmpSystemContact = _SnmpSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 2),
    _SnmpSystemContact_Type()
)
snmpSystemContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSystemContact.setStatus("mandatory")


class _SnmpSystemLocation_Type(OctetString):
    """Custom type snmpSystemLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemLocation_Type.__name__ = "OctetString"
_SnmpSystemLocation_Object = MibScalar
snmpSystemLocation = _SnmpSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 3),
    _SnmpSystemLocation_Type()
)
snmpSystemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSystemLocation.setStatus("mandatory")


class _SnmpSystemAgentTrapsDisable_Type(Integer32):
    """Custom type snmpSystemAgentTrapsDisable based on Integer32"""
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
        *(("trapsDisabled", 0),
          ("trapsV1Enabled", 1),
          ("trapsV3Enabled", 2),
          ("trapsV1V3Enabled", 3))
    )


_SnmpSystemAgentTrapsDisable_Type.__name__ = "Integer32"
_SnmpSystemAgentTrapsDisable_Object = MibScalar
snmpSystemAgentTrapsDisable = _SnmpSystemAgentTrapsDisable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 4),
    _SnmpSystemAgentTrapsDisable_Type()
)
snmpSystemAgentTrapsDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSystemAgentTrapsDisable.setStatus("mandatory")
_SnmpAgentCommunityConfig_ObjectIdentity = ObjectIdentity
snmpAgentCommunityConfig = _SnmpAgentCommunityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 5)
)


class _SnmpCommunityEntryCommunityName_Type(DisplayString):
    """Custom type snmpCommunityEntryCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SnmpCommunityEntryCommunityName_Type.__name__ = "DisplayString"
_SnmpCommunityEntryCommunityName_Object = MibScalar
snmpCommunityEntryCommunityName = _SnmpCommunityEntryCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 5, 1),
    _SnmpCommunityEntryCommunityName_Type()
)
snmpCommunityEntryCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityName.setStatus("mandatory")


class _SnmpCommunityEntryCommunityIpAddress_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpCommunityEntryCommunityIpAddress_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityIpAddress_Object = MibScalar
snmpCommunityEntryCommunityIpAddress = _SnmpCommunityEntryCommunityIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 5, 2),
    _SnmpCommunityEntryCommunityIpAddress_Type()
)
snmpCommunityEntryCommunityIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityIpAddress.setStatus("mandatory")


class _Snmpv3SystemAgentEnable_Type(Integer32):
    """Custom type snmpv3SystemAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Snmpv3SystemAgentEnable_Type.__name__ = "Integer32"
_Snmpv3SystemAgentEnable_Object = MibScalar
snmpv3SystemAgentEnable = _Snmpv3SystemAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 7),
    _Snmpv3SystemAgentEnable_Type()
)
snmpv3SystemAgentEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3SystemAgentEnable.setStatus("mandatory")
_SnmpAgentUserProfileConfig_ObjectIdentity = ObjectIdentity
snmpAgentUserProfileConfig = _SnmpAgentUserProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8)
)
_SnmpUserProfileTable_Object = MibTable
snmpUserProfileTable = _SnmpUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    snmpUserProfileTable.setStatus("mandatory")
_SnmpUserProfileEntry_Object = MibTableRow
snmpUserProfileEntry = _SnmpUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8, 1, 1)
)
snmpUserProfileEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "snmpUserProfileEntryIndex"),
)
if mibBuilder.loadTexts:
    snmpUserProfileEntry.setStatus("mandatory")


class _SnmpUserProfileEntryIndex_Type(Integer32):
    """Custom type snmpUserProfileEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpUserProfileEntryIndex_Type.__name__ = "Integer32"
_SnmpUserProfileEntryIndex_Object = MibTableColumn
snmpUserProfileEntryIndex = _SnmpUserProfileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8, 1, 1, 1),
    _SnmpUserProfileEntryIndex_Type()
)
snmpUserProfileEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserProfileEntryIndex.setStatus("mandatory")


class _SnmpUserProfileEntryAuthProt_Type(Integer32):
    """Custom type snmpUserProfileEntryAuthProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sha", 3))
    )


_SnmpUserProfileEntryAuthProt_Type.__name__ = "Integer32"
_SnmpUserProfileEntryAuthProt_Object = MibTableColumn
snmpUserProfileEntryAuthProt = _SnmpUserProfileEntryAuthProt_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8, 1, 1, 2),
    _SnmpUserProfileEntryAuthProt_Type()
)
snmpUserProfileEntryAuthProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserProfileEntryAuthProt.setStatus("mandatory")


class _SnmpUserProfileEntryPrivProt_Type(Integer32):
    """Custom type snmpUserProfileEntryPrivProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("des", 2),
          ("aes", 4))
    )


_SnmpUserProfileEntryPrivProt_Type.__name__ = "Integer32"
_SnmpUserProfileEntryPrivProt_Object = MibTableColumn
snmpUserProfileEntryPrivProt = _SnmpUserProfileEntryPrivProt_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8, 1, 1, 3),
    _SnmpUserProfileEntryPrivProt_Type()
)
snmpUserProfileEntryPrivProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserProfileEntryPrivProt.setStatus("mandatory")


class _SnmpUserProfileEntryViewType_Type(Integer32):
    """Custom type snmpUserProfileEntryViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("get", 1)
    )


_SnmpUserProfileEntryViewType_Type.__name__ = "Integer32"
_SnmpUserProfileEntryViewType_Object = MibTableColumn
snmpUserProfileEntryViewType = _SnmpUserProfileEntryViewType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8, 1, 1, 5),
    _SnmpUserProfileEntryViewType_Type()
)
snmpUserProfileEntryViewType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserProfileEntryViewType.setStatus("mandatory")


class _SnmpUserProfileEntryIpAddress_Type(OctetString):
    """Custom type snmpUserProfileEntryIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpUserProfileEntryIpAddress_Type.__name__ = "OctetString"
_SnmpUserProfileEntryIpAddress_Object = MibTableColumn
snmpUserProfileEntryIpAddress = _SnmpUserProfileEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 1, 8, 1, 1, 6),
    _SnmpUserProfileEntryIpAddress_Type()
)
snmpUserProfileEntryIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserProfileEntryIpAddress.setStatus("mandatory")
_DnsConfig_ObjectIdentity = ObjectIdentity
dnsConfig = _DnsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2)
)


class _DnsEnabled_Type(Integer32):
    """Custom type dnsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dnsDisabled", 0),
          ("dnsEnabled", 1))
    )


_DnsEnabled_Type.__name__ = "Integer32"
_DnsEnabled_Object = MibScalar
dnsEnabled = _DnsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 1),
    _DnsEnabled_Type()
)
dnsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsEnabled.setStatus("mandatory")
_DnsServerIPAddress1_Type = IpAddress
_DnsServerIPAddress1_Object = MibScalar
dnsServerIPAddress1 = _DnsServerIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 2),
    _DnsServerIPAddress1_Type()
)
dnsServerIPAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIPAddress1.setStatus("mandatory")
_DnsServerIPAddress2_Type = IpAddress
_DnsServerIPAddress2_Object = MibScalar
dnsServerIPAddress2 = _DnsServerIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 3),
    _DnsServerIPAddress2_Type()
)
dnsServerIPAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIPAddress2.setStatus("mandatory")
_DnsServerIPAddress3_Type = IpAddress
_DnsServerIPAddress3_Object = MibScalar
dnsServerIPAddress3 = _DnsServerIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 4),
    _DnsServerIPAddress3_Type()
)
dnsServerIPAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIPAddress3.setStatus("mandatory")
_DnsServerIPv6Address1_Type = InetAddressIPv6
_DnsServerIPv6Address1_Object = MibScalar
dnsServerIPv6Address1 = _DnsServerIPv6Address1_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 12),
    _DnsServerIPv6Address1_Type()
)
dnsServerIPv6Address1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIPv6Address1.setStatus("mandatory")
_DnsServerIPv6Address2_Type = InetAddressIPv6
_DnsServerIPv6Address2_Object = MibScalar
dnsServerIPv6Address2 = _DnsServerIPv6Address2_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 13),
    _DnsServerIPv6Address2_Type()
)
dnsServerIPv6Address2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIPv6Address2.setStatus("mandatory")
_DnsServerIPv6Address3_Type = InetAddressIPv6
_DnsServerIPv6Address3_Object = MibScalar
dnsServerIPv6Address3 = _DnsServerIPv6Address3_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 14),
    _DnsServerIPv6Address3_Type()
)
dnsServerIPv6Address3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerIPv6Address3.setStatus("mandatory")


class _DnsPriority_Type(Integer32):
    """Custom type dnsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv6", 1),
          ("ipv4", 2))
    )


_DnsPriority_Type.__name__ = "Integer32"
_DnsPriority_Object = MibScalar
dnsPriority = _DnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 20),
    _DnsPriority_Type()
)
dnsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsPriority.setStatus("mandatory")


class _DnsLXCADiscovery_Type(Integer32):
    """Custom type dnsLXCADiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dnsLXCADiscoveryDisabled", 0),
          ("dnsLXCADiscoveryEnabled", 1))
    )


_DnsLXCADiscovery_Type.__name__ = "Integer32"
_DnsLXCADiscovery_Object = MibScalar
dnsLXCADiscovery = _DnsLXCADiscovery_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 2, 21),
    _DnsLXCADiscovery_Type()
)
dnsLXCADiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsLXCADiscovery.setStatus("mandatory")
_SmtpConfig_ObjectIdentity = ObjectIdentity
smtpConfig = _SmtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 3)
)


class _SmtpServerNameOrIPAddress_Type(OctetString):
    """Custom type smtpServerNameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SmtpServerNameOrIPAddress_Type.__name__ = "OctetString"
_SmtpServerNameOrIPAddress_Object = MibScalar
smtpServerNameOrIPAddress = _SmtpServerNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 3, 1),
    _SmtpServerNameOrIPAddress_Type()
)
smtpServerNameOrIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerNameOrIPAddress.setStatus("mandatory")
_SmtpServerPort_Type = Integer32
_SmtpServerPort_Object = MibScalar
smtpServerPort = _SmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 3, 2),
    _SmtpServerPort_Type()
)
smtpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerPort.setStatus("mandatory")


class _SmtpServerAuthentication_Type(Integer32):
    """Custom type smtpServerAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("disabled", 1))
    )


_SmtpServerAuthentication_Type.__name__ = "Integer32"
_SmtpServerAuthentication_Object = MibScalar
smtpServerAuthentication = _SmtpServerAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 3, 3),
    _SmtpServerAuthentication_Type()
)
smtpServerAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerAuthentication.setStatus("mandatory")


class _SmtpServerAuthenticationUser_Type(OctetString):
    """Custom type smtpServerAuthenticationUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmtpServerAuthenticationUser_Type.__name__ = "OctetString"
_SmtpServerAuthenticationUser_Object = MibScalar
smtpServerAuthenticationUser = _SmtpServerAuthenticationUser_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 3, 4),
    _SmtpServerAuthenticationUser_Type()
)
smtpServerAuthenticationUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerAuthenticationUser.setStatus("mandatory")


class _SmtpServerAuthenticationMethod_Type(Integer32):
    """Custom type smtpServerAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("plain", 0),
          ("cram-md5", 1))
    )


_SmtpServerAuthenticationMethod_Type.__name__ = "Integer32"
_SmtpServerAuthenticationMethod_Object = MibScalar
smtpServerAuthenticationMethod = _SmtpServerAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 3, 6),
    _SmtpServerAuthenticationMethod_Type()
)
smtpServerAuthenticationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerAuthenticationMethod.setStatus("mandatory")


class _SmtpServerReversePath_Type(OctetString):
    """Custom type smtpServerReversePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmtpServerReversePath_Type.__name__ = "OctetString"
_SmtpServerReversePath_Object = MibScalar
smtpServerReversePath = _SmtpServerReversePath_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 3, 7),
    _SmtpServerReversePath_Type()
)
smtpServerReversePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerReversePath.setStatus("mandatory")
_TcpApplicationConfig_ObjectIdentity = ObjectIdentity
tcpApplicationConfig = _TcpApplicationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4)
)


class _SlpAddrType_Type(Integer32):
    """Custom type slpAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 0),
          ("broadcast", 1))
    )


_SlpAddrType_Type.__name__ = "Integer32"
_SlpAddrType_Object = MibScalar
slpAddrType = _SlpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 2),
    _SlpAddrType_Type()
)
slpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpAddrType.setStatus("mandatory")
_SlpMulticastAddr_Type = IpAddress
_SlpMulticastAddr_Object = MibScalar
slpMulticastAddr = _SlpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 3),
    _SlpMulticastAddr_Type()
)
slpMulticastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpMulticastAddr.setStatus("mandatory")
_SshServerConfig_ObjectIdentity = ObjectIdentity
sshServerConfig = _SshServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 5)
)


class _SshServerHostKeySize_Type(Integer32):
    """Custom type sshServerHostKeySize based on Integer32"""
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
        *(("bits512", 1),
          ("bits768", 2),
          ("bits1024", 3),
          ("bits2048", 4),
          ("bits4096", 5))
    )


_SshServerHostKeySize_Type.__name__ = "Integer32"
_SshServerHostKeySize_Object = MibScalar
sshServerHostKeySize = _SshServerHostKeySize_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 5, 1),
    _SshServerHostKeySize_Type()
)
sshServerHostKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerHostKeySize.setStatus("mandatory")
_SshServerHostKeyFingerprint_Type = OctetString
_SshServerHostKeyFingerprint_Object = MibScalar
sshServerHostKeyFingerprint = _SshServerHostKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 5, 2),
    _SshServerHostKeyFingerprint_Type()
)
sshServerHostKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerHostKeyFingerprint.setStatus("mandatory")


class _SshEnable_Type(Integer32):
    """Custom type sshEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SshEnable_Type.__name__ = "Integer32"
_SshEnable_Object = MibScalar
sshEnable = _SshEnable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 5, 5),
    _SshEnable_Type()
)
sshEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshEnable.setStatus("mandatory")
_SslConfig_ObjectIdentity = ObjectIdentity
sslConfig = _SslConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6)
)


class _SslEnableHTTPSforWeb_Type(Integer32):
    """Custom type sslEnableHTTPSforWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SslEnableHTTPSforWeb_Type.__name__ = "Integer32"
_SslEnableHTTPSforWeb_Object = MibScalar
sslEnableHTTPSforWeb = _SslEnableHTTPSforWeb_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 1),
    _SslEnableHTTPSforWeb_Type()
)
sslEnableHTTPSforWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslEnableHTTPSforWeb.setStatus("mandatory")


class _SslEnableHTTPSforCIMXML_Type(Integer32):
    """Custom type sslEnableHTTPSforCIMXML based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SslEnableHTTPSforCIMXML_Type.__name__ = "Integer32"
_SslEnableHTTPSforCIMXML_Object = MibScalar
sslEnableHTTPSforCIMXML = _SslEnableHTTPSforCIMXML_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 2),
    _SslEnableHTTPSforCIMXML_Type()
)
sslEnableHTTPSforCIMXML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslEnableHTTPSforCIMXML.setStatus("mandatory")


class _SslEnableSecureClientLDAP_Type(Integer32):
    """Custom type sslEnableSecureClientLDAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SslEnableSecureClientLDAP_Type.__name__ = "Integer32"
_SslEnableSecureClientLDAP_Object = MibScalar
sslEnableSecureClientLDAP = _SslEnableSecureClientLDAP_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 3),
    _SslEnableSecureClientLDAP_Type()
)
sslEnableSecureClientLDAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslEnableSecureClientLDAP.setStatus("mandatory")
_SslServerCertificate_ObjectIdentity = ObjectIdentity
sslServerCertificate = _SslServerCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 4)
)


class _SslServerCertificateStatus_Type(Integer32):
    """Custom type sslServerCertificateStatus based on Integer32"""
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
        *(("no-cert-installed", 1),
          ("self-signed-installed", 2),
          ("ca-signed-installed", 3),
          ("csr-generated", 4),
          ("self-signed-and-csr-generated", 5),
          ("ca-signed-and-csr-generated", 6))
    )


_SslServerCertificateStatus_Type.__name__ = "Integer32"
_SslServerCertificateStatus_Object = MibScalar
sslServerCertificateStatus = _SslServerCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 4, 1),
    _SslServerCertificateStatus_Type()
)
sslServerCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslServerCertificateStatus.setStatus("mandatory")


class _SslServerCertificateExpirationDate_Type(OctetString):
    """Custom type sslServerCertificateExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SslServerCertificateExpirationDate_Type.__name__ = "OctetString"
_SslServerCertificateExpirationDate_Object = MibScalar
sslServerCertificateExpirationDate = _SslServerCertificateExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 4, 2),
    _SslServerCertificateExpirationDate_Type()
)
sslServerCertificateExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslServerCertificateExpirationDate.setStatus("mandatory")
_SslLDAPTrustedCertificate_ObjectIdentity = ObjectIdentity
sslLDAPTrustedCertificate = _SslLDAPTrustedCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5)
)


class _SslLDAPTrustedCertificate1Status_Type(Integer32):
    """Custom type sslLDAPTrustedCertificate1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-installed", 0),
          ("installed", 1))
    )


_SslLDAPTrustedCertificate1Status_Type.__name__ = "Integer32"
_SslLDAPTrustedCertificate1Status_Object = MibScalar
sslLDAPTrustedCertificate1Status = _SslLDAPTrustedCertificate1Status_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 1),
    _SslLDAPTrustedCertificate1Status_Type()
)
sslLDAPTrustedCertificate1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate1Status.setStatus("mandatory")


class _SslLDAPTrustedCertificate1ExpirationDate_Type(OctetString):
    """Custom type sslLDAPTrustedCertificate1ExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SslLDAPTrustedCertificate1ExpirationDate_Type.__name__ = "OctetString"
_SslLDAPTrustedCertificate1ExpirationDate_Object = MibScalar
sslLDAPTrustedCertificate1ExpirationDate = _SslLDAPTrustedCertificate1ExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 2),
    _SslLDAPTrustedCertificate1ExpirationDate_Type()
)
sslLDAPTrustedCertificate1ExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate1ExpirationDate.setStatus("mandatory")


class _SslLDAPTrustedCertificate2Status_Type(Integer32):
    """Custom type sslLDAPTrustedCertificate2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-installed", 0),
          ("installed", 1))
    )


_SslLDAPTrustedCertificate2Status_Type.__name__ = "Integer32"
_SslLDAPTrustedCertificate2Status_Object = MibScalar
sslLDAPTrustedCertificate2Status = _SslLDAPTrustedCertificate2Status_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 3),
    _SslLDAPTrustedCertificate2Status_Type()
)
sslLDAPTrustedCertificate2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate2Status.setStatus("mandatory")


class _SslLDAPTrustedCertificate2ExpirationDate_Type(OctetString):
    """Custom type sslLDAPTrustedCertificate2ExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SslLDAPTrustedCertificate2ExpirationDate_Type.__name__ = "OctetString"
_SslLDAPTrustedCertificate2ExpirationDate_Object = MibScalar
sslLDAPTrustedCertificate2ExpirationDate = _SslLDAPTrustedCertificate2ExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 4),
    _SslLDAPTrustedCertificate2ExpirationDate_Type()
)
sslLDAPTrustedCertificate2ExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate2ExpirationDate.setStatus("mandatory")


class _SslLDAPTrustedCertificate3Status_Type(Integer32):
    """Custom type sslLDAPTrustedCertificate3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-installed", 0),
          ("installed", 1))
    )


_SslLDAPTrustedCertificate3Status_Type.__name__ = "Integer32"
_SslLDAPTrustedCertificate3Status_Object = MibScalar
sslLDAPTrustedCertificate3Status = _SslLDAPTrustedCertificate3Status_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 5),
    _SslLDAPTrustedCertificate3Status_Type()
)
sslLDAPTrustedCertificate3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate3Status.setStatus("mandatory")


class _SslLDAPTrustedCertificate3ExpirationDate_Type(OctetString):
    """Custom type sslLDAPTrustedCertificate3ExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SslLDAPTrustedCertificate3ExpirationDate_Type.__name__ = "OctetString"
_SslLDAPTrustedCertificate3ExpirationDate_Object = MibScalar
sslLDAPTrustedCertificate3ExpirationDate = _SslLDAPTrustedCertificate3ExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 6),
    _SslLDAPTrustedCertificate3ExpirationDate_Type()
)
sslLDAPTrustedCertificate3ExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate3ExpirationDate.setStatus("mandatory")


class _SslLDAPTrustedCertificate4Status_Type(Integer32):
    """Custom type sslLDAPTrustedCertificate4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-installed", 0),
          ("installed", 1))
    )


_SslLDAPTrustedCertificate4Status_Type.__name__ = "Integer32"
_SslLDAPTrustedCertificate4Status_Object = MibScalar
sslLDAPTrustedCertificate4Status = _SslLDAPTrustedCertificate4Status_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 7),
    _SslLDAPTrustedCertificate4Status_Type()
)
sslLDAPTrustedCertificate4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate4Status.setStatus("mandatory")


class _SslLDAPTrustedCertificate4ExpirationDate_Type(OctetString):
    """Custom type sslLDAPTrustedCertificate4ExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SslLDAPTrustedCertificate4ExpirationDate_Type.__name__ = "OctetString"
_SslLDAPTrustedCertificate4ExpirationDate_Object = MibScalar
sslLDAPTrustedCertificate4ExpirationDate = _SslLDAPTrustedCertificate4ExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 6, 5, 8),
    _SslLDAPTrustedCertificate4ExpirationDate_Type()
)
sslLDAPTrustedCertificate4ExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslLDAPTrustedCertificate4ExpirationDate.setStatus("mandatory")
_CertDomainNames_ObjectIdentity = ObjectIdentity
certDomainNames = _CertDomainNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 8)
)
_CertDomainNameTable_Object = MibTable
certDomainNameTable = _CertDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 8, 1)
)
if mibBuilder.loadTexts:
    certDomainNameTable.setStatus("mandatory")
_CertDomainNameEntry_Object = MibTableRow
certDomainNameEntry = _CertDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 8, 1, 1)
)
certDomainNameEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "certDomainNameIndex"),
)
if mibBuilder.loadTexts:
    certDomainNameEntry.setStatus("mandatory")


class _CertDomainNameIndex_Type(Integer32):
    """Custom type certDomainNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CertDomainNameIndex_Type.__name__ = "Integer32"
_CertDomainNameIndex_Object = MibTableColumn
certDomainNameIndex = _CertDomainNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 8, 1, 1, 1),
    _CertDomainNameIndex_Type()
)
certDomainNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certDomainNameIndex.setStatus("mandatory")
_CertDomainName_Type = OctetString
_CertDomainName_Object = MibTableColumn
certDomainName = _CertDomainName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 8, 1, 1, 2),
    _CertDomainName_Type()
)
certDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certDomainName.setStatus("mandatory")
_CertDomainNameStatus_Type = OctetString
_CertDomainNameStatus_Object = MibTableColumn
certDomainNameStatus = _CertDomainNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 8, 1, 1, 3),
    _CertDomainNameStatus_Type()
)
certDomainNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certDomainNameStatus.setStatus("mandatory")
_SkrServers_ObjectIdentity = ObjectIdentity
skrServers = _SkrServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9)
)
_SkrServerTable_Object = MibTable
skrServerTable = _SkrServerTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 1)
)
if mibBuilder.loadTexts:
    skrServerTable.setStatus("mandatory")
_SkrServerEntry_Object = MibTableRow
skrServerEntry = _SkrServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 1, 1)
)
skrServerEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "skrServerIndex"),
)
if mibBuilder.loadTexts:
    skrServerEntry.setStatus("mandatory")


class _SkrServerIndex_Type(Integer32):
    """Custom type skrServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SkrServerIndex_Type.__name__ = "Integer32"
_SkrServerIndex_Object = MibTableColumn
skrServerIndex = _SkrServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 1, 1, 1),
    _SkrServerIndex_Type()
)
skrServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrServerIndex.setStatus("mandatory")


class _SkrServerHostname_Type(OctetString):
    """Custom type skrServerHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SkrServerHostname_Type.__name__ = "OctetString"
_SkrServerHostname_Object = MibTableColumn
skrServerHostname = _SkrServerHostname_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 1, 1, 2),
    _SkrServerHostname_Type()
)
skrServerHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrServerHostname.setStatus("mandatory")
_SkrServerPort_Type = Integer32
_SkrServerPort_Object = MibTableColumn
skrServerPort = _SkrServerPort_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 1, 1, 3),
    _SkrServerPort_Type()
)
skrServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrServerPort.setStatus("mandatory")


class _SkrDeviceGroup_Type(OctetString):
    """Custom type skrDeviceGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SkrDeviceGroup_Type.__name__ = "OctetString"
_SkrDeviceGroup_Object = MibScalar
skrDeviceGroup = _SkrDeviceGroup_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 3),
    _SkrDeviceGroup_Type()
)
skrDeviceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrDeviceGroup.setStatus("mandatory")
_SkrClientConfigCertficate_ObjectIdentity = ObjectIdentity
skrClientConfigCertficate = _SkrClientConfigCertficate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 4)
)


class _SkrClientCertificateStatus_Type(Integer32):
    """Custom type skrClientCertificateStatus based on Integer32"""
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
        *(("no-cert-installed", 1),
          ("self-signed-installed", 2),
          ("ca-signed-installed", 3),
          ("csr-generated", 4),
          ("self-signed-and-csr-generated", 5),
          ("ca-signed-and-csr-generated", 6))
    )


_SkrClientCertificateStatus_Type.__name__ = "Integer32"
_SkrClientCertificateStatus_Object = MibScalar
skrClientCertificateStatus = _SkrClientCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 4, 3),
    _SkrClientCertificateStatus_Type()
)
skrClientCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrClientCertificateStatus.setStatus("mandatory")


class _SkrClientCertificateExpirationDate_Type(OctetString):
    """Custom type skrClientCertificateExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SkrClientCertificateExpirationDate_Type.__name__ = "OctetString"
_SkrClientCertificateExpirationDate_Object = MibScalar
skrClientCertificateExpirationDate = _SkrClientCertificateExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 4, 4),
    _SkrClientCertificateExpirationDate_Type()
)
skrClientCertificateExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrClientCertificateExpirationDate.setStatus("mandatory")


class _SkrServerCertificateExpirationDate_Type(OctetString):
    """Custom type skrServerCertificateExpirationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SkrServerCertificateExpirationDate_Type.__name__ = "OctetString"
_SkrServerCertificateExpirationDate_Object = MibScalar
skrServerCertificateExpirationDate = _SkrServerCertificateExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 4, 9, 12),
    _SkrServerCertificateExpirationDate_Type()
)
skrServerCertificateExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrServerCertificateExpirationDate.setStatus("mandatory")
_TcpPortAssignmentCfg_ObjectIdentity = ObjectIdentity
tcpPortAssignmentCfg = _TcpPortAssignmentCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5)
)
_HttpPortAssignment_Type = Integer32
_HttpPortAssignment_Object = MibScalar
httpPortAssignment = _HttpPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5, 2),
    _HttpPortAssignment_Type()
)
httpPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpPortAssignment.setStatus("mandatory")
_HttpsPortAssignment_Type = Integer32
_HttpsPortAssignment_Object = MibScalar
httpsPortAssignment = _HttpsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5, 3),
    _HttpsPortAssignment_Type()
)
httpsPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpsPortAssignment.setStatus("mandatory")
_SshLegacyCLIPortAssignment_Type = Integer32
_SshLegacyCLIPortAssignment_Object = MibScalar
sshLegacyCLIPortAssignment = _SshLegacyCLIPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5, 6),
    _SshLegacyCLIPortAssignment_Type()
)
sshLegacyCLIPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshLegacyCLIPortAssignment.setStatus("mandatory")
_SnmpAgentPortAssignment_Type = Integer32
_SnmpAgentPortAssignment_Object = MibScalar
snmpAgentPortAssignment = _SnmpAgentPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5, 8),
    _SnmpAgentPortAssignment_Type()
)
snmpAgentPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentPortAssignment.setStatus("mandatory")
_SnmpTrapsPortAssignment_Type = Integer32
_SnmpTrapsPortAssignment_Object = MibScalar
snmpTrapsPortAssignment = _SnmpTrapsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5, 9),
    _SnmpTrapsPortAssignment_Type()
)
snmpTrapsPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapsPortAssignment.setStatus("mandatory")
_RemvidPortAssignment_Type = Integer32
_RemvidPortAssignment_Object = MibScalar
remvidPortAssignment = _RemvidPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5, 10),
    _RemvidPortAssignment_Type()
)
remvidPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remvidPortAssignment.setStatus("mandatory")
_CimOverHttpsPortAssignment_Type = Integer32
_CimOverHttpsPortAssignment_Object = MibScalar
cimOverHttpsPortAssignment = _CimOverHttpsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 5, 12),
    _CimOverHttpsPortAssignment_Type()
)
cimOverHttpsPortAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimOverHttpsPortAssignment.setStatus("mandatory")
_LdapClientCfg_ObjectIdentity = ObjectIdentity
ldapClientCfg = _LdapClientCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6)
)


class _LdapServer1NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer1NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer1NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer1NameOrIPAddress_Object = MibScalar
ldapServer1NameOrIPAddress = _LdapServer1NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 1),
    _LdapServer1NameOrIPAddress_Type()
)
ldapServer1NameOrIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer1NameOrIPAddress.setStatus("mandatory")
_LdapServer1PortNumber_Type = Integer32
_LdapServer1PortNumber_Object = MibScalar
ldapServer1PortNumber = _LdapServer1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 2),
    _LdapServer1PortNumber_Type()
)
ldapServer1PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer1PortNumber.setStatus("mandatory")


class _LdapServer2NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer2NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer2NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer2NameOrIPAddress_Object = MibScalar
ldapServer2NameOrIPAddress = _LdapServer2NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 3),
    _LdapServer2NameOrIPAddress_Type()
)
ldapServer2NameOrIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer2NameOrIPAddress.setStatus("mandatory")
_LdapServer2PortNumber_Type = Integer32
_LdapServer2PortNumber_Object = MibScalar
ldapServer2PortNumber = _LdapServer2PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 4),
    _LdapServer2PortNumber_Type()
)
ldapServer2PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer2PortNumber.setStatus("mandatory")


class _LdapServer3NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer3NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer3NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer3NameOrIPAddress_Object = MibScalar
ldapServer3NameOrIPAddress = _LdapServer3NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 5),
    _LdapServer3NameOrIPAddress_Type()
)
ldapServer3NameOrIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer3NameOrIPAddress.setStatus("mandatory")
_LdapServer3PortNumber_Type = Integer32
_LdapServer3PortNumber_Object = MibScalar
ldapServer3PortNumber = _LdapServer3PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 6),
    _LdapServer3PortNumber_Type()
)
ldapServer3PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer3PortNumber.setStatus("mandatory")


class _LdapServer4NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer4NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer4NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer4NameOrIPAddress_Object = MibScalar
ldapServer4NameOrIPAddress = _LdapServer4NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 7),
    _LdapServer4NameOrIPAddress_Type()
)
ldapServer4NameOrIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer4NameOrIPAddress.setStatus("mandatory")
_LdapServer4PortNumber_Type = Integer32
_LdapServer4PortNumber_Object = MibScalar
ldapServer4PortNumber = _LdapServer4PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 8),
    _LdapServer4PortNumber_Type()
)
ldapServer4PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServer4PortNumber.setStatus("mandatory")


class _LdapRootDN_Type(OctetString):
    """Custom type ldapRootDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 300),
    )


_LdapRootDN_Type.__name__ = "OctetString"
_LdapRootDN_Object = MibScalar
ldapRootDN = _LdapRootDN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 9),
    _LdapRootDN_Type()
)
ldapRootDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapRootDN.setStatus("mandatory")


class _LdapGroupFilter_Type(OctetString):
    """Custom type ldapGroupFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_LdapGroupFilter_Type.__name__ = "OctetString"
_LdapGroupFilter_Object = MibScalar
ldapGroupFilter = _LdapGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 11),
    _LdapGroupFilter_Type()
)
ldapGroupFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapGroupFilter.setStatus("mandatory")


class _LdapBindingMethod_Type(Integer32):
    """Custom type ldapBindingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anonymousAuthentication", 0),
          ("clientAuthentication", 1),
          ("userPrincipalName", 2))
    )


_LdapBindingMethod_Type.__name__ = "Integer32"
_LdapBindingMethod_Object = MibScalar
ldapBindingMethod = _LdapBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 12),
    _LdapBindingMethod_Type()
)
ldapBindingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapBindingMethod.setStatus("mandatory")


class _LdapClientAuthenticationDN_Type(OctetString):
    """Custom type ldapClientAuthenticationDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 300),
    )


_LdapClientAuthenticationDN_Type.__name__ = "OctetString"
_LdapClientAuthenticationDN_Object = MibScalar
ldapClientAuthenticationDN = _LdapClientAuthenticationDN_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 13),
    _LdapClientAuthenticationDN_Type()
)
ldapClientAuthenticationDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapClientAuthenticationDN.setStatus("mandatory")


class _LdapRoleBasedSecurityEnabled_Type(Integer32):
    """Custom type ldapRoleBasedSecurityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LdapRoleBasedSecurityEnabled_Type.__name__ = "Integer32"
_LdapRoleBasedSecurityEnabled_Object = MibScalar
ldapRoleBasedSecurityEnabled = _LdapRoleBasedSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 15),
    _LdapRoleBasedSecurityEnabled_Type()
)
ldapRoleBasedSecurityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapRoleBasedSecurityEnabled.setStatus("mandatory")


class _LdapServerTargetName_Type(OctetString):
    """Custom type ldapServerTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LdapServerTargetName_Type.__name__ = "OctetString"
_LdapServerTargetName_Object = MibScalar
ldapServerTargetName = _LdapServerTargetName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 16),
    _LdapServerTargetName_Type()
)
ldapServerTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServerTargetName.setStatus("mandatory")


class _LdapUIDsearchAttribute_Type(OctetString):
    """Custom type ldapUIDsearchAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapUIDsearchAttribute_Type.__name__ = "OctetString"
_LdapUIDsearchAttribute_Object = MibScalar
ldapUIDsearchAttribute = _LdapUIDsearchAttribute_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 17),
    _LdapUIDsearchAttribute_Type()
)
ldapUIDsearchAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapUIDsearchAttribute.setStatus("mandatory")


class _LdapGroupSearchAttribute_Type(OctetString):
    """Custom type ldapGroupSearchAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapGroupSearchAttribute_Type.__name__ = "OctetString"
_LdapGroupSearchAttribute_Object = MibScalar
ldapGroupSearchAttribute = _LdapGroupSearchAttribute_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 18),
    _LdapGroupSearchAttribute_Type()
)
ldapGroupSearchAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapGroupSearchAttribute.setStatus("mandatory")


class _LdapLoginPermissionAttribute_Type(OctetString):
    """Custom type ldapLoginPermissionAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapLoginPermissionAttribute_Type.__name__ = "OctetString"
_LdapLoginPermissionAttribute_Object = MibScalar
ldapLoginPermissionAttribute = _LdapLoginPermissionAttribute_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 19),
    _LdapLoginPermissionAttribute_Type()
)
ldapLoginPermissionAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapLoginPermissionAttribute.setStatus("mandatory")


class _LdapUseDNSOrPreConfiguredServers_Type(Integer32):
    """Custom type ldapUseDNSOrPreConfiguredServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("usePreConfiguredLDAPServers", 0),
          ("useDNSToFindLDAPServers", 1))
    )


_LdapUseDNSOrPreConfiguredServers_Type.__name__ = "Integer32"
_LdapUseDNSOrPreConfiguredServers_Object = MibScalar
ldapUseDNSOrPreConfiguredServers = _LdapUseDNSOrPreConfiguredServers_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 20),
    _LdapUseDNSOrPreConfiguredServers_Type()
)
ldapUseDNSOrPreConfiguredServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapUseDNSOrPreConfiguredServers.setStatus("mandatory")


class _LdapDomainSource_Type(Integer32):
    """Custom type ldapDomainSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extractSearchDomainFromLoginID", 0),
          ("useOnlyConfiguredSearchDomainBelow", 1),
          ("tryLoginFirstThenConfiguredValue", 2))
    )


_LdapDomainSource_Type.__name__ = "Integer32"
_LdapDomainSource_Object = MibScalar
ldapDomainSource = _LdapDomainSource_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 21),
    _LdapDomainSource_Type()
)
ldapDomainSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapDomainSource.setStatus("mandatory")


class _LdapForestName_Type(OctetString):
    """Custom type ldapForestName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapForestName_Type.__name__ = "OctetString"
_LdapForestName_Object = MibScalar
ldapForestName = _LdapForestName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 22),
    _LdapForestName_Type()
)
ldapForestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapForestName.setStatus("mandatory")


class _LdapAuthCfg_Type(Integer32):
    """Custom type ldapAuthCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authenticationAndAuthorization", 0),
          ("authenticationOnly", 1))
    )


_LdapAuthCfg_Type.__name__ = "Integer32"
_LdapAuthCfg_Object = MibScalar
ldapAuthCfg = _LdapAuthCfg_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 23),
    _LdapAuthCfg_Type()
)
ldapAuthCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapAuthCfg.setStatus("mandatory")


class _LdapSearchDomain_Type(OctetString):
    """Custom type ldapSearchDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapSearchDomain_Type.__name__ = "OctetString"
_LdapSearchDomain_Object = MibScalar
ldapSearchDomain = _LdapSearchDomain_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 24),
    _LdapSearchDomain_Type()
)
ldapSearchDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapSearchDomain.setStatus("mandatory")


class _LdapServiceName_Type(OctetString):
    """Custom type ldapServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LdapServiceName_Type.__name__ = "OctetString"
_LdapServiceName_Object = MibScalar
ldapServiceName = _LdapServiceName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 6, 25),
    _LdapServiceName_Type()
)
ldapServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldapServiceName.setStatus("mandatory")
_NtpConfig_ObjectIdentity = ObjectIdentity
ntpConfig = _NtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 8)
)


class _NtpEnable_Type(Integer32):
    """Custom type ntpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtpEnable_Type.__name__ = "Integer32"
_NtpEnable_Object = MibScalar
ntpEnable = _NtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 8, 1),
    _NtpEnable_Type()
)
ntpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEnable.setStatus("mandatory")


class _NtpIpAddressHostname1_Type(OctetString):
    """Custom type ntpIpAddressHostname1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname1_Type.__name__ = "OctetString"
_NtpIpAddressHostname1_Object = MibScalar
ntpIpAddressHostname1 = _NtpIpAddressHostname1_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 8, 2),
    _NtpIpAddressHostname1_Type()
)
ntpIpAddressHostname1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpIpAddressHostname1.setStatus("mandatory")
_NtpUpdateFrequency_Type = Integer32
_NtpUpdateFrequency_Object = MibScalar
ntpUpdateFrequency = _NtpUpdateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 8, 3),
    _NtpUpdateFrequency_Type()
)
ntpUpdateFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpUpdateFrequency.setStatus("mandatory")


class _NtpIpAddressHostname2_Type(OctetString):
    """Custom type ntpIpAddressHostname2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname2_Type.__name__ = "OctetString"
_NtpIpAddressHostname2_Object = MibScalar
ntpIpAddressHostname2 = _NtpIpAddressHostname2_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 8, 4),
    _NtpIpAddressHostname2_Type()
)
ntpIpAddressHostname2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpIpAddressHostname2.setStatus("mandatory")


class _NtpIpAddressHostname3_Type(OctetString):
    """Custom type ntpIpAddressHostname3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname3_Type.__name__ = "OctetString"
_NtpIpAddressHostname3_Object = MibScalar
ntpIpAddressHostname3 = _NtpIpAddressHostname3_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 8, 6),
    _NtpIpAddressHostname3_Type()
)
ntpIpAddressHostname3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpIpAddressHostname3.setStatus("mandatory")


class _NtpIpAddressHostname4_Type(OctetString):
    """Custom type ntpIpAddressHostname4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname4_Type.__name__ = "OctetString"
_NtpIpAddressHostname4_Object = MibScalar
ntpIpAddressHostname4 = _NtpIpAddressHostname4_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 8, 7),
    _NtpIpAddressHostname4_Type()
)
ntpIpAddressHostname4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpIpAddressHostname4.setStatus("mandatory")
_IpmiConfig_ObjectIdentity = ObjectIdentity
ipmiConfig = _IpmiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 10)
)


class _IpmiStatus_Type(Integer32):
    """Custom type ipmiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IpmiStatus_Type.__name__ = "Integer32"
_IpmiStatus_Object = MibScalar
ipmiStatus = _IpmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 10, 1),
    _IpmiStatus_Type()
)
ipmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiStatus.setStatus("mandatory")
_CimxmlConfig_ObjectIdentity = ObjectIdentity
cimxmlConfig = _CimxmlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 11)
)


class _CimxmlStatus_Type(Integer32):
    """Custom type cimxmlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CimxmlStatus_Type.__name__ = "Integer32"
_CimxmlStatus_Object = MibScalar
cimxmlStatus = _CimxmlStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 11, 1),
    _CimxmlStatus_Type()
)
cimxmlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cimxmlStatus.setStatus("mandatory")
_RestConfig_ObjectIdentity = ObjectIdentity
restConfig = _RestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 12)
)


class _RestStatus_Type(Integer32):
    """Custom type restStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RestStatus_Type.__name__ = "Integer32"
_RestStatus_Object = MibScalar
restStatus = _RestStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 4, 2, 12, 1),
    _RestStatus_Type()
)
restStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restStatus.setStatus("mandatory")


class _XccVersionCheck_Type(Integer32):
    """Custom type xccVersionCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("xccVersion", 1)
    )


_XccVersionCheck_Type.__name__ = "Integer32"
_XccVersionCheck_Object = MibScalar
xccVersionCheck = _XccVersionCheck_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 3, 7),
    _XccVersionCheck_Type()
)
xccVersionCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xccVersionCheck.setStatus("mandatory")
_GeneralSystemSettings_ObjectIdentity = ObjectIdentity
generalSystemSettings = _GeneralSystemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 4)
)
_ServerTimers_ObjectIdentity = ObjectIdentity
serverTimers = _ServerTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 4, 1)
)


class _OSHang_Type(Integer32):
    """Custom type oSHang based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              150,
              180,
              210,
              240,
              600)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("twoAndHalfMinutes", 150),
          ("threeMinutes", 180),
          ("threeAndHalfMinutes", 210),
          ("fourMinutes", 240),
          ("tenMinutes", 600))
    )


_OSHang_Type.__name__ = "Integer32"
_OSHang_Object = MibScalar
oSHang = _OSHang_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 4, 1, 1),
    _OSHang_Type()
)
oSHang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSHang.setStatus("mandatory")


class _OSLoader_Type(Integer32):
    """Custom type oSLoader based on Integer32"""
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
              15,
              20,
              30,
              40,
              60,
              120,
              240)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("oneHalfMinutes", 1),
          ("oneMinutes", 2),
          ("oneAndHalfMinutes", 3),
          ("twoMinutes", 4),
          ("twoAndHalfMinutes", 5),
          ("threeMinutes", 6),
          ("threeAndHalfMinutes", 7),
          ("fourMinutes", 8),
          ("fourAndHalfMinutes", 9),
          ("fiveMinutes", 10),
          ("sevenAndHalfMinutes", 15),
          ("tenMinutes", 20),
          ("fifteenMinutes", 30),
          ("twentyMinutes", 40),
          ("thirtyMinutes", 60),
          ("oneHour", 120),
          ("twoHours", 240))
    )


_OSLoader_Type.__name__ = "Integer32"
_OSLoader_Object = MibScalar
oSLoader = _OSLoader_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 4, 1, 2),
    _OSLoader_Type()
)
oSLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSLoader.setStatus("mandatory")


class _NetworkPXEboot_Type(Integer32):
    """Custom type networkPXEboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkPXEBootDisabled", 0),
          ("networkPXEBootEnabled", 1))
    )


_NetworkPXEboot_Type.__name__ = "Integer32"
_NetworkPXEboot_Object = MibScalar
networkPXEboot = _NetworkPXEboot_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 4, 2),
    _NetworkPXEboot_Type()
)
networkPXEboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkPXEboot.setStatus("mandatory")
_SystemPower_ObjectIdentity = ObjectIdentity
systemPower = _SystemPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5)
)
_PowerStatistics_ObjectIdentity = ObjectIdentity
powerStatistics = _PowerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 1)
)


class _CurrentSysPowerStatus_Type(Integer32):
    """Custom type currentSysPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("poweredOff", 0),
          ("sleepS3", 1),
          ("poweredOn", 255))
    )


_CurrentSysPowerStatus_Type.__name__ = "Integer32"
_CurrentSysPowerStatus_Object = MibScalar
currentSysPowerStatus = _CurrentSysPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 1, 1),
    _CurrentSysPowerStatus_Type()
)
currentSysPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSysPowerStatus.setStatus("mandatory")
_PowerOnHours_Type = Integer32
_PowerOnHours_Object = MibScalar
powerOnHours = _PowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 1, 2),
    _PowerOnHours_Type()
)
powerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnHours.setStatus("mandatory")
_RestartCount_Type = Integer32
_RestartCount_Object = MibScalar
restartCount = _RestartCount_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 1, 3),
    _RestartCount_Type()
)
restartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartCount.setStatus("mandatory")


class _SystemState_Type(Integer32):
    """Custom type systemState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("systemPowerOfforStateUnknown", 0),
          ("systemPowerOnorStartingUEFI", 1),
          ("systemInUEFI", 2),
          ("uEFIErrorDetected", 3),
          ("bootingOSorInUnsupportedOS", 4),
          ("oSBooted", 5),
          ("suspendToRAM", 6),
          ("systemInSetup", 7),
          ("systemInLXPMMaintenanceMode", 8),
          ("systemInMemoryTest", 9))
    )


_SystemState_Type.__name__ = "Integer32"
_SystemState_Object = MibScalar
systemState = _SystemState_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 1, 4),
    _SystemState_Type()
)
systemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemState.setStatus("mandatory")
_PowerSysConfig_ObjectIdentity = ObjectIdentity
powerSysConfig = _PowerSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 2)
)


class _PowerSysOffDelay_Type(Integer32):
    """Custom type powerSysOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              120,
              180,
              240,
              300,
              450,
              600,
              900,
              1200,
              1800,
              3600,
              7200)
        )
    )
    namedValues = NamedValues(
        *(("noDelay", 0),
          ("oneHalfMinute", 30),
          ("oneMinute", 60),
          ("twoMinutes", 120),
          ("threeMinutes", 180),
          ("fourMinutes", 240),
          ("fiveMinute", 300),
          ("sevenAndHalfMinutes", 450),
          ("tenMinutes", 600),
          ("fifteenMinutes", 900),
          ("twentyMinutes", 1200),
          ("thirtyMinutes", 1800),
          ("oneHour", 3600),
          ("twoHours", 7200))
    )


_PowerSysOffDelay_Type.__name__ = "Integer32"
_PowerSysOffDelay_Object = MibScalar
powerSysOffDelay = _PowerSysOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 2, 1),
    _PowerSysOffDelay_Type()
)
powerSysOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSysOffDelay.setStatus("mandatory")
_PowerSysOnClockSetting_Type = OctetString
_PowerSysOnClockSetting_Object = MibScalar
powerSysOnClockSetting = _PowerSysOnClockSetting_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 2, 2),
    _PowerSysOnClockSetting_Type()
)
powerSysOnClockSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSysOnClockSetting.setStatus("mandatory")
_PowerCyclingSchedule_ObjectIdentity = ObjectIdentity
powerCyclingSchedule = _PowerCyclingSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 5)
)
_SchedulePowerOffWithOsShutdown_Type = OctetString
_SchedulePowerOffWithOsShutdown_Object = MibScalar
schedulePowerOffWithOsShutdown = _SchedulePowerOffWithOsShutdown_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 5, 1),
    _SchedulePowerOffWithOsShutdown_Type()
)
schedulePowerOffWithOsShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulePowerOffWithOsShutdown.setStatus("mandatory")
_SchedulePowerOnSystem_Type = OctetString
_SchedulePowerOnSystem_Object = MibScalar
schedulePowerOnSystem = _SchedulePowerOnSystem_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 5, 5, 2),
    _SchedulePowerOnSystem_Type()
)
schedulePowerOnSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulePowerOnSystem.setStatus("mandatory")
_ServiceAdvisor_ObjectIdentity = ObjectIdentity
serviceAdvisor = _ServiceAdvisor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8)
)
_AutoCallHomeSetup_ObjectIdentity = ObjectIdentity
autoCallHomeSetup = _AutoCallHomeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 1)
)


class _AcceptLicenseAgreement_Type(Integer32):
    """Custom type acceptLicenseAgreement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AcceptLicenseAgreement_Type.__name__ = "Integer32"
_AcceptLicenseAgreement_Object = MibScalar
acceptLicenseAgreement = _AcceptLicenseAgreement_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 1, 1),
    _AcceptLicenseAgreement_Type()
)
acceptLicenseAgreement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acceptLicenseAgreement.setStatus("mandatory")


class _ServiceAdvisorEnable_Type(Integer32):
    """Custom type serviceAdvisorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ServiceAdvisorEnable_Type.__name__ = "Integer32"
_ServiceAdvisorEnable_Object = MibScalar
serviceAdvisorEnable = _ServiceAdvisorEnable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 1, 2),
    _ServiceAdvisorEnable_Type()
)
serviceAdvisorEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceAdvisorEnable.setStatus("mandatory")
_ServiceSupportCenter_ObjectIdentity = ObjectIdentity
serviceSupportCenter = _ServiceSupportCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 2)
)
_LenovoSupportCenter_Type = OctetString
_LenovoSupportCenter_Object = MibScalar
lenovoSupportCenter = _LenovoSupportCenter_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 2, 1),
    _LenovoSupportCenter_Type()
)
lenovoSupportCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lenovoSupportCenter.setStatus("mandatory")
_ContactInformation_ObjectIdentity = ObjectIdentity
contactInformation = _ContactInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3)
)
_CompanyName_Type = OctetString
_CompanyName_Object = MibScalar
companyName = _CompanyName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 1),
    _CompanyName_Type()
)
companyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    companyName.setStatus("mandatory")
_ContactName_Type = OctetString
_ContactName_Object = MibScalar
contactName = _ContactName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 2),
    _ContactName_Type()
)
contactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactName.setStatus("mandatory")
_PhoneNumber_Type = OctetString
_PhoneNumber_Object = MibScalar
phoneNumber = _PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 3),
    _PhoneNumber_Type()
)
phoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneNumber.setStatus("mandatory")
_EmailAddress_Type = OctetString
_EmailAddress_Object = MibScalar
emailAddress = _EmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 4),
    _EmailAddress_Type()
)
emailAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailAddress.setStatus("mandatory")
_Address_Type = OctetString
_Address_Object = MibScalar
address = _Address_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 5),
    _Address_Type()
)
address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    address.setStatus("mandatory")
_City_Type = OctetString
_City_Object = MibScalar
city = _City_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 6),
    _City_Type()
)
city.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    city.setStatus("mandatory")
_State_Type = OctetString
_State_Object = MibScalar
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 7),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("mandatory")
_PostalCode_Type = OctetString
_PostalCode_Object = MibScalar
postalCode = _PostalCode_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 8),
    _PostalCode_Type()
)
postalCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postalCode.setStatus("mandatory")
_PhoneExtension_Type = OctetString
_PhoneExtension_Object = MibScalar
phoneExtension = _PhoneExtension_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 9),
    _PhoneExtension_Type()
)
phoneExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneExtension.setStatus("mandatory")
_AltContactName_Type = OctetString
_AltContactName_Object = MibScalar
altContactName = _AltContactName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 10),
    _AltContactName_Type()
)
altContactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altContactName.setStatus("mandatory")
_AltPhoneNumber_Type = OctetString
_AltPhoneNumber_Object = MibScalar
altPhoneNumber = _AltPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 11),
    _AltPhoneNumber_Type()
)
altPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altPhoneNumber.setStatus("mandatory")
_AltPhoneExtension_Type = OctetString
_AltPhoneExtension_Object = MibScalar
altPhoneExtension = _AltPhoneExtension_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 12),
    _AltPhoneExtension_Type()
)
altPhoneExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altPhoneExtension.setStatus("mandatory")
_AltEmailAddress_Type = OctetString
_AltEmailAddress_Object = MibScalar
altEmailAddress = _AltEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 13),
    _AltEmailAddress_Type()
)
altEmailAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altEmailAddress.setStatus("mandatory")
_MachineLocationPhoneNumber_Type = OctetString
_MachineLocationPhoneNumber_Object = MibScalar
machineLocationPhoneNumber = _MachineLocationPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 3, 14),
    _MachineLocationPhoneNumber_Type()
)
machineLocationPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLocationPhoneNumber.setStatus("mandatory")
_HttpProxyConfig_ObjectIdentity = ObjectIdentity
httpProxyConfig = _HttpProxyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 4)
)


class _HttpProxyEnable_Type(Integer32):
    """Custom type httpProxyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HttpProxyEnable_Type.__name__ = "Integer32"
_HttpProxyEnable_Object = MibScalar
httpProxyEnable = _HttpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 4, 1),
    _HttpProxyEnable_Type()
)
httpProxyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyEnable.setStatus("mandatory")
_HttpProxyLocation_Type = OctetString
_HttpProxyLocation_Object = MibScalar
httpProxyLocation = _HttpProxyLocation_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 4, 2),
    _HttpProxyLocation_Type()
)
httpProxyLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyLocation.setStatus("mandatory")
_HttpProxyPort_Type = Integer32
_HttpProxyPort_Object = MibScalar
httpProxyPort = _HttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 4, 3),
    _HttpProxyPort_Type()
)
httpProxyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyPort.setStatus("mandatory")
_HttpProxyUserName_Type = OctetString
_HttpProxyUserName_Object = MibScalar
httpProxyUserName = _HttpProxyUserName_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 4, 4),
    _HttpProxyUserName_Type()
)
httpProxyUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyUserName.setStatus("mandatory")
_HttpProxyPassword_Type = OctetString
_HttpProxyPassword_Object = MibScalar
httpProxyPassword = _HttpProxyPassword_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 4, 5),
    _HttpProxyPassword_Type()
)
httpProxyPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpProxyPassword.setStatus("mandatory")
_ActivityLogs_ObjectIdentity = ObjectIdentity
activityLogs = _ActivityLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 5)
)
_ActivityLogTable_Object = MibTable
activityLogTable = _ActivityLogTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 5, 1)
)
if mibBuilder.loadTexts:
    activityLogTable.setStatus("mandatory")
_ActivityLogEntry_Object = MibTableRow
activityLogEntry = _ActivityLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 5, 1, 1)
)
activityLogEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "activityLogIndex"),
)
if mibBuilder.loadTexts:
    activityLogEntry.setStatus("mandatory")


class _ActivityLogIndex_Type(Integer32):
    """Custom type activityLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_ActivityLogIndex_Type.__name__ = "Integer32"
_ActivityLogIndex_Object = MibTableColumn
activityLogIndex = _ActivityLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 5, 1, 1, 1),
    _ActivityLogIndex_Type()
)
activityLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activityLogIndex.setStatus("mandatory")
_ActivityLogString_Type = OctetString
_ActivityLogString_Object = MibTableColumn
activityLogString = _ActivityLogString_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 5, 1, 1, 2),
    _ActivityLogString_Type()
)
activityLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activityLogString.setStatus("mandatory")


class _ActivityLogAcknowledge_Type(Integer32):
    """Custom type activityLogAcknowledge based on Integer32"""
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


_ActivityLogAcknowledge_Type.__name__ = "Integer32"
_ActivityLogAcknowledge_Object = MibTableColumn
activityLogAcknowledge = _ActivityLogAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 5, 1, 1, 3),
    _ActivityLogAcknowledge_Type()
)
activityLogAcknowledge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activityLogAcknowledge.setStatus("mandatory")
_ActivityLogAttribute_Type = OctetString
_ActivityLogAttribute_Object = MibTableColumn
activityLogAttribute = _ActivityLogAttribute_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 5, 1, 1, 4),
    _ActivityLogAttribute_Type()
)
activityLogAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activityLogAttribute.setStatus("mandatory")
_AutoFTPSetup_ObjectIdentity = ObjectIdentity
autoFTPSetup = _AutoFTPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 6)
)


class _AutoFTPCallMode_Type(Integer32):
    """Custom type autoFTPCallMode based on Integer32"""
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
        *(("disabled", 0),
          ("ftp", 1),
          ("tftp", 2),
          ("sftp", 3))
    )


_AutoFTPCallMode_Type.__name__ = "Integer32"
_AutoFTPCallMode_Object = MibScalar
autoFTPCallMode = _AutoFTPCallMode_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 6, 1),
    _AutoFTPCallMode_Type()
)
autoFTPCallMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFTPCallMode.setStatus("mandatory")


class _AutoFTPCallAddr_Type(OctetString):
    """Custom type autoFTPCallAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AutoFTPCallAddr_Type.__name__ = "OctetString"
_AutoFTPCallAddr_Object = MibScalar
autoFTPCallAddr = _AutoFTPCallAddr_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 6, 2),
    _AutoFTPCallAddr_Type()
)
autoFTPCallAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFTPCallAddr.setStatus("mandatory")
_AutoFTPCallPort_Type = Integer32
_AutoFTPCallPort_Object = MibScalar
autoFTPCallPort = _AutoFTPCallPort_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 6, 3),
    _AutoFTPCallPort_Type()
)
autoFTPCallPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFTPCallPort.setStatus("mandatory")


class _AutoFTPCallUserID_Type(OctetString):
    """Custom type autoFTPCallUserID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AutoFTPCallUserID_Type.__name__ = "OctetString"
_AutoFTPCallUserID_Object = MibScalar
autoFTPCallUserID = _AutoFTPCallUserID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 6, 4),
    _AutoFTPCallUserID_Type()
)
autoFTPCallUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFTPCallUserID.setStatus("mandatory")
_CallHomeExclusionEvents_ObjectIdentity = ObjectIdentity
callHomeExclusionEvents = _CallHomeExclusionEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 7)
)
_ReadCallHomeExclusionEventTable_Object = MibTable
readCallHomeExclusionEventTable = _ReadCallHomeExclusionEventTable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 7, 1)
)
if mibBuilder.loadTexts:
    readCallHomeExclusionEventTable.setStatus("mandatory")
_ReadCallHomeExclusionEventEntry_Object = MibTableRow
readCallHomeExclusionEventEntry = _ReadCallHomeExclusionEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 7, 1, 1)
)
readCallHomeExclusionEventEntry.setIndexNames(
    (0, "LENOVO-XCC-MIB", "readCallHomeExclusionEventIndex"),
)
if mibBuilder.loadTexts:
    readCallHomeExclusionEventEntry.setStatus("mandatory")


class _ReadCallHomeExclusionEventIndex_Type(Integer32):
    """Custom type readCallHomeExclusionEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ReadCallHomeExclusionEventIndex_Type.__name__ = "Integer32"
_ReadCallHomeExclusionEventIndex_Object = MibTableColumn
readCallHomeExclusionEventIndex = _ReadCallHomeExclusionEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 7, 1, 1, 1),
    _ReadCallHomeExclusionEventIndex_Type()
)
readCallHomeExclusionEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readCallHomeExclusionEventIndex.setStatus("mandatory")
_ReadCallHomeExclusionEventID_Type = OctetString
_ReadCallHomeExclusionEventID_Object = MibTableColumn
readCallHomeExclusionEventID = _ReadCallHomeExclusionEventID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 8, 7, 1, 1, 2),
    _ReadCallHomeExclusionEventID_Type()
)
readCallHomeExclusionEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readCallHomeExclusionEventID.setStatus("mandatory")
_SupportProcessor_ObjectIdentity = ObjectIdentity
supportProcessor = _SupportProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LENOVO-XCC-MIB",
    **{"EntryStatus": EntryStatus,
       "lenovoXCCMIB": lenovoXCCMIB,
       "monitors": monitors,
       "temperature": temperature,
       "tempNumber": tempNumber,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempDescr": tempDescr,
       "tempReading": tempReading,
       "tempNominalReading": tempNominalReading,
       "tempNonRecovLimitHigh": tempNonRecovLimitHigh,
       "tempCritLimitHigh": tempCritLimitHigh,
       "tempNonCritLimitHigh": tempNonCritLimitHigh,
       "tempNonRecovLimitLow": tempNonRecovLimitLow,
       "tempCritLimitLow": tempCritLimitLow,
       "tempNonCritLimitLow": tempNonCritLimitLow,
       "tempHealthStatus": tempHealthStatus,
       "voltage": voltage,
       "voltNumber": voltNumber,
       "voltTable": voltTable,
       "voltEntry": voltEntry,
       "voltIndex": voltIndex,
       "voltDescr": voltDescr,
       "voltReading": voltReading,
       "voltNominalReading": voltNominalReading,
       "voltNonRecovLimitHigh": voltNonRecovLimitHigh,
       "voltCritLimitHigh": voltCritLimitHigh,
       "voltNonCritLimitHigh": voltNonCritLimitHigh,
       "voltNonRecovLimitLow": voltNonRecovLimitLow,
       "voltCritLimitLow": voltCritLimitLow,
       "voltNonCritLimitLow": voltNonCritLimitLow,
       "voltHealthStatus": voltHealthStatus,
       "fans": fans,
       "fanNumber": fanNumber,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanDescr": fanDescr,
       "fanSpeed": fanSpeed,
       "fanNonRecovLimitHigh": fanNonRecovLimitHigh,
       "fanCritLimitHigh": fanCritLimitHigh,
       "fanNonCritLimitHigh": fanNonCritLimitHigh,
       "fanNonRecovLimitLow": fanNonRecovLimitLow,
       "fanCritLimitLow": fanCritLimitLow,
       "fanNonCritLimitLow": fanNonCritLimitLow,
       "fanHealthStatus": fanHealthStatus,
       "systemHealth": systemHealth,
       "systemHealthStat": systemHealthStat,
       "systemHealthSummaryTable": systemHealthSummaryTable,
       "systemHealthSummaryEntry": systemHealthSummaryEntry,
       "systemHealthSummaryIndex": systemHealthSummaryIndex,
       "systemHealthSummarySeverity": systemHealthSummarySeverity,
       "systemHealthSummaryDescription": systemHealthSummaryDescription,
       "vpdInformation": vpdInformation,
       "xccVpdTable": xccVpdTable,
       "xccVpdEntry": xccVpdEntry,
       "xccVpdIndex": xccVpdIndex,
       "xccVpdType": xccVpdType,
       "xccVpdVersionString": xccVpdVersionString,
       "xccVpdReleaseDate": xccVpdReleaseDate,
       "machineVpd": machineVpd,
       "machineLevelVpd": machineLevelVpd,
       "machineLevelVpdMachineType": machineLevelVpdMachineType,
       "machineLevelVpdMachineModel": machineLevelVpdMachineModel,
       "machineLevelSerialNumber": machineLevelSerialNumber,
       "machineLevelUUID": machineLevelUUID,
       "machineLevelProductName": machineLevelProductName,
       "systemComponentLevelVpdTable": systemComponentLevelVpdTable,
       "systemComponentLevelVpdEntry": systemComponentLevelVpdEntry,
       "componentLevelVpdIndex": componentLevelVpdIndex,
       "componentLevelVpdFruNumber": componentLevelVpdFruNumber,
       "componentLevelVpdFruName": componentLevelVpdFruName,
       "componentLevelVpdSerialNumber": componentLevelVpdSerialNumber,
       "componentLevelVpdManufacturingId": componentLevelVpdManufacturingId,
       "systemComponentLevelVpdTrackingTable": systemComponentLevelVpdTrackingTable,
       "systemComponentLevelVpdTrackingEntry": systemComponentLevelVpdTrackingEntry,
       "componentLevelVpdTrackingIndex": componentLevelVpdTrackingIndex,
       "componentLevelVpdTrackingFruNumber": componentLevelVpdTrackingFruNumber,
       "componentLevelVpdTrackingFruName": componentLevelVpdTrackingFruName,
       "componentLevelVpdTrackingSerialNumber": componentLevelVpdTrackingSerialNumber,
       "componentLevelVpdTrackingManufacturingId": componentLevelVpdTrackingManufacturingId,
       "componentLevelVpdTrackingAction": componentLevelVpdTrackingAction,
       "componentLevelVpdTrackingTimestamp": componentLevelVpdTrackingTimestamp,
       "hostMACAddressTable": hostMACAddressTable,
       "hostMACAddressEntry": hostMACAddressEntry,
       "hostMACAddressIndex": hostMACAddressIndex,
       "hostMACAddressDescription": hostMACAddressDescription,
       "hostMACAddress": hostMACAddress,
       "systemCPUVpdTable": systemCPUVpdTable,
       "systemCPUVpdEntry": systemCPUVpdEntry,
       "cpuVpdIndex": cpuVpdIndex,
       "cpuVpdDescription": cpuVpdDescription,
       "cpuVpdSpeed": cpuVpdSpeed,
       "cpuVpdIdentifier": cpuVpdIdentifier,
       "cpuVpdType": cpuVpdType,
       "cpuVpdFamily": cpuVpdFamily,
       "cpuVpdCores": cpuVpdCores,
       "cpuVpdThreads": cpuVpdThreads,
       "cpuVpdVoltage": cpuVpdVoltage,
       "cpuVpdDataWidth": cpuVpdDataWidth,
       "cpuVpdHealthStatus": cpuVpdHealthStatus,
       "cpuVpdCpuModel": cpuVpdCpuModel,
       "systemMemoryVpdTable": systemMemoryVpdTable,
       "systemMemoryVpdEntry": systemMemoryVpdEntry,
       "memoryVpdIndex": memoryVpdIndex,
       "memoryVpdDescription": memoryVpdDescription,
       "memoryVpdPartNumber": memoryVpdPartNumber,
       "memoryVpdFRUSerialNumber": memoryVpdFRUSerialNumber,
       "memoryVpdManufactureDate": memoryVpdManufactureDate,
       "memoryVpdType": memoryVpdType,
       "memoryVpdSize": memoryVpdSize,
       "memoryHealthStatus": memoryHealthStatus,
       "memoryConfigSpeed": memoryConfigSpeed,
       "memoryRatedSpeed": memoryRatedSpeed,
       "memoryLenovoPartNumber": memoryLenovoPartNumber,
       "memoryVpdAEPFlag": memoryVpdAEPFlag,
       "systemAepDIMMVpdTable": systemAepDIMMVpdTable,
       "systemAepDIMMVpdEntry": systemAepDIMMVpdEntry,
       "aepDIMMVpdIndex": aepDIMMVpdIndex,
       "aepDIMMVpdMemory": aepDIMMVpdMemory,
       "aepDIMMVpdBankLocator": aepDIMMVpdBankLocator,
       "aepDIMMVpdMaxSpeed": aepDIMMVpdMaxSpeed,
       "aepDIMMVpdClockSpeed": aepDIMMVpdClockSpeed,
       "aepDIMMVpdManufacturer": aepDIMMVpdManufacturer,
       "aepDIMMVpdSerialNumber": aepDIMMVpdSerialNumber,
       "aepDIMMVpdPartNumber": aepDIMMVpdPartNumber,
       "aepDIMMVpdRawCapacity": aepDIMMVpdRawCapacity,
       "aepDIMMVpdMemoryCapacity": aepDIMMVpdMemoryCapacity,
       "aepDIMMVpdAppDirectCapacity": aepDIMMVpdAppDirectCapacity,
       "aepDIMMVpdUnconfiguredCapacity": aepDIMMVpdUnconfiguredCapacity,
       "aepDIMMVpdInaccessibleCapacity": aepDIMMVpdInaccessibleCapacity,
       "aepDIMMVpdReservedCapacity": aepDIMMVpdReservedCapacity,
       "aepDIMMVpdClassification": aepDIMMVpdClassification,
       "aepDIMMVpdFirmwareVersion": aepDIMMVpdFirmwareVersion,
       "aepDIMMVpdSoftwareID": aepDIMMVpdSoftwareID,
       "users": users,
       "xccUsers": xccUsers,
       "currentlyLoggedInTable": currentlyLoggedInTable,
       "currentlyLoggedInEntry": currentlyLoggedInEntry,
       "currentlyLoggedInEntryIndex": currentlyLoggedInEntryIndex,
       "currentlyLoggedInEntryUserId": currentlyLoggedInEntryUserId,
       "currentlyLoggedInEntryAccMethod": currentlyLoggedInEntryAccMethod,
       "leds": leds,
       "identityLED": identityLED,
       "allLEDsTable": allLEDsTable,
       "allLEDsEntry": allLEDsEntry,
       "ledIndex": ledIndex,
       "ledIdentifier": ledIdentifier,
       "ledLabel": ledLabel,
       "ledState": ledState,
       "ledColor": ledColor,
       "informationLED": informationLED,
       "fuelGauge": fuelGauge,
       "fuelGaugeInformation": fuelGaugeInformation,
       "fuelGaugePowerCappingPolicySetting": fuelGaugePowerCappingPolicySetting,
       "fuelGaugeStaticPowerPcapSoftMin": fuelGaugeStaticPowerPcapSoftMin,
       "fuelGaugeStaticPowerPcapMin": fuelGaugeStaticPowerPcapMin,
       "fuelGaugeStaticPowerPcapCurrentSetting": fuelGaugeStaticPowerPcapCurrentSetting,
       "fuelGaugeStaticPowerPcapMax": fuelGaugeStaticPowerPcapMax,
       "fuelGaugeStaticPowerPcapMode": fuelGaugeStaticPowerPcapMode,
       "fuelGaugeSystemMaxPower": fuelGaugeSystemMaxPower,
       "fuelGaugePowerRemaining": fuelGaugePowerRemaining,
       "fuelGaugeTotalPowerAvailable": fuelGaugeTotalPowerAvailable,
       "fuelGaugeTotalPowerInUse": fuelGaugeTotalPowerInUse,
       "fuelGaugePowerConsumptionCpu": fuelGaugePowerConsumptionCpu,
       "fuelGaugePowerConsumptionMemory": fuelGaugePowerConsumptionMemory,
       "fuelGaugePowerConsumptionOther": fuelGaugePowerConsumptionOther,
       "powerPolicyInformation": powerPolicyInformation,
       "powerPolicyTable": powerPolicyTable,
       "powerPolicyEntry": powerPolicyEntry,
       "powerPolicyIndex": powerPolicyIndex,
       "powerPolicyName": powerPolicyName,
       "powerPolicyPwrSupplyFailureLimit": powerPolicyPwrSupplyFailureLimit,
       "powerPolicyMaxPowerLimit": powerPolicyMaxPowerLimit,
       "powerPolicyEstimatedUtilization": powerPolicyEstimatedUtilization,
       "powerPolicyActivate": powerPolicyActivate,
       "powerRestorePolicyControl": powerRestorePolicyControl,
       "powerRestorePolicy": powerRestorePolicy,
       "powerRestoreDelay": powerRestoreDelay,
       "powerPowerTrending": powerPowerTrending,
       "powerTrendingSampleTable": powerTrendingSampleTable,
       "powerTrendingSampleEntry": powerTrendingSampleEntry,
       "powerTrendingSampleIndex": powerTrendingSampleIndex,
       "powerTrendingSampleTimeStamp": powerTrendingSampleTimeStamp,
       "powerTrendingSampleInputAve": powerTrendingSampleInputAve,
       "powerTrendingSampleInputMin": powerTrendingSampleInputMin,
       "powerTrendingSampleInputMax": powerTrendingSampleInputMax,
       "powerTrendingSampleOutputAve": powerTrendingSampleOutputAve,
       "powerTrendingSampleOutputMin": powerTrendingSampleOutputMin,
       "powerTrendingSampleOutputMax": powerTrendingSampleOutputMax,
       "powerModule": powerModule,
       "powerNumber": powerNumber,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerIndex": powerIndex,
       "powerFruName": powerFruName,
       "powerPartNumber": powerPartNumber,
       "powerFRUNumber": powerFRUNumber,
       "powerFRUSerialNumber": powerFRUSerialNumber,
       "powerHealthStatus": powerHealthStatus,
       "disks": disks,
       "diskNumber": diskNumber,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskFruName": diskFruName,
       "diskHealthStatus": diskHealthStatus,
       "localStorage": localStorage,
       "raid": raid,
       "raidOOBCapable": raidOOBCapable,
       "raidControllerTable": raidControllerTable,
       "raidControllerEntry": raidControllerEntry,
       "raidCtrlIndex": raidCtrlIndex,
       "raidCtrlName": raidCtrlName,
       "raidCtrlVPDProdName": raidCtrlVPDProdName,
       "raidCtrlFWPkgVersion": raidCtrlFWPkgVersion,
       "raidCtrlBatBCK": raidCtrlBatBCK,
       "raidCtrlVPDManufacture": raidCtrlVPDManufacture,
       "raidCtrlVPDUUID": raidCtrlVPDUUID,
       "raidCtrlVPDMachineType": raidCtrlVPDMachineType,
       "raidCtrlVPDModel": raidCtrlVPDModel,
       "raidCtrlVPDSerialNo": raidCtrlVPDSerialNo,
       "raidCtrlVPDFRUNo": raidCtrlVPDFRUNo,
       "raidCtrlVPDPartNo": raidCtrlVPDPartNo,
       "raidCtrlCacheMdlStatus": raidCtrlCacheMdlStatus,
       "raidCtrlCacheMdlMemSize": raidCtrlCacheMdlMemSize,
       "raidCtrlCacheMdlSerialNo": raidCtrlCacheMdlSerialNo,
       "raidCtrlPCISlotNo": raidCtrlPCISlotNo,
       "raidCtrlPCIBusNo": raidCtrlPCIBusNo,
       "raidCtrlPCIDevNo": raidCtrlPCIDevNo,
       "raidCtrlPCIFuncNo": raidCtrlPCIFuncNo,
       "raidCtrlPCIDevID": raidCtrlPCIDevID,
       "raidCtrlPCISubDevID": raidCtrlPCISubDevID,
       "raidCtrlBatBCKProdName": raidCtrlBatBCKProdName,
       "raidCtrlBatBCKManufacture": raidCtrlBatBCKManufacture,
       "raidCtrlBatBCKStatus": raidCtrlBatBCKStatus,
       "raidCtrlBatBCKType": raidCtrlBatBCKType,
       "raidCtrlBatBCKChem": raidCtrlBatBCKChem,
       "raidCtrlBatBCKSerialNo": raidCtrlBatBCKSerialNo,
       "raidCtrlBatBCKChgCap": raidCtrlBatBCKChgCap,
       "raidCtrlBatBCKFirmware": raidCtrlBatBCKFirmware,
       "raidCtrlBatBCKDgnVoltage": raidCtrlBatBCKDgnVoltage,
       "raidCtrlBatBCKVoltage": raidCtrlBatBCKVoltage,
       "raidCtrlBatCurrent": raidCtrlBatCurrent,
       "raidCtrlBatBCKDgnChgCap": raidCtrlBatBCKDgnChgCap,
       "raidCtrlBatBCKCrtTemp": raidCtrlBatBCKCrtTemp,
       "raidCtrlFWNames": raidCtrlFWNames,
       "raidCtrlPortDetails": raidCtrlPortDetails,
       "raidCtrlStoragepools": raidCtrlStoragepools,
       "raidCtrlDrives": raidCtrlDrives,
       "raidDriveTable": raidDriveTable,
       "raidDriveEntry": raidDriveEntry,
       "raidDriveIndex": raidDriveIndex,
       "raidDriveName": raidDriveName,
       "raidDriveVPDProdName": raidDriveVPDProdName,
       "raidDriveState": raidDriveState,
       "raidDriveSlotNo": raidDriveSlotNo,
       "raidDriveDeviceID": raidDriveDeviceID,
       "raidDriveDiskType": raidDriveDiskType,
       "raidDriveMediaType": raidDriveMediaType,
       "raidDriveSpeed": raidDriveSpeed,
       "raidDriveCurTemp": raidDriveCurTemp,
       "raidDriveHealthStataus": raidDriveHealthStataus,
       "raidDriveCapacity": raidDriveCapacity,
       "raidDriveVPDManufacture": raidDriveVPDManufacture,
       "raidDriveEnclosureID": raidDriveEnclosureID,
       "raidDriveVPDMachineType": raidDriveVPDMachineType,
       "raidDriveVPDModel": raidDriveVPDModel,
       "raidDriveVPDSerialNo": raidDriveVPDSerialNo,
       "raidDriveVPDFRUNo": raidDriveVPDFRUNo,
       "raidDriveVPDPartNo": raidDriveVPDPartNo,
       "raidDriveFWNames": raidDriveFWNames,
       "raidDriveRotationRate": raidDriveRotationRate,
       "raidDriveMediaErrCnt": raidDriveMediaErrCnt,
       "raidDriveOtherErrCnt": raidDriveOtherErrCnt,
       "raidDrivePredFailCnt": raidDrivePredFailCnt,
       "raidDriveRemainingLife": raidDriveRemainingLife,
       "raidDriveFdeCapable": raidDriveFdeCapable,
       "raidDriveSecured": raidDriveSecured,
       "raidControllerFirmwareTable": raidControllerFirmwareTable,
       "raidControllerFirmwareEntry": raidControllerFirmwareEntry,
       "raidControllerFirmwareIndex": raidControllerFirmwareIndex,
       "raidControllerFirmwareName": raidControllerFirmwareName,
       "raidControllerFirmwareCtrlName": raidControllerFirmwareCtrlName,
       "raidControllerFirmwareDescription": raidControllerFirmwareDescription,
       "raidControllerFirmwareManufacture": raidControllerFirmwareManufacture,
       "raidControllerFirmwareVersion": raidControllerFirmwareVersion,
       "raidControllerFirmwareReleaseDate": raidControllerFirmwareReleaseDate,
       "raidDriveFirmwareTable": raidDriveFirmwareTable,
       "raidDriveFirmwareEntry": raidDriveFirmwareEntry,
       "raidDriveFirmwareIndex": raidDriveFirmwareIndex,
       "raidDriveFirmwareName": raidDriveFirmwareName,
       "raidDriveFirmwareDriveName": raidDriveFirmwareDriveName,
       "raidDriveFirmwareDescription": raidDriveFirmwareDescription,
       "raidDriveFirmwareManufacture": raidDriveFirmwareManufacture,
       "raidDriveFirmwareVersion": raidDriveFirmwareVersion,
       "raidDriveFirmwareReleaseDate": raidDriveFirmwareReleaseDate,
       "raidStoragepoolTable": raidStoragepoolTable,
       "raidStoragepoolEntry": raidStoragepoolEntry,
       "raidStoragepoolIndex": raidStoragepoolIndex,
       "raidStoragepoolName": raidStoragepoolName,
       "raidStoragepoolControllerName": raidStoragepoolControllerName,
       "raidStoragepoolState": raidStoragepoolState,
       "raidStoragepoolCapacity": raidStoragepoolCapacity,
       "raidStoragepoolVols": raidStoragepoolVols,
       "raidStoragepoolDrives": raidStoragepoolDrives,
       "raidVolumeTable": raidVolumeTable,
       "raidVolumeEntry": raidVolumeEntry,
       "raidVolumeIndex": raidVolumeIndex,
       "raidVolumeName": raidVolumeName,
       "raidVolumeControllerName": raidVolumeControllerName,
       "raidVolumeStatus": raidVolumeStatus,
       "raidVolumeCapacity": raidVolumeCapacity,
       "raidVolumeStripSize": raidVolumeStripSize,
       "raidVolumeBootable": raidVolumeBootable,
       "adapters": adapters,
       "adapterOOBCapable": adapterOOBCapable,
       "adapterGenericTable": adapterGenericTable,
       "adapterGenericEntry": adapterGenericEntry,
       "adapterGenericIndex": adapterGenericIndex,
       "adapterGenericVPDProdName": adapterGenericVPDProdName,
       "adapterGenericSlotNo": adapterGenericSlotNo,
       "adapterGenericLocation": adapterGenericLocation,
       "adapterGenericCardInterface": adapterGenericCardInterface,
       "adapterNetworkFunctionTable": adapterNetworkFunctionTable,
       "adapterNetworkFunctionEntry": adapterNetworkFunctionEntry,
       "adapterNetworkFunctionIndex": adapterNetworkFunctionIndex,
       "adapterNetworkFunctionNetworkVPDProdName": adapterNetworkFunctionNetworkVPDProdName,
       "adapterNetworkFunctionAdapterVPDProdName": adapterNetworkFunctionAdapterVPDProdName,
       "adapterNetworkFunctionNetworkVPDManufacturer": adapterNetworkFunctionNetworkVPDManufacturer,
       "adapterNetworkFunctionNetworkVPDUUID": adapterNetworkFunctionNetworkVPDUUID,
       "adapterNetworkFunctionNetworkVPDModel": adapterNetworkFunctionNetworkVPDModel,
       "adapterNetworkFunctionNetworkVPDSerialNo": adapterNetworkFunctionNetworkVPDSerialNo,
       "adapterNetworkFunctionNetworkVPDFRUNo": adapterNetworkFunctionNetworkVPDFRUNo,
       "adapterNetworkFunctionNetworkVPDPartNo": adapterNetworkFunctionNetworkVPDPartNo,
       "adapterNetworkFunctionFoDUID": adapterNetworkFunctionFoDUID,
       "adapterNetworkFunctionSupportHotPlug": adapterNetworkFunctionSupportHotPlug,
       "adapterNetworkFunctionPhysicalPortNumber": adapterNetworkFunctionPhysicalPortNumber,
       "adapterNetworkFunctionMaxPortNumber": adapterNetworkFunctionMaxPortNumber,
       "adapterNetworkFunctionPortNumber": adapterNetworkFunctionPortNumber,
       "adapterNetworkFunctionMaxDataWidth": adapterNetworkFunctionMaxDataWidth,
       "adapterNetworkFunctionPackageType": adapterNetworkFunctionPackageType,
       "adapterNetworkFunctionPCIBusNo": adapterNetworkFunctionPCIBusNo,
       "adapterNetworkFunctionPCIDevNo": adapterNetworkFunctionPCIDevNo,
       "adapterNetworkFunctionPCIFuncNo": adapterNetworkFunctionPCIFuncNo,
       "adapterNetworkFunctionPCIVendorId": adapterNetworkFunctionPCIVendorId,
       "adapterNetworkFunctionPCIDevId": adapterNetworkFunctionPCIDevId,
       "adapterNetworkFunctionPCIDevType": adapterNetworkFunctionPCIDevType,
       "adapterNetworkFunctionPCIRevId": adapterNetworkFunctionPCIRevId,
       "adapterNetworkFunctionPCISubVendorId": adapterNetworkFunctionPCISubVendorId,
       "adapterNetworkFunctionPCISubDevId": adapterNetworkFunctionPCISubDevId,
       "adapterNetworkFunctionPCISlotDesignation": adapterNetworkFunctionPCISlotDesignation,
       "adapterNetworkPortTable": adapterNetworkPortTable,
       "adapterNetworkPortEntry": adapterNetworkPortEntry,
       "adapterNetworkPortIndex": adapterNetworkPortIndex,
       "adapterNetworkPortNetworkVPDProdName": adapterNetworkPortNetworkVPDProdName,
       "adapterNetworkPortPhyPortNo": adapterNetworkPortPhyPortNo,
       "adapterNetworkPortPhyPortConnector": adapterNetworkPortPhyPortConnector,
       "adapterNetworkPortPhyPortBurnedinAddress": adapterNetworkPortPhyPortBurnedinAddress,
       "adapterNetworkPortNo": adapterNetworkPortNo,
       "adapterNetworkPortMaxDataSize": adapterNetworkPortMaxDataSize,
       "adapterNetworkPortPermanentAddress": adapterNetworkPortPermanentAddress,
       "adapterNetworkPortNetworkAddress": adapterNetworkPortNetworkAddress,
       "adapterNetworkPortLinkTechnology": adapterNetworkPortLinkTechnology,
       "adapterNetworkPortvNICMode": adapterNetworkPortvNICMode,
       "adapterNetworkPortMaxSpeed": adapterNetworkPortMaxSpeed,
       "adapterNetworkPortProtocolType": adapterNetworkPortProtocolType,
       "adapterNetworkPortCurrentProtocol": adapterNetworkPortCurrentProtocol,
       "adapterNetworkPortFCoEPermanentAddress": adapterNetworkPortFCoEPermanentAddress,
       "adapterNetworkPortFCoENetworkAddress": adapterNetworkPortFCoENetworkAddress,
       "adapterNetworkPortConnectionType": adapterNetworkPortConnectionType,
       "adapterNetworkPortRole": adapterNetworkPortRole,
       "adapterNetworkPortTargetRelativePortNo": adapterNetworkPortTargetRelativePortNo,
       "adapterNetworkPortPhyPortLinkStatus": adapterNetworkPortPhyPortLinkStatus,
       "adapterNetworkPortPhyPortLinkSpeed": adapterNetworkPortPhyPortLinkSpeed,
       "adapterGPUFunctionTable": adapterGPUFunctionTable,
       "adapterGPUFunctionEntry": adapterGPUFunctionEntry,
       "adapterGPUFunctionIndex": adapterGPUFunctionIndex,
       "adapterGPUFunctionGpuVPDProdName": adapterGPUFunctionGpuVPDProdName,
       "adapterGPUFunctionAdapterVPDProdName": adapterGPUFunctionAdapterVPDProdName,
       "adapterGPUFunctionGpuVPDManufacturer": adapterGPUFunctionGpuVPDManufacturer,
       "adapterGPUFunctionGpuVPDUUID": adapterGPUFunctionGpuVPDUUID,
       "adapterGPUFunctionGpuVPDModel": adapterGPUFunctionGpuVPDModel,
       "adapterGPUFunctionGpuVPDSerialNo": adapterGPUFunctionGpuVPDSerialNo,
       "adapterGPUFunctionGpuVPDFRUNo": adapterGPUFunctionGpuVPDFRUNo,
       "adapterGPUFunctionGpuVPDPartNo": adapterGPUFunctionGpuVPDPartNo,
       "adapterGPUFunctionFoDUID": adapterGPUFunctionFoDUID,
       "adapterGPUFunctionSupportHotPlug": adapterGPUFunctionSupportHotPlug,
       "adapterGPUFunctionVideoMemorySize": adapterGPUFunctionVideoMemorySize,
       "adapterGPUFunctionVideoMemoryType": adapterGPUFunctionVideoMemoryType,
       "adapterGPUFunctionChipNumber": adapterGPUFunctionChipNumber,
       "adapterGPUFunctionMaxDataWidth": adapterGPUFunctionMaxDataWidth,
       "adapterGPUFunctionPackageType": adapterGPUFunctionPackageType,
       "adapterGPUFunctionPCIBusNo": adapterGPUFunctionPCIBusNo,
       "adapterGPUFunctionPCIDevNo": adapterGPUFunctionPCIDevNo,
       "adapterGPUFunctionPCIFuncNo": adapterGPUFunctionPCIFuncNo,
       "adapterGPUFunctionPCIVendorId": adapterGPUFunctionPCIVendorId,
       "adapterGPUFunctionPCIDevId": adapterGPUFunctionPCIDevId,
       "adapterGPUFunctionPCIDevType": adapterGPUFunctionPCIDevType,
       "adapterGPUFunctionPCIRevId": adapterGPUFunctionPCIRevId,
       "adapterGPUFunctionPCISubVendorId": adapterGPUFunctionPCISubVendorId,
       "adapterGPUFunctionPCISubDevId": adapterGPUFunctionPCISubDevId,
       "adapterGPUFunctionPCISlotDesignation": adapterGPUFunctionPCISlotDesignation,
       "adapterGPUChipTable": adapterGPUChipTable,
       "adapterGPUChipEntry": adapterGPUChipEntry,
       "adapterGPUChipIndex": adapterGPUChipIndex,
       "adapterGPUChipGpuVPDProdName": adapterGPUChipGpuVPDProdName,
       "adapterGPUChipNo": adapterGPUChipNo,
       "adapterGPUChipName": adapterGPUChipName,
       "adapterGPUChipFamily": adapterGPUChipFamily,
       "adapterGPUChipManufacturer": adapterGPUChipManufacturer,
       "adapterGPUChipCoresEnabled": adapterGPUChipCoresEnabled,
       "adapterGPUChipMaxClockSpeed": adapterGPUChipMaxClockSpeed,
       "adapterGPUChipExtBusClockSpeed": adapterGPUChipExtBusClockSpeed,
       "adapterGPUChipAddressWidth": adapterGPUChipAddressWidth,
       "adapterGPUChipDataWidth": adapterGPUChipDataWidth,
       "adapterGPUChipFormFactor": adapterGPUChipFormFactor,
       "adapterGPUChipModel": adapterGPUChipModel,
       "adapterGPUChipSerialNo": adapterGPUChipSerialNo,
       "adapterGPUChipFRUNo": adapterGPUChipFRUNo,
       "adapterGPUChipPartNo": adapterGPUChipPartNo,
       "adapterGPUChipUniqueID": adapterGPUChipUniqueID,
       "adapterRAIDFunctionTable": adapterRAIDFunctionTable,
       "adapterRAIDFunctionEntry": adapterRAIDFunctionEntry,
       "adapterRAIDFunctionIndex": adapterRAIDFunctionIndex,
       "adapterRAIDFunctionRaidVPDProdName": adapterRAIDFunctionRaidVPDProdName,
       "adapterRAIDFunctionAdapterVPDProdName": adapterRAIDFunctionAdapterVPDProdName,
       "adapterRAIDFunctionRaidVPDManufacturer": adapterRAIDFunctionRaidVPDManufacturer,
       "adapterRAIDFunctionRaidVPDUUID": adapterRAIDFunctionRaidVPDUUID,
       "adapterRAIDFunctionRaidVPDModel": adapterRAIDFunctionRaidVPDModel,
       "adapterRAIDFunctionRaidVPDSerialNo": adapterRAIDFunctionRaidVPDSerialNo,
       "adapterRAIDFunctionRaidVPDFRUNo": adapterRAIDFunctionRaidVPDFRUNo,
       "adapterRAIDFunctionRaidVPDPartNo": adapterRAIDFunctionRaidVPDPartNo,
       "adapterRAIDFunctionFoDUID": adapterRAIDFunctionFoDUID,
       "adapterRAIDFunctionSupportHotPlug": adapterRAIDFunctionSupportHotPlug,
       "adapterRAIDFunctionMaxDataWidth": adapterRAIDFunctionMaxDataWidth,
       "adapterRAIDFunctionPackageType": adapterRAIDFunctionPackageType,
       "adapterRAIDFunctionPCIBusNo": adapterRAIDFunctionPCIBusNo,
       "adapterRAIDFunctionPCIDevNo": adapterRAIDFunctionPCIDevNo,
       "adapterRAIDFunctionPCIFuncNo": adapterRAIDFunctionPCIFuncNo,
       "adapterRAIDFunctionPCIVendorId": adapterRAIDFunctionPCIVendorId,
       "adapterRAIDFunctionPCIDevId": adapterRAIDFunctionPCIDevId,
       "adapterRAIDFunctionPCIDevType": adapterRAIDFunctionPCIDevType,
       "adapterRAIDFunctionPCIRevId": adapterRAIDFunctionPCIRevId,
       "adapterRAIDFunctionPCISubVendorId": adapterRAIDFunctionPCISubVendorId,
       "adapterRAIDFunctionPCISubDevId": adapterRAIDFunctionPCISubDevId,
       "adapterRAIDFunctionPCISlotDesignation": adapterRAIDFunctionPCISlotDesignation,
       "adapterFirmwareTable": adapterFirmwareTable,
       "adapterFirmwareEntry": adapterFirmwareEntry,
       "adapterFwIndex": adapterFwIndex,
       "adapterFwFunctionVPDProdName": adapterFwFunctionVPDProdName,
       "adapterFwName": adapterFwName,
       "adapterFwClassification": adapterFwClassification,
       "adapterFwDescription": adapterFwDescription,
       "adapterFwManufacture": adapterFwManufacture,
       "adapterFwVersion": adapterFwVersion,
       "adapterFwReleaseDate": adapterFwReleaseDate,
       "adapterFwSoftwareID": adapterFwSoftwareID,
       "errorLogs": errorLogs,
       "eventLog": eventLog,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogString": eventLogString,
       "eventLogSeverity": eventLogSeverity,
       "eventLogDate": eventLogDate,
       "eventLogTime": eventLogTime,
       "configureSP": configureSP,
       "remoteAccessConfig": remoteAccessConfig,
       "generalRemoteCfg": generalRemoteCfg,
       "remoteAlertRetryDelay": remoteAlertRetryDelay,
       "remoteAlertRetryCount": remoteAlertRetryCount,
       "remoteAlertEntryDelay": remoteAlertEntryDelay,
       "snmpCriticalAlerts": snmpCriticalAlerts,
       "snmpWarningAlerts": snmpWarningAlerts,
       "snmpSystemAlerts": snmpSystemAlerts,
       "remoteAccessTamperDelay": remoteAccessTamperDelay,
       "userAuthenticationMethod": userAuthenticationMethod,
       "webInactivityTimeout": webInactivityTimeout,
       "snmpAlertFilters": snmpAlertFilters,
       "safSpTrapTempC": safSpTrapTempC,
       "safSpTrapVoltC": safSpTrapVoltC,
       "safSpTrapPowerC": safSpTrapPowerC,
       "safSpTrapHdC": safSpTrapHdC,
       "safSpTrapFanC": safSpTrapFanC,
       "safSpTrapIhcC": safSpTrapIhcC,
       "safSpTrapCPUC": safSpTrapCPUC,
       "safSpTrapMemoryC": safSpTrapMemoryC,
       "safSpTrapRdpsC": safSpTrapRdpsC,
       "safSpTrapHardwareC": safSpTrapHardwareC,
       "safSpTrapRdpsN": safSpTrapRdpsN,
       "safSpTrapTempN": safSpTrapTempN,
       "safSpTrapVoltN": safSpTrapVoltN,
       "safSpTrapPowerN": safSpTrapPowerN,
       "safSpTrapFanN": safSpTrapFanN,
       "safSpTrapCPUN": safSpTrapCPUN,
       "safSpTrapMemoryN": safSpTrapMemoryN,
       "safSpTrapHardwareN": safSpTrapHardwareN,
       "safSpTrapRLogin": safSpTrapRLogin,
       "safSpTrapOsToS": safSpTrapOsToS,
       "safSpTrapAppS": safSpTrapAppS,
       "safSpTrapPowerS": safSpTrapPowerS,
       "safSpTrapBootS": safSpTrapBootS,
       "safSpTrapLdrToS": safSpTrapLdrToS,
       "safSpTrapPFAS": safSpTrapPFAS,
       "safSpTrapSysLogS": safSpTrapSysLogS,
       "safSpTrapNwChangeS": safSpTrapNwChangeS,
       "customSecuritySettings": customSecuritySettings,
       "passwordExpirationWarningPeriod": passwordExpirationWarningPeriod,
       "passwordExpirationPeriod": passwordExpirationPeriod,
       "minimumPasswordReuseCycle": minimumPasswordReuseCycle,
       "minimumPasswordLength": minimumPasswordLength,
       "defaultAdminPasswordExpired": defaultAdminPasswordExpired,
       "changePasswordFirstAccess": changePasswordFirstAccess,
       "accountLockoutPeriod": accountLockoutPeriod,
       "maxLoginFailures": maxLoginFailures,
       "passwordChangeInterval": passwordChangeInterval,
       "serialPortCfg": serialPortCfg,
       "portBaud": portBaud,
       "portParity": portParity,
       "serialRedirect": serialRedirect,
       "enterCLIkeySeq": enterCLIkeySeq,
       "portStopBits": portStopBits,
       "portCLImode": portCLImode,
       "remoteAlertIds": remoteAlertIds,
       "remoteAlertIdsTable": remoteAlertIdsTable,
       "remoteAlertIdsEntry": remoteAlertIdsEntry,
       "remoteAlertIdEntryIndex": remoteAlertIdEntryIndex,
       "remoteAlertIdEntryStatus": remoteAlertIdEntryStatus,
       "remoteAlertIdEntryName": remoteAlertIdEntryName,
       "remoteAlertIdEmailAddr": remoteAlertIdEmailAddr,
       "remoteAlertIdEntryCriticalAlert": remoteAlertIdEntryCriticalAlert,
       "remoteAlertIdEntryWarningAlert": remoteAlertIdEntryWarningAlert,
       "remoteAlertIdEntrySystemAlert": remoteAlertIdEntrySystemAlert,
       "remoteAlertIdEntryAuditAlert": remoteAlertIdEntryAuditAlert,
       "remoteAlertIdEntryAttachmentsToEmailAlerts": remoteAlertIdEntryAttachmentsToEmailAlerts,
       "remoteAlertIdEntrySyslogPortAssignment": remoteAlertIdEntrySyslogPortAssignment,
       "remoteAlertIdEntrySyslogHostname": remoteAlertIdEntrySyslogHostname,
       "remoteAlertIdEntryType": remoteAlertIdEntryType,
       "remoteAlertFiltersTable": remoteAlertFiltersTable,
       "remoteAlertFiltersEntry": remoteAlertFiltersEntry,
       "rafIndex": rafIndex,
       "rafSpTrapTempC": rafSpTrapTempC,
       "rafSpTrapVoltC": rafSpTrapVoltC,
       "rafSpTrapPowerC": rafSpTrapPowerC,
       "rafSpTrapHdC": rafSpTrapHdC,
       "rafSpTrapFanC": rafSpTrapFanC,
       "rafSpTrapIhcC": rafSpTrapIhcC,
       "rafSpTrapCPUC": rafSpTrapCPUC,
       "rafSpTrapMemoryC": rafSpTrapMemoryC,
       "rafSpTrapRdpsC": rafSpTrapRdpsC,
       "rafSpTrapHardwareC": rafSpTrapHardwareC,
       "rafSpTrapRdpsN": rafSpTrapRdpsN,
       "rafSpTrapTempN": rafSpTrapTempN,
       "rafSpTrapVoltN": rafSpTrapVoltN,
       "rafSpTrapPowerN": rafSpTrapPowerN,
       "rafSpTrapFanN": rafSpTrapFanN,
       "rafSpTrapCPUN": rafSpTrapCPUN,
       "rafSpTrapMemoryN": rafSpTrapMemoryN,
       "rafSpTrapHardwareN": rafSpTrapHardwareN,
       "rafSpTrapRLogin": rafSpTrapRLogin,
       "rafSpTrapOsToS": rafSpTrapOsToS,
       "rafSpTrapAppS": rafSpTrapAppS,
       "rafSpTrapPowerS": rafSpTrapPowerS,
       "rafSpTrapBootS": rafSpTrapBootS,
       "rafSpTrapLdrToS": rafSpTrapLdrToS,
       "rafSpTrapPFAS": rafSpTrapPFAS,
       "rafSpTrapSysLogS": rafSpTrapSysLogS,
       "rafSpTrapNwChangeS": rafSpTrapNwChangeS,
       "rafSpTrapAllAuditS": rafSpTrapAllAuditS,
       "remoteAccessIds": remoteAccessIds,
       "remoteAccessIdsTable": remoteAccessIdsTable,
       "remoteAccessIdsEntry": remoteAccessIdsEntry,
       "remoteAccessIdEntryIndex": remoteAccessIdEntryIndex,
       "remoteAccessIdEntryUserId": remoteAccessIdEntryUserId,
       "remoteAccessIdEntryUserPwdLeftDays": remoteAccessIdEntryUserPwdLeftDays,
       "remoteAccessUserAuthorityLevelTable": remoteAccessUserAuthorityLevelTable,
       "remoteAccessUserAuthorityLevelEntry": remoteAccessUserAuthorityLevelEntry,
       "ualIndex": ualIndex,
       "ualId": ualId,
       "ualSupervisor": ualSupervisor,
       "ualReadOnly": ualReadOnly,
       "ualAccountManagement": ualAccountManagement,
       "ualConsoleAccess": ualConsoleAccess,
       "ualConsoleAndVirtualMediaAccess": ualConsoleAndVirtualMediaAccess,
       "ualServerPowerAccess": ualServerPowerAccess,
       "ualAllowClearLog": ualAllowClearLog,
       "ualAdapterBasicConfig": ualAdapterBasicConfig,
       "ualAdapterNetworkAndSecurityConfig": ualAdapterNetworkAndSecurityConfig,
       "ualAdapterAdvancedConfig": ualAdapterAdvancedConfig,
       "groupProfiles": groupProfiles,
       "groupIdsTable": groupIdsTable,
       "groupIdsEntry": groupIdsEntry,
       "groupIndex": groupIndex,
       "groupId": groupId,
       "groupRole": groupRole,
       "groupRBSroleTable": groupRBSroleTable,
       "groupRBSroleEntry": groupRBSroleEntry,
       "groupRBSroleIndex": groupRBSroleIndex,
       "groupRBSroleId": groupRBSroleId,
       "groupRBSSupervisor": groupRBSSupervisor,
       "groupRBSOperator": groupRBSOperator,
       "groupRBSNetworkSecurity": groupRBSNetworkSecurity,
       "groupRBSUserAccountManagement": groupRBSUserAccountManagement,
       "groupRBSRemoteConsoleAccess": groupRBSRemoteConsoleAccess,
       "groupRBSRemoteConsoleRemoteDiskAccess": groupRBSRemoteConsoleRemoteDiskAccess,
       "groupRBSServerPowerRestartAccess": groupRBSServerPowerRestartAccess,
       "groupRBSBasicAdapterConfiguration": groupRBSBasicAdapterConfiguration,
       "groupRBSClearEventLog": groupRBSClearEventLog,
       "groupRBSAdvancedAdapterConfiguration": groupRBSAdvancedAdapterConfiguration,
       "sshClientAuth": sshClientAuth,
       "sshClientAuthPubKeyTable": sshClientAuthPubKeyTable,
       "sshClientAuthPubKeyEntry": sshClientAuthPubKeyEntry,
       "sshClientAuthRemoteAccessIdIndex": sshClientAuthRemoteAccessIdIndex,
       "sshClientAuthPubKeyIndex": sshClientAuthPubKeyIndex,
       "sshClientAuthPubKeyType": sshClientAuthPubKeyType,
       "sshClientAuthPubKeySize": sshClientAuthPubKeySize,
       "sshClientAuthPubKeyFingerprint": sshClientAuthPubKeyFingerprint,
       "sshClientAuthPubKeyAcceptFrom": sshClientAuthPubKeyAcceptFrom,
       "sshClientAuthPubKeyUnused": sshClientAuthPubKeyUnused,
       "spClock": spClock,
       "spClockDateAndTimeSetting": spClockDateAndTimeSetting,
       "spClockTimezoneSetting": spClockTimezoneSetting,
       "spIdentification": spIdentification,
       "spTxtId": spTxtId,
       "spRoomID": spRoomID,
       "spRackID": spRackID,
       "spRackUnitPosition": spRackUnitPosition,
       "spRackUnitHeight": spRackUnitHeight,
       "spRackBladeBay": spRackBladeBay,
       "spFullPostalAddress": spFullPostalAddress,
       "networkConfiguration": networkConfiguration,
       "networkInterfaces": networkInterfaces,
       "ethernetInterface": ethernetInterface,
       "ethernetInterfaceType": ethernetInterfaceType,
       "ethernetInterfaceEnabled": ethernetInterfaceEnabled,
       "ethernetInterfaceHostName": ethernetInterfaceHostName,
       "ethernetInterfaceIPAddress": ethernetInterfaceIPAddress,
       "ethernetInterfaceAutoNegotiate": ethernetInterfaceAutoNegotiate,
       "ethernetInterfaceDataRate": ethernetInterfaceDataRate,
       "ethernetInterfaceDuplexSetting": ethernetInterfaceDuplexSetting,
       "ethernetInterfaceLAA": ethernetInterfaceLAA,
       "ethernetInterfaceDhcpEnabled": ethernetInterfaceDhcpEnabled,
       "ethernetInterfaceGatewayIPAddress": ethernetInterfaceGatewayIPAddress,
       "ethernetInterfaceBIA": ethernetInterfaceBIA,
       "ethernetInterfaceMTU": ethernetInterfaceMTU,
       "ethernetInterfaceSubnetMask": ethernetInterfaceSubnetMask,
       "dhcpEthernetInterface": dhcpEthernetInterface,
       "dhcpHostName": dhcpHostName,
       "dhcpIPAddress": dhcpIPAddress,
       "dhcpGatewayIPAddress": dhcpGatewayIPAddress,
       "dhcpSubnetMask": dhcpSubnetMask,
       "dhcpDomainName": dhcpDomainName,
       "dhcpPrimaryDNSServer": dhcpPrimaryDNSServer,
       "dhcpSecondaryDNSServer": dhcpSecondaryDNSServer,
       "dhcpTertiaryDNSServer": dhcpTertiaryDNSServer,
       "ethernetInterfaceVlan": ethernetInterfaceVlan,
       "ethernetInterfaceVlanID": ethernetInterfaceVlanID,
       "ethernetInterfaceIPv6": ethernetInterfaceIPv6,
       "ethernetInterfaceIPv6Enabled": ethernetInterfaceIPv6Enabled,
       "ethernetInterfaceIPv6Config": ethernetInterfaceIPv6Config,
       "ethernetInterfaceIPv6LocalAddress": ethernetInterfaceIPv6LocalAddress,
       "ethernetInterfaceIPv6LinkLocalAddress": ethernetInterfaceIPv6LinkLocalAddress,
       "ethernetInterfaceIPv6StaticIPConfig": ethernetInterfaceIPv6StaticIPConfig,
       "ethernetInterfaceIPv6StaticIPConfigEnabled": ethernetInterfaceIPv6StaticIPConfigEnabled,
       "ethernetInterfaceIPv6StaticIPAddress": ethernetInterfaceIPv6StaticIPAddress,
       "ethernetInterfaceIPv6StaticIPAddressPrefixLen": ethernetInterfaceIPv6StaticIPAddressPrefixLen,
       "ethernetInterfaceIPv6StaticIPDefaultRoute": ethernetInterfaceIPv6StaticIPDefaultRoute,
       "ethernetInterfaceIPv6AutoIPConfig": ethernetInterfaceIPv6AutoIPConfig,
       "ethernetInterfaceDHCPv6Config": ethernetInterfaceDHCPv6Config,
       "ethernetInterfaceDHCPv6Enabled": ethernetInterfaceDHCPv6Enabled,
       "ethernetInterfaceDHCPv6IPAddress": ethernetInterfaceDHCPv6IPAddress,
       "ethernetInterfaceDHCPv6DomainName": ethernetInterfaceDHCPv6DomainName,
       "ethernetInterfaceDHCPv6PrimaryDNSServer": ethernetInterfaceDHCPv6PrimaryDNSServer,
       "ethernetInterfaceDHCPv6SecondaryDNSServer": ethernetInterfaceDHCPv6SecondaryDNSServer,
       "ethernetInterfaceDHCPv6TertiaryDNSServer": ethernetInterfaceDHCPv6TertiaryDNSServer,
       "ethernetInterfaceDHCPv6Server": ethernetInterfaceDHCPv6Server,
       "ethernetInterfaceIPv6StatelessAutoConfig": ethernetInterfaceIPv6StatelessAutoConfig,
       "ethernetInterfaceIPv6StatelessAutoConfigEnabled": ethernetInterfaceIPv6StatelessAutoConfigEnabled,
       "ethernetInterfaceStatelessAutoConfigAddressesTable": ethernetInterfaceStatelessAutoConfigAddressesTable,
       "ethernetInterfaceStatelessAutoConfigAddressesEntry": ethernetInterfaceStatelessAutoConfigAddressesEntry,
       "ethernetInterfaceStatelessAutoConfigAddressesIndex": ethernetInterfaceStatelessAutoConfigAddressesIndex,
       "ethernetInterfaceStatelessAutoConfigAddresses": ethernetInterfaceStatelessAutoConfigAddresses,
       "ethernetInterfaceStatelessAutoConfigAddressesPrefixLen": ethernetInterfaceStatelessAutoConfigAddressesPrefixLen,
       "vlansSM": vlansSM,
       "vlansSMvlan1config": vlansSMvlan1config,
       "vlansSMvlan1Name": vlansSMvlan1Name,
       "vlansSMvlan1vlanId": vlansSMvlan1vlanId,
       "vlansSMvlan1State": vlansSMvlan1State,
       "vlansSMvlan1RemoteControl": vlansSMvlan1RemoteControl,
       "vlansSMvlan1SSerialOverLan": vlansSMvlan1SSerialOverLan,
       "vlansSMvlan2config": vlansSMvlan2config,
       "vlansSMvlan2Name": vlansSMvlan2Name,
       "vlansSMvlan2vlanId": vlansSMvlan2vlanId,
       "vlansSMvlan2State": vlansSMvlan2State,
       "vlansSMvlan2RemoteControl": vlansSMvlan2RemoteControl,
       "vlansSMvlan2SerialOverLan": vlansSMvlan2SerialOverLan,
       "vlansSMvlan2ipv4Config": vlansSMvlan2ipv4Config,
       "vlansSMvlan2IPv4Address": vlansSMvlan2IPv4Address,
       "vlansSMvlan2IPv4Gateway": vlansSMvlan2IPv4Gateway,
       "vlansSMvlan2IPv4SubnetMask": vlansSMvlan2IPv4SubnetMask,
       "vlansSMvlan2ipv6Config": vlansSMvlan2ipv6Config,
       "vlansSMvlan2IPv6Address": vlansSMvlan2IPv6Address,
       "vlansSMvlan2IPv6Gateway": vlansSMvlan2IPv6Gateway,
       "vlansSMvlan2IPv6PrefixLength": vlansSMvlan2IPv6PrefixLength,
       "vlansSMvlan2ipv4StatusRoutes": vlansSMvlan2ipv4StatusRoutes,
       "vlansSMvlan2IPv4StaticRouteIP1": vlansSMvlan2IPv4StaticRouteIP1,
       "vlansSMvlan2IPv4StaticRouteSM1": vlansSMvlan2IPv4StaticRouteSM1,
       "vlansSMvlan2IPv4StaticRouteIP2": vlansSMvlan2IPv4StaticRouteIP2,
       "vlansSMvlan2IPv4StaticRouteSM2": vlansSMvlan2IPv4StaticRouteSM2,
       "vlansSMvlan2IPv4StaticRouteIP3": vlansSMvlan2IPv4StaticRouteIP3,
       "vlansSMvlan2IPv4StaticRouteSM3": vlansSMvlan2IPv4StaticRouteSM3,
       "vlansSMvlan2ipv6StatusRoutes": vlansSMvlan2ipv6StatusRoutes,
       "vlansSMvlan2IPv6StaticRouteIP1": vlansSMvlan2IPv6StaticRouteIP1,
       "vlansSMvlan2IPv6StaticRoutePL1": vlansSMvlan2IPv6StaticRoutePL1,
       "vlansSMvlan2IPv6StaticRouteIP2": vlansSMvlan2IPv6StaticRouteIP2,
       "vlansSMvlan2IPv6StaticRoutePL2": vlansSMvlan2IPv6StaticRoutePL2,
       "vlansSMvlan2IPv6StaticRouteIP3": vlansSMvlan2IPv6StaticRouteIP3,
       "vlansSMvlan2IPv6StaticRoutePL3": vlansSMvlan2IPv6StaticRoutePL3,
       "vlansSMvlanControl": vlansSMvlanControl,
       "vlansSMvlanConfigRevertTimout": vlansSMvlanConfigRevertTimout,
       "ddnsStatus": ddnsStatus,
       "hostName": hostName,
       "ddnsDomainToUse": ddnsDomainToUse,
       "domainName": domainName,
       "lanOverUSBInterface": lanOverUSBInterface,
       "xccUSBIPAddress": xccUSBIPAddress,
       "xccUSBSubnetMask": xccUSBSubnetMask,
       "osUSBIPAddress": osUSBIPAddress,
       "tcpProtocols": tcpProtocols,
       "snmpAgentConfig": snmpAgentConfig,
       "snmpSystemName": snmpSystemName,
       "snmpSystemContact": snmpSystemContact,
       "snmpSystemLocation": snmpSystemLocation,
       "snmpSystemAgentTrapsDisable": snmpSystemAgentTrapsDisable,
       "snmpAgentCommunityConfig": snmpAgentCommunityConfig,
       "snmpCommunityEntryCommunityName": snmpCommunityEntryCommunityName,
       "snmpCommunityEntryCommunityIpAddress": snmpCommunityEntryCommunityIpAddress,
       "snmpv3SystemAgentEnable": snmpv3SystemAgentEnable,
       "snmpAgentUserProfileConfig": snmpAgentUserProfileConfig,
       "snmpUserProfileTable": snmpUserProfileTable,
       "snmpUserProfileEntry": snmpUserProfileEntry,
       "snmpUserProfileEntryIndex": snmpUserProfileEntryIndex,
       "snmpUserProfileEntryAuthProt": snmpUserProfileEntryAuthProt,
       "snmpUserProfileEntryPrivProt": snmpUserProfileEntryPrivProt,
       "snmpUserProfileEntryViewType": snmpUserProfileEntryViewType,
       "snmpUserProfileEntryIpAddress": snmpUserProfileEntryIpAddress,
       "dnsConfig": dnsConfig,
       "dnsEnabled": dnsEnabled,
       "dnsServerIPAddress1": dnsServerIPAddress1,
       "dnsServerIPAddress2": dnsServerIPAddress2,
       "dnsServerIPAddress3": dnsServerIPAddress3,
       "dnsServerIPv6Address1": dnsServerIPv6Address1,
       "dnsServerIPv6Address2": dnsServerIPv6Address2,
       "dnsServerIPv6Address3": dnsServerIPv6Address3,
       "dnsPriority": dnsPriority,
       "dnsLXCADiscovery": dnsLXCADiscovery,
       "smtpConfig": smtpConfig,
       "smtpServerNameOrIPAddress": smtpServerNameOrIPAddress,
       "smtpServerPort": smtpServerPort,
       "smtpServerAuthentication": smtpServerAuthentication,
       "smtpServerAuthenticationUser": smtpServerAuthenticationUser,
       "smtpServerAuthenticationMethod": smtpServerAuthenticationMethod,
       "smtpServerReversePath": smtpServerReversePath,
       "tcpApplicationConfig": tcpApplicationConfig,
       "slpAddrType": slpAddrType,
       "slpMulticastAddr": slpMulticastAddr,
       "sshServerConfig": sshServerConfig,
       "sshServerHostKeySize": sshServerHostKeySize,
       "sshServerHostKeyFingerprint": sshServerHostKeyFingerprint,
       "sshEnable": sshEnable,
       "sslConfig": sslConfig,
       "sslEnableHTTPSforWeb": sslEnableHTTPSforWeb,
       "sslEnableHTTPSforCIMXML": sslEnableHTTPSforCIMXML,
       "sslEnableSecureClientLDAP": sslEnableSecureClientLDAP,
       "sslServerCertificate": sslServerCertificate,
       "sslServerCertificateStatus": sslServerCertificateStatus,
       "sslServerCertificateExpirationDate": sslServerCertificateExpirationDate,
       "sslLDAPTrustedCertificate": sslLDAPTrustedCertificate,
       "sslLDAPTrustedCertificate1Status": sslLDAPTrustedCertificate1Status,
       "sslLDAPTrustedCertificate1ExpirationDate": sslLDAPTrustedCertificate1ExpirationDate,
       "sslLDAPTrustedCertificate2Status": sslLDAPTrustedCertificate2Status,
       "sslLDAPTrustedCertificate2ExpirationDate": sslLDAPTrustedCertificate2ExpirationDate,
       "sslLDAPTrustedCertificate3Status": sslLDAPTrustedCertificate3Status,
       "sslLDAPTrustedCertificate3ExpirationDate": sslLDAPTrustedCertificate3ExpirationDate,
       "sslLDAPTrustedCertificate4Status": sslLDAPTrustedCertificate4Status,
       "sslLDAPTrustedCertificate4ExpirationDate": sslLDAPTrustedCertificate4ExpirationDate,
       "certDomainNames": certDomainNames,
       "certDomainNameTable": certDomainNameTable,
       "certDomainNameEntry": certDomainNameEntry,
       "certDomainNameIndex": certDomainNameIndex,
       "certDomainName": certDomainName,
       "certDomainNameStatus": certDomainNameStatus,
       "skrServers": skrServers,
       "skrServerTable": skrServerTable,
       "skrServerEntry": skrServerEntry,
       "skrServerIndex": skrServerIndex,
       "skrServerHostname": skrServerHostname,
       "skrServerPort": skrServerPort,
       "skrDeviceGroup": skrDeviceGroup,
       "skrClientConfigCertficate": skrClientConfigCertficate,
       "skrClientCertificateStatus": skrClientCertificateStatus,
       "skrClientCertificateExpirationDate": skrClientCertificateExpirationDate,
       "skrServerCertificateExpirationDate": skrServerCertificateExpirationDate,
       "tcpPortAssignmentCfg": tcpPortAssignmentCfg,
       "httpPortAssignment": httpPortAssignment,
       "httpsPortAssignment": httpsPortAssignment,
       "sshLegacyCLIPortAssignment": sshLegacyCLIPortAssignment,
       "snmpAgentPortAssignment": snmpAgentPortAssignment,
       "snmpTrapsPortAssignment": snmpTrapsPortAssignment,
       "remvidPortAssignment": remvidPortAssignment,
       "cimOverHttpsPortAssignment": cimOverHttpsPortAssignment,
       "ldapClientCfg": ldapClientCfg,
       "ldapServer1NameOrIPAddress": ldapServer1NameOrIPAddress,
       "ldapServer1PortNumber": ldapServer1PortNumber,
       "ldapServer2NameOrIPAddress": ldapServer2NameOrIPAddress,
       "ldapServer2PortNumber": ldapServer2PortNumber,
       "ldapServer3NameOrIPAddress": ldapServer3NameOrIPAddress,
       "ldapServer3PortNumber": ldapServer3PortNumber,
       "ldapServer4NameOrIPAddress": ldapServer4NameOrIPAddress,
       "ldapServer4PortNumber": ldapServer4PortNumber,
       "ldapRootDN": ldapRootDN,
       "ldapGroupFilter": ldapGroupFilter,
       "ldapBindingMethod": ldapBindingMethod,
       "ldapClientAuthenticationDN": ldapClientAuthenticationDN,
       "ldapRoleBasedSecurityEnabled": ldapRoleBasedSecurityEnabled,
       "ldapServerTargetName": ldapServerTargetName,
       "ldapUIDsearchAttribute": ldapUIDsearchAttribute,
       "ldapGroupSearchAttribute": ldapGroupSearchAttribute,
       "ldapLoginPermissionAttribute": ldapLoginPermissionAttribute,
       "ldapUseDNSOrPreConfiguredServers": ldapUseDNSOrPreConfiguredServers,
       "ldapDomainSource": ldapDomainSource,
       "ldapForestName": ldapForestName,
       "ldapAuthCfg": ldapAuthCfg,
       "ldapSearchDomain": ldapSearchDomain,
       "ldapServiceName": ldapServiceName,
       "ntpConfig": ntpConfig,
       "ntpEnable": ntpEnable,
       "ntpIpAddressHostname1": ntpIpAddressHostname1,
       "ntpUpdateFrequency": ntpUpdateFrequency,
       "ntpIpAddressHostname2": ntpIpAddressHostname2,
       "ntpIpAddressHostname3": ntpIpAddressHostname3,
       "ntpIpAddressHostname4": ntpIpAddressHostname4,
       "ipmiConfig": ipmiConfig,
       "ipmiStatus": ipmiStatus,
       "cimxmlConfig": cimxmlConfig,
       "cimxmlStatus": cimxmlStatus,
       "restConfig": restConfig,
       "restStatus": restStatus,
       "xccVersionCheck": xccVersionCheck,
       "generalSystemSettings": generalSystemSettings,
       "serverTimers": serverTimers,
       "oSHang": oSHang,
       "oSLoader": oSLoader,
       "networkPXEboot": networkPXEboot,
       "systemPower": systemPower,
       "powerStatistics": powerStatistics,
       "currentSysPowerStatus": currentSysPowerStatus,
       "powerOnHours": powerOnHours,
       "restartCount": restartCount,
       "systemState": systemState,
       "powerSysConfig": powerSysConfig,
       "powerSysOffDelay": powerSysOffDelay,
       "powerSysOnClockSetting": powerSysOnClockSetting,
       "powerCyclingSchedule": powerCyclingSchedule,
       "schedulePowerOffWithOsShutdown": schedulePowerOffWithOsShutdown,
       "schedulePowerOnSystem": schedulePowerOnSystem,
       "serviceAdvisor": serviceAdvisor,
       "autoCallHomeSetup": autoCallHomeSetup,
       "acceptLicenseAgreement": acceptLicenseAgreement,
       "serviceAdvisorEnable": serviceAdvisorEnable,
       "serviceSupportCenter": serviceSupportCenter,
       "lenovoSupportCenter": lenovoSupportCenter,
       "contactInformation": contactInformation,
       "companyName": companyName,
       "contactName": contactName,
       "phoneNumber": phoneNumber,
       "emailAddress": emailAddress,
       "address": address,
       "city": city,
       "state": state,
       "postalCode": postalCode,
       "phoneExtension": phoneExtension,
       "altContactName": altContactName,
       "altPhoneNumber": altPhoneNumber,
       "altPhoneExtension": altPhoneExtension,
       "altEmailAddress": altEmailAddress,
       "machineLocationPhoneNumber": machineLocationPhoneNumber,
       "httpProxyConfig": httpProxyConfig,
       "httpProxyEnable": httpProxyEnable,
       "httpProxyLocation": httpProxyLocation,
       "httpProxyPort": httpProxyPort,
       "httpProxyUserName": httpProxyUserName,
       "httpProxyPassword": httpProxyPassword,
       "activityLogs": activityLogs,
       "activityLogTable": activityLogTable,
       "activityLogEntry": activityLogEntry,
       "activityLogIndex": activityLogIndex,
       "activityLogString": activityLogString,
       "activityLogAcknowledge": activityLogAcknowledge,
       "activityLogAttribute": activityLogAttribute,
       "autoFTPSetup": autoFTPSetup,
       "autoFTPCallMode": autoFTPCallMode,
       "autoFTPCallAddr": autoFTPCallAddr,
       "autoFTPCallPort": autoFTPCallPort,
       "autoFTPCallUserID": autoFTPCallUserID,
       "callHomeExclusionEvents": callHomeExclusionEvents,
       "readCallHomeExclusionEventTable": readCallHomeExclusionEventTable,
       "readCallHomeExclusionEventEntry": readCallHomeExclusionEventEntry,
       "readCallHomeExclusionEventIndex": readCallHomeExclusionEventIndex,
       "readCallHomeExclusionEventID": readCallHomeExclusionEventID,
       "supportProcessor": supportProcessor}
)
